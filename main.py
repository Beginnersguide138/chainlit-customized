import chainlit as cl
from typing import Dict, Any, List
import asyncio
import json

# Landing page HTML with modern design
landing_page_html = """
<div class="wrapper">
<div class="compact-hero">
    <div class="hero-content">
        <h1 class="hero-title">
            🚀 Chainlit UI Customization Demo
        </h1>
        <p class="hero-subtitle">
            Showcase of advanced UI/UX customization techniques for Chainlit applications
        </p>
        <div class="features-grid">
            <span class="feature-item">🎨 Custom Components</span>
            <span class="feature-item">📋 Info Cards</span>
            <span class="feature-item">⚡ Interactive Actions</span>
        </div>
    </div>
</div>

<style>
.compact-hero {
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    border-radius: 12px;
    margin: 10px 0;
    padding: 20px;
    color: white;
}

[data-theme="dark"] .compact-hero {
    background: linear-gradient(135deg, #1e3a8a 0%, #312e81 100%);
}

.hero-content {
    text-align: center;
    max-width: 600px;
    margin: 0 auto;
}

.hero-title {
    font-size: 1.8rem;
    font-weight: 700;
    margin-bottom: 8px;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
}

.hero-subtitle {
    font-size: 1rem;
    margin-bottom: 16px;
    opacity: 0.9;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

.features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
    gap: 8px;
    margin-top: 12px;
}

.feature-item {
    background: rgba(255, 255, 255, 0.15);
    padding: 6px 12px;
    border-radius: 6px;
    font-size: 0.85rem;
    backdrop-filter: blur(5px);
    border: 1px solid rgba(255, 255, 255, 0.2);
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 1.5rem;
    }
    
    .hero-subtitle {
        font-size: 0.9rem;
    }
    
    .features-grid {
        grid-template-columns: 1fr 1fr;
        gap: 6px;
    }
    
    .feature-item {
        font-size: 0.8rem;
        padding: 4px 8px;
    }
}
</style>
"""

# Chat profile configuration
chat_profiles = [
    cl.ChatProfile(
        name="UI Demo",
        markdown_description=landing_page_html,
        icon="https://img.icons8.com/?size=100&id=eoxMN35Z6JKg&format=png&color=000000",
        default=True,
        starters=[
            cl.Starter(
                label="🎨 Custom Components",
                message="🎨",
            ),
            cl.Starter(
                label="📋 Info Cards",
                message="📋",
            ),
            cl.Starter(
                label="🚀 Feature Demo",
                message="demo",
            ),
            cl.Starter(
                label="⚙️ UI Settings",
                message="⚙️",
            )
        ]
    ),
    cl.ChatProfile(
        name="Interactive Chat",
        markdown_description="Experience interactive features with action buttons and follow-up messages.\n\n*Demonstrates dynamic conversation flows and UI responses.*",
        icon="https://img.icons8.com/?size=100&id=BpLxiRbSRN80&format=png",
        starters=[
            cl.Starter(
                label="Interactive Demo",
                message="Show me interactive features",
            ),
            cl.Starter(
                label="Action Buttons",
                message="Demonstrate action buttons",
            )
        ]
    ),
    cl.ChatProfile(
        name="File Processing",
        markdown_description="File upload and processing demonstration with sidebar display.\n\nUpload files to see dynamic content rendering in the sidebar.",
        icon="https://img.icons8.com/?size=100&id=85784&format=png",
        starters=[
            cl.Starter(
                label="File Features",
                message="What file processing features are available?",
            ),
            cl.Starter(
                label="Upload Demo",
                message="How does file upload work?",
            )
        ]
    )
]

@cl.set_chat_profiles
async def chat_profile():
    return chat_profiles

@cl.on_chat_start
async def start():
    # Initialize settings from config_editor if available
    try:
        from config_editor import create_config_settings
        await create_config_settings()
    except ImportError:
        pass  # config_editor is optional
    
    # Command configuration
    commands = [
        {"id": "components", "icon": "palette", "description": "Show custom components"},
        {"id": "cards", "icon": "info", "description": "Display info cards"},
        {"id": "demo", "icon": "rocket", "description": "Full feature demo"},
        {"id": "settings", "icon": "settings", "description": "UI settings"},
    ]
    
    await cl.context.emitter.set_commands(commands)
    
    # Initialize empty sidebar
    await cl.ElementSidebar.set_elements([])

@cl.on_message
async def main(message: cl.Message):
    chat_profile = cl.user_session.get("chat_profile")
    
    if chat_profile == "UI Demo":
        await handle_ui_demo(message)
    elif chat_profile == "Interactive Chat":
        await handle_interactive_chat(message)
    elif chat_profile == "File Processing":
        await handle_file_processing(message)
    else:
        await cl.Message(content="Please select a chat profile.").send()

async def handle_ui_demo(message: cl.Message):
    # Process commands with highest priority
    if message.command:
        command = message.command
        if command == "components":
            await show_custom_components()
            return
        elif command == "cards":
            await show_info_cards()
            return
        elif command == "demo":
            await show_feature_demo()
            return
        elif command == "settings":
            await show_ui_settings()
            return
    
    # Handle special content messages
    if message.content == "🎨":
        await show_custom_components()
        return
    elif message.content in ["📋", "info"]:
        await show_info_cards()
        return
    elif message.content.lower() in ["demo", "features"]:
        await show_feature_demo()
        return
    elif message.content == "⚙️":
        await show_ui_settings()
        return
    
    # Default response with action buttons
    response = f"**UI Demo Assistant**\n\nProcessing: {message.content}\n\nExplore the available UI features using the action buttons below."
    
    # Main action buttons
    actions = [
        cl.Action(name="action_summary", label="📝 Create Summary", payload={"action": "summary"}),
        cl.Action(name="action_detail", label="🔍 Show Details", payload={"action": "detail"}),
        cl.Action(name="action_components", label="🎨 Custom Components", payload={"action": "components"}),
        cl.Action(name="action_cards", label="📋 Info Cards", payload={"action": "cards"}),
        cl.Action(name="action_demo", label="⭐ Full Demo", payload={"action": "demo"}),
        cl.Action(name="action_settings", label="⚙️ UI Settings", payload={"action": "settings"}),
    ]
    
    await cl.Message(content=response, actions=actions).send()

async def handle_interactive_chat(message: cl.Message):
    response = f"**Interactive Chat Mode**\n\nYour message: {message.content}\n\nThis mode demonstrates dynamic conversation flows with contextual action buttons."
    
    # Interactive actions
    actions = [
        cl.Action(name="action_analyze", label="� Deep Analysis", payload={"action": "analyze"}),
        cl.Action(name="action_expand", label="📈 Expand Topic", payload={"action": "expand"}),
        cl.Action(name="action_related", label="🔗 Related Topics", payload={"action": "related"}),
    ]
    
    await cl.Message(content=response, actions=actions).send()

async def handle_file_processing(message: cl.Message):
    files = message.elements or []
    
    if files:
        # Process uploaded files
        sidebar_elements = []
        for file in files:
            if file.mime and file.mime.startswith('image/'):
                sidebar_elements.append(cl.Image(name=file.name, path=file.path))
            elif file.mime == 'application/pdf':
                sidebar_elements.append(cl.Pdf(name=file.name, path=file.path))
            elif file.mime and (file.mime.startswith('text/') or 'json' in file.mime):
                try:
                    with open(file.path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    sidebar_elements.append(cl.Text(name=file.name, content=content))
                except:
                    sidebar_elements.append(cl.File(name=file.name, path=file.path))
            else:
                sidebar_elements.append(cl.File(name=file.name, path=file.path))
        
        # Display files in sidebar
        await cl.ElementSidebar.set_elements(sidebar_elements)
        await cl.ElementSidebar.set_title("Uploaded Files")
        
        file_list = [f"- {file.name}" for file in files]
        response = f"**File Processing Complete**\n\nProcessed {len(files)} file(s):\n" + "\n".join(file_list) + f"\n\nMessage: {message.content}\n\nFiles are displayed in the sidebar for reference."
        
    else:
        response = f"**File Processing Mode**\n\nMessage: {message.content}\n\nUpload files to see dynamic sidebar rendering and file processing capabilities."
    
    await cl.Message(content=response).send()

async def show_custom_components():
    """Display custom React components"""
    # Sample custom prompts data
    prompts_data = [
        {
            "id": "1",
            "title": "Summarize Content",
            "prompt": "Please provide a concise summary focusing on the main points and key insights.",
            "icon": "📝",
            "category": "Analysis"
        },
        {
            "id": "2", 
            "title": "Technical Explanation",
            "prompt": "Explain this technical concept in simple terms with practical examples.",
            "icon": "🔧",
            "category": "Technical"
        },
        {
            "id": "3",
            "title": "Creative Ideas",
            "prompt": "Generate 3 innovative ideas with feasibility analysis for each.",
            "icon": "💡",
            "category": "Creative"
        },
        {
            "id": "4",
            "title": "Problem Solving",
            "prompt": "Break down this problem into manageable steps with prioritized solutions.",
            "icon": "🔍",
            "category": "Analysis" 
        },
        {
            "id": "5",
            "title": "Code Review",
            "prompt": "Review this code for improvements in performance, readability, and best practices.",
            "icon": "💻",
            "category": "Technical"
        },
        {
            "id": "6",
            "title": "Business Strategy",
            "prompt": "Develop a strategic business approach with clear objectives and measurable outcomes.",
            "icon": "📊",
            "category": "Business"
        }
    ]
    
    await cl.Message(
        content="🎨 **Custom React Components**\n\nInteractive prompt management system with editable functionality:",
        elements=[
            cl.CustomElement(
                name="CustomPromptsList",
                props={
                    "data": prompts_data,
                    "editable": True
                }
            )
        ]
    ).send()

async def show_info_cards():
    """Display information cards with structured data"""
    info_data = {
        "title": "Chainlit UI Customization Techniques",
        "description": "Advanced UI/UX patterns for modern web applications",
        "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&h=200&fit=crop",
        "category": "UI/UX Demo",
        "features": [
            {"icon": "🎨", "text": "Glassmorphism Effects"},
            {"icon": "⚡", "text": "Smooth Animations"},
            {"icon": "📱", "text": "Responsive Design"},
            {"icon": "🌙", "text": "Dark Mode Support"},
            {"icon": "💾", "text": "Local Storage"},
            {"icon": "🔧", "text": "Custom Components"}
        ],
        "items": [
            {
                "title": "Custom Component System",
                "description": "React-based custom elements with local storage integration for persistent user preferences."
            },
            {
                "title": "Dynamic Info Cards",
                "description": "Flexible card components supporting various content types, images, and interactive features."
            },
            {
                "title": "Modern CSS Techniques",
                "description": "Implementation of cutting-edge CSS features including glassmorphism, gradients, and hover effects."
            }
        ]
    }
    
    await cl.Message(
        content="📋 **Interactive Info Cards**\n\nShowcasing structured data presentation:",
        elements=[
            cl.CustomElement(
                name="InfoCards",
                props={"data": info_data}
            )
        ]
    ).send()

async def show_feature_demo():
    """Comprehensive feature demonstration"""
    await cl.Message(
        content="🚀 **Complete Feature Demonstration**\n\nExploring all customization capabilities:"
    ).send()
    
    # Show all features in sequence
    await show_custom_components()
    await asyncio.sleep(1)
    await show_info_cards()
    
    # Feature summary
    features_text = """
**🎯 Key Features Demonstrated:**

• **Custom React Components**: Interactive elements with real-time state management
• **Dynamic Content Rendering**: Responsive cards and layouts
• **Modern UI Patterns**: Glassmorphism, gradients, and smooth animations
• **File Processing**: Automatic sidebar population based on file types
• **Action Systems**: Contextual buttons with payload handling
• **Theme Support**: Dark/light mode compatibility
• **Responsive Design**: Mobile-first approach with flexible layouts

**💡 Implementation Highlights:**
- Local storage integration for user preferences
- Custom CSS with CSS Grid and Flexbox
- React JSX components in Chainlit
- Dynamic sidebar content management
- Interactive command system
"""
    
    await cl.Message(content=features_text).send()

async def show_ui_settings():
    """Display UI configuration options"""
    try:
        from config_editor import show_config_editor
        await show_config_editor()
    except ImportError:
        await cl.Message(
            content="⚙️ **UI Settings**\n\nConfiguration options would appear here.\n\n*Note: Config editor is optional and not included in this simplified demo.*"
        ).send()

# Action callback handlers
@cl.action_callback("action_summary")
async def on_action_summary(action):
    content = """📝 **Summary Generation**

Creating a comprehensive summary with structured analysis:

**Key Points Extraction:**
• Main themes and concepts
• Supporting details and context  
• Actionable insights and recommendations

The summary will be organized for maximum clarity and usefulness."""

    follow_up_actions = [
        cl.Action(name="action_deep_analysis", label="🔬 Deep Analysis", payload={"action": "deep_analysis"}),
        cl.Action(name="action_questions", label="❓ Related Questions", payload={"action": "questions"}),
        cl.Action(name="action_export", label="📄 Export Summary", payload={"action": "export"})
    ]
    
    await cl.Message(content=content, actions=follow_up_actions).send()

@cl.action_callback("action_detail") 
async def on_action_detail(action):
    content = """🔍 **Detailed Analysis**

Providing comprehensive explanation from multiple perspectives:

**Technical Analysis:**
• Implementation details and specifications
• Advantages and potential limitations
• Use cases and application scenarios

**Practical Considerations:**  
• Real-world implementation factors
• Cost-benefit analysis
• Best practices and recommendations"""

    follow_up_actions = [
        cl.Action(name="action_implementation", label="⚙️ Implementation Guide", payload={"action": "implementation"}),
        cl.Action(name="action_examples", label="💡 Examples", payload={"action": "examples"}),
        cl.Action(name="action_best_practices", label="🎯 Best Practices", payload={"action": "best_practices"})
    ]
    
    await cl.Message(content=content, actions=follow_up_actions).send()

@cl.action_callback("action_components")
async def on_action_components(action):
    await show_custom_components()
    
    guidance_content = """💡 **Custom Component Usage**

• **Interactive Selection**: Click prompts for immediate application
• **Edit Mode**: Modify existing prompts or create new ones
• **Category Organization**: Efficient management by topic area
• **Local Storage**: Persistent customizations across sessions"""

    await cl.Message(content=guidance_content).send()

@cl.action_callback("action_cards")
async def on_action_cards(action):
    await show_info_cards()
    
    tech_content = """🔧 **Info Cards Technology**

Built with modern web technologies:

• **React Components**: Dynamic rendering and state management
• **CSS Grid/Flexbox**: Responsive layout systems
• **Glassmorphism**: Modern visual effects
• **Image Integration**: Dynamic content loading"""

    await cl.Message(content=tech_content).send()

@cl.action_callback("action_demo") 
async def on_action_demo(action):
    await show_feature_demo()

@cl.action_callback("action_settings")
async def on_action_settings(action):
    await show_ui_settings()

# Additional action handlers for follow-up interactions
@cl.action_callback("action_analyze")
async def on_action_analyze(action):
    await cl.Message(content="🔬 **Deep Analysis Mode**\n\nPerforming comprehensive analysis with data correlation and trend identification...").send()

@cl.action_callback("action_expand")
async def on_action_expand(action):
    await cl.Message(content="📈 **Topic Expansion**\n\nExploring related concepts and broader implications...").send()

@cl.action_callback("action_related")
async def on_action_related(action):
    content = """🔗 **Related Topics**

Explore these connected concepts:

• **UI/UX Design Patterns**: Modern interface design principles
• **React Component Architecture**: Building scalable component systems
• **CSS Advanced Techniques**: Contemporary styling approaches
• **Interactive Web Applications**: User engagement strategies"""
    
    await cl.Message(content=content).send()

@cl.action_callback("action_implementation")
async def on_action_implementation(action):
    content = """⚙️ **Implementation Guide**

**Phase 1**: Foundation Setup
- Project initialization and dependencies
- Basic structure and configuration

**Phase 2**: Core Development  
- Component implementation
- Styling and responsive design

**Phase 3**: Enhancement
- Interactive features and animations
- Testing and optimization"""
    
    await cl.Message(content=content).send()

if __name__ == "__main__":
    print("Chainlit UI Customization Demo")
    print("Run with: chainlit run main.py")
