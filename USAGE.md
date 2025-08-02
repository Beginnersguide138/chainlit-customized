# 使用方法ガイド

## 🚀 クイックスタート

### 1. アプリケーションの起動

```bash
# 依存関係のインストール（初回のみ）
uv sync

# アプリケーション起動
uv run chainlit run main.py
```

ブラウザで http://localhost:8000 にアクセス

### 2. チャットプロファイルの選択

左側のパネルから以下のプロファイルを選択できます：

- **AI Assistant**: 汎用的なチャット
- **Web Search**: 検索機能デモ
- **Document Helper**: ファイル処理デモ

## 🎨 機能の使い方

### カスタムプロンプトメニュー

任意のプロファイルで `🎨` を送信すると、カスタムプロンプト選択UIが表示されます。

例：
```
🎨
```

### アクションボタン

AI Assistantプロファイルでメッセージを送信すると、以下のアクションボタンが表示されます：

- **📝 要約を作成**: 要約機能のデモ
- **🔍 詳細を説明**: 詳細説明機能のデモ  
- **🎨 カスタムプロンプト**: プロンプト選択UIを表示

### ファイルアップロード

Document Helperプロファイルでファイルをアップロードすると、ファイル情報が表示されます。

対応ファイル形式：
- テキストファイル (.txt, .md)
- 画像ファイル (.jpg, .png, .gif)
- PDFファイル (.pdf)
- その他のファイル形式

## 🛠️ カスタマイズ方法

### 新しいチャットプロファイルの追加

`main.py` の `chat_profiles` リストに追加：

```python
chat_profiles = [
    # 既存のプロファイル...
    cl.ChatProfile(
        name="Your New Profile",
        markdown_description="新しいプロファイルの説明",
        icon="https://example.com/icon.png",
    )
]
```

対応するハンドラー関数も追加：

```python
@cl.on_message
async def main(message: cl.Message):
    chat_profile = cl.user_session.get("chat_profile")
    
    if chat_profile == "Your New Profile":
        await handle_your_new_profile(message)
    # その他の条件...

async def handle_your_new_profile(message: cl.Message):
    # 新しいプロファイルの処理ロジック
    await cl.Message(content=f"新しいプロファイル: {message.content}").send()
```

### カスタムプロンプトの追加

`show_custom_prompts()` 関数の `prompts_data` を編集：

```python
prompts_data = [
    {
        "title": "新しいプロンプト",
        "prompt": "あなたのカスタムプロンプトテキスト",
        "icon": "🆕"
    },
    # 既存のプロンプト...
]
```

### UI要素のカスタマイズ

1. **CSS**: `public/styles.css` でスタイルを編集
2. **JavaScript**: `public/script.js` で動作を追加
3. **React要素**: `public/elements/` で新しいコンポーネントを作成

### 新しいReactコンポーネントの作成

1. `public/elements/YourComponent.jsx` を作成：

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

2. Pythonコードで使用：

```python
await cl.Message(
    content="カスタムコンポーネントの例",
    elements=[
        cl.CustomElement(
            name="YourComponent",
            props={
                "data": {
                    "title": "タイトル",
                    "content": "コンテンツ"
                }
            }
        )
    ]
).send()
```

## 🔧 トラブルシューティング

### よくある問題

1. **モジュールが見つからない**
   ```bash
   uv sync
   ```

2. **ポートが使用中**
   ```bash
   uv run chainlit run main.py --port 8001
   ```

3. **カスタム要素が表示されない**
   - `public/elements/` のファイル名とコンポーネント名を確認
   - JSXの構文エラーをチェック

### デバッグ方法

1. **コンソールログの確認**
   - ブラウザの開発者ツール（F12）でコンソールをチェック

2. **サーバーログの確認**
   - ターミナルでChainlitサーバーのログを確認

3. **Python構文チェック**
   ```bash
   uv run python -c "import main"
   ```

## 📚 さらなる学習

- [Chainlit公式ドキュメント](https://docs.chainlit.io/)
- [React公式ドキュメント](https://react.dev/)
- `sample/dione/` ディレクトリの実装例を参照

---

*このガイドは基本的な使用方法を説明しています。より高度なカスタマイズについては、サンプルコードや公式ドキュメントを参考にしてください。*