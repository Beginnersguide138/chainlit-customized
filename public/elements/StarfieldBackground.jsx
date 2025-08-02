import React, { useEffect, useRef } from 'react';

export default function StarfieldBackground({ 
  enabled = true, 
  density = 'medium', 
  speed = 'normal',
  color = '#ffffff'
}) {
  const canvasRef = useRef(null);
  const animationRef = useRef(null);
  const starsRef = useRef([]);

  useEffect(() => {
    if (!enabled) return;

    const canvas = canvasRef.current;
    if (!canvas) return;

    const ctx = canvas.getContext('2d');
    
    // キャンバスサイズをウィンドウサイズに合わせる
    const resizeCanvas = () => {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
      initStars();
    };

    // 星の初期化
    const initStars = () => {
      const densityMap = {
        'low': 200,
        'medium': 400,
        'high': 800
      };
      
      const starCount = densityMap[density] || 400;
      starsRef.current = [];

      for (let i = 0; i < starCount; i++) {
        starsRef.current.push({
          x: Math.random() * canvas.width,
          y: Math.random() * canvas.height,
          size: Math.random() * 2 + 0.5,
          speed: Math.random() * 0.5 + 0.1,
          opacity: Math.random() * 0.8 + 0.2,
          twinkle: Math.random() * 0.02 + 0.01
        });
      }
    };

    // アニメーションループ
    const animate = () => {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      
      const speedMap = {
        'slow': 0.3,
        'normal': 1,
        'fast': 2
      };
      
      const speedMultiplier = speedMap[speed] || 1;

      starsRef.current.forEach(star => {
        // 星の移動
        star.y += star.speed * speedMultiplier;
        if (star.y > canvas.height) {
          star.y = -5;
          star.x = Math.random() * canvas.width;
        }

        // キラキラ効果
        star.opacity += Math.sin(Date.now() * star.twinkle) * 0.1;
        star.opacity = Math.max(0.1, Math.min(1, star.opacity));

        // 星を描画
        ctx.save();
        ctx.globalAlpha = star.opacity;
        ctx.fillStyle = color;
        ctx.shadowBlur = star.size * 2;
        ctx.shadowColor = color;
        ctx.beginPath();
        ctx.arc(star.x, star.y, star.size, 0, Math.PI * 2);
        ctx.fill();
        ctx.restore();
      });

      animationRef.current = requestAnimationFrame(animate);
    };

    // 初期化
    resizeCanvas();
    animate();

    // リサイズイベントリスナー
    window.addEventListener('resize', resizeCanvas);

    // クリーンアップ
    return () => {
      window.removeEventListener('resize', resizeCanvas);
      if (animationRef.current) {
        cancelAnimationFrame(animationRef.current);
      }
    };
  }, [enabled, density, speed, color]);

  if (!enabled) return null;

  return (
    <canvas
      ref={canvasRef}
      style={{
        position: 'fixed',
        top: 0,
        left: 0,
        width: '100vw',
        height: '100vh',
        pointerEvents: 'none',
        zIndex: -1,
        opacity: 0.6
      }}
    />
  );
}
