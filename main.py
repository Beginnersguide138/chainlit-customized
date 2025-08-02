import chainlit as cl
from typing import Dict, Any, List
import asyncio

# ランディングページHTML
landing_page_html = """
<div class="custom-hero">
    <div class="hero-background"></div>
    <div class="hero-content">
        <div class="hero-text">
            <h1 class="hero-title">
                🚀 Chainlit カスタマイズデモ
            </h1>
            <h2 class="hero-subtitle">
                商用プロジェクトのカスタマイズ手法を一般化したデモアプリ
            </h2>
            <h3 class="hero-description">
                様々なChainlitカスタマイズ機能を体験できます
            </h3>
            <div class="hero-tips">
                <p class="tip-item">💡 ヒント: <code>🎨</code> を送信するとカスタムプロンプトメニューが表示されます</p>
                <p class="tip-item">📁 ファイルをアップロードしてDocument Helperを試してみてください</p>
                <p class="tip-item">⚡ 各プロファイルで異なる機能を体験できます</p>
            </div>
        </div>
    </div>
</div>

<style>
.custom-hero {
    position: relative;
    min-height: 60vh;
    display: flex;
    align-items: center;
    justify-content: center;
    overflow: hidden;
    border-radius: 16px;
    margin: 20px 0;
}

.hero-background {
    position: absolute;
    top: 0;
    left: 0;
    right: 0;
    bottom: 0;
    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
    opacity: 0.9;
}

[data-theme="dark"] .hero-background {
    background: linear-gradient(135deg, #1e3a8a 0%, #312e81 100%);
}

.hero-content {
    position: relative;
    z-index: 2;
    text-align: center;
    padding: 40px 20px;
    color: white;
    max-width: 800px;
}

.hero-title {
    font-size: 2.5rem;
    font-weight: 700;
    margin-bottom: 16px;
    text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.3);
    line-height: 1.2;
}

.hero-subtitle {
    font-size: 1.4rem;
    font-weight: 500;
    margin-bottom: 12px;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    opacity: 0.95;
}

.hero-description {
    font-size: 1.1rem;
    font-weight: 400;
    margin-bottom: 32px;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.3);
    opacity: 0.9;
}

.hero-tips {
    background: rgba(255, 255, 255, 0.1);
    backdrop-filter: blur(10px);
    border-radius: 12px;
    padding: 24px;
    border: 1px solid rgba(255, 255, 255, 0.2);
}

.tip-item {
    margin: 12px 0;
    font-size: 0.95rem;
    display: flex;
    align-items: center;
    justify-content: center;
    text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.2);
}

.tip-item code {
    background: rgba(255, 255, 255, 0.2);
    padding: 2px 8px;
    border-radius: 4px;
    font-family: 'Monaco', 'Menlo', monospace;
    margin: 0 4px;
}

@media (max-width: 768px) {
    .hero-title {
        font-size: 2rem;
    }
    
    .hero-subtitle {
        font-size: 1.2rem;
    }
    
    .hero-description {
        font-size: 1rem;
    }
    
    .tip-item {
        font-size: 0.9rem;
        text-align: left;
    }
}
</style>
"""

# チャットプロファイル設定
chat_profiles = [
    cl.ChatProfile(
        name="AI Assistant",
        markdown_description=landing_page_html,
        icon="https://img.icons8.com/?size=128&id=kTuxVYRKeKEY&format=png",
        default=True,
        starters=[
            cl.Starter(
                label="カスタムプロンプトを開く",
                message="🎨",
                icon="🎨"
            ),
            cl.Starter(
                label="要約機能を試す",
                message="この機能について詳しく説明してください",
                icon="📝"
            ),
            cl.Starter(
                label="詳細説明を試す",
                message="Chainlitのカスタマイズについて教えてください",
                icon="🔍"
            )
        ]
    ),
    cl.ChatProfile(
        name="Web Search",
        markdown_description="Web検索機能付きのアシスタント。最新情報を調べます。\n\n*注意: このデモでは実際の検索は行いません。*",
        icon="https://img.icons8.com/?size=100&id=BpLxiRbSRN80&format=png",
        starters=[
            cl.Starter(
                label="検索デモ",
                message="最新のAI技術について調べてください",
                icon="🔍"
            ),
            cl.Starter(
                label="ニュース検索",
                message="今日のテック関連ニュースを教えてください",
                icon="📰"
            )
        ]
    ),
    cl.ChatProfile(
        name="Document Helper",
        markdown_description="ドキュメント分析・要約が得意なアシスタント。\n\nファイルをアップロードして分析機能を試してみてください。",
        icon="https://img.icons8.com/?size=100&id=85784&format=png",
        starters=[
            cl.Starter(
                label="ファイル分析の説明",
                message="ファイル分析機能について教えてください",
                icon="📄"
            ),
            cl.Starter(
                label="対応ファイル形式",
                message="どのようなファイル形式に対応していますか？",
                icon="📋"
            )
        ]
    )
]

@cl.set_chat_profiles
async def chat_profile():
    return chat_profiles

@cl.on_chat_start
async def start():
    # プロファイル切り替え時にメッセージを送信しない
    # ランディングページHTMLで情報を表示
    pass

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
        await cl.Message(content="プロファイルを選択してください。").send()

async def handle_ai_assistant(message: cl.Message):
    # カスタムプロンプト呼び出し
    if message.content == "🎨":
        await show_custom_prompts()
        return
    
    # 基本的な応答
    response = f"AI Assistant として回答します：\n\n{message.content} について考えてみますね。"
    
    # アクション付きメッセージ
    actions = [
        cl.Action(name="action_summary", label="📝 要約を作成", value="summary"),
        cl.Action(name="action_detail", label="🔍 詳細を説明", value="detail"),
        cl.Action(name="action_custom", label="🎨 カスタムプロンプト", value="custom"),
    ]
    
    await cl.Message(content=response, actions=actions).send()

async def handle_web_search(message: cl.Message):
    response = f"Web Search モードです。\n\n検索クエリ：{message.content}\n\n（実際の検索機能は実装されていません）"
    await cl.Message(content=response).send()

async def handle_document_helper(message: cl.Message):
    # ファイル処理の例
    files = message.elements or []
    
    if files:
        file_list = [f"- {file.name}" for file in files]
        response = f"アップロードされたファイル（{len(files)}個）を分析しました。\n\n" + "\n".join(file_list) + f"\n\n質問：{message.content}"
    else:
        response = f"Document Helper として回答します：\n\n{message.content}\n\nファイルをアップロードすると、より詳細な分析が可能です。"
    
    await cl.Message(content=response).send()

async def show_custom_prompts():
    # カスタムプロンプトのサンプルデータ
    prompts_data = [
        {
            "title": "要約作成",
            "prompt": "以下の内容を簡潔に要約してください。",
            "icon": "📝"
        },
        {
            "title": "技術説明",
            "prompt": "技術的な内容を分かりやすく説明してください。",
            "icon": "🔧"
        },
        {
            "title": "アイデア生成",
            "prompt": "創造的なアイデアを3つ提案してください。",
            "icon": "💡"
        }
    ]
    
    # カスタム要素でプロンプト選択UI表示
    await cl.Message(
        content="カスタムプロンプトを選択してください：",
        elements=[
            cl.CustomElement(
                name="CustomPrompts",
                props={"data": prompts_data}
            )
        ]
    ).send()

@cl.action_callback("action_summary")
async def on_action_summary(action):
    await cl.Message(content="📝 要約を作成します...").send()

@cl.action_callback("action_detail") 
async def on_action_detail(action):
    await cl.Message(content="🔍 詳細を説明します...").send()

@cl.action_callback("action_custom")
async def on_action_custom(action):
    await show_custom_prompts()

if __name__ == "__main__":
    print("Chainlit Customized Demo - Run with: chainlit run main.py")
