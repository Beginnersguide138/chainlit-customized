import chainlit as cl
from chainlit.input_widget import Select, Switch, Slider, TextInput
import toml
import os

@cl.on_settings_update
async def update_settings(settings):
    """Process when settings are updated"""
    cl.user_session.set("config_settings", settings)
    
    # Save settings to config.toml
    await save_config_to_file(settings)
    
    await cl.Message(content="⚙️ Settings updated! Please restart the application to apply changes.").send()

async def create_config_settings():
    """Create Chainlit settings editor"""
    current_config = load_current_config()
    
    settings = await cl.ChatSettings([
        TextInput(
            id="ui_name",
            label="Assistant Name",
            initial=current_config.get("UI", {}).get("name", "Assistant"),
            description="Display name of the chatbot"
        ),
        Select(
            id="ui_theme",
            label="Default Theme",
            items={"light": "Light", "dark": "Dark"},
            initial_value=current_config.get("UI", {}).get("default_theme", "light"),
            description="Default theme of the application"
        ),
        Select(
            id="ui_layout",
            label="Layout",
            items={"default": "Default", "wide": "Wide"},
            initial_value=current_config.get("UI", {}).get("layout", "default"),
            description="Chat screen layout"
        ),
        Switch(
            id="features_html",
            label="Allow HTML",
            initial=current_config.get("features", {}).get("unsafe_allow_html", False),
            description="Allow HTML display in messages"
        ),
        Switch(
            id="features_latex",
            label="Allow LaTeX Math",
            initial=current_config.get("features", {}).get("latex", False),
            description="Enable mathematical expression display"
        ),
        Switch(
            id="features_edit_message",
            label="Allow Message Editing",
            initial=current_config.get("features", {}).get("edit_message", True),
            description="Users can edit their own messages"
        ),
        Slider(
            id="project_session_timeout",
            label="Session Timeout (seconds)",
            initial=current_config.get("project", {}).get("session_timeout", 3600),
            min=300,
            max=7200,
            step=300,
            description="Session retention time when connection is lost"
        )
    ]).send()
    
    return settings

def load_current_config():
    """Load current config.toml"""
    config_path = ".chainlit/config.toml"
    if os.path.exists(config_path):
        with open(config_path, 'r', encoding='utf-8') as f:
            return toml.load(f)
    return {}

async def save_config_to_file(settings):
    """Save settings to config.toml file"""
    config = load_current_config()
    
    # UI settings
    if "UI" not in config:
        config["UI"] = {}
    config["UI"]["name"] = settings["ui_name"]
    config["UI"]["default_theme"] = settings["ui_theme"]
    config["UI"]["layout"] = settings["ui_layout"]
    
    # features settings
    if "features" not in config:
        config["features"] = {}
    config["features"]["unsafe_allow_html"] = settings["features_html"]
    config["features"]["latex"] = settings["features_latex"]
    config["features"]["edit_message"] = settings["features_edit_message"]
    
    # project settings
    if "project" not in config:
        config["project"] = {}
    config["project"]["session_timeout"] = settings["project_session_timeout"]
    
    # Save to file
    config_path = ".chainlit/config.toml"
    with open(config_path, 'w', encoding='utf-8') as f:
        toml.dump(config, f)

async def show_config_editor():
    """Display settings editor"""
    await create_config_settings()
    
    await cl.Message(
        content="⚙️ **Chainlit Settings Editor**\n\nYou can change settings from the settings panel in the top right.\nApplication restart is required to apply changes."
    ).send()