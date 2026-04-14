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
    .guide-content h3 {{ font-family: 'Space Grotesk', 'Lexend', sans-serif; font-weight: 800; font-size: 1.4rem; margin-top: 2rem; color: #4f46e5; }}
    .info-card {{ background: var(--nb-mint, #dcfce7); border: 3px solid #111827; box-shadow: 5px 5px 0 #111827; border-radius: 8px; padding: 2rem; margin: 2rem 0; }}
    .tool-link-card {{
        display: flex; align-items: center; gap: 1rem; padding: 1.25rem;
        background: white; border: 3px solid #111827; border-radius: 12px;
        text-decoration: none; color: #111827; font-weight: 700; transition: all 0.2s;
        margin-bottom: 1.5rem; box-shadow: 4px 4px 0 #111827;
    }}
    .tool-link-card:hover {{ transform: translate(-3px, -3px); box-shadow: 7px 7px 0 #111827; background: var(--nb-lavender); }}
    .emoji-box {{ font-size: 2.5rem; }}
    </style>
</head>
<body>
    <header></header>
    <main class="container">
        <div class="guide-container">
            <div class="guide-header" style="text-align: center; margin-bottom: 3rem;">
                <span style="background: var(--nb-yellow); border: 2px solid #000; padding: 0.25rem 1rem; border-radius: 99px; font-weight: 800; display: inline-block; margin-bottom: 1rem;">🌟 {tag}</span>
                <h1>{title}</h1>
                <p style="font-size: 1.25rem; color: #4b5563;">{desc}</p>
            </div>
            <div class="guide-content">
                {content}
            </div>
        </div>
    </main>
    <footer></footer>
    <script src="/js/common.js?v=6.1"></script>
</body>
</html>
"""

guides = [
    {
        "lang_code": "hi",
        "slug": "hindi-tools-guide",
        "tag": "हिंदी गाइड",
        "title": "WorldOfTools - सभी फ्री टूल्स का हिंदी गाइड (GST, EMI, Image Editing)",
        "desc": "अपनी सभी रोज़मर्रा की ज़रुरतों (GST, EMI, SIP, Image) के लिए हमारे 70+ फ्री ऑनलाइन टूल्स का उपयोग करना सीखें। बिना किसी वॉटरमार्क के बिल्कुल मुफ्त!",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 Welcome to WorldOfTools</h3>
                <p>आज के डिजिटल युग में हर छोटे व्यापारी, फ्रीलांसर, और स्टूडेंट को रोज़ाना कई तरह के कैलकुलेशन्स और इंटरनेट टूल्स की आवश्यकता होती है। लेकिन इंटरनेट पर मौजूद ज़्यादातर वेबसाइट्स या तो आपसे सब्सक्रिप्शन (पैसे) मांगती हैं, या फिर आपके ज़रूरी डॉक्यूमेंट्स पर अपना वॉटरमार्क (Watermark) लगा देती हैं।</p>
                <p>WorldOfTools पर आपका स्वागत है। यहां आप बिना किसी लॉगिन या फीस के फाइनेंस, इमेज एडिटिंग, और डेवेलपर टूल्स का 100% मुफ्त उपयोग कर सकते हैं। हमारा मिशन है आपके डिजिटल काम को तेज़ और आसान बनाना। हमारे सभी टूल्स आपके ब्राउज़र में चलते हैं, जिसका मतलब है आपका डेटा पूरी तरह सुरक्षित रहता है।</p>
            </div>

            <h2>1. फाइनेंस और बिज़नेस टूल्स (Finance & Accounting Tools)</h2>
            <p>भारत में टैक्स और लोन का गणित थोड़ा जटिल हो सकता है। 5%, 12%, 18%, और 28% के GST स्लैब को समझना और इसमें से CGST/SGST अलग करना मुश्किल होता है। इसीलिए हमने नीचे दिए गए टूल्स बनाए हैं ताकि आप मिनटों में अपनी एकाउंटिंग पूरी कर सकें।</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">Free GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Add/Remove GST for Indian Tax Slabs (5%, 12%, 18%, 28%)</div>
                </div>
            </a>
            
            <h3>लोन और SIP की जानकारी (EMI & Mutual Funds)</h3>
            <p>अगर आप घर या गाड़ी के लिए लोन लेने की सोच रहे हैं, तो बैंक में जाने से पहले आपको अपनी EMI पता होनी चाहिए। हमारा लोन कैलकुलेटर आपको बताता है कि आप अगले 20 सालों में कुल कितना ब्याज भरेंगे (Amortization Chart)। इसी तरह, SIP कैलकुलेटर से आप देख सकते हैं कि म्यूच्यूअल फंड (Mutual Fund) में हर महीने 5000 रुपये निवेश करके 20 सालों में कितना बड़ा वेल्थ (Wealth) बन सकता है।</p>

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

            <h2>2. फोटो और वीडियो एडिटिंग (Image & Video Editing)</h2>
            <p>इंस्टाग्राम (Instagram) और व्हाट्सएप (WhatsApp) के लिए बड़े वीडियो फाइल को कॉम्प्रेस करना ज़रूरी होता है। ऑनलाइन कई वीडियो कंप्रेसर वेबसाइट्स हैं, लेकिन वो 250MB की लिमिट लगा देती हैं। हमारा इमेज और वीडियो कंप्रेसर सीधे आपके डिवाइस की प्रोसेसिंग पॉवर का इस्तेमाल करता है, जिससे आप 2GB तक की फाइल्स को बिना अपलोड किए कंप्रेस कर सकते हैं।</p>

            <a href="/video-compressor" class="tool-link-card">
                <span class="emoji-box">📹</span>
                <div>
                    <div style="font-size: 1.2rem;">Video Compressor (No Limit)</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Reduce MP4/MKV sizes without uploading to unsafe servers.</div>
                </div>
            </a>

            <a href="/remove-watermark-from-image" class="tool-link-card">
                <span class="emoji-box">✨</span>
                <div>
                    <div style="font-size: 1.2rem;">Remove Watermark</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Extract unwanted objects or text from images via AI</div>
                </div>
            </a>

            <h2>3. शिक्षा और रोज़मर्रा के टूल्स (Daily Utility)</h2>
            <p>उम्र की सही गणना करनी हो (दिन, महीने और साल में), या फिर अपनी टाइपिंग स्पीड (WPM) को बेहतर बनाना हो, हमारे टूल्स रोज़ाना इस्तेमाल के लिए सबसे अच्छे हैं।</p>
            
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
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Get exact chronological age and next birthday countdown</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">हमारे 70+ टूल्स पूरी तरह से फ्री हैं!</h3>
                <p>WorldOfTools का इस्तेमाल करने के लिए आपको कोई अकाउंट बनाने की या पैसे देने की ज़रूरत नहीं है। बस वेबसाइट खोलें और अपना काम शुरू करें।</p>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    },
    {
        "lang_code": "mr",
        "slug": "marathi-tools-guide",
        "tag": "मराठी मार्गदर्शक",
        "title": "WorldOfTools - मोफत ऑनलाइन टूल्स (Marathi Guide for EMI, GST & Marketing)",
        "desc": "घरी बसून GST, EMI, SIP आणि प्रतिमा संपादित करण्याचे 70+ मोफत टूल्स. WorldOfTools चा वापर कसा करायचा ते शिका.",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 WorldOfTools वर आपले स्वागत आहे!</h3>
                <p>आजकाल प्रत्येक छोट्या-मोठ्या व्यावसायिकाला, विद्यार्थ्याला आणि नोकरदारांना इंटरनेटवर वेगवेगळ्या 'टूल्स' (Tools) ची गरज पडते. जसे की, फोटोची साईझ कमी करणे किंवा GST चे गणित सोडवणे. पण बऱ्याच वेबसाइट्स त्यासाठी पैसे (Subscription) मागतात किंवा त्यांच्या नावाचा 'वॉटरमार्क' (Watermark) लावतात.</p>
                <p>WorldOfTools हे अशा सर्व त्रासांवर मात करणारे एक व्यासपीठ आहे. येथे तुम्हाला 70 हून अधिक टूल्स अगदी मोफत वापरता येतात. आमच्या वेबसाइटचा सर्वात मोठा फायदा म्हणजे ही सर्व टूल्स थेट तुमच्या ब्राउझरमध्ये (Client-side) चालतात; म्हणजे तुमचा प्रायव्हेट डेटा आमच्या सर्व्हरवर अपलोड होत नाही.</p>
            </div>

            <h2>1. आर्थिक आणि व्यवसाय टूल्स (Finance & Tools)</h2>
            <p>भारतातील GST स्लॅब (५%, १२%, १८%, २८%) समजून घेणे आणि बिलांमधून CGST व SGST वेगळे काढणे सोपे नाही. यासोबतच, घर घेण्यासाठी 'होम लोन' (Home Loan) किती बसेल हे ठरवणे आवश्यक असते. आम्ही यासाठी खास टूल्स बनवली आहेत.</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">मोफत GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Add/Remove GST for Indian Tax Slabs (5%, 12%, 18%, 28%)</div>
                </div>
            </a>
            
            <h3>EMI आणि म्युच्युअल फंड (Mutual Funds & SIP)</h3>
            <p>तुम्ही जर 'SIP' द्वारे शेअर बाजारात (Stock Market) गुंतवणूक करणार असाल, तर आमचे 'SIP Calculator' तुम्हाला मदत करेल. याद्वारे तुम्ही पाहू शकता की, पुढील १५-२० वर्षांत ५००० रुपयांची गुंतवणूक किती लाख रुपये बनवून देईल. तसेच 'Loan EMI' कॅल्क्युलेटरने तुमचे मासिक हप्ते चेक करा.</p>

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

            <h2>2. फोटो आणि व्हिडिओ संपादन टूल्स (Image & Video)</h2>
            <p>इन्स्टाग्रामवरील (Instagram) किंवा युट्युबवरील (YouTube) तुमच्या पोस्ट्स आणखी चांगल्या करण्यासाठी 'Background Remover' किंवा 'Image Upscaler' उपयुक्त ठरते. कुठल्याही सॉफ्टवेअरशिवाय तुम्ही स्वतःच्या ब्राउझरवरून हे काम मोफत करू शकता.</p>

            <a href="/background-remover" class="tool-link-card">
                <span class="emoji-box">✂️</span>
                <div>
                    <div style="font-size: 1.2rem;">AI Background Remover</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Extract products and people seamlessly with a single click.</div>
                </div>
            </a>

            <a href="/video-compressor" class="tool-link-card">
                <span class="emoji-box">📹</span>
                <div>
                    <div style="font-size: 1.2rem;">Video Compressor (No Upload Limit)</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Reduce large MP4 files safely on your local device.</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">आजच आमच्या वेबसाइटवर सर्व टूल्स तपासा!</h3>
                <p>या सर्व उपकरणांचा कोणताही खर्च नाही. कोणतीही नोंदणी (Login/Signup) करण्याची आवश्यकता नाही.</p>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    },
    {
        "lang_code": "bn",
        "slug": "bengali-tools-guide",
        "tag": "বাংলা গাইড",
        "title": "WorldOfTools - বিনামূল্যের অনলাইন টুলস গাইড (Bengali)",
        "desc": "বিনামূল্যে GST, EMI, SIP, ও ইমেজ এডিটিং করতে আমাদের 70+ টুলস ব্যবহার করুন। কোন ওয়াটারমার্ক বা সাইনআপের প্রয়োজন নেই।",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 WorldOfTools এ স্বাগতম!</h3>
                <p>বর্তমান ডিজিটাল যুগে ছাত্র, ব্যবসায়ী এবং ফ্রিল্যান্সারদের প্রতিদিনের কাজে বিভিন্ন অনলাইন টুলের প্রয়োজন হয়, যেমন ভিডিও কম্প্রেসর, GST ক্যালকুলেটর কিংবা ব্যাকগ্রাউন্ড রিমুভার। কিন্তু বেশিরভাগ ওয়েবসাইট এই পরিষেবার জন্য মূল্য দাবি করে অথবা ফাইলের ওপর ওয়াটারমার্ক বসিয়ে দেয়।</p>
                <p>এখানে <strong>WorldOfTools</strong> ব্যতিক্রম। আমরা 70 টিরও বেশি পেশাদার টুল বিনামূল্যে নিয়ে এসেছি, যা সরাসরি আপনার ব্রাউজারে চলবে, মানে আপনার ব্যক্তিগত ডেটা সম্পূর্ণ নিরাপদ।</p>
            </div>

            <h2>1. ফাইন্যান্সিয়াল ও বিজনেস টুলস (Finance)</h2>
            <p>GST স্ল্যাব, লোন (Loan) এবং EMI ক্যালকুলেট করার মতো জটিল কাজ এখন আপনার হাতের মুঠোয়। আপনার লোন পিরিয়ড এবং ইন্টারেস্ট রেট অনুযায়ী আপনার EMI কত হবে, তা জানতে আমাদের টুলটি অত্যন্ত কার্যকরী।</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">Free GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">ভারতীয় ট্যাক্স স্ল্যাব অনুযায়ী GST এবং নেট প্রাইস বের করুন।</div>
                </div>
            </a>
            
            <a href="/emi-calculator" class="tool-link-card">
                <span class="emoji-box">🏠</span>
                <div>
                    <div style="font-size: 1.2rem;">Loan EMI Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">আপনার গাড়ির বা বাড়ির লোন এর EMI হিসাব করুন।</div>
                </div>
            </a>
            <a href="/sip-calculator" class="tool-link-card">
                <span class="emoji-box">📈</span>
                <div>
                    <div style="font-size: 1.2rem;">SIP Investment Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">মিউচুয়াল ফান্ডে বিনিয়োগের ভবিষ্যৎ রিটার্ন চেক করুন।</div>
                </div>
            </a>

            <h2>2. ছবি ও ভিডিও কম্প্রেসর টুলস (Media Tools)</h2>
            <p>বড় ফাইল কম্প্রেস করতে আমাদের টুলগুলো সেরা। আপনি 2GB পর্যন্ত ভিডিও কোন সার্ভারে আপলোড করা ছাড়াই কম্প্রেস করতে পারবেন।</p>

            <a href="/video-compressor" class="tool-link-card">
                <span class="emoji-box">📹</span>
                <div>
                    <div style="font-size: 1.2rem;">Video Compressor (No Limit)</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">বড় MP4 ভিডিওগুলির কোয়ালিটি বজায় রেখে সাইজ কমান।</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">আমাদের 70+ টুলস আজই এক্সপ্লোর করুন!</h3>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    },
    {
        "lang_code": "gu",
        "slug": "gujarati-tools-guide",
        "tag": "ગુજરાતી ગાઈડ",
        "title": "WorldOfTools - મફત 70+ ઓનલાઈન ટૂલ્સનો ઉપયોગ કરો (Gujarati)",
        "desc": "તમારા બિઝનેસ માટે GST, EMI, SIP અને વિડીયો કમ્પ્રેશન મેનેજ કરો તદ્દન મફત. વોટરમાર્ક વગર અને સુરક્ષિત રીતે.",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 WorldOfTools માં તમારું સ્વાગત છે!</h3>
                <p>આજના સમયમાં દરેક નાના વેપારી, વિદ્યાર્થીઓ અને ફ્રીલાન્સરને રોબરોજના કામ માટે ઘણી પ્રકારના ઓનલાઈન ટૂલ્સની જરૂર પડે છે. GST ગણવું હોય કે ફોટોની સાઇઝ નાની કરવી હોય, પરંતુ ઘણી બધી વેબ્સાઇટ તેના માટે પૈસા માંગે છે (Subscription) અથવા તેમના નામનો વોટરમાર્ક લગાવી દે છે.</p>
                <p>અહીં <strong>WorldOfTools</strong> તમારી મદદ કરવા આવ્યું છે. અમે 70 થી વધુ શક્તિશાળી સ્માર્ટ ટૂલ્સ બિલકુલ ફ્રી (મફત) પૂરા પાડીએ છીએ. અહીં તમારે કોઈ લોગીન (Login) કે ચાર્જ ચૂકવવો પડતો નથી.</p>
            </div>

            <h2>1. ફાઇનાન્સ અને બિઝનેસ ટૂલ્સ (Finance)</h2>
            <p>ગુજરાતમાં બિઝનેસ કરનારા માટે GST સૌથી અગત્યની વસ્તુ છે. શું તમારે બિલ બનાવતી વખતે 18% કે 12% GST નોકરી કે અલગથી હિસાબ માંડવો છે? અમારા કેલ્ક્યુલેટર્સ એ વસ્તુ ચપટી વગાડતામાં ગોતી આપે છે.</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">Free GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">તમારા ઇન્વોઇસ માટે CGST અને SGST સરળતાથી શોધો.</div>
                </div>
            </a>
            
            <a href="/emi-calculator" class="tool-link-card">
                <span class="emoji-box">🏠</span>
                <div>
                    <div style="font-size: 1.2rem;">Loan EMI Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">તમારા હોમ લોનના હપ્તા (EMI) અને વ્યાજ ની ગણતરી કરો.</div>
                </div>
            </a>
            <a href="/sip-calculator" class="tool-link-card">
                <span class="emoji-box">📈</span>
                <div>
                    <div style="font-size: 1.2rem;">SIP Investment Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">15 થી 20 વર્ષના સિપ રોકાણનો (Mutual Fund) નફો તપાસો.</div>
                </div>
            </a>

            <h2>2. ફોટો અને મીડિયા ટૂલ્સ (Image & Video Editing)</h2>
            <p>તમારી દુકાન કે પ્રોડક્ટ્સના ફોટા ઇન્ટરનેટ ઉપર મૂકવા માટે તેનું બેકગ્રાઉન્ડ દૂર કરવું પડે છે. અમારી વેબસાઈટ ઉપર AI ટૂલ છે, જેનાથી એક જ સેકન્ડમાં વસ્તુ પરથી બેકગ્રાઉન્ડ દૂર કરી શકાય છે.</p>

            <a href="/background-remover" class="tool-link-card">
                <span class="emoji-box">✂️</span>
                <div>
                    <div style="font-size: 1.2rem;">AI Background Remover</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">પ્રોડક્ટ્સના ફોટાઓ પાછળનું બેકગ્રાઉન્ડ 1 ક્લિકથી દૂર કરો.</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">આપણા ગુજરાતના ભાઈઓ માટે 70+ ફ્રી ટૂલ્સ!</h3>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    },
    {
        "lang_code": "ta",
        "slug": "tamil-tools-guide",
        "tag": "தமிழ் வழிகாட்டி",
        "title": "WorldOfTools - இலவச ஆன்லைன் கருவிகள் வழிகாட்டி (Tamil GST & Media Tools)",
        "desc": "இலவசமாக GST, EMI, SIP, புகைப்பட மாற்றிகள் போன்ற 70+ கருவிகளைப் பயன்படுத்த தமிழ் வழிகாட்டி. வாட்டர்மார்க் இல்லை!",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 WorldOfTools உங்களை வரவேற்கிறது!</h3>
                <p>இன்றைய டிஜிட்டல் உலகில் தொழில் செய்பவர்கள், மாணவர்கள் மற்றும் மென்பொருள் உருவாக்குநர்கள் தினசரி பல অনলাইন கருவிகளை நம்பியுள்ளனர். வீடியோவை கம்ப்ரஸ் (Compress) செய்யவோ அல்லது GST கணக்கிடவோ பல இணையதளங்கள் கட்டணம் வசூலிக்கின்றன அல்லது அவற்றின் வாட்டர்மார்க்கை சேர்க்கின்றன.</p>
                <p>WorldOfTools இணையதளம் உங்கள் தேவைகளை முற்றிலும் 100% இலவசமாக தீர்க்கும். எங்களின் 70+ கருவிகள் எந்த ஒரு சர்வரிலும் உங்கள் டேட்டாவை பதிவேற்றம் செய்யாமல், நேரடியாக உங்களின் பிரவுசரில் செயல்படுகின்றன. இதனால் பாதுகாப்பும் வேகமும் அதிகம்.</p>
            </div>

            <h2>1. வணிக மற்றும் நிதி கருவிகள் (Finance Tools)</h2>
            <p>இந்தியாவின் GST வரிவிதிப்புகளை (5%, 12%, 18%) கணக்கிடுவது சில நேரங்களில் கடினமாக இருக்கலாம். எங்களின் ஜிஎஸ்டி கால்குலேட்டர் உங்கள் பில்களுக்கான துல்லியமான CGST/SGST வரியை எளிதாக கணக்கிட உதவும்.</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">Free GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Add/Remove GST for Indian Tax Slabs (5%, 12%, 18%, 28%)</div>
                </div>
            </a>
            
            <h3>கடன் மற்றும் சேமிப்பு (Loan & Investments)</h3>
            <p>வீடு அல்லது வாகனம் வாங்கும் முன், மாத தவணை (EMI) எவ்வளவு வரும் என்று தெரிந்துகொள்வது அவசியம். அதேபோல நீங்கள் மாதாந்திரம் மியூச்சுவல் ஃபண்டில் (Mutual Fund - SIP) முதலீடு செய்தால், 20 வருடங்களுக்கு பிறகு எவ்வளவு தொகை கிடைக்கும் என்பதை காண எங்கள் SIP Calculator உதவும்.</p>

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

            <h2>2. புகைப்பட மற்றும் வீடியோ கருவிகள் (Tamil Media Tools)</h2>
            <p>உங்கள் இன்ஸ்டாகிராம் மற்றும் சமூக வலைதள பதிவுகளுக்கு படங்களை மாற்ற அல்லது பெரிய வீடியோ பைல்களின் அளவை குறைக்க (Video Compress) எங்களின் சக்திவாய்ந்த கருவிகள் உதவும்.</p>

            <a href="/video-compressor" class="tool-link-card">
                <span class="emoji-box">📹</span>
                <div>
                    <div style="font-size: 1.2rem;">Video Compressor (No Upload Limit)</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Reduce large MP4 files safely on your local device.</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">எங்களின் அனைத்து 70+ கருவிகளும் முற்றிலும் இலவசம்!</h3>
                <p>நீங்கள் கணக்கு (Account) திறக்கவோ அல்லது லாகின் செய்யவோ தேவையில்லை.</p>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    },
    {
        "lang_code": "kn",
        "slug": "kannada-tools-guide",
        "tag": "ಕನ್ನಡ ಮಾರ್ಗದರ್ಶಿ",
        "title": "WorldOfTools - 70+ ಉಚಿತ ಉಪಕರಣಗಳು (Kannada Guide for Developers & Finance)",
        "desc": "GST, EMI, SIP ಮತ್ತು ಇತರ ಹಲವು ಉಚಿತ ಆನ್ಲೈನ್ ಉಪಕರಣಗಳನ್ನು ಹೇಗೆ ಬಳಸುವುದು ಎಂಬುದರ ಬಗ್ಗೆ ಕನ್ನಡದಲ್ಲಿ ತಿಳಿಯಿರಿ.",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 WorldOfTools ಗೆ ಸ್ವಾಗತ!</h3>
                <p>ದೈನಂದಿನ ಕೆಲಸ ಕಾರ್ಯಗಳಿಗೆ ನಮಗೆ ಹಲವು ವಿಧದ ಟೂಲ್ಸ್ ಬೇಕಾಗುತ್ತವೆ – ಅದು ವೀಡಿಯೋ ಕಂಪ್ರೆಸ್ ಮಾಡುವುದಾಗಿರಲಿ ಅಥವಾ ಹೊಸ GST ರೇಟ್ ಲೆಕ್ಕ ಹಾಕುವುದು ಇರಲಿ. ಹೆಚ್ಚಿನ ವೆಬ್‌ಸೈಟ್‌ಗಳು यासाठी ಹಣವನ್ನು ಕೇಳುತ್ತವೆ ಅಥವಾ ಚಿತ್ರದ ಮೇಲೆ ವಾಟರ್‌ಮಾರ್ಕ್ ಹಾಕುತ್ತವೆ.</p>
                <p>ಆದರೆ WorldOfTools ನಲ್ಲಿ ನೀವು ನಿಮ್ಮ ಅವಶ್ಯಕತೆಯ 70+ ಉತ್ತಮ ಟೂಲ್ಸ್ ಅನ್ನು ಯಾವುದೇ ಲಾಗಿನ್ ಇಲ್ಲದೆ, 100% ಸುರಕ್ಷಿತವಾಗಿ ಉಚಿತವಾಗಿ ಬಳಸಬಹುದು. ವೀಡಿಯೋಗಳು ಮತ್ತು ಫೈಲ್ ಗಳು ನಿಮ್ಮದೇ ಬ್ರೌಸರ್ ನಲ್ಲಿ ಪ್ರಕ್ರಿಯೆಗೊಂಡು ನಿಮ್ಮ ಡೇಟಾ ರಕ್ಷಿಸಲ್ಪಡುತ್ತದೆ.</p>
            </div>

            <h2>1. ಹಣಕಾಸು ಮತ್ತು ವ್ಯಾಪಾರ ಸಾಧನಗಳು (Finance & Calculation)</h2>
            <p>ನಮ್ಮ ಭಾರತದಲ್ಲಿನ ಜಿಎಸ್‌ಟಿ ವ್ಯವಸ್ಥೆಯನ್ನು (5%, 12%, 18%) ಸುಲಭವಾಗಿ ಲೆಕ್ಕಹಾಕಲು, ಮತ್ತು ನಿಮ್ಮ ಇನ್ವಾಯ್ಸ್ ಗಳ ಮೇಲೆ CGST / SGST ಪ್ರಮಾಣ ತಿಳಿಯಲು ಈ ಟೂಲ್ ಉಪಯೋಗಕಾರಿ.</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">Free GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Add/Remove GST for Indian Tax Slabs (5%, 12%, 18%, 28%)</div>
                </div>
            </a>
            
            <h3>ಗೃಹ ಸಾಲ, ವಾಹನ ಸಾಲ (EMI & Loans)</h3>
            <p>ನಿಮ್ಮ ಭವಿಷ್ಯದ ಸಾಲವನ್ನು (Loan) ಯೋಜನೆ ಮಾಡಲು, ನಮ್ಮ 'EMI ಕ್ಯಾಲ್ಕುಲೇಟರ್' ನಿಂದ ನಿಮ್ಮ ಪ್ರತಿ ತಿಂಗಳ ಹಂತ (Installment) ಎಷ್ಟಾಗಲಿದೆ ಎಂದು ನೋಡಿ. ಅದೇ ರೀತಿ, ನೀವು 'Mutual Funds' ಅಥವಾ 'SIP' ಮೂಲಕ ಹೂಡಿಕೆ ಮಾಡಲು ಬಯಸಿದರೆ, 20 ವರ್ಷಗಳಲ್ಲಿ ಎಷ್ಟು ಲಾಭ ಎಂದು ಪರಿಶೀಲಿಸಬಹುದು.</p>

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

            <h2>2. ಡೆವಲಪರ್ & ಇಮೇಜ್ ಟೂಲ್ಸ್ (Media)</h2>
            <p>ಬೆನ್ನಿನ ಹಿನ್ನೆಲೆ ತೆಗೆಯುವುದು (Background Remove) ಮತ್ತು ದೊಡ್ಡ ವೀಡಿಯೊ ಫೈಲ್ ಗಳನ್ನು ಚಿಕ್ಕದಾಗಿಸುವುದು ( compress ) ಈ ರೀತಿಯ ಕೆಲಸಗಳನ್ನು ನಮ್ಮ ಉಚಿತ ಟೂಲ್ಸ್ ನೀಡುತ್ತವೆ.</p>

            <a href="/background-remover" class="tool-link-card">
                <span class="emoji-box">✂️</span>
                <div>
                    <div style="font-size: 1.2rem;">AI Background Remover</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Extract products and people seamlessly with a single click.</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">ನಮ್ಮ 70+ ಉಚಿತ ಉಪಕರಣಗಳನ್ನು ಈಗಲೇ ಬಳಸಿ!</h3>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    },
    {
        "lang_code": "te",
        "slug": "telugu-tools-guide",
        "tag": "తెలుగు గైడ్",
        "title": "WorldOfTools - ఉచిత ఆన్‌లైన్ టూల్స్ గైడ్ (Telugu Finance & SEO Tools)",
        "desc": "ఫైనాన్స్, ఇమేజ్, డెవలపర్ వంటి 70+ ఉచిత డిజిటల్ సాధనాలను సులభంగా ఎలా ఉపయోగించాలో ఈ తెలుగు గైడ్ ద్వారా తెలుసుకోండి.",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">🚀 WorldOfTools కి స్వాగతం!</h3>
                <p>ప్రస్తుత డిజిటల్ యుగంలో విద్యార్ధులు, ఉద్యోగులు మరియు వ్యాపారస్తులు రోజువారీ పనులకు ఎన్నో వెబ్‌సైట్లపై ఆధారపడుతున్నారు. అయితే వీడియో సైజ్ తగ్గించడానికి (Compress) మరియు బ్యాక్‌గ్రౌండ్ రిమూవ్ (Remove Background) చేయడానికి ఇంటర్నెట్ లో దొరికే చాలా సాధనాలు డబ్బును డిమాండ్ చేస్తాయి దానికి తోడు వాటర్ మార్క్‌లు (Watermarks) జతచేస్తాయి.</p>
                <p>కానీ <strong>WorldOfTools</strong> లో ఉన్న 70 కు పైగా ప్రొఫెషనల్ సాధనాలు (Tools) పూర్తిగా 100% ఉచితంగా ఎలాంటి వాటర్ మార్క్ లేకుండా పని చేస్తాయి. ఇవి అన్నీ మీ బ్రౌజర్ లోనే రన్ అవుతాయి కనుక, మీ డేటా క్లౌడ్ (Cloud) కి ఎప్పటికీ అప్‌లోడ్ అవ్వదు. పూర్తి భద్రత!</p>
            </div>

            <h2>1. ఫైనాన్స్ మరియు బిజినెస్ టూల్స్ (Telugu Finance Tools)</h2>
            <p>మీరు ఒక వ్యాపారం నడుపుతుంటే బిల్లులపైన GST శాతాలను (5%, 12%, 18%) సులభంగా లెక్క కట్టడానికి మా GST కాలిక్యులేటర్ ఎంతో బాగా ఉపయోగపడుతుంది.</p>
            
            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">💰</span>
                <div>
                    <div style="font-size: 1.2rem;">Free GST Calculator</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Add/Remove GST for Indian Tax Slabs (5%, 12%, 18%, 28%)</div>
                </div>
            </a>
            
            <h3>లోన్స్ మరియు ఇన్వెస్ట్‌మెంట్ (Loans & EMI Calculation)</h3>
            <p>హోమ్ లోన్ లేదా కార్ లోన్ తీసుకునే ముందు రాబోయే కాలపరిమితిలో (Tenure) మీరు కట్టాల్సిన అసలు, వడ్డీ, మరియు నెలవారీ కంతుల (EMI) వివరాలను స్పష్టంగా తెలుసుకోవడానికి మా 'లోన్ EMI కాలిక్యులేటర్' ఉపయోగపడుతుంది. మీరు మ్యూచువల్ ఫండ్లలో SIP చేస్తుంటే భవిష్యత్ సంపదను లెక్కకట్టడానికి మా 'SIP కాలిక్యులేటర్' చూడండి.</p>

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

            <h2>2. ఇమేజ్ మరియు వీడియో టూల్స్ (Images & Media)</h2>
            <p>ఫోటోలో ఉన్న బ్యాక్‌గ్రౌండ్ రిమూవ్ చేయడానికి, అలాగే 2GB కి మించిన వీడియోలను కంప్రెస్ చేయడానికి మా ఉచిత టూల్స్‌ను ఉపయోగించండి.</p>

            <a href="/video-compressor" class="tool-link-card">
                <span class="emoji-box">📹</span>
                <div>
                    <div style="font-size: 1.2rem;">Video Compressor (No Upload Limit)</div>
                    <div style="font-size: 0.85rem; font-weight: 500; color: #444;">Reduce large MP4 files safely on your local device.</div>
                </div>
            </a>

            <div class="info-card" style="margin-top: 4rem; text-align: center; background: var(--nb-lavender);">
                <h3 style="margin-top:0;">ఈ రోజే మా 70 ఉచిత డిజిటల్ టూల్స్ ని ప్రయత్నించండి!</h3>
                <a href="/index.html" style="display:inline-block; padding: 1rem 2rem; background: #000; color: #fff; text-decoration: none; font-weight: 800; border-radius: 12px; margin-top: 1rem;">Explore All 70+ Tools</a>
            </div>
        """
    }
]

for g in guides:
    html = HTML_TEMPLATE.format(**g)
    path = os.path.join(ROOT, "guides", g["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {g['slug']}.html")
