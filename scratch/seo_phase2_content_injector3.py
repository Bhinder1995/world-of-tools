import os

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

content_map = {
    "sip-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is a SIP Calculator?</h2>
    <p>The <strong>SIP (Systematic Investment Plan) Calculator</strong> by WorldOfTools is a free, instant financial utility designed to help Indian investors forecast the future value of their mutual fund investments. By leveraging the power of compounding, SIPs allow you to invest a fixed amount regularly (monthly), making it one of the most effective strategies for long-term wealth creation.</p>
    <p>Whether you are planning for retirement, saving for your child's education, or building a corpus to buy a house, our calculator instantly projects your expected returns. By simply entering your monthly investment amount, the expected annual return rate, and the investment tenure, the tool generates a clear breakdown of your total invested amount versus your wealth gained, complete with an interactive visual pie chart.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How Does the SIP Calculator Work?</h2>
    <p>The calculator uses the standard compound interest formula customized for periodic monthly investments. The mathematical formula running behind the scenes is:</p>
    <div style="background:#f9f9ff;border:2px solid #000;border-radius:12px;padding:1.25rem;font-family:monospace;font-size:1rem;font-weight:700;margin-bottom:1rem;box-shadow:3px 3px 0 #000;text-align:center;">
      M = P × ({[1 + i]^n - 1} / i) × (1 + i)
    </div>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>M:</strong> Maturity Amount (The final future value)</li>
      <li><strong>P:</strong> Monthly Investment Amount</li>
      <li><strong>i:</strong> Periodic Rate of Interest (Annual Rate / 12 / 100)</li>
      <li><strong>n:</strong> Total number of monthly installments (Years × 12)</li>
    </ul>
    <p>Calculating this manually is tedious and prone to errors. Our tool instantly computes the exact maturity value in milliseconds, updating dynamically as you adjust the sliders.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Why Invest via SIP? (The Power of Compounding)</h2>
    <div class="step-item"><div class="step-num">₹</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Rupee Cost Averaging:</strong> By investing a fixed amount every month regardless of market highs and lows, you automatically buy more units when the market is down and fewer when the market is up, reducing overall volatility risk.</p></div>
    <div class="step-item"><div class="step-num">📈</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Power of Compounding:</strong> When you reinvest the returns you earn, those returns start generating their own returns. The longer you stay invested (e.g., 15-20 years), the more exponential your wealth growth becomes.</p></div>
    <div class="step-item"><div class="step-num"> дисциплина</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Financial Discipline:</strong> SIPs force you to save before you spend. An automated monthly deduction ensures you don't try to "time the market," which often leads to missed opportunities.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Is the final amount shown guaranteed?</summary><p>No. Mutual funds are subject to market risks. The expected return rate you enter (e.g., 12% or 15%) is an estimation based on historical equity market performance. The actual maturity amount may be higher or lower depending on future market conditions.</p></details>
    <details><summary>What is a realistic expected return rate?</summary><p>Historically, large-cap Indian equity mutual funds have delivered around 10-12% annualized returns, while mid-cap and small-cap funds have occasionally delivered 14-18% over the long term (10+ years). Debt funds generally yield 6-8%. Always consult a financial advisor.</p></details>
    <details><summary>Can I stop or pause my SIP anytime?</summary><p>Yes, one of the biggest advantages of a standard SIP is flexibility. You can pause, stop, or increase your SIP amount at any time without any penalties from the AMC (Asset Management Company).</p></details>
    <details><summary>Does this calculator account for inflation or taxes?</summary><p>No. The maturity amount shown is the absolute nominal value. You will need to account for Long Term Capital Gains (LTCG) tax upon redemption, and consider that inflation will reduce the purchasing power of the final corpus.</p></details>
    <details><summary>Is my data secure?</summary><p>Yes. All calculations happen entirely in your web browser. We do not store your investment amounts, financial goals, or personal data on any server.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Essential Financial Calculators</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Calculate loan repayments</div></a>
      <a class="tool-card-mini" href="/ppf-calculator"><div class="icon">💰</div><div class="name">PPF Calculator</div><div class="desc">Tax-free investment returns</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
      <a class="tool-card-mini" href="/age-calculator"><div class="icon">🎂</div><div class="name">Age Calculator</div><div class="desc">Exact chronological age</div></a>
    </div>
  </section>

</div>""",

    "cgpa-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the CGPA Calculator?</h2>
    <p>The <strong>CGPA Calculator</strong> by WorldOfTools is a free academic utility designed specifically for university and college students. Whether you are studying under the Choice Based Credit System (CBCS) in India, or attending an international university that uses a standard GPA scale, this tool helps you track your academic performance accurately.</p>
    <p>Instead of manually calculating complex weighted averages, you simply enter your subject credits and grades (or grade points). The tool instantly calculates your <strong>SGPA (Semester Grade Point Average)</strong> for individual semesters and aggregates them to find your overall <strong>CGPA (Cumulative Grade Point Average)</strong>. It also provides a quick conversion to a standard percentage, which is often required for job placements and higher education applications.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Calculate CGPA & SGPA</h2>
    <p>The calculation is based on a weighted average system, where subjects with more credits carry more weight in your final score:</p>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Calculate SGPA (Semester Average):</strong> Multiply the Grade Points earned in each subject by the Credits assigned to that subject. Sum these up for all subjects, and divide by the Total Credits for that semester. <br><br><em>SGPA = Σ (Credits × Grade Points) / Σ Credits</em></p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Calculate CGPA (Cumulative Average):</strong> To find your overall CGPA, you don't just average your SGPAs. You must calculate the weighted average across all semesters. <br><br><em>CGPA = Σ (Semester Credits × SGPA) / Total Credits Across All Semesters</em></p></div>
    <p>Our calculator automates this entire process. You can add multiple subjects for a single semester, and add multiple semesters to see your overarching CGPA grow dynamically.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Convert CGPA to Percentage (Indian Universities)</h2>
    <p>Many Indian employers and foreign universities require your CGPA to be converted into a standard percentage out of 100%. While specific universities (like Mumbai University, VTU, or Anna University) may have their own exact formulas, the most widely accepted standard (often used by CBSE and AICTE) is:</p>
    <div style="background:#f9f9ff;border:2px solid #000;border-radius:12px;padding:1.25rem;font-family:monospace;font-size:1.1rem;font-weight:700;margin-bottom:1rem;box-shadow:3px 3px 0 #000;text-align:center;">
      Percentage = CGPA × 9.5
    </div>
    <p>For example, if your CGPA is 8.0, your estimated percentage is 8.0 × 9.5 = 76%. Our calculator provides this conversion automatically on the results screen.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Does this work for Engineering (B.Tech) students?</summary><p>Yes! The calculator is perfectly suited for B.Tech, B.Sc, B.Com, and BA students studying under the CBCS system where subjects are assigned varying credits (e.g., 4 credits for core subjects, 1 credit for labs).</p></details>
    <details><summary>What is the difference between SGPA and CGPA?</summary><p>SGPA (Semester Grade Point Average) is your performance for one specific semester. CGPA (Cumulative Grade Point Average) is the overall average of your performance across all completed semesters combined.</p></details>
    <details><summary>Why do some subjects affect my CGPA more than others?</summary><p>Because of <strong>Credits</strong>. A 4-credit mathematics course has four times the impact on your final CGPA than a 1-credit physical education lab. You must perform well in high-credit subjects to maintain a high CGPA.</p></details>
    <details><summary>Is my grade data saved on your servers?</summary><p>No. Your privacy is paramount. All academic data you enter is processed locally in your browser using JavaScript. When you close or refresh the page, the data is permanently erased.</p></details>
  </section>

</div>""",

    "ppf-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is a PPF Calculator?</h2>
    <p>The <strong>PPF (Public Provident Fund) Calculator</strong> by WorldOfTools is a free financial utility designed for Indian citizens to project the maturity value of their PPF investments. The Public Provident Fund is one of India's most popular long-term savings schemes, backed by the Government of India, offering guaranteed returns and immense tax benefits under the EEE (Exempt-Exempt-Exempt) category.</p>
    <p>By entering your annual investment amount (up to the maximum limit of ₹1.5 Lakhs), our calculator instantly computes the total interest earned over the mandatory 15-year lock-in period, and displays the exact tax-free maturity corpus you will receive. The tool features an interactive visual pie chart to clearly illustrate the power of compounding on your government-backed savings.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Understanding the PPF Scheme (Rules & Benefits)</h2>
    <p>Before investing, it is crucial to understand the rules governing the Public Provident Fund:</p>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Lock-in Period:</strong> A standard PPF account has a mandatory maturity period of 15 years. After maturity, you can extend the account in blocks of 5 years indefinitely.</li>
      <li><strong>Investment Limits:</strong> You must invest a minimum of ₹500 per financial year to keep the account active. The maximum amount eligible for tax deduction is ₹1,50,000 per financial year.</li>
      <li><strong>Interest Calculation:</strong> Interest is compounded annually but calculated monthly. The crucial rule is that interest is calculated on the minimum balance between the 5th day and the end of the month. To maximize returns, always deposit your money before the 5th of the month!</li>
      <li><strong>Tax Benefits (EEE):</strong> PPF falls under the Exempt-Exempt-Exempt tax status. The money you invest is tax-deductible under Section 80C, the interest earned is tax-free, and the final maturity amount is completely tax-free.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Can I withdraw money before 15 years?</summary><p>Partial withdrawals are permitted from the 7th financial year onwards, subject to specific conditions (e.g., medical emergencies, higher education). You can also avail a loan against your PPF balance between the 3rd and 6th financial year.</p></details>
    <details><summary>Does the interest rate change?</summary><p>Yes. The Government of India (Ministry of Finance) reviews and announces the PPF interest rate every quarter. Historically, it has hovered around 7.1%. Our calculator uses the current prevailing rate by default, but allows you to adjust it for future projections.</p></details>
    <details><summary>Is the maturity amount guaranteed?</summary><p>Yes! Because the Public Provident Fund is a sovereign-backed scheme issued by the Government of India, it carries virtually zero risk. The principal and the interest are fully guaranteed, unlike equity-based mutual funds or SIPs.</p></details>
    <details><summary>Should I invest monthly or as a lump sum?</summary><p>To maximize your interest, it is best to invest the full ₹1.5 Lakhs as a lump sum before April 5th of the financial year. If investing monthly, ensure your deposit hits the account before the 5th of every month to earn interest for that specific month.</p></details>
    <details><summary>Is my data secure on this calculator?</summary><p>Absolutely. All financial calculations occur locally within your web browser using JavaScript. No investment figures are ever sent to our servers.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Essential Financial Calculators</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/sip-calculator"><div class="icon">📈</div><div class="name">SIP Calculator</div><div class="desc">Mutual fund returns</div></a>
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Calculate loan repayments</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
    </div>
  </section>

</div>""",

    "json-formatter.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the JSON Formatter & Validator?</h2>
    <p>The <strong>JSON Formatter</strong> by WorldOfTools is a free, lightning-fast developer utility designed to clean, beautify, minify, and validate JavaScript Object Notation (JSON) data. Whether you are debugging an API response, writing configuration files, or analyzing large datasets, unformatted "minified" JSON is virtually impossible for humans to read. Our tool instantly formats it into a clean, hierarchical, color-coded structure.</p>
    <p>Built for developers with privacy in mind, all processing happens locally in your browser. This means you can safely paste proprietary API payloads, sensitive user data, or confidential configuration files without worrying about the data being intercepted or stored on external servers.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Key Features of the JSON Tool</h2>
    <div class="step-item"><div class="step-num">✨</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Beautify / Format:</strong> Convert messy, single-line JSON strings into beautifully indented, highly readable code. Choose between 2-space or 4-space indentation.</p></div>
    <div class="step-item"><div class="step-num">🗜️</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Minify / Compress:</strong> Strip out all unnecessary whitespace, newlines, and indentation to compress the payload size. Essential before sending JSON data over a network or saving it to a database.</p></div>
    <div class="step-item"><div class="step-num">✅</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Strict Validation:</strong> Instantly check if your JSON syntax is valid. If there is a missing comma, unquoted key, or trailing bracket, the tool provides a descriptive error message indicating exactly where the parsing failed.</p></div>
    <div class="step-item"><div class="step-num">🎨</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Syntax Highlighting:</strong> Visual cues make debugging easier. Keys, strings, numbers, booleans, and null values are color-coded, allowing you to visually scan massive JSON objects in seconds.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Why is my JSON invalid?</summary><p>Common reasons for invalid JSON include: using single quotes (') instead of double quotes (") for keys and strings, leaving a trailing comma after the last item in an array or object, or forgetting to enclose keys in double quotes.</p></details>
    <details><summary>Is there a file size limit?</summary><p>Because the formatting is handled by your browser's local memory (RAM), there is no hard server limit. However, attempting to format multi-gigabyte JSON files may cause your browser tab to freeze. It comfortably handles payloads up to several megabytes instantly.</p></details>
    <details><summary>Can I convert JSON to XML or CSV?</summary><p>Currently, this specific tool focuses on validating, formatting, and minifying JSON. We are working on adding dedicated converter tools for JSON-to-CSV and JSON-to-XML in the near future.</p></details>
    <details><summary>Is it safe to paste production API keys or tokens here?</summary><p>Yes. We use standard HTML5 local processing (JavaScript `JSON.parse` and `JSON.stringify`). We do not send your clipboard data or entered text to any backend server. However, as a general security best practice, you should always obfuscate live API keys when pasting into any browser-based tool.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Developer Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/base64-encoder-decoder"><div class="icon">🔒</div><div class="name">Base64 Tool</div><div class="desc">Encode/Decode data</div></a>
      <a class="tool-card-mini" href="/url-encoder-decoder"><div class="icon">🔗</div><div class="name">URL Encoder</div><div class="desc">Format web links safely</div></a>
      <a class="tool-card-mini" href="/jwt-decoder"><div class="icon">🔑</div><div class="name">JWT Decoder</div><div class="desc">Inspect JSON Web Tokens</div></a>
      <a class="tool-card-mini" href="/qr-code-generator"><div class="icon">📱</div><div class="name">QR Generator</div><div class="desc">Create API QRs</div></a>
      <a class="tool-card-mini" href="/password-generator"><div class="icon">🛡️</div><div class="name">Password Gen</div><div class="desc">Secure random hashes</div></a>
    </div>
  </section>

</div>""",

    "scientific-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Scientific Calculator?</h2>
    <p>The <strong>Scientific Calculator</strong> by WorldOfTools is a highly advanced, free online mathematical utility designed for students, engineers, scientists, and professionals. Going far beyond basic arithmetic, this tool handles complex mathematical operations including trigonometry, logarithms, exponential functions, and root calculations, all within a clean, desktop-and-mobile-friendly interface.</p>
    <p>Built with precision in mind, it executes calculations instantly in your browser without requiring a page reload. Whether you are solving physics equations, calculating engineering stress loads, or simply verifying your high school calculus homework, this tool provides laboratory-grade accuracy up to 15 decimal places.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Key Functions & Capabilities</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Trigonometry:</strong> Calculate Sine (sin), Cosine (cos), and Tangent (tan) instantly. The calculator operates in Radians by default, ensuring compatibility with standard higher-math formulas.</li>
      <li><strong>Logarithms & Exponents:</strong> Effortlessly compute Natural Logs (ln), Base-10 Logs (log), powers (x^y), squares (x²), and the mathematical constant 'e' (Euler's number).</li>
      <li><strong>Roots & Constants:</strong> Access square roots (√), Pi (π ≈ 3.14159), and factorial operations (!) for probability and statistics.</li>
      <li><strong>Memory Functions:</strong> Use parentheses ( ) to enforce strict order of operations (BODMAS/PEMDAS) for complex, multi-step equations.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Are trigonometric functions calculated in Degrees or Radians?</summary><p>By default, standard scientific functions like sin(), cos(), and tan() in this calculator operate using Radians, which is the standard for JavaScript and advanced calculus. If you need degrees, you must convert the value manually (Degrees × π / 180).</p></details>
    <details><summary>What is the order of operations?</summary><p>The calculator strictly adheres to the standard BODMAS / PEMDAS rules. It will evaluate Parentheses first, then Exponents (Orders/Roots), followed by Multiplication and Division, and finally Addition and Subtraction.</p></details>
    <details><summary>Is there a limit to how large a number can be calculated?</summary><p>The calculator uses standard double-precision 64-bit floating-point format (IEEE 754). It is highly accurate up to 15-17 significant decimal digits. Extremely large factorials or exponents exceeding browser memory limits will return "Infinity".</p></details>
    <details><summary>Is this calculator free to use?</summary><p>Yes, 100% free with no intrusive popup ads, no registration required, and no limits on the number of calculations you can perform.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Useful Free Calculators</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
      <a class="tool-card-mini" href="/cgpa-calculator"><div class="icon">🎓</div><div class="name">CGPA Calculator</div><div class="desc">Convert SGPA/CGPA</div></a>
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Calculate loan EMIs</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST</div></a>
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
