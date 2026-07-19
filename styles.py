def get_custom_css():
    return """
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;500;600;700&display=swap');

/* Sayfa Arkaplanı ve Yazı Tipleri */
html, body, [data-testid="stAppViewContainer"], .stWidgetLabel {
    font-family: 'Outfit', sans-serif !important;
}

[data-testid="stAppViewContainer"] {
    background: transparent !important;
}

/* Sol Sidebar Tasarımı (Floating Glass Island) */
[data-testid="stSidebar"] {
    background-color: transparent !important;
    border-right: none !important;
}

[data-testid="stSidebarUserContent"] {
    background-color: rgba(10, 15, 28, 0.6) !important;
    backdrop-filter: blur(20px) !important;
    -webkit-backdrop-filter: blur(20px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 20px !important;
    margin: 15px !important;
    height: calc(100vh - 30px) !important;
    padding: 24px 20px !important;
    box-shadow: 0 15px 35px rgba(0, 0, 0, 0.5) !important;
    transition: all 0.3s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
}

[data-testid="stSidebarUserContent"]:hover {
    border-color: rgba(14, 165, 233, 0.25) !important;
    box-shadow: 0 20px 45px rgba(14, 165, 233, 0.12) !important;
}

/* Sidebar Radio Button custom navigation pills */
div[data-testid="stRadio"] label {
    font-weight: 600 !important;
    font-size: 14px !important;
    color: #94a3b8 !important;
    margin-bottom: 10px !important;
}

/* Style active/inactive navigation pills */
div[data-testid="stRadio"] div[role="radiogroup"] > div {
    background-color: rgba(255, 255, 255, 0.01) !important;
    border: 1px solid rgba(255, 255, 255, 0.02) !important;
    border-radius: 10px !important;
    padding: 10px 14px !important;
    margin-bottom: 8px !important;
    transition: all 0.25s cubic-bezier(0.25, 0.8, 0.25, 1) !important;
    cursor: pointer !important;
}

div[data-testid="stRadio"] div[role="radiogroup"] > div:hover {
    background-color: rgba(14, 165, 233, 0.06) !important;
    border-color: rgba(14, 165, 233, 0.2) !important;
    transform: translateX(5px) !important;
}

/* Style selected active radio pill */
div[data-testid="stRadio"] div[role="radiogroup"] div[data-checked="true"] {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(14, 165, 233, 0.15) 100%) !important;
    border-color: rgba(16, 185, 129, 0.4) !important;
    box-shadow: 0 0 12px rgba(16, 185, 129, 0.12) !important;
}

/* Hide Streamlit default radio check circles inside sidebar group */
div[data-testid="stRadio"] div[role="radiogroup"] label div[dir="ltr"] {
    display: none !important;
}

/* Hareketli Balon (Panning Gradient Blobs) Efekti */
@keyframes float-blob-1 {
    0% { transform: translate(0px, 0px) scale(1); }
    33% { transform: translate(80px, -100px) scale(1.25); }
    66% { transform: translate(-60px, 50px) scale(0.85); }
    100% { transform: translate(0px, 0px) scale(1); }
}
@keyframes float-blob-2 {
    0% { transform: translate(0px, 0px) scale(1); }
    50% { transform: translate(-100px, 100px) scale(1.15); }
    100% { transform: translate(0px, 0px) scale(1); }
}

.bg-blob {
    position: fixed;
    border-radius: 50%;
    filter: blur(90px);
    z-index: -1;
    pointer-events: none;
    opacity: 0.5;
}
.bg-blob-1 {
    top: 10%;
    left: 15%;
    width: 320px;
    height: 320px;
    background: radial-gradient(circle, rgba(16, 185, 129, 0.25) 0%, rgba(0,0,0,0) 70%);
    animation: float-blob-1 22s infinite ease-in-out;
}
.bg-blob-2 {
    bottom: 12%;
    right: 18%;
    width: 420px;
    height: 420px;
    background: radial-gradient(circle, rgba(14, 165, 233, 0.25) 0%, rgba(0,0,0,0) 70%);
    animation: float-blob-2 28s infinite ease-in-out;
}

/* Dinamik Renk Geçişli Yazı Efekti */
.animated-gradient-text {
    background: linear-gradient(-45deg, #10b981, #0ea5e9, #6366f1, #10b981);
    background-size: 300% 300%;
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    animation: text-gradient 7s ease infinite;
}
@keyframes text-gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Balon Gibi Yüzme & Sallanma Animasyonları */
@keyframes sway-slow {
    0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    50% { transform: translateY(-8px) translateX(4px) rotate(0.4deg); }
    100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
}

@keyframes sway-medium {
    0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    50% { transform: translateY(-10px) translateX(-4px) rotate(-0.3deg); }
    100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
}

@keyframes sway-fast {
    0% { transform: translateY(0px) translateX(0px) rotate(0deg); }
    50% { transform: translateY(-7px) translateX(3px) rotate(0.2deg); }
    100% { transform: translateY(0px) translateX(0px) rotate(0deg); }
}

/* Premium Kart Tasarımı (Custom Card) */
.custom-card {
    background: transparent !important;
    border: none !important;
    box-shadow: none !important;
    backdrop-filter: none !important;
    -webkit-backdrop-filter: none !important;
    padding: 10px 0 !important;
    margin-bottom: 20px;
    animation: sway-slow 12s infinite ease-in-out !important;
}

/* Giriş Kartı Özel Tasarımı */
.login-card {
    background: rgba(10, 14, 23, 0.7) !important;
    backdrop-filter: blur(12px) !important;
    -webkit-backdrop-filter: blur(12px) !important;
    border: 1px solid rgba(255, 255, 255, 0.08) !important;
    border-radius: 16px !important;
    padding: 30px !important;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.6) !important;
}

/* Metrik Kartı Tasarımları (Vibrant Border & Glow) */
.kpi-container {
    display: flex;
    gap: 20px;
    margin-bottom: 25px;
}
.kpi-card {
    flex: 1;
    border-radius: 12px;
    padding: 20px;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.4);
    transition: all 0.3s ease;
    animation: sway-fast 7s infinite ease-in-out !important;
}
.kpi-card:nth-child(even) {
    animation: sway-medium 9s infinite ease-in-out !important;
}

.kpi-card.blue {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(14, 165, 233, 0.25) !important;
}
.kpi-card.blue:hover {
    background-color: rgba(14, 165, 233, 0.08) !important;
    border: 1px solid rgba(14, 165, 233, 0.5) !important;
    box-shadow: 0 8px 24px rgba(14, 165, 233, 0.15) !important;
}
.kpi-card.blue .kpi-value {
    color: #0ea5e9 !important;
}

.kpi-card.red {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(239, 68, 68, 0.25) !important;
}
.kpi-card.red:hover {
    background-color: rgba(239, 68, 68, 0.08) !important;
    border: 1px solid rgba(239, 68, 68, 0.5) !important;
    box-shadow: 0 8px 24px rgba(239, 68, 68, 0.15) !important;
}
.kpi-card.red .kpi-value {
    color: #ef4444 !important;
}

.kpi-card.orange {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(245, 158, 11, 0.25) !important;
}
.kpi-card.orange:hover {
    background-color: rgba(245, 158, 11, 0.08) !important;
    border: 1px solid rgba(245, 158, 11, 0.5) !important;
    box-shadow: 0 8px 24px rgba(245, 158, 11, 0.15) !important;
}
.kpi-card.orange .kpi-value {
    color: #f59e0b !important;
}

.kpi-card.green {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(16, 185, 129, 0.25) !important;
}
.kpi-card.green:hover {
    background-color: rgba(16, 185, 129, 0.08) !important;
    border: 1px solid rgba(16, 185, 129, 0.5) !important;
    box-shadow: 0 8px 24px rgba(16, 185, 129, 0.15) !important;
}
.kpi-card.green .kpi-value {
    color: #10b981 !important;
}

.kpi-card.purple {
    background-color: rgba(10, 14, 23, 0.5) !important;
    backdrop-filter: blur(10px) !important;
    border: 1px solid rgba(139, 92, 246, 0.25) !important;
}
.kpi-card.purple:hover {
    background-color: rgba(139, 92, 246, 0.08) !important;
    border: 1px solid rgba(139, 92, 246, 0.5) !important;
    box-shadow: 0 8px 24px rgba(139, 92, 246, 0.15) !important;
}
.kpi-card.purple .kpi-value {
    color: #8b5cf6 !important;
}
.kpi-title {
    color: #94a3b8;
    font-size: 14px;
    font-weight: 500;
    margin-bottom: 5px;
}
.kpi-value {
    color: #f8fafc;
    font-size: 28px;
    font-weight: 700;
}

/* Tablolar ve Veri Çerçeveleri */
[data-testid="stDataFrame"] {
    animation: sway-medium 10s infinite ease-in-out !important;
    background: #111827 !important;
    border: 1px solid rgba(255, 255, 255, 0.05) !important;
    border-radius: 12px !important;
    padding: 10px !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4) !important;
}

/* Sonuç Panelleri */
.result-card {
    border-radius: 12px;
    padding: 24px;
    margin-top: 20px;
    color: #f8fafc;
    box-shadow: 0 10px 25px rgba(0,0,0,0.4);
    animation: sway-slow 7s infinite ease-in-out !important;
}
.result-card.risk {
    background: linear-gradient(135deg, rgba(244, 63, 94, 0.15) 0%, rgba(159, 18, 57, 0.3) 100%);
    border: 1px solid rgba(244, 63, 94, 0.4);
}
.result-card.loyal {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.15) 0%, rgba(6, 78, 59, 0.3) 100%);
    border: 1px solid rgba(16, 185, 129, 0.4);
}

/* ====================================================
   AÇIK MOD (LIGHT THEME) OVERRIDES & FIXES
   ==================================================== */
.light-theme {
    color: #0f172a !important;
}

.light-theme .kpi-title {
    color: #475569 !important;
}
.light-theme .kpi-value {
    color: #0f172a !important;
}

.light-theme .kpi-card {
    background-color: rgba(255, 255, 255, 0.45) !important;
    backdrop-filter: blur(8px) !important;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.04) !important;
}

.light-theme .kpi-card.blue {
    border: 1px solid rgba(14, 165, 233, 0.4) !important;
}
.light-theme .kpi-card.blue .kpi-value {
    color: #0369a1 !important;
}

.light-theme .kpi-card.red {
    border: 1px solid rgba(239, 68, 68, 0.4) !important;
}
.light-theme .kpi-card.red .kpi-value {
    color: #b91c1c !important;
}

.light-theme .kpi-card.orange {
    border: 1px solid rgba(245, 158, 11, 0.4) !important;
}
.light-theme .kpi-card.orange .kpi-value {
    color: #c2410c !important;
}

.light-theme .kpi-card.green {
    border: 1px solid rgba(16, 185, 129, 0.4) !important;
}
.light-theme .kpi-card.green .kpi-value {
    color: #047857 !important;
}

.light-theme .kpi-card.purple {
    border: 1px solid rgba(139, 92, 246, 0.4) !important;
}
.light-theme .kpi-card.purple .kpi-value {
    color: #6d28d9 !important;
}

/* Light mode login overrides */
.light-theme .login-card {
    background: rgba(255, 255, 255, 0.75) !important;
    border: 1px solid rgba(0, 0, 0, 0.08) !important;
    box-shadow: 0 10px 30px -10px rgba(0, 0, 0, 0.08) !important;
}
.light-theme .login-card h3 {
    color: #0f172a !important;
}

/* Light mode support ticket & results card text fix */
.light-theme .result-card {
    color: #1e293b !important;
    box-shadow: 0 10px 25px rgba(0,0,0,0.05) !important;
}
.light-theme .result-card.risk {
    background: linear-gradient(135deg, rgba(244, 63, 94, 0.08) 0%, rgba(244, 63, 94, 0.15) 100%) !important;
    border: 1px solid rgba(244, 63, 94, 0.3) !important;
}
.light-theme .result-card.loyal {
    background: linear-gradient(135deg, rgba(16, 185, 129, 0.08) 0%, rgba(16, 185, 129, 0.15) 100%) !important;
    border: 1px solid rgba(16, 185, 129, 0.3) !important;
}

/* Light mode text gradient adjustment for better contrast */
.light-theme .animated-gradient-text {
    background: linear-gradient(-45deg, #047857, #0284c7, #5b21b6, #047857) !important;
    -webkit-background-clip: text !important;
    -webkit-text-fill-color: transparent !important;
}

/* Dynamic text colors inside general custom-markdown blocks */
.light-theme p, .light-theme span, .light-theme li {
    color: #334155 !important;
}
.light-theme strong {
    color: #0f172a !important;
}

/* Light mode sidebar overrides (Floating Island) */
.light-theme [data-testid="stSidebar"] {
    background-color: transparent !important;
    border-right: none !important;
}

.light-theme [data-testid="stSidebarUserContent"] {
    background-color: rgba(255, 255, 255, 0.55) !important;
    border: 1px solid rgba(0, 0, 0, 0.08) !important;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05) !important;
}

.light-theme div[data-testid="stRadio"] label {
    color: #475569 !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] > div {
    background-color: rgba(0, 0, 0, 0.02) !important;
    border: 1px solid rgba(0, 0, 0, 0.03) !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] > div:hover {
    background-color: rgba(3, 105, 161, 0.06) !important;
    border-color: rgba(3, 105, 161, 0.15) !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] div[data-checked="true"] {
    background: linear-gradient(135deg, rgba(4, 120, 87, 0.1) 0%, rgba(3, 105, 161, 0.1) 100%) !important;
    border-color: rgba(4, 120, 87, 0.3) !important;
    box-shadow: 0 0 12px rgba(4, 120, 87, 0.05) !important;
}

.light-theme div[data-testid="stRadio"] div[role="radiogroup"] label p {
    color: #1e293b !important;
}
</style>
"""

def get_3d_javascript():
    return """
<div class="bg-blob bg-blob-1"></div>
<div class="bg-blob bg-blob-2"></div>

<script>
const injectInteractiveEffects = () => {
    const parentDoc = window.parent.document;
    
    // Background canvas control
    if (!parentDoc.getElementById('cyber-interactive-bg')) {
        const canvas = parentDoc.createElement('canvas');
        canvas.id = 'cyber-interactive-bg';
        canvas.style.position = 'fixed';
        canvas.style.top = '0';
        canvas.style.left = '0';
        canvas.style.width = '100vw';
        canvas.style.height = '100vh';
        canvas.style.zIndex = '-2';
        canvas.style.pointerEvents = 'none';
        canvas.style.background = '#03050a'; // Ultra dark black mode
        parentDoc.body.appendChild(canvas);
        
        const ctx = canvas.getContext('2d');
        let width = canvas.width = parentDoc.documentElement.clientWidth;
        let height = canvas.height = parentDoc.documentElement.clientHeight;
        
        window.parent.addEventListener('resize', () => {
            width = canvas.width = parentDoc.documentElement.clientWidth;
            height = canvas.height = parentDoc.documentElement.clientHeight;
        });
        
        let mouse = { x: width / 2, y: height / 2, tx: width / 2, ty: height / 2 };
        parentDoc.addEventListener('mousemove', (e) => {
            mouse.tx = e.clientX;
            mouse.ty = e.clientY;
        });
        
        // Money rain definitions
        const moneyChars = ['$', '€', '₺', '£', '₿'];
        const numDrops = 110;
        const drops = [];
        for (let i = 0; i < numDrops; i++) {
            drops.push({
                x: Math.random() * width,
                y: Math.random() * height - height,
                z: Math.random() * 600,
                speed: Math.random() * 1.5 + 0.6,
                char: moneyChars[Math.floor(Math.random() * moneyChars.length)],
                fontSize: Math.random() * 12 + 10
            });
        }
        
        const animate = () => {
            // Check light mode dynamically from parent document text color
            const mainEl = parentDoc.querySelector('section.main') || parentDoc.body;
            const textColor = window.parent.getComputedStyle(mainEl).getPropertyValue('--text-color').trim();
            const isLight = textColor.includes('49') || textColor.includes('51') || textColor.includes('31333F') || textColor.includes('rgb(49') || textColor.includes('rgb(51');
            
            // Toggle light-theme class on iframe body
            if (isLight) {
                document.body.classList.add('light-theme');
                document.body.classList.remove('dark-theme');
                canvas.style.background = '#f8fafc';
                ctx.fillStyle = 'rgba(248, 250, 252, 0.18)';
            } else {
                document.body.classList.add('dark-theme');
                document.body.classList.remove('light-theme');
                canvas.style.background = '#03050a';
                ctx.fillStyle = 'rgba(3, 5, 10, 0.18)';
            }
            
            mouse.x += (mouse.tx - mouse.x) * 0.08;
            mouse.y += (mouse.ty - mouse.y) * 0.08;
            
            ctx.fillRect(0, 0, width, height);
            
            drops.forEach(d => {
                d.y += d.speed;
                
                if (d.y > height) {
                    d.y = -50;
                    d.x = Math.random() * width;
                    d.char = moneyChars[Math.floor(Math.random() * moneyChars.length)];
                }
                
                // Mouse interaction: push drops away horizontally
                const dx = d.x - mouse.x;
                const dy = d.y - mouse.y;
                const dist = Math.sqrt(dx * dx + dy * dy);
                if (dist < 150) {
                    const force = (150 - dist) * 0.05;
                    d.x += (dx / dist) * force;
                }
                
                // 3D Perspective math
                const fov = 300;
                const scale = fov / (fov + d.z);
                const projX = d.x;
                const projY = d.y;
                
                // Opacity based on Z depth: deeper drops are smaller and darker
                const alpha = (1 - d.z / 600) * (isLight ? 0.14 : 0.18);
                const size = d.fontSize * scale;
                
                ctx.font = `600 ${size}px Outfit, sans-serif`;
                ctx.fillStyle = isLight ? `rgba(15, 118, 110, ${alpha})` : `rgba(16, 185, 129, ${alpha})`;
                ctx.fillText(d.char, projX, projY);
            });
            
            // Mouse gradient glow light beam
            const grad = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 220);
            if (isLight) {
                grad.addColorStop(0, 'rgba(3, 105, 161, 0.05)');
                grad.addColorStop(0.5, 'rgba(15, 118, 110, 0.02)');
            } else {
                grad.addColorStop(0, 'rgba(14, 165, 233, 0.06)');
                grad.addColorStop(0.5, 'rgba(16, 185, 129, 0.02)');
            }
            grad.addColorStop(1, 'rgba(0, 0, 0, 0)');
            ctx.fillStyle = grad;
            ctx.fillRect(0, 0, width, height);
            
            requestAnimationFrame(animate);
        };
        animate();
    }
    
    // Global 3D Perspective Tilt on the entire Streamlit page viewport
    const applyGlobal3D = () => {
        const appContainer = parentDoc.querySelector('[data-testid="stAppViewContainer"]');
        const mainContent = parentDoc.querySelector('section.main');
        if (appContainer && mainContent && !mainContent.dataset.global3dActive) {
            mainContent.dataset.global3dActive = "true";
            appContainer.style.perspective = '1500px';
            appContainer.style.perspectiveOrigin = '50% 50%';
            
            mainContent.style.transformStyle = 'preserve-3d';
            mainContent.style.transition = 'transform 0.25s cubic-bezier(0.25, 0.8, 0.25, 1)';
            
            parentDoc.addEventListener('mousemove', (e) => {
                const xc = parentDoc.documentElement.clientWidth / 2;
                const yc = parentDoc.documentElement.clientHeight / 2;
                const angleX = -((e.clientY - yc) / yc) * 3; // Up to 3 deg tilt
                const angleY = ((e.clientX - xc) / xc) * 3; // Up to 3 deg tilt
                
                mainContent.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg) translateZ(0px)`;
            });
        }
    };
    
    // 3D Tilt effects for KPI cards (Local Parallax)
    const apply3DTilt = () => {
        const cards = parentDoc.querySelectorAll('.kpi-card, .login-card, [data-testid="stMetricValue"]');
        cards.forEach(card => {
            if (card.dataset.tiltActive) return;
            card.dataset.tiltActive = "true";
            
            card.style.transformStyle = 'preserve-3d';
            card.style.perspective = '1000px';
            card.style.transition = 'transform 0.15s ease-out, box-shadow 0.15s ease-out';
            
            card.addEventListener('mousemove', (e) => {
                const rect = card.getBoundingClientRect();
                const x = e.clientX - rect.left;
                const y = e.clientY - rect.top;
                const xc = rect.width / 2;
                const yc = rect.height / 2;
                
                const angleX = -(y - yc) / 7;
                const angleY = (x - xc) / 7;
                
                card.style.transform = `rotateX(${angleX}deg) rotateY(${angleY}deg) scale3d(1.025, 1.025, 1.025) translateZ(10px)`;
                card.style.boxShadow = `0 15px 35px rgba(14, 165, 233, 0.22)`;
            });
            
            card.addEventListener('mouseleave', () => {
                card.style.transform = 'rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1) translateZ(0px)';
                card.style.boxShadow = '';
            });
        });
    };
    
    const observer = new MutationObserver(() => {
        applyGlobal3D();
        apply3DTilt();
    });
    observer.observe(parentDoc.body, { childList: true, subtree: true });
    applyGlobal3D();
    apply3DTilt();
};

// Delay initialization slightly to guarantee DOM stability
setTimeout(injectInteractiveEffects, 500);
</script>
"""
