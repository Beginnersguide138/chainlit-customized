// Chainlit カスタマイズ用JavaScript

// ページ読み込み完了時の初期化
document.addEventListener('DOMContentLoaded', function() {
    console.log('Chainlit Customized Demo loaded');
    
    // メッセージ送信関数をグローバルに公開（カスタム要素から使用）
    window.sendUserMessage = sendUserMessage;
    
    // ファイルドロップ機能を初期化
    initFileDropZone();
    
    // カスタムイベントリスナーを追加
    initCustomEventListeners();
    
    // テーマ切り替え時のトランジション効果を追加
    addThemeTransition();
    
    // ダークモード・ライトモードの監視を開始
    initThemeObserver();
    
    // 初期化処理（少し遅延させてChainlitのスタイル適用後に実行）
    setTimeout(() => {
        applyInitialTheme();
        // テスト用の動的要素を即座に作成
        createTestAnimation();
    }, 1000);
});

// テスト用の動的アニメーション（デバッグ用）
function createTestAnimation() {
    console.log('Creating test animation...');
    
    // 既存のテスト要素を削除
    document.getElementById('test-animation')?.remove();
    
    const testContainer = document.createElement('div');
    testContainer.id = 'test-animation';
    testContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: -1;
        opacity: 0.8;
    `;
    
    // 5個のテスト用粒子を作成
    for (let i = 0; i < 5; i++) {
        const particle = document.createElement('div');
        particle.style.cssText = `
            position: absolute;
            width: 10px;
            height: 10px;
            background: radial-gradient(circle, #667eea 0%, transparent 70%);
            border-radius: 50%;
            top: 90%;
            left: ${20 + i * 15}%;
            animation: simpleFloat 3s infinite ease-in-out ${i * 0.5}s;
            box-shadow: 0 0 15px rgba(102, 126, 234, 0.5);
        `;
        testContainer.appendChild(particle);
    }
    
    document.body.appendChild(testContainer);
    
    // CSS アニメーションを追加
    if (!document.getElementById('test-animation-style')) {
        const style = document.createElement('style');
        style.id = 'test-animation-style';
        style.textContent = `
            @keyframes simpleFloat {
                0% {
                    transform: translateY(0px);
                    opacity: 0.3;
                }
                50% {
                    transform: translateY(-100px);
                    opacity: 1;
                }
                100% {
                    transform: translateY(-200px);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    console.log('Test animation created');
}

// テーマ監視の初期化
function initThemeObserver() {
    // MutationObserverの設定 | ダークモード・ライトモードの切り替え後の処理
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            if (mutation.attributeName === 'class') {
                const htmlElement = document.getElementsByTagName('html')[0];
                const isDarkMode = htmlElement.classList.contains('dark');
                
                console.log('Theme changed:', isDarkMode ? 'dark' : 'light');
                
                if (!isDarkMode) {
                    applyLightTheme();
                } else {
                    applyDarkTheme();
                }
                
                // テーマ切り替え時の脈動効果
                document.body.classList.add('theme-pulse');
                setTimeout(() => {
                    document.body.classList.remove('theme-pulse');
                }, 600);
            }
        });
    });

    // 監視の開始
    const htmlElement = document.getElementsByTagName('html')[0];
    observer.observe(htmlElement, {
        attributes: true, // 属性の変更を監視
        attributeFilter: ['class'] // classの変更のみを監視
    });
}

// 初期テーマの適用
function applyInitialTheme() {
    const htmlElement = document.getElementsByTagName('html')[0];
    const isDarkMode = htmlElement.classList.contains('dark');
    
    if (!isDarkMode) {
        applyLightTheme();
    } else {
        applyDarkTheme();
    }
}

// ライトテーマの適用
function applyLightTheme() {
    console.log('Applying light theme');
    
    // CSS変数を動的に設定
    const root = document.documentElement;
    root.style.setProperty('--primary-color', '#667eea');
    root.style.setProperty('--primary-gradient', 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)');
    root.style.setProperty('--hero-gradient', 'linear-gradient(135deg, #667eea 0%, #764ba2 100%)');
    root.style.setProperty('--secondary-color', '#f8fafc');
    root.style.setProperty('--background-color', '#ffffff');
    root.style.setProperty('--surface-color', '#ffffff');
    root.style.setProperty('--text-color', '#1f2937');
    root.style.setProperty('--text-muted', '#6b7280');
    root.style.setProperty('--border-color', '#e5e7eb');
    root.style.setProperty('--chat-bg', '#f9fafb');
    
    // 背景グラデーション
    createLightBackground();
    
    // グラスモーフィズム効果を適用
    applyGlassmorphism(true);
}

// ダークテーマの適用
function applyDarkTheme() {
    console.log('Applying dark theme');
    
    // CSS変数を動的に設定
    const root = document.documentElement;
    root.style.setProperty('--primary-color', '#818cf8');
    root.style.setProperty('--primary-gradient', 'linear-gradient(135deg, #818cf8 0%, #a855f7 100%)');
    root.style.setProperty('--hero-gradient', 'linear-gradient(135deg, #1e3a8a 0%, #312e81 100%)');
    root.style.setProperty('--secondary-color', '#374151');
    root.style.setProperty('--background-color', '#111827');
    root.style.setProperty('--surface-color', '#1f2937');
    root.style.setProperty('--text-color', '#f9fafb');
    root.style.setProperty('--text-muted', '#9ca3af');
    root.style.setProperty('--border-color', '#374151');
    root.style.setProperty('--chat-bg', '#0f172a');
    
    // 背景グラデーション
    createDarkBackground();
    
    // グラスモーフィズム効果を適用
    applyGlassmorphism(false);
}

// ライトテーマの背景作成
function createLightBackground() {
    // 既存の背景を削除
    clearDarkBackground();
    
    // ライト用の動的背景を作成
    let lightBg = document.getElementById('light-background');
    if (!lightBg) {
        lightBg = document.createElement('div');
        lightBg.id = 'light-background';
        lightBg.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 20%, rgba(102, 126, 234, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(118, 75, 162, 0.1) 0%, transparent 50%),
                radial-gradient(circle at 40% 60%, rgba(102, 126, 234, 0.05) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
            transition: opacity 0.5s ease;
            overflow: hidden;
        `;
        document.body.appendChild(lightBg);
    }
    
    // 浮遊する光の粒子を作成
    createFloatingParticles();
    
    // 雲のような動く背景を作成
    createFloatingClouds();
}

// 浮遊する光の粒子（ライトモード用）
function createFloatingParticles() {
    let particleContainer = document.getElementById('floating-particles');
    if (particleContainer) {
        particleContainer.remove();
    }
    
    particleContainer = document.createElement('div');
    particleContainer.id = 'floating-particles';
    particleContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: -1;
        opacity: 0.6;
    `;
    
    // 30個の光の粒子を生成
    for (let i = 0; i < 30; i++) {
        const particle = document.createElement('div');
        const size = Math.random() * 6 + 2;
        const duration = Math.random() * 20 + 15;
        const delay = Math.random() * 10;
        const animationNames = ['floatLight', 'floatLight2', 'floatLight3'];
        const animationName = animationNames[i % 3];
        
        particle.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: radial-gradient(circle, rgba(102, 126, 234, 0.8) 0%, rgba(102, 126, 234, 0.2) 70%, transparent 100%);
            border-radius: 50%;
            top: 100%;
            left: ${Math.random() * 100}%;
            animation: ${animationName} ${duration}s infinite linear ${delay}s;
            filter: blur(1px);
            box-shadow: 0 0 10px rgba(102, 126, 234, 0.3);
        `;
        particleContainer.appendChild(particle);
    }
    
    // CSS アニメーションを追加
    if (!document.getElementById('light-particles-style')) {
        const style = document.createElement('style');
        style.id = 'light-particles-style';
        style.textContent = `
            @keyframes floatLight {
                0% {
                    transform: translateY(100vh) translateX(0px) scale(0);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(-100px) translateX(100px) scale(1);
                    opacity: 0;
                }
            }
            
            @keyframes floatLight2 {
                0% {
                    transform: translateY(100vh) translateX(0px) scale(0);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(-100px) translateX(-50px) scale(1);
                    opacity: 0;
                }
            }
            
            @keyframes floatLight3 {
                0% {
                    transform: translateY(100vh) translateX(0px) scale(0);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateY(-100px) translateX(0px) scale(1);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(particleContainer);
}

// 浮遊する雲（ライトモード用）
function createFloatingClouds() {
    let cloudsContainer = document.getElementById('floating-clouds');
    if (cloudsContainer) {
        cloudsContainer.remove();
    }
    
    cloudsContainer = document.createElement('div');
    cloudsContainer.id = 'floating-clouds';
    cloudsContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: -1;
        opacity: 0.3;
    `;
    
    // 5個の雲を生成
    for (let i = 0; i < 5; i++) {
        const cloud = document.createElement('div');
        const size = Math.random() * 150 + 100;
        const duration = Math.random() * 30 + 40;
        const delay = Math.random() * 20;
        
        cloud.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size * 0.6}px;
            background: radial-gradient(ellipse, rgba(102, 126, 234, 0.1) 0%, rgba(118, 75, 162, 0.05) 50%, transparent 100%);
            border-radius: 50px;
            top: ${Math.random() * 80}%;
            left: -${size}px;
            animation: floatCloud ${duration}s infinite linear ${delay}s;
            filter: blur(2px);
        `;
        cloudsContainer.appendChild(cloud);
    }
    
    // CSS アニメーションを追加
    if (!document.getElementById('light-clouds-style')) {
        const style = document.createElement('style');
        style.id = 'light-clouds-style';
        style.textContent = `
            @keyframes floatCloud {
                0% {
                    transform: translateX(0);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateX(calc(100vw + 200px));
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(cloudsContainer);
}

// ダークテーマの背景作成
function createDarkBackground() {
    // 既存の背景を削除
    clearLightBackground();
    
    // ダークな背景グラデーションを作成
    let darkBg = document.getElementById('dark-background');
    if (!darkBg) {
        darkBg = document.createElement('div');
        darkBg.id = 'dark-background';
        darkBg.style.cssText = `
            position: fixed;
            top: 0;
            left: 0;
            right: 0;
            bottom: 0;
            background: 
                radial-gradient(circle at 20% 20%, rgba(30, 58, 138, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 80% 80%, rgba(49, 46, 129, 0.2) 0%, transparent 50%),
                radial-gradient(circle at 40% 60%, rgba(30, 58, 138, 0.1) 0%, transparent 50%);
            pointer-events: none;
            z-index: -1;
            transition: opacity 0.5s ease;
            overflow: hidden;
        `;
        document.body.appendChild(darkBg);
    }
    
    // 星空効果を追加
    createStarField();
    
    // 流星群を追加
    createShootingStars();
    
    // 浮遊するエネルギー粒子を追加
    createEnergyParticles();
}

// 星空エフェクトの作成（改良版）
function createStarField() {
    let starField = document.getElementById('star-field');
    if (starField) {
        starField.remove();
    }
    
    starField = document.createElement('div');
    starField.id = 'star-field';
    starField.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: -1;
        opacity: 0.8;
    `;
    
    // 星を生成（大きさを変えて奥行き感を出す）
    for (let i = 0; i < 80; i++) {
        const star = document.createElement('div');
        const size = Math.random() * 3 + 1;
        const twinkleSpeed = Math.random() * 3 + 2;
        
        star.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: radial-gradient(circle, rgba(255, 255, 255, 1) 0%, rgba(129, 140, 248, 0.8) 40%, transparent 100%);
            border-radius: 50%;
            top: ${Math.random() * 100}%;
            left: ${Math.random() * 100}%;
            animation: twinkle ${twinkleSpeed}s infinite, drift ${20 + Math.random() * 30}s infinite linear;
            filter: blur(0.5px);
        `;
        starField.appendChild(star);
    }
    
    // アニメーション用のCSS
    if (!document.getElementById('star-animation-style')) {
        const style = document.createElement('style');
        style.id = 'star-animation-style';
        style.textContent = `
            @keyframes twinkle {
                0%, 100% { 
                    opacity: 0.3; 
                }
                50% { 
                    opacity: 1; 
                }
            }
            
            @keyframes drift {
                0% { 
                    transform: translateX(0px) translateY(0px); 
                }
                25% { 
                    transform: translateX(10px) translateY(-5px); 
                }
                50% { 
                    transform: translateX(-5px) translateY(-10px); 
                }
                75% { 
                    transform: translateX(-10px) translateY(5px); 
                }
                100% { 
                    transform: translateX(0px) translateY(0px); 
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(starField);
}

// 流星群エフェクト（ダークモード用）
function createShootingStars() {
    let shootingStarsContainer = document.getElementById('shooting-stars');
    if (shootingStarsContainer) {
        shootingStarsContainer.remove();
    }
    
    shootingStarsContainer = document.createElement('div');
    shootingStarsContainer.id = 'shooting-stars';
    shootingStarsContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;
        bottom: 0;
        pointer-events: none;
        z-index: -1;
        opacity: 0.9;
    `;
    
    // 流星を定期的に生成
    function createShootingStar() {
        const shootingStar = document.createElement('div');
        const length = Math.random() * 80 + 40;
        const duration = Math.random() * 2 + 1;
        const startX = Math.random() * window.innerWidth;
        const startY = -20;
        
        shootingStar.style.cssText = `
            position: absolute;
            width: ${length}px;
            height: 2px;
            background: linear-gradient(90deg, transparent 0%, rgba(129, 140, 248, 1) 20%, rgba(168, 85, 247, 0.8) 80%, transparent 100%);
            top: ${startY}px;
            left: ${startX}px;
            transform: rotate(45deg);
            animation: shootingStar ${duration}s linear;
            filter: blur(0.5px);
            box-shadow: 0 0 10px rgba(129, 140, 248, 0.5);
        `;
        
        shootingStarsContainer.appendChild(shootingStar);
        
        // アニメーション終了後に要素を削除
        setTimeout(() => {
            if (shootingStar.parentNode) {
                shootingStar.remove();
            }
        }, duration * 1000);
    }
    
    // CSS アニメーションを追加
    if (!document.getElementById('shooting-stars-style')) {
        const style = document.createElement('style');
        style.id = 'shooting-stars-style';
        style.textContent = `
            @keyframes shootingStar {
                0% {
                    transform: translateX(0) translateY(0) rotate(45deg);
                    opacity: 0;
                }
                10% {
                    opacity: 1;
                }
                90% {
                    opacity: 1;
                }
                100% {
                    transform: translateX(300px) translateY(300px) rotate(45deg);
                    opacity: 0;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(shootingStarsContainer);
    
    // 定期的に流星を生成（3-8秒間隔）
    function scheduleNextShootingStar() {
        const delay = Math.random() * 5000 + 3000;
        setTimeout(() => {
            createShootingStar();
            scheduleNextShootingStar();
        }, delay);
    }
    
    scheduleNextShootingStar();
}

// エネルギー粒子エフェクト（ダークモード用）
function createEnergyParticles() {
    let energyContainer = document.getElementById('energy-particles');
    if (energyContainer) {
        energyContainer.remove();
    }
    
    energyContainer = document.createElement('div');
    energyContainer.id = 'energy-particles';
    energyContainer.style.cssText = `
        position: fixed;
        top: 0;
        left: 0;
        right: 0;  
        bottom: 0;
        pointer-events: none;
        z-index: -1;
        opacity: 0.7;
    `;
    
    // 20個のエネルギー粒子を生成
    for (let i = 0; i < 20; i++) {
        const particle = document.createElement('div');
        const size = Math.random() * 8 + 3;
        const duration = Math.random() * 15 + 10;
        const delay = Math.random() * 10;
        
        particle.style.cssText = `
            position: absolute;
            width: ${size}px;
            height: ${size}px;
            background: radial-gradient(circle, rgba(129, 140, 248, 0.9) 0%, rgba(168, 85, 247, 0.6) 50%, transparent 100%);
            border-radius: 50%;
            top: ${Math.random() * 100}%;
            left: ${Math.random() * 100}%;
            animation: energyFloat ${duration}s infinite ease-in-out ${delay}s;
            filter: blur(1px);
            box-shadow: 0 0 20px rgba(129, 140, 248, 0.3);
        `;
        energyContainer.appendChild(particle);
    }
    
    // CSS アニメーションを追加
    if (!document.getElementById('energy-particles-style')) {
        const style = document.createElement('style');
        style.id = 'energy-particles-style';
        style.textContent = `
            @keyframes energyFloat {
                0%, 100% {
                    transform: translateY(0px) translateX(0px) scale(1);
                    opacity: 0.3;
                }
                25% {
                    transform: translateY(-30px) translateX(20px) scale(1.2);
                    opacity: 0.8;
                }
                50% {
                    transform: translateY(-60px) translateX(-10px) scale(0.8);
                    opacity: 1;
                }
                75% {
                    transform: translateY(-30px) translateX(-25px) scale(1.1);
                    opacity: 0.6;
                }
            }
        `;
        document.head.appendChild(style);
    }
    
    document.body.appendChild(energyContainer);
}

// 背景をクリア
function clearLightBackground() {
    document.getElementById('light-background')?.remove();
    document.getElementById('floating-particles')?.remove();
    document.getElementById('floating-clouds')?.remove();
}

function clearDarkBackground() {
    document.getElementById('dark-background')?.remove();
    document.getElementById('star-field')?.remove();
    document.getElementById('shooting-stars')?.remove();
    document.getElementById('energy-particles')?.remove();
}

// テーマ切り替え時のトランジションエフェクト
function addThemeTransition() {
    if (!document.getElementById('theme-transition-style')) {
        const style = document.createElement('style');
        style.id = 'theme-transition-style';
        style.textContent = `
            /* テーマ切り替え時のスムーズなトランジション */
            body, 
            .message-bubble, 
            .custom-element, 
            .chat-profile, 
            .action-button,
            .sidebar {
                transition: all 0.3s ease !important;
            }
            
            /* 背景要素のフェードイン効果 */
            #light-background,
            #dark-background,
            #star-field,
            #floating-particles,
            #floating-clouds,
            #energy-particles {
                animation: fadeIn 0.8s ease-out;
            }
            
            @keyframes fadeIn {
                from {
                    opacity: 0;
                }
                to {
                    opacity: 1;
                }
            }
            
            /* テーマ切り替え時の脈動効果 */
            .theme-pulse {
                animation: themePulse 0.6s ease-out;
            }
            
            @keyframes themePulse {
                0% { transform: scale(1); }
                50% { transform: scale(1.02); }
                100% { transform: scale(1); }
            }
        `;
        document.head.appendChild(style);
    }
}

// グラスモーフィズム効果の適用
function applyGlassmorphism(isLight = true) {
    let existingStyle = document.getElementById('glassmorphism-style');
    if (existingStyle) {
        existingStyle.remove();
    }
    
    const style = document.createElement('style');
    style.id = 'glassmorphism-style';
    
    if (isLight) {
        // ライトモード用
        style.textContent = `
            .message-bubble, .custom-element, .chat-profile, .action-button {
                backdrop-filter: blur(10px) !important;
                background: rgba(255, 255, 255, 0.8) !important;
                border: 1px solid rgba(255, 255, 255, 0.2) !important;
            }
            
            .message-bubble.user {
                background: var(--primary-gradient) !important;
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(255, 255, 255, 0.3) !important;
            }
            
            .custom-hero .hero-background {
                backdrop-filter: blur(20px) !important;
            }
        `;
    } else {
        // ダークモード用
        style.textContent = `
            .message-bubble, .custom-element, .chat-profile, .action-button {
                backdrop-filter: blur(10px) !important;
                background: rgba(31, 41, 55, 0.8) !important;
                border: 1px solid rgba(55, 65, 81, 0.5) !important;
            }
            
            .message-bubble.user {
                background: var(--primary-gradient) !important;
                backdrop-filter: blur(10px) !important;
                border: 1px solid rgba(129, 140, 248, 0.3) !important;
            }
            
            .custom-hero .hero-background {
                backdrop-filter: blur(20px) !important;
            }
        `;
    }
    
    document.head.appendChild(style);
}

// メッセージ送信関数
function sendUserMessage(content) {
    // Chainlitのメッセージ送信APIを呼び出し
    if (window.chainlit && window.chainlit.sendMessage) {
        window.chainlit.sendMessage(content);
    } else {
        // フォールバック: 入力フィールドに値を設定して送信
        const inputField = document.querySelector('input[type="text"], textarea');
        if (inputField) {
            inputField.value = content;
            inputField.dispatchEvent(new Event('input', { bubbles: true }));
            
            // 送信ボタンをクリック
            const sendButton = document.querySelector('button[type="submit"]');
            if (sendButton) {
                sendButton.click();
            }
        }
    }
    
    // トースト通知を表示
    showToast('メッセージを送信しました', 'info');
}

// トースト通知の表示
function showToast(message, type = 'info', duration = 3000) {
    const toast = document.createElement('div');
    toast.className = `toast ${type}`;
    toast.textContent = message;
    
    document.body.appendChild(toast);
    
    // 自動削除
    setTimeout(() => {
        if (toast.parentNode) {
            toast.remove();
        }
    }, duration);
}

// ファイルドロップゾーンの初期化
function initFileDropZone() {
    const dropZones = document.querySelectorAll('.file-upload-area, [data-drop-zone]');
    
    dropZones.forEach(zone => {
        zone.addEventListener('dragover', handleDragOver);
        zone.addEventListener('drop', handleDrop);
        zone.addEventListener('dragenter', handleDragEnter);
        zone.addEventListener('dragleave', handleDragLeave);
    });
}

function handleDragOver(e) {
    e.preventDefault();
    e.currentTarget.classList.add('dragover');
}

function handleDragEnter(e) {
    e.preventDefault();
    e.currentTarget.classList.add('dragover');
}

function handleDragLeave(e) {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');
}

function handleDrop(e) {
    e.preventDefault();
    e.currentTarget.classList.remove('dragover');
    
    const files = Array.from(e.dataTransfer.files);
    if (files.length > 0) {
        showToast(`${files.length}個のファイルがアップロードされました`, 'success');
        // ここでファイル処理ロジックを実装
        handleFileUpload(files);
    }
}

// ファイルアップロード処理
function handleFileUpload(files) {
    files.forEach(file => {
        console.log('Processing file:', file.name, file.type, file.size);
        
        // ファイルタイプに応じた処理
        if (file.type.startsWith('image/')) {
            handleImageFile(file);
        } else if (file.type.includes('pdf')) {
            handlePDFFile(file);
        } else if (file.type.includes('text')) {
            handleTextFile(file);
        }
    });
}

function handleImageFile(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        console.log('Image loaded:', e.target.result.substring(0, 50) + '...');
        // 画像プレビュー表示などの処理
    };
    reader.readAsDataURL(file);
}

function handlePDFFile(file) {
    console.log('PDF file detected:', file.name);
    // PDF処理ロジック
}

function handleTextFile(file) {
    const reader = new FileReader();
    reader.onload = function(e) {
        console.log('Text content:', e.target.result.substring(0, 100) + '...');
        // テキスト処理ロジック
    };
    reader.readAsText(file);
}

// カスタムイベントリスナーの初期化
function initCustomEventListeners() {
    // アクションボタンのクリックイベント
    document.addEventListener('click', function(e) {
        if (e.target.classList.contains('action-button')) {
            handleActionButtonClick(e.target);
        }
    });
    
    // メッセージバブルのアニメーション
    const observer = new MutationObserver(function(mutations) {
        mutations.forEach(function(mutation) {
            mutation.addedNodes.forEach(function(node) {
                if (node.nodeType === 1 && node.classList.contains('message-bubble')) {
                    node.style.opacity = '0';
                    node.style.transform = 'translateY(10px)';
                    
                    requestAnimationFrame(() => {
                        node.style.transition = 'opacity 0.3s ease-out, transform 0.3s ease-out';
                        node.style.opacity = '1';
                        node.style.transform = 'translateY(0)';
                    });
                }
            });
        });
    });
    
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
}

// アクションボタンのクリック処理
function handleActionButtonClick(button) {
    const action = button.dataset.action;
    const label = button.textContent;
    
    console.log('Action button clicked:', action, label);
    
    // ボタンアニメーション
    button.style.transform = 'scale(0.95)';
    setTimeout(() => {
        button.style.transform = 'scale(1)';
    }, 150);
    
    // アクションに応じた処理
    switch (action) {
        case 'summary':
            showToast('要約を作成しています...', 'info');
            break;
        case 'detail':
            showToast('詳細を説明しています...', 'info');
            break;
        case 'custom':
            showToast('カスタムプロンプトを表示します', 'info');
            break;
        default:
            showToast(`${label} を実行中`, 'info');
    }
}

// ユーティリティ関数
const utils = {
    // 文字列のハイライト
    highlightText: function(text, query) {
        if (!query) return text;
        const regex = new RegExp(`(${query})`, 'gi');
        return text.replace(regex, '<mark>$1</mark>');
    },
    
    // 文字数制限
    truncateText: function(text, maxLength = 100) {
        if (text.length <= maxLength) return text;
        return text.substring(0, maxLength) + '...';
    },
    
    // 時間フォーマット
    formatTime: function(date) {
        return new Intl.DateTimeFormat('ja-JP', {
            hour: '2-digit',
            minute: '2-digit'
        }).format(date);
    },
    
    // ファイルサイズフォーマット
    formatFileSize: function(bytes) {
        const sizes = ['Bytes', 'KB', 'MB', 'GB'];
        if (bytes === 0) return '0 Bytes';
        const i = Math.floor(Math.log(bytes) / Math.log(1024));
        return Math.round(bytes / Math.pow(1024, i) * 100) / 100 + ' ' + sizes[i];
    }
};

// グローバルユーティリティとして公開
window.chainlitUtils = utils;