import React, { useState, useEffect } from 'react';

export default function CustomPromptsList({ data = [], onPromptSelect, editable = false }) {
  const [prompts, setPrompts] = useState(data);
  const [newPrompt, setNewPrompt] = useState({ title: '', prompt: '', icon: '💡', category: 'General' });
  const [showAddForm, setShowAddForm] = useState(false);
  const [editingId, setEditingId] = useState(null);

  // Load prompts from local storage
  useEffect(() => {
    if (data.length === 0) {
      const savedPrompts = localStorage.getItem('chainlit-custom-prompts');
      if (savedPrompts) {
        try {
          setPrompts(JSON.parse(savedPrompts));
        } catch (error) {
          console.error('Error loading prompts from localStorage:', error);
        }
      }
    } else {
      setPrompts(data);
    }
  }, [data]);

  // Save prompts to local storage
  const savePrompts = (updatedPrompts) => {
    setPrompts(updatedPrompts);
    localStorage.setItem('chainlit-custom-prompts', JSON.stringify(updatedPrompts));
  };

  // Add prompt
  const addPrompt = () => {
    if (newPrompt.title && newPrompt.prompt) {
      const prompt = {
        id: Date.now().toString(),
        ...newPrompt,
        created: new Date().toISOString()
      };
      const updatedPrompts = [...prompts, prompt];
      savePrompts(updatedPrompts);
      setNewPrompt({ title: '', prompt: '', icon: '💡', category: 'General' });
      setShowAddForm(false);
    }
  };

  // Delete prompt
  const deletePrompt = (id) => {
    const updatedPrompts = prompts.filter(p => p.id !== id);
    savePrompts(updatedPrompts);
  };

  // Edit prompt
  const editPrompt = (id, updatedData) => {
    const updatedPrompts = prompts.map(p => 
      p.id === id ? { ...p, ...updatedData } : p
    );
    savePrompts(updatedPrompts);
    setEditingId(null);
  };

  // Handle prompt selection
  const handlePromptSelect = (prompt) => {
    if (onPromptSelect && typeof onPromptSelect === 'function') {
      onPromptSelect(prompt);
    } else {
      // Default behavior: copy prompt to clipboard
      navigator.clipboard.writeText(prompt.prompt).then(() => {
        // Simple toast notification
        const toast = document.createElement('div');
        toast.textContent = 'Prompt copied to clipboard';
        toast.className = 'toast success';
        document.body.appendChild(toast);
        setTimeout(() => document.body.removeChild(toast), 3000);
      });
    }
  };

  const categories = ['General', 'Development', 'Business', 'Creative', 'Analysis'];
  const icons = ['💡', '🔥', '⚡', '🚀', '💻', '📊', '🎨', '📝', '🔍', '⭐'];

  return (
    <div className="custom-prompts-container">
      <style jsx>{`
        .custom-prompts-container {
          width: 100%;
          max-width: 800px;
          margin: 0 auto;
          padding: 20px;
        }

        .prompts-header {
          display: flex;
          justify-content: space-between;
          align-items: center;
          margin-bottom: 24px;
          padding-bottom: 12px;
          border-bottom: 2px solid var(--border-color, #e5e7eb);
        }

        .prompts-title {
          font-size: 24px;
          font-weight: 700;
          color: var(--text-color, #1f2937);
          margin: 0;
        }

        .add-button {
          background: var(--primary-gradient, linear-gradient(135deg, #667eea 0%, #764ba2 100%));
          color: white;
          border: none;
          padding: 10px 20px;
          border-radius: 8px;
          cursor: pointer;
          font-weight: 500;
          transition: all 0.2s ease;
          display: flex;
          align-items: center;
          gap: 8px;
        }

        .add-button:hover {
          transform: translateY(-1px);
          box-shadow: var(--shadow-lg, 0 10px 15px rgba(0, 0, 0, 0.1));
        }

        .prompts-grid {
          display: grid;
          gap: 16px;
          margin-bottom: 20px;
        }

        .prompt-card {
          background: var(--surface-color, white);
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 12px;
          padding: 20px;
          cursor: pointer;
          transition: all 0.2s ease;
          position: relative;
        }

        [data-theme="dark"] .prompt-card {
          background: rgba(31, 41, 55, 0.8);
          border-color: var(--border-color, #374151);
        }

        .prompt-card:hover {
          border-color: var(--primary-color, #667eea);
          transform: translateY(-2px);
          box-shadow: var(--shadow-lg, 0 10px 15px rgba(0, 0, 0, 0.1));
        }

        .prompt-header {
          display: flex;
          align-items: center;
          gap: 12px;
          margin-bottom: 12px;
        }

        .prompt-icon {
          font-size: 24px;
          width: 40px;
          height: 40px;
          display: flex;
          align-items: center;
          justify-content: center;
          background: var(--secondary-color, #f8fafc);
          border-radius: 50%;
        }

        [data-theme="dark"] .prompt-icon {
          background: rgba(55, 65, 81, 0.5);
        }

        .prompt-info {
          flex: 1;
        }

        .prompt-title {
          font-size: 16px;
          font-weight: 600;
          color: var(--text-color, #1f2937);
          margin: 0 0 4px 0;
        }

        .prompt-category {
          font-size: 12px;
          color: var(--text-muted, #6b7280);
          background: var(--secondary-color, #f8fafc);
          padding: 2px 8px;
          border-radius: 12px;
          display: inline-block;
        }

        [data-theme="dark"] .prompt-category {
          background: rgba(55, 65, 81, 0.5);
        }

        .prompt-text {
          font-size: 14px;
          color: var(--text-muted, #6b7280);
          line-height: 1.5;
          margin: 12px 0;
          max-height: 60px;
          overflow: hidden;
          text-overflow: ellipsis;
          display: -webkit-box;
          -webkit-line-clamp: 3;
          -webkit-box-orient: vertical;
        }

        .prompt-actions {
          position: absolute;
          top: 16px;
          right: 16px;
          display: flex;
          gap: 8px;
          opacity: 0;
          transition: opacity 0.2s ease;
        }

        .prompt-card:hover .prompt-actions {
          opacity: 1;
        }

        .action-btn {
          background: none;
          border: none;
          padding: 4px;
          border-radius: 4px;
          cursor: pointer;
          color: var(--text-muted, #6b7280);
          transition: all 0.2s ease;
        }

        .action-btn:hover {
          background: var(--secondary-color, #f8fafc);
          color: var(--text-color, #1f2937);
        }

        [data-theme="dark"] .action-btn:hover {
          background: rgba(55, 65, 81, 0.5);
        }

        .add-form {
          background: var(--surface-color, white);
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 12px;
          padding: 24px;
          margin-bottom: 20px;
        }

        [data-theme="dark"] .add-form {
          background: rgba(31, 41, 55, 0.8);
          border-color: var(--border-color, #374151);
        }

        .form-row {
          display: flex;
          gap: 12px;
          margin-bottom: 16px;
        }

        .form-group {
          flex: 1;
        }

        .form-label {
          display: block;
          font-size: 14px;
          font-weight: 500;
          color: var(--text-color, #1f2937);
          margin-bottom: 6px;
        }

        .form-input {
          width: 100%;
          padding: 10px 12px;
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 6px;
          font-size: 14px;
          color: var(--text-color, #1f2937);
          background: var(--background-color, white);
          transition: border-color 0.2s ease;
        }

        [data-theme="dark"] .form-input {
          background: rgba(17, 24, 39, 0.8);
          border-color: var(--border-color, #374151);
        }

        .form-input:focus {
          outline: none;
          border-color: var(--primary-color, #667eea);
        }

        .form-textarea {
          min-height: 80px;
          resize: vertical;
          font-family: inherit;
        }

        .form-actions {
          display: flex;
          gap: 12px;
          justify-content: flex-end;
        }

        .btn {
          padding: 8px 16px;
          border-radius: 6px;
          font-size: 14px;
          font-weight: 500;
          cursor: pointer;
          transition: all 0.2s ease;
          border: none;
        }

        .btn-primary {
          background: var(--primary-color, #667eea);
          color: white;
        }

        .btn-primary:hover {
          background: var(--primary-color, #5a67d8);
        }

        .btn-secondary {
          background: var(--secondary-color, #f8fafc);
          color: var(--text-color, #1f2937);
          border: 1px solid var(--border-color, #e5e7eb);
        }

        .btn-secondary:hover {
          background: var(--border-color, #e5e7eb);
        }

        [data-theme="dark"] .btn-secondary {
          background: rgba(55, 65, 81, 0.5);
          border-color: var(--border-color, #374151);
        }

        .empty-state {
          text-align: center;
          padding: 60px 20px;
          color: var(--text-muted, #6b7280);
        }

        .empty-icon {
          font-size: 48px;
          margin-bottom: 16px;
        }

        .empty-title {
          font-size: 18px;
          font-weight: 600;
          margin-bottom: 8px;
          color: var(--text-color, #1f2937);
        }

        .empty-description {
          font-size: 14px;
          line-height: 1.5;
        }

        @media (max-width: 768px) {
          .custom-prompts-container {
            padding: 16px;
          }
          
          .prompts-header {
            flex-direction: column;
            gap: 16px;
            align-items: stretch;
          }
          
          .form-row {
            flex-direction: column;
          }
          
          .form-actions {
            flex-direction: column;
          }
        }
      `}</style>

      <div className="prompts-header">
        <h2 className="prompts-title">Custom Prompts</h2>
        {editable && (
          <button 
            className="add-button"
            onClick={() => setShowAddForm(!showAddForm)}
          >
            ➕ Add Prompt
          </button>
        )}
      </div>

      {showAddForm && editable && (
        <div className="add-form">
          <div className="form-row">
            <div className="form-group">
              <label className="form-label">Title</label>
              <input
                className="form-input"
                type="text"
                value={newPrompt.title}
                onChange={(e) => setNewPrompt({...newPrompt, title: e.target.value})}
                placeholder="Enter prompt title"
              />
            </div>
            <div className="form-group" style={{maxWidth: '120px'}}>
              <label className="form-label">Icon</label>
              <select
                className="form-input"
                value={newPrompt.icon}
                onChange={(e) => setNewPrompt({...newPrompt, icon: e.target.value})}
              >
                {icons.map(icon => (
                  <option key={icon} value={icon}>{icon}</option>
                ))}
              </select>
            </div>
            <div className="form-group" style={{maxWidth: '150px'}}>
              <label className="form-label">Category</label>
              <select
                className="form-input"
                value={newPrompt.category}
                onChange={(e) => setNewPrompt({...newPrompt, category: e.target.value})}
              >
                {categories.map(cat => (
                  <option key={cat} value={cat}>{cat}</option>
                ))}
              </select>
            </div>
          </div>
          <div className="form-group">
            <label className="form-label">Prompt Content</label>
            <textarea
              className="form-input form-textarea"
              value={newPrompt.prompt}
              onChange={(e) => setNewPrompt({...newPrompt, prompt: e.target.value})}
              placeholder="Enter prompt content..."
            />
          </div>
          <div className="form-actions">
            <button className="btn btn-secondary" onClick={() => setShowAddForm(false)}>
              Cancel
            </button>
            <button className="btn btn-primary" onClick={addPrompt}>
              Add
            </button>
          </div>
        </div>
      )}

      {prompts.length === 0 ? (
        <div className="empty-state">
          <div className="empty-icon">💭</div>
          <div className="empty-title">No Custom Prompts</div>
          <div className="empty-description">
            Add prompts to template frequently used messages.
            {editable && " You can create new prompts using the 'Add Prompt' button above."}
          </div>
        </div>
      ) : (
        <div className="prompts-grid">
          {prompts.map((prompt) => (
            <div 
              key={prompt.id} 
              className="prompt-card"
              onClick={() => handlePromptSelect(prompt)}
            >
              <div className="prompt-header">
                <div className="prompt-icon">{prompt.icon}</div>
                <div className="prompt-info">
                  <div className="prompt-title">{prompt.title}</div>
                  <span className="prompt-category">{prompt.category}</span>
                </div>
              </div>
              <div className="prompt-text">{prompt.prompt}</div>
              
              {editable && (
                <div className="prompt-actions">
                  <button 
                    className="action-btn"
                    onClick={(e) => {
                      e.stopPropagation();
                      setEditingId(prompt.id);
                    }}
                  >
                    ✏️
                  </button>
                  <button 
                    className="action-btn"
                    onClick={(e) => {
                      e.stopPropagation();
                      deletePrompt(prompt.id);
                    }}
                  >
                    🗑️
                  </button>
                </div>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
}
