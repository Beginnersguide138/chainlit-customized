import React from 'react';

export default function CustomPrompts({ data = [] }) {
  // データが正しく渡されているかチェック
  const prompts = Array.isArray(data) ? data : [];
  
  const handlePromptClick = (prompt) => {
    // Chainlitのメッセージ送信関数を呼び出し
    if (window.sendUserMessage) {
      window.sendUserMessage(prompt.prompt);
    } else {
      // フォールバック: コンソールに出力
      console.log('Sending message:', prompt.prompt);
      // 直接入力フィールドに設定を試行
      const inputField = document.querySelector('textarea[placeholder*="メッセージ"], input[type="text"]');
      if (inputField) {
        inputField.value = prompt.prompt;
        inputField.dispatchEvent(new Event('input', { bubbles: true }));
        
        // 送信ボタンをクリック
        const sendButton = document.querySelector('button[type="submit"], button[aria-label*="送信"]');
        if (sendButton) {
          sendButton.click();
        }
      }
    }
  };

  return (
    <div className="custom-prompts-container">
      <style jsx>{`
        .custom-prompts-container {
          display: grid;
          gap: 16px;
          padding: 16px;
          max-width: 600px;
        }
        
        .prompt-card {
          display: flex;
          align-items: center;
          padding: 16px;
          background: var(--surface-color, white);
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 12px;
          cursor: pointer;
          transition: all 0.2s ease;
          box-shadow: var(--shadow, 0 1px 3px rgba(0, 0, 0, 0.1));
          backdrop-filter: blur(10px);
        }
        
        .prompt-card:hover {
          transform: translateY(-2px);
          box-shadow: 0 4px 12px rgba(0, 0, 0, 0.15);
          border-color: #3b82f6;
        }
        
        .prompt-card:active {
          transform: translateY(0);
        }
        
        .prompt-icon {
          width: 48px;
          height: 48px;
          display: flex;
          align-items: center;
          justify-content: center;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
          border-radius: 12px;
          margin-right: 16px;
          font-size: 24px;
        }
        
        .prompt-content {
          flex: 1;
        }
        
        .prompt-title {
          font-size: 18px;
          font-weight: 600;
          color: var(--text-color, #1f2937);
          margin-bottom: 4px;
        }
        
        .prompt-description {
          font-size: 14px;
          color: var(--text-muted, #6b7280);
          line-height: 1.4;
        }
        
        .no-prompts {
          text-align: center;
          padding: 32px;
          color: #6b7280;
        }
        
        .no-prompts-title {
          font-size: 20px;
          font-weight: 600;
          color: var(--text-color, #1f2937);
          margin-bottom: 12px;
        }
      `}</style>
      
      {prompts.length === 0 ? (
        <div className="no-prompts">
          <div className="no-prompts-title">カスタムプロンプト</div>
          <p>カスタムプロンプトが登録されていません。</p>
          <p>プロンプトを追加すると、ここから選択して送信できます。</p>
        </div>
      ) : (
        prompts.map((prompt, index) => (
          <div
            key={index}
            className="prompt-card"
            onClick={() => handlePromptClick(prompt)}
          >
            <div className="prompt-icon">
              {prompt.icon}
            </div>
            <div className="prompt-content">
              <div className="prompt-title">{prompt.title}</div>
              <div className="prompt-description">{prompt.prompt}</div>
            </div>
          </div>
        ))
      )}
    </div>
  );
}