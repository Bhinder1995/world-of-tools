import os

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en">
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
    table {{ width: 100%; border-collapse: collapse; margin-top: 1.5rem; border: 3px solid #111827; }}
    th, td {{ border: 2px solid #111827; padding: 1rem; text-align: left; }}
    th {{ background: var(--nb-pink, #fce7f3); font-weight: 800; font-family: 'Space Grotesk', sans-serif; }}
    ul {{ padding-left: 1.5rem; }}
    li {{ margin-bottom: 0.75rem; }}
    </style>
</head>
<body>
    <header></header>
    <main class="container">
        <div class="guide-container">
            <div class="guide-header" style="text-align: center; margin-bottom: 3rem;">
                <span style="background: var(--nb-yellow); border: 2px solid #000; padding: 0.25rem 1rem; border-radius: 99px; font-weight: 800; display: inline-block; margin-bottom: 1rem;">🔥 {tag}</span>
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
        "slug": "best-veed-clideo-alternatives",
        "tag": "Video Tools Guide",
        "title": "Best VEED & Clideo Alternatives (Free & No Watermark)",
        "desc": "Are you tired of massive subscription fees and watermarks on your videos? Discover the best 100% free alternatives for video compression and editing.",
        "content": """
            <div class="info-card" style="background: var(--nb-pink);">
                <h3 style="margin-top:0;">Why Look for Alternatives?</h3>
                <p>Platforms like VEED.io and Clideo are incredibly popular, but they come with massive drawbacks for free users: forced watermarks on your exported videos, severe file size limits (often maxing out at 250MB or 500MB), and subscription paywalls that cost upwards of $30/month.</p>
                <p>For creators who just need to quickly compress a video for Discord or WhatsApp, this is unacceptable.</p>
            </div>

            <h2>How WorldOfTools Replaces Expensive Video Suites</h2>
            <p>At WorldOfTools, we built our video tools directly into your browser using WebAssembly. This means <strong>we process your videos using your own device's hardware</strong>. The benefits?</p>
            <ul>
                <li><strong>No Watermarks:</strong> We never brand your videos. What you compress is exactly what you get.</li>
                <li><strong>No File Size Limits:</strong> Because you aren't uploading to a cloud server, you can process videos up to 2GB organically.</li>
                <li><strong>100% Free:</strong> No login, no credit cards, no premium tiers.</li>
                <li><strong>Total Privacy:</strong> Your sensitive video files never leave your computer.</li>
            </ul>

            <h3>Explore Our Free Video Tools</h3>
            <a href="/video-compressor" class="tool-link-card">
                <span class="emoji-box">📹</span>
                <div>
                    <div style="font-size: 1.25rem;">Video Compressor (No Limit)</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Reduce MP4 sizes without losing quality. Better than Clideo's free tier.</div>
                </div>
            </a>
            
            <a href="/video-to-gif" class="tool-link-card">
                <span class="emoji-box">🎞️</span>
                <div>
                    <div style="font-size: 1.25rem;">Video to GIF Converter</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Extract high-quality GIFs from video clips instantly.</div>
                </div>
            </a>

            <a href="/aspect-ratio-calculator" class="tool-link-card">
                <span class="emoji-box">📐</span>
                <div>
                    <div style="font-size: 1.25rem;">Aspect Ratio Calculator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Perfectly resize dimensions for Instagram Reels, TikTok, and YouTube.</div>
                </div>
            </a>

            <h2>Feature Comparison: WorldOfTools vs VEED / Clideo</h2>
            <table>
                <tr>
                    <th>Feature</th>
                    <th>WorldOfTools</th>
                    <th>VEED / Clideo (Free)</th>
                </tr>
                <tr>
                    <td>Watermark added</td>
                    <td>❌ No</td>
                    <td>✅ Yes</td>
                </tr>
                <tr>
                    <td>File Size Limit</td>
                    <td>2GB / Browser Limit</td>
                    <td>250MB - 500MB</td>
                </tr>
                <tr>
                    <td>Processing</td>
                    <td>Local (Fast & Secure)</td>
                    <td>Cloud (Requires Upload)</td>
                </tr>
                <tr>
                    <td>Cost</td>
                    <td>100% Free</td>
                    <td>$14 - $30/month</td>
                </tr>
            </table>

            <h3>Conclusion</h3>
            <p>If you are a content creator looking to optimize, compress, or manage media files without paying exorbitant monthly fees, ditch the cloud-based platforms. Utilize browser-native WebAssembly tools that protect your IP and wallet.</p>
        """
    },
    {
        "slug": "top-free-seo-developer-utility-tools",
        "tag": "Developer Guide",
        "title": "Top Free SEO & Developer Utility Tools in 2026",
        "desc": "A master breakdown of essential utilities every developer and digital marketer needs to format code, decode tokens, and rank higher on Google.",
        "content": """
            <div class="info-card">
                <h3 style="margin-top:0;">The Problem with Developer Tooling Today</h3>
                <p>Every developer has experienced this: You need to decode a JWT token or format a messy JSON payload. You Google a tool, click a link, and get bombarded by banner ads, paywalls, and slow server-side loading.</p>
                <p>WorldOfTools was built differently. We ship entirely client-side developer utilities designed with our "Playful Neo-Brutalist" UI—meaning they are instantly fast, completely private, and stunning to look at.</p>
            </div>

            <h2>Must-Have Tools for Full-Stack Developers</h2>
            <p>Whether you are debugging API responses or securing user passwords, these browser-native utilities are non-negotiable for a fast workflow.</p>
            
            <a href="/jwt-decoder" class="tool-link-card">
                <span class="emoji-box">🔐</span>
                <div>
                    <div style="font-size: 1.25rem;">JWT Token Decoder</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Securely inspect headers and payloads without sending them to a server.</div>
                </div>
            </a>

            <a href="/json-formatter" class="tool-link-card">
                <span class="emoji-box">{}</span>
                <div>
                    <div style="font-size: 1.25rem;">Advanced JSON Formatter</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Beautify, validate, and minify massive JSON files instantly.</div>
                </div>
            </a>
            
            <a href="/sql-formatter" class="tool-link-card">
                <span class="emoji-box">💾</span>
                <div>
                    <div style="font-size: 1.25rem;">SQL Query Formatter</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Clean up unreadable raw SQL databases dumps into clean code.</div>
                </div>
            </a>

            <h2>Essential Suite for SEO Experts</h2>
            <p>For organic growth hackers, technical SEO is what separates page 1 from page 2. Generating precise Schema markup and evaluating keyword density organically boosts your Google visibility.</p>

            <a href="/schema-generator-online" class="tool-link-card">
                <span class="emoji-box">🌐</span>
                <div>
                    <div style="font-size: 1.25rem;">Schema Markup (JSON-LD) Generator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Create rich snippets for Articles, FAQs, Products, and Reviews.</div>
                </div>
            </a>

            <a href="/keyword-density-checker" class="tool-link-card">
                <span class="emoji-box">📊</span>
                <div>
                    <div style="font-size: 1.25rem;">Keyword Density Checker</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Analyze 1-word, 2-word, and 3-word combinations to avoid keyword stuffing penalties.</div>
                </div>
            </a>

            <a href="/seo-meta-tag-generator" class="tool-link-card">
                <span class="emoji-box">📝</span>
                <div>
                    <div style="font-size: 1.25rem;">SEO Meta Tag Generator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Visually preview your Google SERP listings with generated title/meta attributes.</div>
                </div>
            </a>
            
            <h3>Client-side vs Server-side: The Privacy Perspective</h3>
            <p>Security architectures heavily favor tools that do not rely on server-side execution. If you are decoding a JWT that contains proprietary company scopes or customer PII, using a standard cloud-based decoder is a severe security risk. By using WorldOfTools, your data never leaves your RAM.</p>
        """
    },
    {
        "slug": "india-best-free-gst-emi-loan-calculators",
        "tag": "Finance Guide",
        "title": "India's Best Free GST, EMI & Loan Calculators (FY 2026-27)",
        "desc": "A comprehensive guide to managing your personal and business finances in India without paying for premium accounting suites.",
        "content": """
            <div class="info-card">
                <h3 style="margin-top:0;">Navigating Indian Finance Tools</h3>
                <p>The financial landscape in India requires exact precision. If you are a freelancer invoicing a client, you need an exact 18% GST breakdown. If you are buying a home, you need to understand how the Repo Rate affects your monthly EMI.</p>
                <p>We built our financial suite to completely replace clunky spreadsheets and ad-heavy banking tools.</p>
            </div>

            <h2>Mastering the Goods and Services Tax (GST)</h2>
            <p>The Indian GST system operates on multiple rate slabs primarily fixed at 5%, 12%, 18%, and 28%. Many business owners struggle to understand the difference between <strong>Exclusive</strong> and <strong>Inclusive</strong> taxation.</p>
            <ul>
                <li><strong>Exclusive GST:</strong> Calculating the tax amount to add <em>on top</em> of a base price (e.g., ₹1000 + 18% GST = ₹1180).</li>
                <li><strong>Inclusive GST:</strong> Extracting the base price from a total amount that already includes tax (e.g., ₹1180 inclusive of 18% GST means the base price is ₹1000).</li>
            </ul>

            <a href="/gst-calculator" class="tool-link-card">
                <span class="emoji-box">🇮🇳</span>
                <div>
                    <div style="font-size: 1.25rem;">Advanced GST Calculator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Instantly calculate CGST, SGST, and IGST for all standard Indian tax slabs.</div>
                </div>
            </a>
            <a href="/invoice-generator" class="tool-link-card">
                <span class="emoji-box">🧾</span>
                <div>
                    <div style="font-size: 1.25rem;">Free PDF Invoice Maker</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Generate beautiful, GST-compliant invoices natively in your browser.</div>
                </div>
            </a>

            <h2>Cracking Loan EMI & Amortization</h2>
            <p>Equated Monthly Installments (EMIs) depend on three factors: Principal, Interest Rate, and Tenure. But understanding just your monthly payment isn't enough; you need to see the Amortization Schedule to understand how much you are losing to interest over 20 years.</p>

            <a href="/emi-calculator" class="tool-link-card">
                <span class="emoji-box">🏠</span>
                <div>
                    <div style="font-size: 1.25rem;">Home/Personal Loan EMI Calculator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Get detailed breakout charts of your interest vs principal components.</div>
                </div>
            </a>
            <a href="/loan-comparison-calculator" class="tool-link-card">
                <span class="emoji-box">⚖️</span>
                <div>
                    <div style="font-size: 1.25rem;">Loan Comparison Calculator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Compare HDFC vs SBI interest rates side-by-side to save lakhs of rupees.</div>
                </div>
            </a>
            <a href="/sip-calculator" class="tool-link-card">
                <span class="emoji-box">📈</span>
                <div>
                    <div style="font-size: 1.25rem;">SIP Mutual Fund Calculator</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Visualize exponential compounding wealth over 10, 15, and 30-year horizons.</div>
                </div>
            </a>
            
            <h3>Why Use Our Financial Suite?</h3>
            <p>Unlike banking apps, our calculators do not ask for your phone number or track your financial data for lead generation. Everything runs using mathematically precise Javascript algorithms purely on your own device.</p>
        """
    },
    {
        "slug": "best-free-background-remover-image-upscaler",
        "tag": "Design Guide",
        "title": "Image Optimization Guide: Best Free BG Remover & Upscaler Online",
        "desc": "How e-commerce sellers and digital artists can leverage free AI tools to double their resolution, compress files, and remove backgrounds flawlessly.",
        "content": """
            <div class="info-card" style="background: var(--nb-lavender);">
                <h3 style="margin-top:0;">The Secret to Premium Product Listings</h3>
                <p>If you run an Etsy shop or Shopify store, image quality dictates your conversion rate. Unfortunately, professional photo editing suites (like Adobe Photoshop) or AI APIs (like Remove.bg) charge exorbitant fees per image.</p>
                <p>We've integrated advanced web-based APIs and canvas drawing algorithms to provide the same studio-quality results without the paywall.</p>
            </div>

            <h2>How to Prepare Your Images for Web</h2>
            <p>There are typically three phases to preparing an image for a high-performance website: <strong>Isolation, Enhancement, and Optimization.</strong></p>
            
            <h3>Phase 1: Isolation (Background Removal)</h3>
            <p>A pure white or transparent background forces the user's eye directly onto the product. Traditional magic wand tools leave jagged edges and halos. Our AI-driven Background Remover automatically detects foreground saliency mapping to cleanly extract subjects.</p>
            <a href="/background-remover" class="tool-link-card">
                <span class="emoji-box">✂️</span>
                <div>
                    <div style="font-size: 1.25rem;">AI Background Remover</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Extract products and people seamlessly with a single click.</div>
                </div>
            </a>

            <h3>Phase 2: Enhancement (Upscaling)</h3>
            <p>Sometimes you only have a low-res 500x500 image from a supplier, but you need 2000x2000 for eBay's zoom feature. Bi-cubic interpolation causes blurry pixels. Instead, our AI Image Upscaler hallucinates missing pixels to double the resolution sharply.</p>
            <a href="/image-upscaler" class="tool-link-card">
                <span class="emoji-box">🔭</span>
                <div>
                    <div style="font-size: 1.25rem;">4K Image Upscaler</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Enhance resolution 2x and 4x without losing clarity.</div>
                </div>
            </a>

            <h3>Phase 3: Optimization (Compression)</h3>
            <p>Huge 5MB PNGs will kill your page speed score, which hurts SEO. You must compress assets without introducing visible artifacts.</p>
            <a href="/image-compressor" class="tool-link-card">
                <span class="emoji-box">🖼️</span>
                <div>
                    <div style="font-size: 1.25rem;">Smart Image Compressor</div>
                    <div style="font-size: 0.95rem; font-weight: 500; color: #444;">Shrink massive JPGs and WebP files by up to 80% visually losslessly.</div>
                </div>
            </a>

            <h2>The Workflow</h2>
            <p>If your ultimate goal is speed and retention, you should first remove the background, upscale the resulting image if necessary, convert the format to modern WebP using our <a href="/image-converter">Image Converter</a>, and finally run it through our Compressor. This guarantees blazing-fast TTFB (Time to First Byte) on modern browsers.</p>
        """
    }
]

for g in guides:
    html = HTML_TEMPLATE.format(**g)
    path = os.path.join(ROOT, "guides", g["slug"] + ".html")
    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print(f"Created: {g['slug']}.html")
