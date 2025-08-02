# Chainlit Customization Demo

A demo application showcasing various Chainlit customization features and techniques.

## 🚀 Features

### Chat Profiles
- **AI Assistant**: General-purpose AI assistant
- **Web Search**: Assistant with web search functionality
- **Document Helper**: Document analysis specialist

### Custom UI Elements
- Custom prompt selection interface
- Interactive action buttons
- File upload support
- Responsive design

### Advanced Features
- Dynamic chat profile switching
- Custom React component integration
- CSS/JavaScript UI customization
- File processing with drag & drop
- **Right-side panel file display** - Uploaded files are automatically displayed in the side panel for reference

## 🛠️ Tech Stack

- **Chainlit 2.6.4+**: Chat UI framework
- **Python 3.13+**: Backend implementation
- **React/JSX**: Custom UI components
- **uv**: Package management

## 📦 Installation

### Prerequisites
- Python 3.13+
- uv package manager

### Setup

```bash
# Clone repository
git clone <repository-url>
cd chainlit-customized

# Install dependencies
uv sync

# Launch application
uv run chainlit run main.py
```

## 🎯 Usage

1. **Launch Application**
   ```bash
   uv run chainlit run main.py
   ```

2. **Access in Browser**
   - Default: http://localhost:8000
   - Select a chat profile from the sidebar

3. **Try Features**
   - **Basic Chat**: Type any message to interact with the AI Assistant
   - **Custom Prompts**: Send `🎨` to display the custom prompt selection menu
   - **Tech Info**: Send `📋` or "info" to show technical information cards
   - **Full Demo**: Send "demo" to see all available features
   - **File Upload**: In Document Helper profile, drag & drop or upload files for analysis
   - **Right-side Panel**: Uploaded files automatically appear in the side panel for easy reference
   - **Action Buttons**: Click on action buttons that appear after sending messages

## 🎨 Customization Elements

### 1. Custom Prompts (`CustomPrompts.jsx`)
```jsx
// Prompt selection UI
<CustomElement name="CustomPrompts" props={{data: prompts}} />
```

### 2. Style Customization (`styles.css`)
- Theme management with CSS variables
- Responsive design
- Animation effects

### 3. JavaScript Extensions (`script.js`)
- File drop functionality
- Toast notifications
- Interactive elements

## 📁 Project Structure

```
chainlit-customized/
├── main.py                 # Main application
├── chainlit.md            # Welcome message
├── pyproject.toml         # Project configuration
└── public/                # Static files
    ├── elements/          # Custom React components
    │   ├── CustomPrompts.jsx
    │   └── InfoCards.jsx
    ├── styles.css         # Custom styles
    └── script.js          # Custom JavaScript
```

## 🔧 Customization Examples

### Adding Chat Profiles
```python
chat_profiles = [
    cl.ChatProfile(
        name="New Assistant",
        markdown_description="Description of new assistant",
        icon="https://example.com/icon.png",
        starters=[
            cl.Starter(
                label="Quick Start",
                message="Hello, how can you help me?"
            )
        ]
    )
]
```

### Creating Custom Elements
```python
await cl.Message(
    content="Custom element example",
    elements=[
        cl.CustomElement(
            name="YourCustomComponent",
            props={"data": your_data}
        )
    ]
).send()
```

### Adding Custom Prompts
```python
# In show_custom_prompts() function
prompts_data = [
    {
        "id": "custom1",
        "title": "Your Custom Prompt",
        "prompt": "Your prompt text here",
        "icon": "🆕",
        "category": "Custom"
    }
]
```

### Right-side Panel Implementation
```python
# Display files in side panel
sidebar_elements = []
for file in files:
    if file.mime and file.mime.startswith('image/'):
        sidebar_elements.append(cl.Image(name=file.name, path=file.path))
    elif file.mime == 'application/pdf':
        sidebar_elements.append(cl.Pdf(name=file.name, path=file.path))
    else:
        sidebar_elements.append(cl.Text(name=file.name, content=content))

await cl.ElementSidebar.set_elements(sidebar_elements)
await cl.ElementSidebar.set_title("アップロードファイル")
```

### Styling with CSS Variables
```css
:root {
  --primary-color: #667eea;
  --surface-color: white;
  --text-color: #1f2937;
  --border-color: #e5e7eb;
}

[data-theme="dark"] {
  --surface-color: #1f2937;
  --text-color: #f9fafb;
  --border-color: #374151;
}
```

## 🎬 Demo Features

1. **Basic Chat**: Interaction with each profile
2. **Custom Prompts**: `🎨` command for prompt selection with editable interface
3. **File Processing**: Document Helper file upload with analysis
4. **Right-side Panel Display**: Uploaded files automatically displayed in side panel
5. **Action Buttons**: Interactive UI components with follow-up actions
6. **Theme Support**: Automatic dark/light mode detection
7. **Responsive Design**: Works on desktop and mobile devices
8. **Local Storage**: Custom prompts are saved locally
9. **Command System**: Built-in commands for quick access to features

## 🛠️ Development

### File Structure Details
- `main.py`: Core application logic and chat handlers
- `.chainlit/config.toml`: Configuration with wide layout for side panel
- `public/elements/`: React components for custom UI elements
- `public/styles.css`: Global styles and theme variables
- `public/themeToggle.js`: Theme switching functionality
- `chainlit.md`: Welcome message displayed on startup
- `USAGE.md`: Detailed usage guide and customization instructions

### Adding New Features
1. **New Chat Profile**: Add to `chat_profiles` list and create handler function
2. **Custom Component**: Create JSX file in `public/elements/` and use with `cl.CustomElement`
3. **New Commands**: Add to `commands` list in `start()` function
4. **Right-side Panel**: Use `cl.ElementSidebar.set_elements()` to display content
5. **Styling**: Use CSS variables for consistent theming

### Troubleshooting
- **Port in use**: Use `--port 8001` flag
- **Module errors**: Run `uv sync` to install dependencies
- **Custom elements not loading**: Check JSX syntax and file names
- **Styles not applying**: Verify CSS variable names and theme selectors

## 🤝 Contributing

This project is created for learning and sharing Chainlit customization techniques.

### Improvement Suggestions
- Add new customization techniques
- UI/UX improvements
- Performance optimization
- Documentation improvements
- More interactive examples
- Additional React components

## 📝 License

This project is released under the MIT License.

## 🔗 Related Links

- [Chainlit Official Documentation](https://docs.chainlit.io/)
- [Python uv](https://github.com/astral-sh/uv)
