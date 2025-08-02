# Usage Guide

## 🚀 Quick Start

### 1. Application Launch

```bash
# Install dependencies (first time only)
uv sync

# Launch application
uv run chainlit run main.py
```

Access http://localhost:8000 in your browser

### 2. Chat Profile Selection

You can select from the following profiles in the left panel:

- **AI Assistant**: General-purpose chat
- **Web Search**: Search functionality demo
- **Document Helper**: File processing demo

## 🎨 How to Use Features

### Custom Prompt Menu

Send `🎨` in any profile to display the custom prompt selection UI.

Example:
```
🎨
```

### Action Buttons

When you send a message in the AI Assistant profile, the following action buttons will appear:

- **📝 Create Summary**: Summary function demo
- **🔍 Explain Details**: Detailed explanation function demo  
- **🎨 Custom Prompts**: Display prompt selection UI

### File Upload

When you upload files in the Document Helper profile, file information will be displayed.

Supported file formats:
- Text files (.txt, .md)
- Image files (.jpg, .png, .gif)
- PDF files (.pdf)
- Other file formats

## 🛠️ Customization Methods

### Adding New Chat Profiles

Add to the `chat_profiles` list in `main.py`:

```python
chat_profiles = [
    # Existing profiles...
    cl.ChatProfile(
        name="Your New Profile",
        markdown_description="Description of new profile",
        icon="https://example.com/icon.png",
    )
]
```

Also add corresponding handler function:

```python
@cl.on_message
async def main(message: cl.Message):
    chat_profile = cl.user_session.get("chat_profile")
    
    if chat_profile == "Your New Profile":
        await handle_your_new_profile(message)
    # Other conditions...

async def handle_your_new_profile(message: cl.Message):
    # Processing logic for new profile
    await cl.Message(content=f"New profile: {message.content}").send()
```

### Adding Custom Prompts

Edit `prompts_data` in the `show_custom_prompts()` function:

```python
prompts_data = [
    {
        "title": "New Prompt",
        "prompt": "Your custom prompt text",
        "icon": "🆕"
    },
    # Existing prompts...
]
```

### Customizing UI Elements

1. **CSS**: Edit styles in `public/styles.css`
2. **JavaScript**: Add functionality in `public/script.js`
3. **React Elements**: Create new components in `public/elements/`

### Creating New React Components

1. Create `public/elements/YourComponent.jsx`:

```jsx
import React from 'react';

export default function YourComponent({ data }) {
  return (
    <div className="your-component">
      <h3>{data.title}</h3>
      <p>{data.content}</p>
    </div>
  );
}
```

2. Use in Python code:

```python
await cl.Message(
    content="Custom component example",
    elements=[
        cl.CustomElement(
            name="YourComponent",
            props={
                "data": {
                    "title": "Title",
                    "content": "Content"
                }
            }
        )
    ]
).send()
```

## 🔧 Troubleshooting

### Common Issues

1. **Module not found**
   ```bash
   uv sync
   ```

2. **Port in use**
   ```bash
   uv run chainlit run main.py --port 8001
   ```

3. **Custom elements not displaying**
   - Check file names and component names in `public/elements/`
   - Check for JSX syntax errors

### Debugging Methods

1. **Check console logs**
   - Check console in browser developer tools (F12)

2. **Check server logs**
   - Check Chainlit server logs in terminal

3. **Python syntax check**
   ```bash
   uv run python -c "import main"
   ```

## 📚 Further Learning

- [Chainlit Official Documentation](https://docs.chainlit.io/)
- [React Official Documentation](https://react.dev/)
- Refer to implementation examples in `sample/dione/` directory

---

*This guide explains basic usage methods. For more advanced customization, please refer to sample code and official documentation.*