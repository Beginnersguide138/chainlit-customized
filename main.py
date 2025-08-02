import chainlit as cl
from typing import Dict, Any, List
import asyncio
import json

# Simple landing page HTML
landing_page_html = """
<div class"wrapper">
<div class="compact-hero">
    <div class="hero-content">
        <h1 class="hero-title">
            🚀 Chainlit Customization Demo
        </h1>
        <p class="hero-subtitle">
            Demo app showcasing commercial project customization techniques
        </p>
        <div class="features-grid">
            <span class="feature-item">🎨 Custom Prompts</span>
            <span class="feature-item">📋 Tech Info Cards</span>
            <span class="feature-item">🚀 Full Feature Demo</span>
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
        name="AI Assistant",
        markdown_description=landing_page_html,
        icon="https://img.icons8.com/?size=100&id=eoxMN35Z6JKg&format=png&color=000000",
        default=True,
        starters=[
            cl.Starter(
                label="🎨 Custom Prompt Management",
                message="🎨",
            ),
            cl.Starter(
                label="📋 Tech Info Cards",
                message="📋",
            ),
            cl.Starter(
                label="🚀 Full Feature Demo",
                message="demo",
            )
        ]
    ),
    cl.ChatProfile(
        name="Web Search",
        markdown_description="Assistant with web search capabilities. Finds the latest information.\n\n*Note: This demo does not perform actual searches.*",
        icon="https://img.icons8.com/?size=100&id=BpLxiRbSRN80&format=png",
        starters=[
            cl.Starter(
                label="Search Demo",
                message="Please search for the latest AI technologies",
            ),
            cl.Starter(
                label="News Search",
                message="Tell me about today's tech-related news",
            )
        ]
    ),
    cl.ChatProfile(
        name="Document Helper",
        markdown_description="Assistant specialized in document analysis and summarization.\n\nUpload files to try the analysis features.",
        icon="https://img.icons8.com/?size=100&id=85784&format=png",
        starters=[
            cl.Starter(
                label="File Analysis Explanation",
                message="Please explain the file analysis features",
            ),
            cl.Starter(
                label="Supported File Formats",
                message="What file formats are supported?",
            )
        ]
    )
]

@cl.set_chat_profiles
async def chat_profile():
    return chat_profiles

@cl.on_chat_start
async def start():
    # Command configuration
    commands = [
        {"id": "search", "icon": "search", "description": "Web search functionality"},
        {"id": "analysis", "icon": "chart-bar", "description": "Data analysis & insights"},
        {"id": "custom", "icon": "palette", "description": "Show custom prompts"},
        {"id": "info", "icon": "info", "description": "Show tech info cards"},
        {"id": "demo", "icon": "rocket", "description": "Full feature demo"}
    ]
    
    await cl.context.emitter.set_commands(commands)

@cl.on_message
async def main(message: cl.Message):
    chat_profile = cl.user_session.get("chat_profile")
    
    if chat_profile == "AI Assistant":
        await handle_ai_assistant(message)
    elif chat_profile == "Web Search":
        await handle_web_search(message)
    elif chat_profile == "Document Helper":
        await handle_document_helper(message)
    else:
        await cl.Message(content="Please select a profile.").send()

async def handle_ai_assistant(message: cl.Message):
    # Process commands with highest priority
    if message.command:
        command = message.command
        if command == "search":
            response = f"🔍 **Web Search Command Executed**\n\nSearch Query: {message.content}\n\n(Actual search functionality is not implemented)"
            await cl.Message(content=response).send()
            return
        elif command == "analysis":
            response = f"📊 **Data Analysis Command Executed**\n\nAnalysis Target: {message.content}\n\nRunning advanced analysis...\n\n(Actual analysis functionality is not implemented)"
            await cl.Message(content=response).send()
            return
        elif command == "custom":
            await show_custom_prompts()
            return
        elif command == "info":
            await show_info_cards()
            return
        elif command == "demo":
            await show_feature_demo()
            return
    
    # Handle special content messages
    if message.content == "🎨":
        await show_custom_prompts()
        return
    elif message.content in ["📋", "info"]:
        await show_info_cards()
        return
    elif message.content.lower() in ["demo", "features"]:
        await show_feature_demo()
        return
    
    # Basic response
    response = f"AI Assistant responding:\\n\\nLet me think about {message.content}."
    
    # Message with actions
    actions = [
        cl.Action(name="action_summary", label="📝 Create Summary", payload="summary"),
        cl.Action(name="action_detail", label="🔍 Explain Details", payload="detail"),
        cl.Action(name="action_custom", label="🎨 Custom Prompts", payload="custom"),
        cl.Action(name="action_info", label="📋 Tech Info", payload="info"),
        cl.Action(name="action_demo", label="⭐ Full Demo", payload="demo"),
    ]
    
    await cl.Message(content=response, actions=actions).send()

async def show_feature_demo():
    """Display full feature demo"""
    await cl.Message(
        content="🚀 **Chainlit Customization Demo - All Features**\\n\\nExperience each feature with the following commands:"
    ).send()
    
    # Feature description
    features_text = """
**📱 Basic Features:**
- `🎨` - Custom prompt management (add, edit, delete)
- `📋` - Tech info card display

**🎯 Advanced Features:**
- Glassmorphism effects
- Neumorphism UI
- Responsive design
- Dark mode support
- Local storage utilization

**💡 Usage Tips:**
- Upload files to try Document Helper
- Experience different features in each profile
- Quick access to features via action buttons
"""
    
    await cl.Message(content=features_text).send()
    
    # 全機能の実際のデモ
    await show_custom_prompts()
    await asyncio.sleep(1)
    await show_info_cards()

async def handle_web_search(message: cl.Message):
    response = f"Web Search mode active.\n\nSearch Query: {message.content}\n\n(Actual search functionality is not implemented)"
    await cl.Message(content=response).send()

async def handle_document_helper(message: cl.Message):
    # File processing example
    files = message.elements or []
    
    if files:
        file_list = [f"- {file.name}" for file in files]
        response = f"Analyzed uploaded files ({len(files)} files).\n\n" + "\n".join(file_list) + f"\n\nQuestion: {message.content}"
    else:
        response = f"Document Helper responding:\n\n{message.content}\n\nUpload files for more detailed analysis."
    
    await cl.Message(content=response).send()

async def show_custom_prompts():
    # Custom prompt sample data
    prompts_data = [
        {
            "id": "1",
            "title": "Create Summary",
            "prompt": "Please summarize the following content concisely. Focus on 3 key points.",
            "icon": "📝",
            "category": "Analysis"
        },
        {
            "id": "2", 
            "title": "Technical Explanation",
            "prompt": "Please explain technical content in an easy-to-understand way. Avoid jargon and make it accessible to beginners.",
            "icon": "🔧",
            "category": "Development"
        },
        {
            "id": "3",
            "title": "Idea Generation",
            "prompt": "Please propose 3 creative ideas. Include feasibility considerations in your explanation.",
            "icon": "💡",
            "category": "Creative"
        },
        {
            "id": "4",
            "title": "Problem Solving",
            "prompt": "Please propose step-by-step solutions to this problem. Include priority considerations.",
            "icon": "🔍",
            "category": "Analysis" 
        },
        {
            "id": "5",
            "title": "Code Review",
            "prompt": "Please point out improvements for this code. Focus on performance and readability aspects.",
            "icon": "💻",
            "category": "Development"
        },
        {
            "id": "6",
            "title": "Business Proposal",
            "prompt": "Please format the proposal as a business plan. Clearly define objectives, methods, and expected outcomes.",
            "icon": "📊",
            "category": "Business"
        }
    ]
    
    # Display advanced custom prompt list
    await cl.Message(
        content="🎨 **Custom Prompt Menu**\n\nSelect from below or create your own prompts in editable mode:",
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
    # Info card sample data
    info_data = {
        "title": "Chainlit Customization Technology",
        "description": "Generalized advanced UI/UX techniques learned from sample projects",
        "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&h=200&fit=crop",
        "category": "Tech Demo",
        "features": [
            {"icon": "🎨", "text": "Glassmorphism Effects"},
            {"icon": "⚡", "text": "High-Performance Animations"},
            {"icon": "📱", "text": "Responsive Design"},
            {"icon": "🌙", "text": "Dark Mode Support"},
            {"icon": "💾", "text": "Local Storage Utilization"},
            {"icon": "🔧", "text": "Custom Components"}
        ],
        "items": [
            {
                "title": "Custom Prompt Management",
                "description": "Local storage-based prompt management system. Supports add, edit, and delete operations."
            },
            {
                "title": "Info Card Display",
                "description": "Card components that beautifully display structured information. Supports background images and animation effects."
            },
            {
                "title": "Advanced CSS Effects",
                "description": "Utilizes latest CSS technologies including neumorphism, glassmorphism, and hover effects."
            }
        ]
    }
    
    await cl.Message(
        content="📋 **Tech Info Cards**\n\nDetails of implemented technologies:",
        elements=[
            cl.CustomElement(
                name="InfoCards",
                props={"data": info_data}
            )
        ]
    ).send()


@cl.action_callback("action_summary")
async def on_action_summary(action):
    """Summary creation action - send additional messages and related questions"""
    summary_content = """📝 **Starting Summary Creation**

I will concisely summarize the following content, organizing it into 3 key points:

**Summary Perspectives:**
• Main points and themes
• Important details and background information  
• Conclusions and recommendations

Once the summary is complete, feel free to ask for more detailed analysis or related questions."""

    # Additional actions with message
    follow_up_actions = [
        cl.Action(name="action_analysis_deep", label="🔬 Deep Analysis", payload="deep_analysis"),
        cl.Action(name="action_questions", label="❓ Related Questions", payload="questions"),
        cl.Action(name="action_export_summary", label="📄 Export Summary", payload="export_summary")
    ]
    
    await cl.Message(content=summary_content, actions=follow_up_actions).send()

@cl.action_callback("action_detail") 
async def on_action_detail(action):
    """Detailed explanation action - provide additional messages and professional perspectives"""
    detail_content = """🔍 **Starting Detailed Explanation**

I will explain in detail from the following perspectives:

**Technical Perspective:**
• Implementation methods and technical specifications
• Advantages and disadvantages
• Use cases and application scope

**Business Perspective:**  
• Practicality and effectiveness
• Cost and ROI
• Implementation considerations

After the detailed explanation, I can also answer questions about specific implementation methods or additional technical information."""

    # Additional actions with message
    follow_up_actions = [
        cl.Action(name="action_implementation", label="⚙️ Implementation", payload="implementation"),
        cl.Action(name="action_examples", label="💡 Examples", payload="examples"),
        cl.Action(name="action_best_practices", label="🎯 Best Practices", payload="best_practices")
    ]
    
    await cl.Message(content=detail_content, actions=follow_up_actions).send()

@cl.action_callback("action_custom")
async def on_action_custom(action):
    """Custom prompt display - also suggest related features"""
    await show_custom_prompts()
    
    # Additional guidance message
    guidance_content = """💡 **Custom Prompt Usage Tips**

• Select prompts for immediate application
• Create and edit your own prompts
• Efficient management organized by categories

Feel free to ask about more effective usage methods."""

    guidance_actions = [
        cl.Action(name="action_prompt_tips", label="📚 Usage Tips", payload="prompt_tips"),
        cl.Action(name="action_create_prompt", label="✏️ Create New", payload="create_prompt")
    ]
    
    await cl.Message(content=guidance_content, actions=guidance_actions).send()

@cl.action_callback("action_info")
async def on_action_info(action):
    """Tech info display - also guide about related technologies"""
    await show_info_cards()
    
    # Technical follow-up
    tech_content = """🔧 **About Technical Information Details**

Which areas would you like to know more about regarding the displayed technical information?

• **Frontend Technologies**: React, CSS effects, animations
• **Backend Technologies**: Chainlit, Python, API design  
• **UI/UX Design**: Responsive, accessibility
• **Performance**: Optimization, loading, memory management"""

    tech_actions = [
        cl.Action(name="action_frontend", label="🎨 Frontend", payload="frontend"),
        cl.Action(name="action_backend", label="⚙️ Backend", payload="backend"),
        cl.Action(name="action_performance", label="⚡ Performance", payload="performance")
    ]
    
    await cl.Message(content=tech_content, actions=tech_actions).send()

@cl.action_callback("action_demo") 
async def on_action_demo(action):
    """Full feature demo - also provide customization tips"""
    await show_feature_demo()
    
    # Customization guidance
    customization_content = """🛠️ **Customization Tips**

The technologies showcased in this demo can be customized for various purposes:

• **Enterprise Dashboards**: Apply brand colors and logos
• **Educational Platforms**: Visualize learning progress
• **Customer Support Systems**: FAQ integration and ticket management
• **Data Analysis Tools**: Chart display and report generation

I can also support specific customization methods."""

    customization_actions = [
        cl.Action(name="action_branding", label="🎨 Branding", payload="branding"),
        cl.Action(name="action_integration", label="🔗 System Integration", payload="integration"),
        cl.Action(name="action_deployment", label="🚀 Deployment", payload="deployment")
    ]
    
    await cl.Message(content=customization_content, actions=customization_actions).send()

# Additional action callback functions
@cl.action_callback("action_analysis_deep")
async def on_action_analysis_deep(action):
    await cl.Message(content="🔬 **Running Deep Analysis**\n\nPerforming data deep analysis, trend identification, and correlation detection...").send()

@cl.action_callback("action_questions")
async def on_action_questions(action):
    questions_content = """❓ **Related Question Suggestions**

You can ask additional questions from the following perspectives:

• How can this information be utilized in business?
• Are there similar technologies or alternatives?
• What are the implementation considerations and risks?
• What are the cost and effort estimates?"""
    
    await cl.Message(content=questions_content).send()

@cl.action_callback("action_implementation")
async def on_action_implementation(action):
    impl_content = """⚙️ **Implementation Method Details**

I propose a phased implementation approach:

**Phase 1**: Foundation building and setup
**Phase 2**: Core functionality implementation
**Phase 3**: UI/UX adjustment and optimization
**Phase 4**: Testing and production deployment

I will explain the details of each phase."""
    
    await cl.Message(content=impl_content).send()

@cl.action_callback("action_frontend")
async def on_action_frontend(action):
    frontend_content = """🎨 **Frontend Technology Details**

Main frontend technologies used in this demo:

• **React Components**: Custom component design patterns
• **CSS Effects**: Glassmorphism and neumorphism effects
• **Animations**: Canvas API, CSS Transform, Transition
• **Responsive Design**: Mobile-first, flexible layouts"""
    
    await cl.Message(content=frontend_content).send()

if __name__ == "__main__":
    print("Chainlit Customization Demo - Run with: chainlit run main.py")
