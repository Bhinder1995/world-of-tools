import os

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

content_map = {
    "jwt-decoder.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the JWT Decoder?</h2>
    <p>The <strong>JWT Decoder</strong> by WorldOfTools is a premium, free developer utility designed to instantly decode JSON Web Tokens (JWT). JWTs are the industry standard for securely transmitting information between parties as a JSON object, heavily used in modern web authentication, Single Sign-On (SSO), and RESTful APIs.</p>
    <p>Our tool instantly cracks open the Base64Url-encoded token to reveal its three distinct parts: the <strong>Header</strong> (algorithm and token type), the <strong>Payload</strong> (the actual claims or data being transmitted), and the <strong>Signature</strong>. Built strictly for developers, this tool runs entirely locally in your browser. This means your sensitive authentication tokens and session data are never uploaded to our servers, ensuring 100% security and privacy.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Decode a JWT</h2>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Paste the Token:</strong> A standard JWT looks like three long strings of random characters separated by dots (e.g., xxxxx.yyyyy.zzzzz). Paste this complete string into the input box.</p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Instant Decoding:</strong> The tool instantly splits the token by its periods and decodes the Base64Url strings.</p></div>
    <div class="step-item"><div class="step-num">3</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Analyze the Payload:</strong> View the decoded JSON payload. You will easily spot standard claims like <em>sub</em> (subject/user ID), <em>iat</em> (issued at timestamp), and <em>exp</em> (expiration timestamp), alongside any custom user data.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Can this tool verify the JWT signature?</summary><p>Currently, this tool acts as a decoder, meaning it reads the public Header and Payload information. To cryptographically verify the signature, you must possess the secret key or the public/private key pair used by the issuing server.</p></details>
    <details><summary>Are JSON Web Tokens encrypted?</summary><p>No! This is a critical security concept. A standard JWT (JWS) is signed, but it is NOT encrypted. Anyone who intercepts the token can easily decode the Base64 string and read the payload. You should never store sensitive data like passwords or credit card numbers inside a JWT payload.</p></details>
    <details><summary>Why does the decoded payload show dates as large numbers?</summary><p>JWTs use standard Unix timestamps (the number of seconds since January 1, 1970) for dates like the expiration (<em>exp</em>) and issued at (<em>iat</em>) claims. Our tool automatically displays the raw integer, but you can use an epoch converter to see the human-readable date.</p></details>
    <details><summary>Is my JWT data secure here?</summary><p>Yes. The decoding process utilizes the browser's native JavaScript functions (`atob()`). The token string never leaves your local machine, ensuring your active session tokens cannot be hijacked.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Developer Security Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Tool</div><div class="desc">Encode/Decode data</div></a>
      <a class="tool-card-mini" href="/json-formatter"><div class="icon">{ }</div><div class="name">JSON Formatter</div><div class="desc">Beautify JSON code</div></a>
      <a class="tool-card-mini" href="/hash-generator"><div class="icon">#️⃣</div><div class="name">Hash Generator</div><div class="desc">MD5/SHA Hashes</div></a>
      <a class="tool-card-mini" href="/password-generator"><div class="icon">🛡️</div><div class="name">Password Gen</div><div class="desc">Create secure keys</div></a>
      <a class="tool-card-mini" href="/regex-tester"><div class="icon">🔍</div><div class="name">Regex Tester</div><div class="desc">Test regular expressions</div></a>
    </div>
  </section>

</div>""",

    "password-generator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Secure Password Generator?</h2>
    <p>The <strong>Secure Password Generator</strong> by WorldOfTools is a free, privacy-first cybersecurity utility designed to instantly create unbreakable, cryptographically strong passwords. In an era of constant data breaches and brute-force hacking attempts, relying on easily guessable passwords (like pet names or birthdays) is the fastest way to get compromised.</p>
    <p>Our tool uses your browser's built-in <code>crypto.getRandomValues()</code> API to generate true randomness. You have full control over the complexity: choose the exact password length, and toggle uppercase letters, lowercase letters, numbers, and special symbols. Because the generation happens 100% locally on your device, your new passwords are never transmitted over the internet, guaranteeing absolute security.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Why You Need a Cryptographically Secure Password</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Defeat Brute Force Attacks:</strong> A standard 8-character password with only lowercase letters can be cracked by modern hackers in milliseconds. A 16-character password mixing all character types would take trillions of years to crack.</li>
      <li><strong>Prevent Dictionary Attacks:</strong> Hackers use automated scripts that run through the entire English dictionary. A randomly generated string of characters (like <em>$T7p!qW9z#kL2m</em>) defeats this completely.</li>
      <li><strong>Stop Credential Stuffing:</strong> By using a password generator alongside a password manager, you can easily create and use a unique, complex password for every single website. If one site gets breached, your other accounts remain perfectly safe.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>How long should my password be?</summary><p>Cybersecurity experts and organizations like NIST recommend a minimum length of 12 to 14 characters for standard accounts, and 16+ characters for highly sensitive accounts like banking, primary email, or master password managers.</p></details>
    <details><summary>Is this generator truly random?</summary><p>Yes. Instead of using standard pseudo-random number generators (like <code>Math.random()</code>), our tool relies on the Web Crypto API. This generates cryptographically secure pseudo-random numbers using high-entropy hardware seeds from your operating system.</p></details>
    <details><summary>Do you save the passwords I generate?</summary><p>Absolutely not. We have no databases and no server-side tracking. Once you close the browser tab, the password is gone forever. You must copy it and save it in your personal password manager.</p></details>
    <details><summary>What is a passphrase and is it better?</summary><p>A passphrase is a string of random words (e.g., <em>horse-battery-staple-correct</em>). They are often easier for humans to remember while still providing massive entropy due to their extreme length. However, for maximum security where you don't need to memorize the code, a complex random character string is superior.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Security & Developer Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/hash-generator"><div class="icon">#️⃣</div><div class="name">Hash Generator</div><div class="desc">MD5/SHA Hashes</div></a>
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Tool</div><div class="desc">Encode/Decode data</div></a>
      <a class="tool-card-mini" href="/jwt-decoder"><div class="icon">🔑</div><div class="name">JWT Decoder</div><div class="desc">Decode web tokens</div></a>
      <a class="tool-card-mini" href="/qr-code-generator"><div class="icon">📱</div><div class="name">QR Generator</div><div class="desc">Create WiFi QRs</div></a>
      <a class="tool-card-mini" href="/ip-address-lookup"><div class="icon">🌐</div><div class="name">IP Lookup</div><div class="desc">Find IP location</div></a>
    </div>
  </section>

</div>""",

    "unit-converter.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Universal Unit Converter?</h2>
    <p>The <strong>Unit Converter</strong> by WorldOfTools is a comprehensive, free online mathematical utility designed to instantly convert measurements across various global systems. Whether you are a student solving physics problems, an engineer calculating structural loads, a chef scaling an international recipe, or simply trying to convert your height from centimeters to feet, this tool delivers pinpoint accuracy.</p>
    <p>We support all major measurement categories including Length, Weight/Mass, Temperature, Area, Volume, Speed, and Time. The tool provides a seamless, side-by-side interface allowing you to easily switch between the Metric system (used globally) and the Imperial system (used primarily in the US and UK).</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Supported Conversion Categories</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Length & Distance:</strong> Convert between Meters, Centimeters, Kilometers, Inches, Feet, Yards, and Miles. Crucial for construction, tailoring, and travel planning.</li>
      <li><strong>Weight & Mass:</strong> Effortlessly switch between Kilograms, Grams, Milligrams, Pounds, Ounces, and Metric Tonnes. Perfect for fitness tracking (BMI calculations) and shipping logistics.</li>
      <li><strong>Temperature:</strong> Instantly convert Celsius to Fahrenheit or Kelvin. Essential for scientific calculations, cooking, and international weather forecasts.</li>
      <li><strong>Area & Volume:</strong> Calculate Square Meters, Acres, Hectares, Liters, Gallons, and Milliliters. Ideal for real estate, agriculture, and culinary arts.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>How accurate are the conversion rates?</summary><p>Our converter uses exact, internationally standardized mathematical ratios (e.g., 1 Inch = exactly 2.54 Centimeters). For measurements resulting in long decimals, the tool provides high-precision floating-point results which you can round as needed.</p></details>
    <details><summary>What is the difference between Metric and Imperial?</summary><p>The Metric system is a decimal-based system of measurement (base 10) used by almost the entire world, utilizing units like meters and grams. The Imperial system is historically based and used primarily in the United States, utilizing units like feet, inches, and pounds.</p></details>
    <details><summary>Can I use this tool offline?</summary><p>Yes! Once the page loads in your browser, the conversion logic runs entirely via client-side JavaScript. If your internet connection drops, the calculator will continue to work perfectly.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Math & Calculator Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/scientific-calculator"><div class="icon">🔬</div><div class="name">Scientific Calc</div><div class="desc">Advanced Math</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
      <a class="tool-card-mini" href="/bmi-calculator"><div class="icon">⚖️</div><div class="name">BMI Calculator</div><div class="desc">Check body mass</div></a>
      <a class="tool-card-mini" href="/age-calculator"><div class="icon">🎂</div><div class="name">Age Calculator</div><div class="desc">Find exact age</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove tax</div></a>
    </div>
  </section>

</div>""",

    "base64-encoder-decoder.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Base64 Encoder / Decoder?</h2>
    <p>The <strong>Base64 Encoder/Decoder</strong> by WorldOfTools is a free, lightning-fast developer utility designed to translate plain text or raw data into a Base64 encoded string, and vice-versa. Base64 is a binary-to-text encoding scheme that represents binary data in an ASCII string format. It is universally used in programming, network communications, and web development to ensure data remains intact without modification during transport.</p>
    <p>Whether you need to embed small images directly into HTML/CSS files, safely transmit complex JSON payloads in URLs, attach files in MIME emails, or encode authentication credentials for Basic Auth headers, this tool handles it instantly directly inside your browser.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Why Do We Use Base64 Encoding?</h2>
    <p>Many legacy communication protocols (like early email systems) were designed to handle only standard ASCII text. If you tried to send raw binary data (like an image or a compiled program), the system would misinterpret the special characters, corrupting the file.</p>
    <p>Base64 solves this by converting the raw data into a universally safe alphabet consisting of 64 characters: A-Z, a-z, 0-9, plus '+' and '/'. The resulting string is approximately 33% larger than the original data, but is guaranteed to survive transport across any text-based protocol without corruption.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Is Base64 a form of encryption?</summary><p><strong>No.</strong> This is a very common misconception. Base64 is an <em>encoding</em> scheme, not encryption. It provides zero cryptographic security. Anyone with a Base64 decoder can instantly read the original data. Never use Base64 to hide passwords or sensitive data.</p></details>
    <details><summary>Why does my encoded string end with an equals sign (=)?</summary><p>The equals sign is used as "padding" in Base64. Because Base64 processes data in 3-byte chunks, if your input data doesn't divide perfectly by 3, the algorithm adds one or two '=' characters at the end to ensure the output length is a multiple of 4.</p></details>
    <details><summary>What is Base64URL encoding?</summary><p>Base64URL is a slight variation of standard Base64 designed to be safely passed in web URLs. It replaces the '+' and '/' characters (which have special meaning in URLs) with '-' and '_', and removes the padding '='. This is exactly the format used in JSON Web Tokens (JWT).</p></details>
    <details><summary>Is my data uploaded to your server?</summary><p>No. Both encoding and decoding are performed strictly on your local machine using your browser's native JavaScript APIs (`btoa()` and `atob()`). Your data never leaves your device.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Developer Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/jwt-decoder"><div class="icon">🔑</div><div class="name">JWT Decoder</div><div class="desc">Decode web tokens</div></a>
      <a class="tool-card-mini" href="/json-formatter"><div class="icon">{ }</div><div class="name">JSON Formatter</div><div class="desc">Beautify JSON code</div></a>
      <a class="tool-card-mini" href="/url-encoder-decoder"><div class="icon">🔗</div><div class="name">URL Encoder</div><div class="desc">Format web links safely</div></a>
      <a class="tool-card-mini" href="/hash-generator"><div class="icon">#️⃣</div><div class="name">Hash Generator</div><div class="desc">MD5/SHA Hashes</div></a>
      <a class="tool-card-mini" href="/regex-tester"><div class="icon">🔍</div><div class="name">Regex Tester</div><div class="desc">Test expressions</div></a>
    </div>
  </section>

</div>""",

    "hash-generator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Hash Generator?</h2>
    <p>The <strong>Hash Generator</strong> by WorldOfTools is a free, advanced cryptography utility designed for developers and security researchers. It allows you to instantly compute cryptographic hashes for any text string using industry-standard algorithms including MD5, SHA-1, SHA-256, and SHA-512.</p>
    <p>A hash function takes an input of any size and produces a fixed-length string of characters, acting as a unique "digital fingerprint" for that data. Whether you are verifying the integrity of a downloaded file, generating checksums, securely hashing user passwords for a database, or creating API signatures, our tool executes the cryptographic math locally in your browser for absolute data privacy.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Understanding the Hash Algorithms</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>MD5 (128-bit):</strong> Produces a 32-character hex string. While fast, MD5 is cryptographically broken and vulnerable to collision attacks. It should only be used for non-security checksums to verify file integrity.</li>
      <li><strong>SHA-1 (160-bit):</strong> Produces a 40-character hex string. Historically used in SSL certificates and Git, but is now considered insecure against well-funded attackers.</li>
      <li><strong>SHA-256 (256-bit):</strong> The modern industry standard. It produces a 64-character hex string. SHA-256 is highly secure, resistant to collisions, and is the backbone of Bitcoin mining, JWT signatures, and SSL/TLS certificates.</li>
      <li><strong>SHA-512 (512-bit):</strong> Produces a massive 128-character string. Provides maximum security and is surprisingly faster than SHA-256 on 64-bit processors.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Can I decrypt or reverse a hash?</summary><p><strong>No.</strong> Cryptographic hashing is a one-way mathematical function. It is intentionally designed to be irreversible. The only way to "crack" a hash is through brute-force (guessing every possible combination) or using a pre-computed "Rainbow Table".</p></details>
    <details><summary>What is a hash collision?</summary><p>A collision occurs when two completely different inputs produce the exact same hash output. A good cryptographic algorithm makes this statistically impossible. Older algorithms like MD5 have known vulnerabilities where attackers can intentionally generate collisions.</p></details>
    <details><summary>Should I use this to hash user passwords?</summary><p>For modern web applications, you should not rely on simple SHA-256 alone for passwords. You should use specialized password-hashing algorithms that are intentionally slow (like <em>Bcrypt</em>, <em>Argon2</em>, or <em>PBKDF2</em>) and incorporate a unique "salt" to defeat rainbow table attacks.</p></details>
    <details><summary>Are the calculations done securely?</summary><p>Yes. The hashing relies entirely on client-side JavaScript (Web Crypto API or local libraries). Your raw text strings are never transmitted to our servers, keeping your sensitive data secure.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Security & Developer Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/password-generator"><div class="icon">🛡️</div><div class="name">Password Gen</div><div class="desc">Create secure keys</div></a>
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Tool</div><div class="desc">Encode/Decode data</div></a>
      <a class="tool-card-mini" href="/jwt-decoder"><div class="icon">🔑</div><div class="name">JWT Decoder</div><div class="desc">Decode web tokens</div></a>
      <a class="tool-card-mini" href="/uuid-generator"><div class="icon">🆔</div><div class="name">UUID Generator</div><div class="desc">Generate v4 UUIDs</div></a>
      <a class="tool-card-mini" href="/json-formatter"><div class="icon">{ }</div><div class="name">JSON Formatter</div><div class="desc">Beautify JSON code</div></a>
    </div>
  </section>

</div>""",

    "seo-meta-tag-generator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the SEO Meta Tag Generator?</h2>
    <p>The <strong>SEO Meta Tag Generator</strong> by WorldOfTools is a free webmaster utility designed to help website owners rapidly create perfectly optimized HTML meta tags. Meta tags are invisible snippets of code located in the <code>&lt;head&gt;</code> section of your HTML that tell Google, Bing, and social media platforms exactly what your webpage is about.</p>
    <p>By filling out a simple form with your page title, description, and keywords, our tool instantly generates clean, valid HTML code ready to be copied and pasted into your website. Proper meta tags are the foundational first step of on-page SEO, drastically improving your search engine visibility and click-through rates (CTR) from the search results page.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>The Most Important Meta Tags for 2025</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Title Tag:</strong> The most critical SEO factor. It appears as the clickable blue link in Google Search. Best practices dictate keeping it under 60 characters to prevent truncation.</li>
      <li><strong>Meta Description:</strong> While not a direct ranking factor, a compelling description acts as your "sales pitch" on the search results page, heavily influencing whether users click your link. Keep it between 150-160 characters.</li>
      <li><strong>Robots Tag:</strong> Controls how search engine spiders index your page. You can tell them to "index" and "follow" links, or use "noindex" for private pages you want kept off Google.</li>
      <li><strong>Viewport Tag:</strong> Essential for mobile-friendliness. It tells mobile browsers how to scale the page to fit different screen sizes. Without it, your site will fail Google's mobile-friendly test.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Do Meta Keywords still matter for SEO?</summary><p><strong>No.</strong> Google officially announced in 2009 that they completely ignore the "keywords" meta tag due to historical keyword stuffing abuse. While some smaller international search engines (like Yandex) may still look at it, it carries zero weight for Google. Focus your energy on the Title and Description.</p></details>
    <details><summary>Why is Google rewriting my Meta Description?</summary><p>Google frequently ignores your hard-coded meta description if it believes a different snippet of text from your page better answers the user's specific search query. However, providing a strong, highly relevant default description greatly increases the chances they will use yours.</p></details>
    <details><summary>What are Open Graph (OG) tags?</summary><p>Open Graph tags are specialized meta tags originally created by Facebook. They control how your link appears when shared on social media (Facebook, LinkedIn, Discord). They allow you to define a specific preview image, title, and description for social feeds, which is critical for viral marketing.</p></details>
    <details><summary>Where do I paste the generated code?</summary><p>The outputted HTML must be pasted strictly inside the <code>&lt;head&gt;</code> and <code>&lt;/head&gt;</code> tags of your website's HTML document. If pasted in the body, they will not work.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More SEO & Webmaster Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/schema-generator-online"><div class="icon">🏗️</div><div class="name">Schema Gen</div><div class="desc">JSON-LD Builder</div></a>
      <a class="tool-card-mini" href="/serp-preview"><div class="icon">👁️</div><div class="name">SERP Preview</div><div class="desc">Google visualizer</div></a>
      <a class="tool-card-mini" href="/word-counter"><div class="icon">📝</div><div class="name">Word Counter</div><div class="desc">Check character limits</div></a>
      <a class="tool-card-mini" href="/image-compressor"><div class="icon">🗜️</div><div class="name">Image Compressor</div><div class="desc">Boost page speed</div></a>
      <a class="tool-card-mini" href="/favicon-generator"><div class="icon">🖼️</div><div class="name">Favicon Maker</div><div class="desc">Create app icons</div></a>
    </div>
  </section>

</div>""",

    "regex-tester.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Regex Tester?</h2>
    <p>The <strong>Regex Tester</strong> by WorldOfTools is a powerful, real-time developer utility designed for building, debugging, and testing Regular Expressions (Regex). Regular expressions are complex sequences of characters that define a search pattern, universally used in programming languages (JavaScript, Python, PHP, Java) to validate user input, search massive log files, and extract specific data points.</p>
    <p>Writing Regex can feel like deciphering an alien language. Our tool simplifies this by providing a live visual environment. Simply type your pattern, paste your target text, and watch as matches are highlighted instantly. You can easily toggle global, case-insensitive, and multiline flags to fine-tune your expression's behavior.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Common Regex Use Cases</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Form Validation:</strong> Ensure a user's input matches standard formats before submitting to a database. The most common validations include Email addresses, Phone numbers, ZIP codes, and strong password enforcement (requiring capitals, numbers, and symbols).</li>
      <li><strong>Data Extraction (Scraping):</strong> Pull specific information out of massive, unstructured text blocks. For example, extracting all URLs from an HTML file, or pulling all IP addresses from a raw Apache server log.</li>
      <li><strong>Find and Replace:</strong> Perform advanced text manipulation. For example, finding all dates written in DD/MM/YYYY format and programmatically rearranging them to YYYY-MM-DD.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>What do the different Flags (g, i, m) mean?</summary><p>Flags change how the engine searches the text. <strong>g (Global)</strong> forces the engine to find all matches, rather than stopping at the first one. <strong>i (Ignore Case)</strong> makes the search case-insensitive, so 'A' matches 'a'. <strong>m (Multiline)</strong> changes the behavior of the anchor tags (^ and $) to match the start and end of individual lines, rather than the entire string.</p></details>
    <details><summary>Are Regular Expressions identical across all programming languages?</summary><p>Mostly yes, but there are different "flavors." The underlying concepts are universal, but languages like JavaScript, Python, and PCRE (PHP) have slight differences in how they handle advanced features like lookbehinds or named capture groups. Our tester operates using the standard JavaScript Regex engine.</p></details>
    <details><summary>What is a Capture Group?</summary><p>Capture groups are created by wrapping part of your regex in parentheses <code>(...)</code>. They allow you to extract a specific sub-string from a larger match. For example, when matching a phone number, you might capture just the area code to process it separately in your code.</p></details>
    <details><summary>Is my pasted data secure?</summary><p>Yes! Developers often need to test regex against proprietary code or sensitive server logs. Our tool uses the browser's native JavaScript `RegExp` object. Everything is processed locally on your machine, ensuring complete privacy.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Developer Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/json-formatter"><div class="icon">{ }</div><div class="name">JSON Formatter</div><div class="desc">Beautify JSON code</div></a>
      <a class="tool-card-mini" href="/jwt-decoder"><div class="icon">🔑</div><div class="name">JWT Decoder</div><div class="desc">Decode web tokens</div></a>
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Tool</div><div class="desc">Encode/Decode data</div></a>
      <a class="tool-card-mini" href="/hash-generator"><div class="icon">#️⃣</div><div class="name">Hash Generator</div><div class="desc">MD5/SHA Hashes</div></a>
      <a class="tool-card-mini" href="/sql-formatter"><div class="icon">🗄️</div><div class="name">SQL Formatter</div><div class="desc">Beautify SQL queries</div></a>
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
            
        start_idx = html.find('<!-- SEO CONTENT -->')
        if start_idx == -1:
            start_idx = html.find('<div class="seo-section">')
            
        if start_idx == -1:
            print(f"Could not find seo-section start in {filename}")
            continue
            
        end_idx_main = html.find('</main>', start_idx)
        end_idx_footer = html.find('<footer>', start_idx)
        end_idx_script = html.find('<script', start_idx)
        
        possible_ends = [i for i in [end_idx_main, end_idx_footer, end_idx_script] if i != -1]
        if not possible_ends:
            print(f"Could not find end of seo-section in {filename}")
            continue
            
        end_idx = min(possible_ends)
        
        new_html = html[:start_idx] + content + '\n\n' + html[end_idx:]
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Successfully injected content into {filename}")

if __name__ == "__main__":
    inject_content()
