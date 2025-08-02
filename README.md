# Chainlit カスタマイズデモ

商用プロジェクトのChainlitカスタマイズ手法を一般化したデモアプリケーションです。機密情報を除外し、Chainlitの様々なカスタマイズ機能を紹介します。

## 🚀 主な機能

### チャットプロファイル
- **AI Assistant**: 汎用的なAIアシスタント
- **Web Search**: Web検索機能付きアシスタント（実装例）
- **Document Helper**: ドキュメント分析専用アシスタント

### カスタムUI要素
- カスタムプロンプト選択インターフェース
- インタラクティブなアクションボタン
- ファイルアップロード対応
- レスポンシブデザイン

### 高度な機能
- 複数チャットプロファイルの動的切り替え
- カスタムReactコンポーネント統合
- CSS/JavaScript による UI カスタマイズ
- ファイル処理とドラッグ&ドロップ対応

## 🛠️ 技術スタック

- **Chainlit 2.6.4+**: チャットUI フレームワーク
- **Python 3.13+**: バックエンド実装
- **React/JSX**: カスタムUIコンポーネント
- **uv**: パッケージ管理

## 📦 インストール

### 前提条件
- Python 3.13+
- uv パッケージマネージャー

### セットアップ

```bash
# リポジトリをクローン
git clone <repository-url>
cd chainlit-customized

# 依存関係をインストール
uv sync

# アプリケーションを起動
uv run chainlit run main.py
```

## 🎯 使い方

1. **アプリケーション起動**
   ```bash
   uv run chainlit run main.py
   ```

2. **ブラウザでアクセス**
   - 通常: http://localhost:8000
   - チャットプロファイルを選択

3. **機能を試す**
   - 基本的なチャット
   - `🎨` を送信してカスタムプロンプトメニューを表示
   - ファイルをアップロードしてDocument Helper を試用

## 🎨 カスタマイズ要素

### 1. カスタムプロンプト (`CustomPrompts.jsx`)
```jsx
// プロンプト選択UI
<CustomElement name="CustomPrompts" props={{data: prompts}} />
```

### 2. スタイルカスタマイズ (`styles.css`)
- CSS変数によるテーマ管理
- レスポンシブデザイン
- アニメーション効果

### 3. JavaScript拡張 (`script.js`)
- ファイルドロップ機能
- トースト通知
- インタラクティブ要素

## 📁 プロジェクト構造

```
chainlit-customized/
├── main.py                 # メインアプリケーション
├── chainlit.md            # ウェルカムメッセージ
├── pyproject.toml         # プロジェクト設定
├── public/                # 静的ファイル
│   ├── elements/          # カスタムReactコンポーネント
│   │   ├── CustomPrompts.jsx
│   │   └── InfoCards.jsx
│   ├── styles.css         # カスタムスタイル
│   └── script.js          # カスタムJavaScript
└── sample/                # サンプルコード（参考用）
    └── dione/             # 元の商用プロジェクト
```

## 🔧 カスタマイズ例

### チャットプロファイルの追加
```python
chat_profiles = [
    cl.ChatProfile(
        name="New Assistant",
        markdown_description="新しいアシスタントの説明",
        icon="https://example.com/icon.png",
    )
]
```

### カスタム要素の作成
```python
await cl.Message(
    content="カスタム要素の例",
    elements=[
        cl.CustomElement(
            name="YourCustomComponent",
            props={"data": your_data}
        )
    ]
).send()
```

## 🎬 デモンストレーション

1. **基本チャット**: 各プロファイルでの対話
2. **カスタムプロンプト**: `🎨` コマンドでプロンプト選択
3. **ファイル処理**: Document Helper でファイルアップロード
4. **アクションボタン**: インタラクティブなUIコンポーネント

## 🤝 貢献

このプロジェクトは、Chainlitのカスタマイズ手法を学習・共有する目的で作成されています。

### 改善提案
- 新しいカスタマイズ手法の追加
- UI/UXの改善
- パフォーマンス最適化
- ドキュメントの改善

## 📝 ライセンス

このプロジェクトはMITライセンスの下で公開されています。

## 🔗 関連リンク

- [Chainlit公式ドキュメント](https://docs.chainlit.io/)
- [Python uv](https://github.com/astral-sh/uv)

---

*このデモアプリケーションは、実際の商用プロジェクトのChainlitカスタマイズ手法を抽象化・一般化したものです。機密情報は含まれておらず、学習・参考目的で作成されています。*
