import os

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

content_map = {
    "word-counter.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Word Counter Tool?</h2>
    <p>The <strong>Word Counter</strong> by WorldOfTools is a premium, free online text analysis utility designed for writers, students, SEO professionals, and content creators. It goes far beyond simply counting words. It instantly analyzes your text to provide a comprehensive breakdown of character count (with and without spaces), paragraph count, sentence count, and even an estimated reading and speaking time.</p>
    <p>Whether you are drafting a 280-character tweet, writing a 500-word university essay, optimizing a meta description for SEO, or preparing a 10-minute speech, our tool gives you the precise metrics you need. The tool runs completely offline within your browser using JavaScript, meaning your sensitive essays, private emails, and confidential articles are never uploaded to any server.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Advanced Features — More Than Just a Word Count</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Real-Time Analytics:</strong> As you type or paste, the metrics update instantly without needing to click any buttons or reload the page.</li>
      <li><strong>Social Media Limits:</strong> Instantly see if your text fits within the limits of Twitter/X (280 chars), Instagram captions (2200 chars), SEO Meta Titles (60 chars), Meta Descriptions (160 chars), and SMS messages (160 chars).</li>
      <li><strong>Keyword Density Analyzer:</strong> The tool extracts the most frequently used words in your text (with an option to hide common stop words like 'the', 'and', 'is'). This is crucial for SEO content writers ensuring they hit target keywords without keyword stuffing.</li>
      <li><strong>Reading & Speaking Time:</strong> Based on the average reading speed of 225 words per minute (WPM) and speaking speed of 130 WPM, it calculates exactly how long your audience will take to consume your content.</li>
      <li><strong>Case Conversion & Formatting:</strong> Quickly convert your text to UPPERCASE, lowercase, Title Case, or Sentence case with a single click.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Who Uses This Word Counter?</h2>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Students & Academics:</strong> Strict word limits apply to essays, dissertations, and assignments. Ensure you hit the minimum requirement without going over the maximum limit.</p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>SEO Experts & Bloggers:</strong> Search engines favor comprehensive content. Use the keyword density checker to optimize articles and ensure meta descriptions fall within Google's pixel limits.</p></div>
    <div class="step-item"><div class="step-num">3</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Social Media Managers:</strong> Draft perfect posts for Twitter, LinkedIn, and Instagram without hitting the frustrating character limit error upon publishing.</p></div>
    <div class="step-item"><div class="step-num">4</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Public Speakers:</strong> Paste your speech transcript to get an accurate estimation of how many minutes it will take to deliver on stage.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Is there a limit to how much text I can paste?</summary><p>No! Because the tool runs entirely in your browser using your device's memory, you can paste tens of thousands of words (entire book manuscripts) and it will analyze them instantly without crashing or requiring a premium upgrade.</p></details>
    <details><summary>Does it count spaces as characters?</summary><p>Yes, but it gives you both metrics. The top dashboard shows the total character count including spaces (essential for Twitter and SMS), and also provides a separate count for characters excluding spaces.</p></details>
    <details><summary>How is reading time calculated?</summary><p>Reading time is calculated using an industry-standard algorithm that assumes an average adult reading speed of 225 words per minute. Speaking time assumes a slower, presentation-style pace of 130 words per minute.</p></details>
    <details><summary>What is keyword density and why does it matter?</summary><p>Keyword density is the percentage of times a specific word appears compared to the total number of words. For SEO, maintaining a keyword density around 1-2% for target keywords is optimal. Our built-in density checker helps you spot overused words instantly.</p></details>
    <details><summary>Is my text secure and private?</summary><p>100% Yes. We do not use databases or cloud servers to process your text. The calculation happens on your local machine. Once you close the tab, your data is gone forever.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Text & Developer Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/case-converter"><div class="icon">🔠</div><div class="name">Case Converter</div><div class="desc">Change text casing</div></a>
      <a class="tool-card-mini" href="/fancy-font-generator"><div class="icon">✨</div><div class="name">Fancy Fonts</div><div class="desc">Stylish text for bio</div></a>
      <a class="tool-card-mini" href="/json-formatter"><div class="icon">{ }</div><div class="name">JSON Formatter</div><div class="desc">Beautify JSON code</div></a>
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Tool</div><div class="desc">Encode/Decode strings</div></a>
      <a class="tool-card-mini" href="/qr-code-generator"><div class="icon">📱</div><div class="name">QR Generator</div><div class="desc">Create custom QRs</div></a>
      <a class="tool-card-mini" href="/image-to-text-ocr"><div class="icon">👁️</div><div class="name">Image to Text</div><div class="desc">Extract text from images</div></a>
    </div>
  </section>

</div>""",

    "qr-code-generator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the QR Code Generator?</h2>
    <p>The <strong>QR Code Generator</strong> by WorldOfTools is a fast, free, and highly customizable utility designed to create high-quality Quick Response (QR) codes instantly. Whether you need a QR code to share a website URL, connect customers to your WiFi network without a password, share a vCard contact, or prompt a pre-written WhatsApp message, this tool handles it all securely within your browser.</p>
    <p>With built-in customization options, you can change the QR code's foreground and background colors to match your brand identity, adjust the error correction level for higher durability, and set the perfect margin size. Once generated, you can download the QR code in high-resolution PNG format, ready for print on business cards, flyers, restaurant menus, or digital screens.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Available QR Code Types & Use Cases</h2>
    <p>Our tool supports multiple data formats to ensure maximum compatibility with all smartphone cameras and barcode scanners:</p>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Website URL:</strong> The most common use case. Link directly to your website homepage, product page, promotional campaign, or social media profile (Instagram, LinkedIn, YouTube).</li>
      <li><strong>Plain Text:</strong> Encode serial numbers, secret messages, discount codes, or event instructions that can be read offline without an internet connection.</li>
      <li><strong>Email:</strong> Generate a QR code that instantly opens the user's default email client, pre-filled with your email address, subject line, and a customized body message. Great for customer support or lead generation.</li>
      <li><strong>WhatsApp Message:</strong> Enter a phone number and a pre-typed message. When scanned, it opens WhatsApp ready to send the text. Perfect for business inquiries and ordering systems.</li>
      <li><strong>WiFi Network:</strong> Securely share your WiFi credentials. Guests simply scan the code to instantly connect to your network—no more typing complex passwords.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Understanding Error Correction Levels</h2>
    <p>QR codes use Reed-Solomon error correction, which allows them to be readable even if part of the code is damaged, dirty, or obscured (like when placing a logo in the center). Our tool lets you choose from four levels:</p>
    <div class="step-item"><div class="step-num">L</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Low (7%):</strong> Creates the simplest, least dense QR code. Best when printing in very small sizes where damage is unlikely.</p></div>
    <div class="step-item"><div class="step-num">M</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Medium (15%):</strong> The standard default level. Offers a good balance between density and readability. Ideal for general marketing materials.</p></div>
    <div class="step-item"><div class="step-num">Q</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Quartile (25%):</strong> Higher durability. Recommended if the QR code will be placed outdoors or might suffer wear and tear.</p></div>
    <div class="step-item"><div class="step-num">H</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>High (30%):</strong> The most complex pattern, but can sustain up to 30% damage. Mandatory if you plan to overlay a custom logo in the center of the code after downloading.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Do these QR codes expire?</summary><p>No! The QR codes generated here are "Static" QR codes. The data is hard-coded directly into the pattern itself. As long as the destination URL or text remains valid, the QR code will work forever. They never expire and there are no scan limits.</p></details>
    <details><summary>Are the QR codes really free for commercial use?</summary><p>Yes, 100% free. There are no watermarks, no hidden subscription fees, and no sign-up required. You can use them on your business cards, commercial packaging, billboards, or corporate websites.</p></details>
    <details><summary>Can I track how many times my QR code is scanned?</summary><p>Static QR codes cannot be natively tracked. However, if you are using a URL QR code, you can easily track scans by adding UTM parameters to your link (e.g., ?utm_source=qrcode) before generating the code, and monitoring it via Google Analytics.</p></details>
    <details><summary>Why is my QR code not scanning?</summary><p>Ensure there is sufficient contrast between the foreground and background colors (dark foreground on a light background is best). Also, check that the size is large enough (minimum 2x2 cm for print) and the URL/text entered is correct.</p></details>
    <details><summary>Is my data secure?</summary><p>Yes. The generation process happens entirely in your web browser using a local JavaScript library. Your WiFi passwords, emails, and WhatsApp numbers are never transmitted to our servers.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Essential Utilities</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/barcode-generator"><div class="icon">🏷️</div><div class="name">Barcode Gen</div><div class="desc">Create retail barcodes</div></a>
      <a class="tool-card-mini" href="/favicon-generator"><div class="icon">🖼️</div><div class="name">Favicon Maker</div><div class="desc">Create app icons</div></a>
      <a class="tool-card-mini" href="/image-compressor"><div class="icon">🗜️</div><div class="name">Image Compressor</div><div class="desc">Reduce file size</div></a>
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Encode</div><div class="desc">Data encoding tool</div></a>
      <a class="tool-card-mini" href="/password-generator"><div class="icon">🔑</div><div class="name">Password Gen</div><div class="desc">Secure random pass</div></a>
      <a class="tool-card-mini" href="/url-encoder-decoder"><div class="icon">🔗</div><div class="name">URL Encoder</div><div class="desc">Format web links</div></a>
    </div>
  </section>

</div>""",

    "bmi-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the BMI Calculator?</h2>
    <p>The <strong>BMI (Body Mass Index) Calculator</strong> by WorldOfTools is a free, instant health utility designed to estimate your body fat based on your height and weight. Widely used by medical professionals, fitness trainers, and health organizations globally, BMI serves as a crucial screening tool to categorize individuals into underweight, normal weight, overweight, or obese classifications.</p>
    <p>Our calculator features a beautiful, intuitive interface that supports both the <strong>Metric System</strong> (Centimeters & Kilograms) and the <strong>Imperial System</strong> (Feet/Inches & Pounds). Instantly upon entering your details, you receive your precise BMI score, your World Health Organization (WHO) weight category, your ideal healthy weight range, and an actionable insight into how much weight you need to gain or lose to reach optimum health.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Calculate Your BMI</h2>
    <p>Calculating your BMI manually involves a specific mathematical formula, but our tool does the heavy lifting for you instantly:</p>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Metric Formula:</strong> BMI = Weight (kg) / [Height (m)]²</li>
      <li><strong>Imperial Formula:</strong> BMI = 703 × (Weight (lbs) / [Height (in)]²)</li>
    </ul>
    <p><strong>Step-by-step usage:</strong> Simply select your preferred measurement system from the top tabs. Enter your height (e.g., 5 feet 9 inches, or 175 cm) and your current weight. The calculator instantly processes the data without requiring a page reload, presenting a color-coded health gauge and detailed statistics.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Understanding BMI Categories (WHO Standards)</h2>
    <p>The World Health Organization has established standard BMI cutoff points for adults (aged 20 and older). Our calculator uses these exact thresholds to determine your category:</p>
    <div style="overflow-x:auto;">
      <table class="compare-table">
        <thead><tr>
          <th>BMI Range</th>
          <th>Weight Category</th>
          <th>Health Risk Indicator</th>
        </tr></thead>
        <tbody>
          <tr><td><strong>Below 18.5</strong></td><td style="color:#2563eb;font-weight:700;">Underweight</td><td>Possible nutritional deficiency or underlying condition.</td></tr>
          <tr><td><strong>18.5 – 24.9</strong></td><td style="color:#059669;font-weight:700;">Normal (Healthy Weight)</td><td>Lowest risk of weight-related diseases. Maintain this range!</td></tr>
          <tr><td><strong>25.0 – 29.9</strong></td><td style="color:#d97706;font-weight:700;">Overweight</td><td>Increased risk of cardiovascular issues and type 2 diabetes.</td></tr>
          <tr><td><strong>30.0 and Above</strong></td><td style="color:#dc2626;font-weight:700;">Obese</td><td>High risk of severe health complications. Medical consultation advised.</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:0.85rem;color:#666;margin-top:0.75rem;"><em>Note: For populations of Asian descent, some health authorities recommend a lower cutoff for overweight (23.0) and obesity (27.5) due to higher risks of diabetes at lower BMI levels.</em></p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Limitations of the Body Mass Index</h2>
    <p>While BMI is an excellent general screening tool for populations, it is not a perfect diagnostic tool for individual health. It relies solely on height and weight, meaning it cannot distinguish between fat mass, muscle mass, and bone density. Therefore, keep the following exceptions in mind:</p>
    <div class="step-item"><div class="step-num">💪</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Athletes & Bodybuilders:</strong> Individuals with high muscle mass may score in the "Overweight" or "Obese" category despite having very low body fat percentages, because muscle weighs more than fat by volume.</p></div>
    <div class="step-item"><div class="step-num">🧓</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Elderly Populations:</strong> Older adults naturally lose muscle mass and bone density, meaning they could have excess body fat even with a "Normal" BMI score.</p></div>
    <div class="step-item"><div class="step-num">👶</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Children & Teens:</strong> Standard adult BMI formulas do not apply to children. Pediatric BMI must be plotted on age- and gender-specific growth charts provided by pediatricians.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>What is my ideal healthy weight?</summary><p>Your ideal weight is calculated based on the "Normal" BMI range of 18.5 to 24.9. When you calculate your BMI using our tool, we automatically display your specific ideal weight bracket based on your entered height.</p></details>
    <details><summary>Does BMI differ for men and women?</summary><p>No, the standard BMI formula and WHO categorizations are identical for both adult men and adult women. However, women naturally tend to carry slightly more body fat than men at the same BMI level.</p></details>
    <details><summary>Is this calculator suitable for children?</summary><p>No. This adult BMI calculator is designed for individuals aged 20 and older. Children and adolescents require specialized percentile charts that account for ongoing growth and development.</p></details>
    <details><summary>How can I lower my BMI?</summary><p>Lowering your BMI involves reaching a healthier body weight. This is generally achieved through a combination of a caloric-deficit diet (eating fewer calories than you burn), regular cardiovascular exercise, strength training, and adequate sleep. Always consult a healthcare provider before starting a weight-loss program.</p></details>
    <details><summary>Is my health data saved?</summary><p>Never. WorldOfTools is committed to privacy. Your height, weight, and BMI results are processed locally in your browser and instantly discarded when you close the tab. Nothing is stored on our servers.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Health & Everyday Calculators</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/age-calculator"><div class="icon">🎂</div><div class="name">Age Calculator</div><div class="desc">Exact age in seconds</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
      <a class="tool-card-mini" href="/word-counter"><div class="icon">📝</div><div class="name">Word Counter</div><div class="desc">Analyze text & reading time</div></a>
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Calculate home/car loans</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST</div></a>
      <a class="tool-card-mini" href="/random-number-generator"><div class="icon">🎲</div><div class="name">Random Number</div><div class="desc">True random numbers</div></a>
    </div>
  </section>

</div>""",

    "image-compressor.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Image Compressor?</h2>
    <p>The <strong>Image Compressor</strong> by WorldOfTools is a powerful, browser-based utility designed to drastically reduce the file size of your photos without sacrificing visual quality. Large, unoptimized images are the number one cause of slow-loading websites, frustrating user experiences, and excessive storage consumption. Whether you're a web developer optimizing assets for Google Core Web Vitals, a photographer saving cloud storage space, or an everyday user trying to email a batch of photos, this tool is the perfect solution.</p>
    <p>Our compressor utilizes advanced local JavaScript algorithms to perform "Lossy" compression. This intelligently strips away invisible metadata and imperceptibly reduces color palettes to compress JPG, PNG, and WebP images by up to 80-90%. Best of all, because the processing happens entirely on your device, your private photos are never uploaded to the internet, guaranteeing absolute security.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Why Should You Compress Images?</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Boost Website Speed & SEO:</strong> Google explicitly factors page loading speed into its search rankings. Compressing a 3MB banner image down to 300KB ensures your site loads instantly on mobile networks, lowering bounce rates and improving SEO visibility.</li>
      <li><strong>Save Storage Space:</strong> High-resolution smartphone cameras create massive files. Compressing them allows you to store thousands more photos on your phone, hard drive, or cloud storage limits (like Google Drive or iCloud).</li>
      <li><strong>Easier Sharing & Emailing:</strong> Most email clients (like Gmail or Outlook) have strict 20MB to 25MB attachment limits. Compressing your images allows you to attach entire photo albums in a single email without relying on external file-sharing links.</li>
      <li><strong>Faster Uploads:</strong> Uploading profile pictures to social media, uploading inventory to e-commerce platforms, or submitting documents to government portals often requires images to be under 1MB or 500KB.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Use the Image Compressor</h2>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Upload Your Images:</strong> Click the upload area or simply drag and drop your image files (JPG, PNG, WebP) directly into the browser window.</p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Adjust Compression Level:</strong> Use the quality slider to find the perfect balance. Lower quality yields much smaller file sizes. A quality setting between 60% and 80% is generally the sweet spot for web use.</p></div>
    <div class="step-item"><div class="step-num">3</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Resize Dimensions (Optional):</strong> If your image is 4000px wide but only needs to be viewed on a mobile screen, use the Maximum Width slider to resize the image. Scaling down dimensions provides the most drastic file size reduction.</p></div>
    <div class="step-item"><div class="step-num">4</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Download instantly:</strong> Compare the original size vs. the new compressed size. Click download to save the optimized image back to your device instantly.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Will compression ruin the quality of my photo?</summary><p>Not noticeably. Our tool uses smart "lossy" compression. While technical data is discarded, the human eye generally cannot distinguish between an image at 100% quality and one compressed to 80%. You retain crisp visuals at a fraction of the file size.</p></details>
    <details><summary>Are my private photos uploaded to your server?</summary><p>Absolutely not. Privacy is our core feature. Unlike other online compressors that force you to upload images to their servers, WorldOfTools utilizes modern HTML5 Canvas APIs to compress the image directly inside your browser. No data ever leaves your computer.</p></details>
    <details><summary>What image formats are supported?</summary><p>You can compress standard web formats including JPEG/JPG, PNG, and WebP. The tool will output the compressed image in the same format it was uploaded in.</p></details>
    <details><summary>How do I compress an image to under 50KB or 100KB?</summary><p>If you need to hit a strict file size limit for a form submission, apply two steps: First, reduce the Maximum Width slider to something reasonable (e.g., 800px or 1000px). Second, lower the Quality slider to 60%. This combination easily shrinks multi-megabyte files to under 100KB.</p></details>
    <details><summary>Can I compress transparent PNG images?</summary><p>Yes, transparent PNG images are fully supported. The transparency (alpha channel) is preserved during the compression and resizing process.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Image & Design Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/image-to-text-ocr"><div class="icon">👁️</div><div class="name">Image to Text</div><div class="desc">Extract text from images</div></a>
      <a class="tool-card-mini" href="/jpg-to-png-converter"><div class="icon">🔄</div><div class="name">JPG to PNG</div><div class="desc">Convert image formats</div></a>
      <a class="tool-card-mini" href="/background-remover"><div class="icon">✂️</div><div class="name">BG Remover</div><div class="desc">Remove image backgrounds</div></a>
      <a class="tool-card-mini" href="/aspect-ratio-calculator"><div class="icon">📐</div><div class="name">Aspect Ratio</div><div class="desc">Maintain image proportions</div></a>
      <a class="tool-card-mini" href="/favicon-generator"><div class="icon">🖼️</div><div class="name">Favicon Maker</div><div class="desc">Create app icons</div></a>
      <a class="tool-card-mini" href="/qr-code-generator"><div class="icon">📱</div><div class="name">QR Generator</div><div class="desc">Create custom QRs</div></a>
    </div>
  </section>

</div>""",

    "emi-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is an EMI Calculator?</h2>
    <p>The <strong>EMI (Equated Monthly Installment) Calculator</strong> by WorldOfTools is a premium financial planning tool designed to help you accurately calculate your monthly loan repayment schedule. Whether you are planning to take a Home Loan, Car Loan, Personal Loan, or Education Loan in India, understanding your exact monthly outflow is critical to managing your personal finances.</p>
    <p>By simply entering your principal loan amount, the annual interest rate, and the loan tenure (in years or months), our calculator instantly generates your exact EMI amount, the total interest payable over the lifespan of the loan, and the total repayment amount. It also generates a comprehensive, interactive pie chart visually breaking down the ratio of principal vs. interest, empowering you to make informed borrowing decisions.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How is EMI Calculated? (The Formula)</h2>
    <p>Banks and Non-Banking Financial Companies (NBFCs) calculate your EMI using a standardized mathematical formula based on the reducing balance method. Our tool executes this formula instantly:</p>
    <div style="background:#f9f9ff;border:2px solid #000;border-radius:12px;padding:1.25rem;font-family:monospace;font-size:1rem;font-weight:700;margin-bottom:1rem;box-shadow:3px 3px 0 #000;text-align:center;">
      EMI = [P x R x (1+R)^N] / [(1+R)^N-1]
    </div>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>P (Principal):</strong> The total loan amount borrowed from the bank.</li>
      <li><strong>R (Rate):</strong> The monthly interest rate (Annual Interest Rate divided by 12 and then divided by 100).</li>
      <li><strong>N (Tenure):</strong> The total number of monthly installments (Loan tenure in years multiplied by 12).</li>
    </ul>
    <p>Manually calculating this complex formula is error-prone. Our EMI calculator automates the process, delivering 100% accurate results in milliseconds.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Why Should You Use an EMI Calculator Before Borrowing?</h2>
    <div class="step-item"><div class="step-num">📊</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Financial Planning:</strong> Knowing your exact EMI allows you to structure your monthly household budget. Financial experts advise that your total EMI obligations should not exceed 40-50% of your monthly take-home income.</p></div>
    <div class="step-item"><div class="step-num">💰</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Assess Interest Burden:</strong> For long-term loans like a 20-year Home Loan, the interest paid can often exceed the principal amount. The visual pie chart reveals exactly how much "extra" money you are paying the bank.</p></div>
    <div class="step-item"><div class="step-num">⏱️</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Compare Loan Offers:</strong> Use the tool to compare different interest rates and tenures offered by SBI, HDFC, ICICI, or Bajaj Finserv to find the most cost-effective borrowing option.</p></div>
    <div class="step-item"><div class="step-num">⚖️</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Optimize Tenure vs. EMI:</strong> A longer tenure means a smaller, more affordable monthly EMI, but significantly higher total interest paid. Play with the sliders to find your perfect balance.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Does this calculator work for all types of loans in India?</summary><p>Yes! The underlying mathematical formula for a reducing balance loan is universal. You can use this tool to calculate EMIs for Home Loans, Auto/Car Loans, Two-Wheeler Loans, Personal Loans, and Business Loans from any Indian bank or NBFC.</p></details>
    <details><summary>What is a Reducing Balance interest rate?</summary><p>In India, most retail loans operate on a reducing balance method. This means interest is calculated only on the outstanding principal balance. As you pay your EMI each month, a portion goes toward the principal, reducing the base amount upon which the next month's interest is calculated. Our calculator automatically factors this in.</p></details>
    <details><summary>Does the calculated EMI include processing fees or GST?</summary><p>No. The EMI calculated here represents only the principal repayment and the interest charged. Banks usually charge an upfront processing fee (e.g., 1% of the loan amount) plus applicable GST on that fee, which is deducted before disbursement.</p></details>
    <details><summary>How can I reduce my overall interest burden?</summary><p>To save on interest: 1) Opt for a shorter loan tenure if you can afford the higher EMI. 2) Make periodic partial prepayments (part-payments) whenever you have surplus funds, as this directly reduces the principal balance. 3) Negotiate for a lower interest rate or transfer your balance to a cheaper lender.</p></details>
    <details><summary>Is my financial data uploaded to any server?</summary><p>No. WorldOfTools prioritizes your privacy. All loan parameters you enter and calculations generated occur entirely via local JavaScript in your web browser. No data is stored, tracked, or sent to any server.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Finance & Investment Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/sip-calculator"><div class="icon">📈</div><div class="name">SIP Calculator</div><div class="desc">Mutual fund returns</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
      <a class="tool-card-mini" href="/ppf-calculator"><div class="icon">💰</div><div class="name">PPF Calculator</div><div class="desc">Tax-free investment</div></a>
      <a class="tool-card-mini" href="/invoice-generator"><div class="icon">📄</div><div class="name">Invoice Maker</div><div class="desc">Generate PDF invoices</div></a>
      <a class="tool-card-mini" href="/age-calculator"><div class="icon">🎂</div><div class="name">Age Calculator</div><div class="desc">Exact chronological age</div></a>
    </div>
  </section>

</div>"""
}

def inject_content():
    for filename, content in content_map.items():
        filepath = os.path.join(BASE_DIR, filename)
        if not os.path.exists(filepath):
            print(f"File not found: {filepath}")
            continue
            
        with open(filepath, 'r', encoding='utf-8') as f:
            html = f.read()
            
        # Strategy: Find <!-- SEO CONTENT --> and replace everything from there to the next closing tag like <footer> or </main>
        
        # We know that the SEO section is wrapped in <div class="seo-section">
        # So we can search for <!-- SEO CONTENT -->\s*<div class="seo-section"> 
        # and then find the corresponding closing </div>. But a regex approach is simpler if we assume a specific structure.
        import re
        
        # Regex to match from <!-- SEO CONTENT --> up to but not including the next script or footer or </main> or </body>
        # Actually, let's just find "<!-- SEO CONTENT -->" and the end of the div.
        
        # Since the seo-section contains many divs, a simple regex is hard.
        # But we know it always ends with </div> right before <footer> or </main> or <script>
        
        # Find the start index
        start_idx = html.find('<!-- SEO CONTENT -->')
        if start_idx == -1:
            # Maybe it doesn't have the comment. Let's look for <div class="seo-section">
            start_idx = html.find('<div class="seo-section">')
            
        if start_idx == -1:
            print(f"Could not find seo-section start in {filename}")
            continue
            
        # Find the end. We will look for <footer> or </main> that comes AFTER start_idx
        end_idx_main = html.find('</main>', start_idx)
        end_idx_footer = html.find('<footer>', start_idx)
        end_idx_script = html.find('<script', start_idx)
        
        # We want the first tag that follows the seo-section.
        possible_ends = [i for i in [end_idx_main, end_idx_footer, end_idx_script] if i != -1]
        if not possible_ends:
            print(f"Could not find end of seo-section in {filename}")
            continue
            
        end_idx = min(possible_ends)
        
        # we want to replace html[start_idx:end_idx] with our content
        # But wait, our content already includes <!-- SEO CONTENT --> and <div class="seo-section"> and </div>
        
        new_html = html[:start_idx] + content + '\n\n' + html[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Successfully injected content into {filename}")

if __name__ == "__main__":
    inject_content()
