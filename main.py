import chainlit as cl
from typing import Dict, Any, List
import asyncio
import json

# 簡素なランディングページHTML
landing_page_html = """
<div class"wrapper">
<div class="compact-hero">
    <div class="hero-content">
        <h1 class="hero-title">
            🚀 Chainlit カスタマイズデモ
        </h1>
        <p class="hero-subtitle">
            商用プロジェクトのカスタマイズ手法を一般化したデモアプリ
        </p>
        <div class="features-grid">
            <span class="feature-item">🎨 カスタムプロンプト</span>
            <span class="feature-item">📋 技術情報カード</span>
            <span class="feature-item">🚀 全機能デモ</span>
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

# チャットプロファイル設定
chat_profiles = [
    cl.ChatProfile(
        name="AI Assistant",
        markdown_description=landing_page_html,
        icon="https://img.icons8.com/?size=100&id=eoxMN35Z6JKg&format=png&color=000000",
        default=True,
        starters=[
            cl.Starter(
                label="🎨 カスタムプロンプト管理",
                message="🎨",
            ),
            cl.Starter(
                label="📋 技術情報カード",
                message="📋",
            ),
            cl.Starter(
                label="🚀 全機能デモ",
                message="demo",
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
            ),
            cl.Starter(
                label="ニュース検索",
                message="今日のテック関連ニュースを教えてください",
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
            ),
            cl.Starter(
                label="対応ファイル形式",
                message="どのようなファイル形式に対応していますか？",
            )
        ]
    )
]

@cl.set_chat_profiles
async def chat_profile():
    return chat_profiles

@cl.on_chat_start
async def start():
    # コマンドの設定
    commands = [
        {"id": "search", "icon": "search", "description": "Web検索機能"},
        {"id": "analysis", "icon": "chart-bar", "description": "データ分析・解析"},
        {"id": "custom", "icon": "palette", "description": "カスタムプロンプト表示"},
        {"id": "info", "icon": "info", "description": "技術情報カード表示"},
        {"id": "demo", "icon": "rocket", "description": "全機能デモ"}
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
        await cl.Message(content="プロファイルを選択してください。").send()

async def handle_ai_assistant(message: cl.Message):
    # コマンドの処理を最優先で行う
    if message.command:
        command = message.command
        if command == "search":
            response = f"🔍 **Web検索コマンド実行**\n\n検索クエリ: {message.content}\n\n（実際の検索機能は実装されていません）"
            await cl.Message(content=response).send()
            return
        elif command == "analysis":
            response = f"📊 **データ分析コマンド実行**\n\n分析対象: {message.content}\n\n高度な分析を実行中...\n\n（実際の分析機能は実装されていません）"
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
    
    # 特殊コンテンツメッセージの処理
    if message.content == "🎨":
        await show_custom_prompts()
        return
    elif message.content in ["📋", "info", "情報"]:
        await show_info_cards()
        return
    elif message.content.lower() in ["demo", "デモ", "機能一覧"]:
        await show_feature_demo()
        return
    
    # 基本的な応答
    response = f"AI Assistant として回答します：\\n\\n{message.content} について考えてみますね。"
    
    # アクション付きメッセージ
    actions = [
        cl.Action(name="action_summary", label="📝 要約を作成", payload="summary"),
        cl.Action(name="action_detail", label="🔍 詳細を説明", payload="detail"),
        cl.Action(name="action_custom", label="🎨 カスタムプロンプト", payload="custom"),
        cl.Action(name="action_info", label="📋 技術情報", payload="info"),
        cl.Action(name="action_demo", label="⭐ 全機能デモ", payload="demo"),
    ]
    
    await cl.Message(content=response, actions=actions).send()

async def show_feature_demo():
    """全機能のデモを表示"""
    await cl.Message(
        content="🚀 **Chainlit カスタマイズデモ - 全機能**\\n\\n以下のコマンドで各機能を体験できます："
    ).send()
    
    # 機能説明
    features_text = """
**📱 基本機能:**
- `🎨` - カスタムプロンプト管理（追加・編集・削除可能）
- `📋` - 技術情報カード表示

**🎯 高度な機能:**
- グラスモーフィズム効果
- ネオモーフィズムUI
- レスポンシブデザイン
- ダークモード対応
- ローカルストレージ活用

**💡 使い方のヒント:**
- ファイルをアップロードして Document Helper を試してみてください
- 各プロファイルで異なる機能を体験できます
- アクションボタンで素早く機能にアクセスできます
"""
    
    await cl.Message(content=features_text).send()
    
    # 全機能の実際のデモ
    await show_custom_prompts()
    await asyncio.sleep(1)
    await show_info_cards()

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
            "id": "1",
            "title": "要約作成",
            "prompt": "以下の内容を簡潔に要約してください。重要なポイントを3つに絞ってお願いします。",
            "icon": "📝",
            "category": "Analysis"
        },
        {
            "id": "2", 
            "title": "技術説明",
            "prompt": "技術的な内容を分かりやすく説明してください。専門用語は避けて、初心者にも理解できるようにお願いします。",
            "icon": "🔧",
            "category": "Development"
        },
        {
            "id": "3",
            "title": "アイデア生成",
            "prompt": "創造的なアイデアを3つ提案してください。実現可能性も含めて説明してお願いします。",
            "icon": "💡",
            "category": "Creative"
        },
        {
            "id": "4",
            "title": "問題解決",
            "prompt": "この問題に対する解決策を段階的に提案してください。優先順位も含めてお願いします。",
            "icon": "🔍",
            "category": "Analysis" 
        },
        {
            "id": "5",
            "title": "コードレビュー",
            "prompt": "このコードの改善点を指摘してください。パフォーマンスと可読性の観点からお願いします。",
            "icon": "💻",
            "category": "Development"
        },
        {
            "id": "6",
            "title": "企画書作成",
            "prompt": "ビジネス企画書のフォーマットで提案をまとめてください。目標・手段・期待効果を明確にお願いします。",
            "icon": "📊",
            "category": "Business"
        }
    ]
    
    # 高度なカスタムプロンプトリスト表示
    await cl.Message(
        content="🎨 **カスタムプロンプトメニュー**\n\n以下から選択するか、編集可能モードで独自プロンプトを作成できます：",
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
    # 情報カードのサンプルデータ
    info_data = {
        "title": "Chainlit カスタマイズ技術",
        "description": "サンプルプロジェクトから学んだ高度なUI/UX技術を一般化",
        "image_url": "https://images.unsplash.com/photo-1555066931-4365d14bab8c?w=400&h=200&fit=crop",
        "category": "技術デモ",
        "features": [
            {"icon": "🎨", "text": "グラスモーフィズム効果"},
            {"icon": "⚡", "text": "高性能アニメーション"},
            {"icon": "📱", "text": "レスポンシブデザイン"},
            {"icon": "🌙", "text": "ダークモード対応"},
            {"icon": "💾", "text": "ローカルストレージ活用"},
            {"icon": "🔧", "text": "カスタムコンポーネント"}
        ],
        "items": [
            {
                "title": "カスタムプロンプト管理",
                "description": "ローカルストレージベースのプロンプト管理システム。追加・編集・削除が可能です。"
            },
            {
                "title": "情報カード表示",
                "description": "構造化された情報を美しく表示するカードコンポーネント。背景画像やアニメーション効果に対応。"
            },
            {
                "title": "高度なCSS効果",
                "description": "ネオモーフィズム、グラスモーフィズム、ホバー効果など最新のCSS技術を活用。"
            }
        ]
    }
    
    await cl.Message(
        content="📋 **技術情報カード**\n\n実装された技術の詳細：",
        elements=[
            cl.CustomElement(
                name="InfoCards",
                props={"data": info_data}
            )
        ]
    ).send()


@cl.action_callback("action_summary")
async def on_action_summary(action):
    """要約作成アクション - 追加メッセージと関連質問を送信"""
    summary_content = """📝 **要約作成を開始します**

以下の内容を簡潔に要約いたします。重要なポイントを3つに絞って整理します：

**要約の観点:**
• 主要なポイントとテーマ
• 重要な詳細と背景情報  
• 結論と推奨事項

要約が完了しましたら、さらに詳細な分析や関連する質問もお気軽にどうぞ。"""

    # 追加のアクション付きメッセージ
    follow_up_actions = [
        cl.Action(name="action_analysis_deep", label="🔬 詳細分析", payload="deep_analysis"),
        cl.Action(name="action_questions", label="❓ 関連質問", payload="questions"),
        cl.Action(name="action_export_summary", label="📄 要約エクスポート", payload="export_summary")
    ]
    
    await cl.Message(content=summary_content, actions=follow_up_actions).send()

@cl.action_callback("action_detail") 
async def on_action_detail(action):
    """詳細説明アクション - 追加メッセージと専門的な観点を提供"""
    detail_content = """🔍 **詳細説明を開始します**

以下の観点から詳細に説明いたします：

**技術的観点:**
• 実装方法と技術仕様
• メリット・デメリット
• 使用事例と応用範囲

**ビジネス観点:**  
• 実用性と効果
• コストと ROI
• 導入時の考慮事項

詳細説明の後、具体的な実装方法や追加の技術情報についてもお答えできます。"""

    # 追加のアクション付きメッセージ
    follow_up_actions = [
        cl.Action(name="action_implementation", label="⚙️ 実装方法", payload="implementation"),
        cl.Action(name="action_examples", label="💡 具体例", payload="examples"),
        cl.Action(name="action_best_practices", label="🎯 ベストプラクティス", payload="best_practices")
    ]
    
    await cl.Message(content=detail_content, actions=follow_up_actions).send()

@cl.action_callback("action_custom")
async def on_action_custom(action):
    """カスタムプロンプト表示 - 関連機能も提案"""
    await show_custom_prompts()
    
    # 追加のガイダンスメッセージ
    guidance_content = """💡 **カスタムプロンプト活用のヒント**

• プロンプトを選択して即座に適用
• 独自プロンプトの作成・編集が可能
• カテゴリ別に整理された効率的な管理

より効果的な活用方法についてもお気軽にご質問ください。"""

    guidance_actions = [
        cl.Action(name="action_prompt_tips", label="📚 活用法", payload="prompt_tips"),
        cl.Action(name="action_create_prompt", label="✏️ 新規作成", payload="create_prompt")
    ]
    
    await cl.Message(content=guidance_content, actions=guidance_actions).send()

@cl.action_callback("action_info")
async def on_action_info(action):
    """技術情報表示 - 関連技術についても案内"""
    await show_info_cards()
    
    # 技術的なフォローアップ
    tech_content = """🔧 **技術情報の詳細について**

表示された技術情報について、さらに深く知りたい分野はありますか？

• **フロントエンド技術**: React、CSS効果、アニメーション
• **バックエンド技術**: Chainlit、Python、API設計  
• **UI/UX デザイン**: レスポンシブ、アクセシビリティ
• **パフォーマンス**: 最適化、ローディング、メモリ管理"""

    tech_actions = [
        cl.Action(name="action_frontend", label="🎨 フロントエンド", payload="frontend"),
        cl.Action(name="action_backend", label="⚙️ バックエンド", payload="backend"),
        cl.Action(name="action_performance", label="⚡ パフォーマンス", payload="performance")
    ]
    
    await cl.Message(content=tech_content, actions=tech_actions).send()

@cl.action_callback("action_demo") 
async def on_action_demo(action):
    """全機能デモ - カスタマイズのヒントも提供"""
    await show_feature_demo()
    
    # カスタマイズガイダンス
    customization_content = """🛠️ **カスタマイズのヒント**

このデモで紹介している技術は、以下のような用途でカスタマイズ可能です：

• **企業向けダッシュボード**: ブランドカラーとロゴの適用
• **教育プラットフォーム**: 学習進捗の可視化
• **顧客サポートシステム**: FAQ統合とチケット管理
• **データ分析ツール**: チャート表示とレポート生成

具体的なカスタマイズ方法についてもサポートできます。"""

    customization_actions = [
        cl.Action(name="action_branding", label="🎨 ブランディング", payload="branding"),
        cl.Action(name="action_integration", label="🔗 システム連携", payload="integration"),
        cl.Action(name="action_deployment", label="🚀 デプロイメント", payload="deployment")
    ]
    
    await cl.Message(content=customization_content, actions=customization_actions).send()

# 追加のアクションコールバック関数
@cl.action_callback("action_analysis_deep")
async def on_action_analysis_deep(action):
    await cl.Message(content="🔬 **詳細分析を実行中**\n\nデータの深層分析、トレンド識別、相関関係の特定を行います...").send()

@cl.action_callback("action_questions")
async def on_action_questions(action):
    questions_content = """❓ **関連質問の提案**

以下のような観点から追加でご質問いただけます：

• この情報をビジネスにどう活用できるか？
• 類似の技術や代替案はあるか？
• 実装時の注意点やリスクは？
• コストや工数の見積もりは？"""
    
    await cl.Message(content=questions_content).send()

@cl.action_callback("action_implementation")
async def on_action_implementation(action):
    impl_content = """⚙️ **実装方法の詳細**

段階的な実装アプローチを提案します：

**Phase 1**: 基盤構築とセットアップ
**Phase 2**: コア機能の実装
**Phase 3**: UI/UX の調整と最適化
**Phase 4**: テストと本番デプロイ

各フェーズの詳細について説明いたします。"""
    
    await cl.Message(content=impl_content).send()

@cl.action_callback("action_frontend")
async def on_action_frontend(action):
    frontend_content = """🎨 **フロントエンド技術の詳細**

このデモで使用している主要なフロントエンド技術：

• **React Components**: カスタムコンポーネントの設計パターン
• **CSS Effects**: グラスモーフィズム、ネオモーフィズム効果
• **Animations**: Canvas API、CSS Transform、Transition
• **Responsive Design**: モバイルファースト、フレキシブルレイアウト"""
    
    await cl.Message(content=frontend_content).send()

if __name__ == "__main__":
    print("Chainlit Customized Demo - Run with: chainlit run main.py")
