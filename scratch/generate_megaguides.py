import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="{lang_code}">
<head>
    <meta charset="utf-8"/>
    <meta name="viewport" content="width=device-width, initial-scale=1.0"/>
    <title>{title} — WorldOfTools</title>
    <meta name="description" content="{desc}"/>
    <link rel="canonical" href="https://worldoftools.in/guides/{slug}.html"/>
    <link rel="stylesheet" href="/css/style.css?v=6.1"/>
    <link rel="stylesheet" href="/css/neo-brutalism.css?v=6.1"/>
    <link rel="icon" href="/logo.svg" type="image/svg+xml"/>
    
    <style>
    body {{ background-color: var(--bg-color); font-family: 'Lexend', 'Inter', sans-serif; }}
    .guide-container {{
        max-width: 900px; margin: 2rem auto; padding: 3rem 2rem;
        background: #ffffff; border: 3px solid #111827; box-shadow: 8px 8px 0px #111827;
        border-radius: var(--nb-radius-lg, 12px); line-height: 1.8; color: #111827;
    }}
    .guide-header h1 {{ font-family: 'Space Grotesk', 'Lexend', sans-serif; font-weight: 900; letter-spacing: -0.04em; font-size: clamp(2rem, 5vw, 3rem); line-height: 1.1; margin-bottom: 1rem; }}
    .guide-content h2 {{ font-family: 'Space Grotesk', 'Lexend', sans-serif; font-weight: 800; font-size: 1.75rem; margin-top: 2.5rem; padding-bottom: 0.5rem; border-bottom: 3px dashed #e5e7eb; }}
    .info-card {{ background: var(--nb-mint, #dcfce7); border: 3px solid #111827; box-shadow: 5px 5px 0 #111827; border-radius: 8px; padding: 2rem; margin: 2rem 0; }}
    .tool-link-card {{
        display: flex; align-items: center; gap: 1rem; padding: 1.25rem;
        background: white; border: 3px solid #111827; border-radius: 12px;
        text-decoration: none; color: #111827; font-weight: 700; transition: all 0.2s;
        margin-bottom: 1rem; box-shadow: 4px 4px 0 #111827;
    }}
    .tool-link-card:hover {{ transform: translate(-3px, -3px); box-shadow: 7px 7px 0 #111827; background: var(--nb-lavender); }}
    .emoji-box {{ font-size: 2rem; }}
    </style>
</head>
<body>
    <header></header> <!-- Injected via js -->
    
    <main class="container">
        <div class="guide-container">
            <div class="guide-header" style="text-align: center; margin-bottom: 3rem;">
                <span style="background: var(--nb-yellow); border: 2px solid #000; padding: 0.25rem 1rem; border-radius: 99px; font-weight: 800; display: inline-block; margin-bottom: 1rem;">🌟 {tag}</span>
                <h1>{title}</h1>
                <p style="font-size: 1.25rem; color: #4b5563;">{desc}</p>
            </div>
            
            <div class="guide-content">
                <div class="info-card" style="background: var(--nb-pink);">
                    <h3>🚀 Welcome to WorldOfTools</h3>
                    <p>{intro}</p>
                </div>

                <h2>{h2_1}</h2>
                <a href="/gst-calculator" class="tool-link-card">
                    <span class="emoji-box">💰</span>
                    <div>
                        <div style="font-size: 1.2rem;">GST Calculator</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Add/Remove GST for Indian Tax Slabs (5%, 12%, 18%, 28%)</div>
                    </div>
                </a>
                <a href="/emi-calculator" class="tool-link-card">
                    <span class="emoji-box">🏠</span>
                    <div>
                        <div style="font-size: 1.2rem;">Loan EMI Calculator</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Plan your home/car loans and check interest amounts</div>
                    </div>
                </a>
                <a href="/sip-calculator" class="tool-link-card">
                    <span class="emoji-box">📈</span>
                    <div>
                        <div style="font-size: 1.2rem;">SIP Investment Calculator</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Calculate mutual fund returns and wealth growth</div>
                    </div>
                </a>

                <h2>{h2_2}</h2>
                <a href="/image-compressor" class="tool-link-card">
                    <span class="emoji-box">🖼️</span>
                    <div>
                        <div style="font-size: 1.2rem;">Image Compressor</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Reduce JPG/PNG sizes while maintaining quality</div>
                    </div>
                </a>
                <a href="/remove-watermark-from-image" class="tool-link-card">
                    <span class="emoji-box">✨</span>
                    <div>
                        <div style="font-size: 1.2rem;">Remove Watermark</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Extract unwanted objects or text from images</div>
                    </div>
                </a>

                <h2>{h2_3}</h2>
                <a href="/typing-speed-test" class="tool-link-card">
                    <span class="emoji-box">⌨️</span>
                    <div>
                        <div style="font-size: 1.2rem;">Typing Speed Test</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Practice formatting and speed to improve WPM</div>
                    </div>
                </a>
                <a href="/age-calculator" class="tool-link-card">
                    <span class="emoji-box">🎂</span>
                    <div>
                        <div style="font-size: 1.2rem;">Age Calculator</div>
                        <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Get exact chronological age and next birthday</div>
                    </div>
                </a>

                <div class="info-card" style="margin-top: 4rem; text-align: center;">
                    <h3 style="margin-top:0;">{footer_msg}</h3>
                    <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
                </div>
            </div>
        </div>
    </main>
    
    <footer></footer> <!-- Injected via js -->
    <script src="/js/common.js?v=6.1"></script>
</body>
</html>
"""

guides = [
    {
        "lang_code": "hi",
        "slug": "hindi-tools-guide",
        "tag": "हिंदी गाइड",
        "title": "WorldOfTools - सभी फ्री टूल्स का हिंदी गाइड",
        "desc": "अपनी सभी रोज़मर्रा की ज़रुरतों (GST, EMI, SIP, Image) के लिए हमारे 70+ फ्री ऑनलाइन टूल्स का उपयोग करना सीखें। बिल्कुल मुफ्त!",
        "intro": "WorldOfTools पर आपका स्वागत है। यहां आप बिना किसी लॉगिन या फीस के फाइनेंस, इमेज एडिटिंग, और डेवेलपर टूल्स का मुफ्त उपयोग कर सकते हैं। हमारा मिशन है आपके डिजिटल काम को तेज़ और आसान बनाना।",
        "h2_1": "1. फाइनेंस और बिज़नेस टूल्स (Finance Tools)",
        "h2_2": "2. फोटो और इमेज एडिटिंग (Image Editing)",
        "h2_3": "3. शिक्षा और रोज़मर्रा के टूल्स (Daily Utility)",
        "footer_msg": "हमारे सभी 70 टूल्स पूरी तरह से फ्री हैं!"
    },
    {
        "lang_code": "mr",
        "slug": "marathi-tools-guide",
        "tag": "मराठी मार्गदर्शक",
        "title": "WorldOfTools - मोफत ऑनलाइन टूल्स (मराठी मार्गदर्शक)",
        "desc": "घरी बसून GST, EMI, SIP आणि प्रतिमा संपादित करण्याचे 70+ मोफत टूल्स. WorldOfTools चा वापर कसा करायचा ते शिका.",
        "intro": "WorldOfTools वर आपले स्वागत आहे! आमच्या वेबसाइटवर तुम्ही कर्ज/हप्ते, फोटो संपादन आणि दैनंदिन कामांसाठी मोफत टूल्स वापरू शकता.",
        "h2_1": "1. आर्थिक आणि व्यवसाय टूल्स (Finance)",
        "h2_2": "2. फोटो संपादन टूल्स (Image & Video)",
        "h2_3": "3. शिक्षण व इतर उपयुक्त टूल्स",
        "footer_msg": "आजच आमच्या वेबसाइटवर 70+ टूल्स तपासा!"
    },
    {
        "lang_code": "ta",
        "slug": "tamil-tools-guide",
        "tag": "தமிழ் வழிகாட்டி",
        "title": "WorldOfTools - இலவச ஆன்லைன் கருவிகள் வழிகாட்டி (Tamil)",
        "desc": "இலவசமாக GST, EMI, SIP, புகைப்பட மாற்றிகள் போன்ற 70+ கருவிகளைப் பயன்படுத்த தமிழ் வழிகாட்டி.",
        "intro": "WorldOfTools உங்களை வரவேற்கிறது. எங்களிடம் சிறந்த நிதி (Finance), புகைப்படம் (Image) மற்றும் தினசரி பயன்பாட்டிற்கான கருவிகள் முற்றிலும் இலவசமாக உள்ளன.",
        "h2_1": "1. நிதி மற்றும் கணக்கீட்டு கருவிகள் (Finance)",
        "h2_2": "2. புகைப்பட மாறுதல்கள் (Image Tools)",
        "h2_3": "3. மற்ற முக்கியமான கருவிகள்",
        "footer_msg": "மேலும் பல இலவச கருவிகளை ஆராயுங்கள்!"
    },
    {
        "lang_code": "kn",
        "slug": "kannada-tools-guide",
        "tag": "ಕನ್ನಡ ಮಾರ್ಗದರ್ಶಿ",
        "title": "WorldOfTools - 70+ ಉಚಿತ ಉಪಕರಣಗಳು (Kannada Guide)",
        "desc": "GST, EMI, SIP ಮತ್ತು ಇತರ ಹಲವು ಉಚಿತ ಆನ್ಲೈನ್ ಉಪಕರಣಗಳನ್ನು ಹೇಗೆ ಬಳಸುವುದು ಎಂಬುದರ ಬಗ್ಗೆ ಕನ್ನಡದಲ್ಲಿ ತಿಳಿಯಿರಿ.",
        "intro": "WorldOfTools ಗೆ ಸ್ವಾಗತ! ನಮ್ಮ ವೇದಿಕೆಯಲ್ಲಿ ಹಣಕಾಸು, ಚಿತ್ರ (Image) ಸಂಪಾದನೆ ಹಾಗೂ ಇತರೆ ನಿಮ್ಮ ದೈನಂದಿನ ಕೆಲಸಗಳಿಗೆ ಬೇಕಾದ 70+ ಸಾಧನಗಳನ್ನು ಬಳಸಿ.",
        "h2_1": "1. ಹಣಕಾಸು ಮತ್ತು ವ್ಯಾಪಾರ ಸಾಧನಗಳು (Finance)",
        "h2_2": "2. ಚಿತ್ರ ಹಾಗೂ ವಿಡಿಯೋ ಸಾಧನಗಳು (Media)",
        "h2_3": "3. ಇತರೆ ಉಪಯುಕ್ತ ಸಾಧನಗಳು",
        "footer_msg": "ನಮ್ಮ 70+ ಉಚಿತ ವೃತ್ತಿಪರ ಟೂಲ್ಸ್‌ಗಳನ್ನು ಈಗಲೇ ಬಳಸಿ!"
    },
    {
        "lang_code": "te",
        "slug": "telugu-tools-guide",
        "tag": "తెలుగు గైడ్",
        "title": "WorldOfTools - ఉచిత ఆన్‌లైన్ టూల్స్ గైడ్ (Telugu)",
        "desc": "ఫైనాన్స్, ఇమేజ్, డెవలపర్ వంటి 70+ ఉచిత డిజిటల్ సాధనాలను సులభంగా ఎలా ఉపయోగించాలో ఈ తెలుగు గైడ్ లో తెలుసుకోండి.",
        "intro": "WorldOfTools కి స్వాగతం! ఎటువంటి లాగిన్ లేకుండా మీరు వివిధ రకాల ఆన్‌లైన్ టూల్స్ (GST, SIP, Image) పూర్తిగా ఉచితంగా ఉపయోగించవచ్చు.",
        "h2_1": "1. ఫైనాన్స్ (Finance) మరియు బిజినెస్ నెట్వర్క్ టూల్స్",
        "h2_2": "2. ఫోటో (Image) ఎడిటింగ్ టూల్స్",
        "h2_3": "3. మరికొన్ని రోజువారీ ఉపయోగపడే టూల్స్",
        "footer_msg": "ఈ రోజే మా 70 ఉచిత టూల్స్ ని ప్రయత్నించండి!"
    }
]

for g in guides:
    html = HTML_TEMPLATE.format(**g)
    path = os.path.join(ROOT, "guides", g["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {g['slug']}.html")
