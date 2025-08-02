import React from 'react';

export default function InfoCard({ 
  title = "サンプルカード",
  image_url,
  descriptions = [],
  targetAudience = "すべてのユーザー",
  published = "2024年",
  source = "デモ",
  link = "#",
  tags = ["サンプル"],
  frequency = "高"
}) {
  const [currentSlide, setCurrentSlide] = React.useState(0);

  const nextSlide = () => {
    if (descriptions.length > 0) {
      setCurrentSlide((prev) => (prev + 1) % descriptions.length);
    }
  };

  const prevSlide = () => {
    if (descriptions.length > 0) {
      setCurrentSlide((prev) => (prev - 1 + descriptions.length) % descriptions.length);
    }
  };

  return (
    <div className="info-card">
      <style jsx>{`
        .info-card {
          position: relative;
          width: 100%;
          max-width: 400px;
          background: var(--surface-color, white);
          border-radius: 16px;
          overflow: hidden;
          box-shadow: var(--shadow-lg, 0 4px 20px rgba(0, 0, 0, 0.1));
          margin: 16px auto;
          border: 1px solid var(--border-color, #e5e7eb);
          backdrop-filter: blur(10px);
        }
        
        .card-image {
          width: 100%;
          height: 200px;
          object-fit: cover;
          background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        }
        
        .card-header {
          position: absolute;
          top: 0;
          left: 0;
          right: 0;
          padding: 16px;
          background: linear-gradient(to bottom, rgba(0,0,0,0.7), transparent);
          color: white;
          display: flex;
          justify-content: space-between;
          align-items: flex-start;
        }
        
        .card-title {
          font-size: 20px;
          font-weight: 600;
          text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
        }
        
        .frequency-badge {
          background: rgba(255, 255, 255, 0.2);
          backdrop-filter: blur(10px);
          padding: 4px 12px;
          border-radius: 20px;
          font-size: 12px;
          font-weight: 500;
          border: 1px solid rgba(255, 255, 255, 0.3);
        }
        
        .card-content {
          padding: 20px;
        }
        
        .carousel-container {
          position: relative;
          background: var(--secondary-color, #f8fafc);
          border-radius: 12px;
          padding: 20px;
          margin-bottom: 20px;
          min-height: 100px;
          display: flex;
          align-items: center;
          justify-content: center;
          border: 1px solid var(--border-color, #e5e7eb);
        }
        
        .carousel-content {
          text-align: center;
          font-size: 14px;
          color: var(--text-muted, #475569);
          line-height: 1.6;
        }
        
        .carousel-controls {
          position: absolute;
          top: 50%;
          transform: translateY(-50%);
          background: white;
          border: none;
          width: 32px;
          height: 32px;
          border-radius: 50%;
          display: flex;
          align-items: center;
          justify-content: center;
          cursor: pointer;
          box-shadow: 0 2px 8px rgba(0, 0, 0, 0.1);
          font-size: 12px;
        }
        
        .carousel-controls:hover {
          background: #f1f5f9;
        }
        
        .carousel-prev {
          left: 8px;
        }
        
        .carousel-next {
          right: 8px;
        }
        
        .details-grid {
          display: grid;
          grid-template-columns: 1fr 1fr;
          gap: 16px;
          font-size: 14px;
        }
        
        .detail-item {
          display: flex;
          align-items: center;
          gap: 8px;
          color: var(--text-muted, #475569);
        }
        
        .detail-icon {
          width: 16px;
          height: 16px;
          opacity: 0.7;
        }
        
        .detail-link {
          grid-column: span 2;
        }
        
        .detail-tags {
          grid-column: span 2;
        }
        
        .tags-list {
          color: #3b82f6;
          font-weight: 500;
        }
      `}</style>
      
      {image_url && (
        <img src={image_url} alt={title} className="card-image" />
      )}
      
      <div className="card-header">
        <div className="card-title">{title}</div>
        <div className="frequency-badge">{frequency}</div>
      </div>
      
      <div className="card-content">
        {descriptions.length > 0 && (
          <div className="carousel-container">
            <div className="carousel-content">
              {descriptions[currentSlide] || "説明がありません"}
            </div>
            {descriptions.length > 1 && (
              <>
                <button className="carousel-controls carousel-prev" onClick={prevSlide}>
                  ←
                </button>
                <button className="carousel-controls carousel-next" onClick={nextSlide}>
                  →
                </button>
              </>
            )}
          </div>
        )}
        
        <div className="details-grid">
          <div className="detail-item">
            <span className="detail-icon">👤</span>
            <span>{targetAudience}</span>
          </div>
          
          <div className="detail-item">
            <span className="detail-icon">🏢</span>
            <span>{source}</span>
          </div>
          
          <div className="detail-item detail-link">
            <span className="detail-icon">📅</span>
            <span>{published}</span>
          </div>
          
          <div className="detail-item detail-link">
            <span className="detail-icon">🔗</span>
            <span>{link}</span>
          </div>
          
          <div className="detail-item detail-tags">
            <span className="detail-icon">🏷️</span>
            <span className="tags-list">{tags.join(", ")}</span>
          </div>
        </div>
      </div>
    </div>
  );
}