import React from 'react';

export default function InfoCards({ data = {} }) {
  const {
    title = "Info Card",
    description = "Card displaying custom information",
    image_url = null,
    items = [],
    features = [],
    category = "General"
  } = data;

  return (
    <div className="info-card-container">
      <style jsx>{`
        .info-card-container {
          max-width: 600px;
          margin: 16px auto;
          background: var(--surface-color, white);
          border-radius: 16px;
          overflow: hidden;
          box-shadow: var(--shadow-lg, 0 10px 25px rgba(0, 0, 0, 0.1));
          border: 1px solid var(--border-color, #e5e7eb);
          position: relative;
        }

        .info-card-header {
          position: relative;
          padding: 24px;
          background: var(--primary-gradient, linear-gradient(135deg, #667eea 0%, #764ba2 100%));
          color: white;
          min-height: 120px;
          display: flex;
          flex-direction: column;
          justify-content: space-between;
        }

        .info-card-background {
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          bottom: 0;
          background-image: url('${image_url}');
          background-size: cover;
          background-position: center;
          opacity: 0.3;
          filter: blur(1px);
        }

        .info-card-title {
          font-size: 24px;
          font-weight: 700;
          text-shadow: 2px 2px 4px rgba(0, 0, 0, 0.5);
          position: relative;
          z-index: 2;
          margin-bottom: 8px;
        }

        .info-card-description {
          font-size: 16px;
          text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.5);
          position: relative;
          z-index: 2;
          opacity: 0.95;
        }

        .info-card-category {
          position: absolute;
          top: 16px;
          right: 16px;
          background: rgba(255, 255, 255, 0.2);
          color: white;
          padding: 6px 12px;
          border-radius: 20px;
          font-size: 12px;
          font-weight: 500;
          backdrop-filter: blur(10px);
          z-index: 2;
        }

        .info-card-content {
          padding: 24px;
        }

        .features-grid {
          display: grid;
          grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
          gap: 16px;
          margin-bottom: 24px;
        }

        .feature-item {
          display: flex;
          align-items: center;
          gap: 12px;
          padding: 12px 16px;
          background: var(--secondary-color, #f8fafc);
          border-radius: 8px;
          border-left: 4px solid var(--primary-color, #667eea);
          transition: all 0.2s ease;
        }

        [data-theme="dark"] .feature-item {
          background: rgba(55, 65, 81, 0.5);
          border-left-color: var(--primary-color, #818cf8);
        }

        .feature-item:hover {
          transform: translateX(4px);
          box-shadow: var(--shadow, 0 4px 6px rgba(0, 0, 0, 0.1));
        }

        .feature-icon {
          font-size: 18px;
          min-width: 20px;
        }

        .feature-text {
          font-size: 14px;
          color: var(--text-color, #1f2937);
          font-weight: 500;
        }

        .items-list {
          display: grid;
          gap: 12px;
        }

        .item-entry {
          padding: 16px;
          background: var(--surface-color, white);
          border: 1px solid var(--border-color, #e5e7eb);
          border-radius: 8px;
          transition: all 0.2s ease;
        }

        [data-theme="dark"] .item-entry {
          background: rgba(31, 41, 55, 0.8);
          border-color: var(--border-color, #374151);
        }

        .item-entry:hover {
          border-color: var(--primary-color, #667eea);
          box-shadow: var(--shadow, 0 4px 6px rgba(0, 0, 0, 0.1));
        }

        .item-title {
          font-size: 16px;
          font-weight: 600;
          color: var(--text-color, #1f2937);
          margin-bottom: 8px;
        }

        .item-description {
          font-size: 14px;
          color: var(--text-muted, #6b7280);
          line-height: 1.5;
        }

        .section-title {
          font-size: 18px;
          font-weight: 600;
          color: var(--text-color, #1f2937);
          margin-bottom: 16px;
          padding-bottom: 8px;
          border-bottom: 2px solid var(--border-color, #e5e7eb);
        }

        @media (max-width: 768px) {
          .info-card-container {
            margin: 12px;
          }
          
          .info-card-header {
            padding: 20px;
            min-height: 100px;
          }
          
          .info-card-title {
            font-size: 20px;
          }
          
          .features-grid {
            grid-template-columns: 1fr;
          }
          
          .info-card-content {
            padding: 20px;
          }
        }
      `}</style>

      <div className="info-card-header">
        {image_url && <div className="info-card-background"></div>}
        <div className="info-card-category">{category}</div>
        <div>
          <div className="info-card-title">{title}</div>
          <div className="info-card-description">{description}</div>
        </div>
      </div>

      <div className="info-card-content">
        {features.length > 0 && (
          <>
            <div className="section-title">✨ Features</div>
            <div className="features-grid">
              {features.map((feature, index) => (
                <div key={index} className="feature-item">
                  <div className="feature-icon">{feature.icon || '🔥'}</div>
                  <div className="feature-text">{feature.text}</div>
                </div>
              ))}
            </div>
          </>
        )}

        {items.length > 0 && (
          <>
            <div className="section-title">📋 Detailed Information</div>
            <div className="items-list">
              {items.map((item, index) => (
                <div key={index} className="item-entry">
                  <div className="item-title">{item.title}</div>
                  <div className="item-description">{item.description}</div>
                </div>
              ))}
            </div>
          </>
        )}
      </div>
    </div>
  );
}
