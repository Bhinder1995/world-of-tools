import os
import re

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

content_map = {
    "age-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Exact Age Calculator?</h2>
    <p>The <strong>Age Calculator</strong> by WorldOfTools is a premium, 100% free online utility designed to calculate your precise chronological age in years, months, days, hours, and minutes. Built with privacy in mind, our tool processes all data locally within your web browser. Whether you need to verify your age for a government application, check eligibility for school admissions, or calculate the exact duration between two historical dates, this calculator delivers instant, mathematically accurate results.</p>
    <p>Unlike basic calculators, our algorithm accounts for the complexities of the <strong>Gregorian calendar</strong>, including leap years, varying month lengths, and time zone discrepancies. The tool instantly outputs a comprehensive "Life Timeline," complete with a live birthday countdown, astrological zodiac signs, and major life milestones.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Calculate Age for Legal Documents in India</h2>
    <p>In India, strict age verification is mandatory for almost all official, legal, and academic procedures. When applying for government exams (like UPSC, SSC, Banking), the notification typically states an eligibility criteria such as: <em>"Candidate must be between 18 and 25 years of age as of 1st August of the current year."</em></p>
    <p>Using the <strong>Specific Date</strong> feature in our calculator ensures you never make a manual calculation error. Common use cases include:</p>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Aadhar Card & PAN Card:</strong> Verifying age for initial registration or corrections.</li>
      <li><strong>School & College Admissions:</strong> Checking if a child meets the minimum age requirement for Nursery/Class 1 as per the RTE Act criteria.</li>
      <li><strong>Passport Applications:</strong> Determining minor vs. adult status for tatkal processing and document requirements.</li>
      <li><strong>Driving License:</strong> Confirming eligibility for a learner's permit (16 years for gearless, 18 years for geared vehicles).</li>
      <li><strong>Insurance & Banking:</strong> Calculating precise age for life insurance premiums or opening a senior citizen savings account.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>The Science Behind Age Calculation: Leap Years & The Gregorian Calendar</h2>
    <p>Age calculation might seem simple, but doing it accurately to the day requires complex logic based on the <strong>Gregorian Calendar</strong>. A standard year has 365 days, while a leap year has 366 days, occurring every four years (with exceptions for century years not divisible by 400).</p>
    <p>When you enter your date of birth, our tool executes the following formula:</p>
    <div style="background:#f9f9ff;border:2px solid #000;border-radius:12px;padding:1.25rem;font-family:monospace;font-size:0.9rem;margin-bottom:1rem;box-shadow:3px 3px 0 #000;">
      1. Calculate difference in Years: Current Year - Birth Year<br>
      2. Calculate difference in Months: Current Month - Birth Month<br>
      3. Calculate difference in Days: Current Day - Birth Day<br>
      4. Adjust for negative days by borrowing days from the previous month, accounting for the exact number of days in that specific month (28, 29, 30, or 31).<br>
      5. Adjust for negative months by borrowing a year (12 months).
    </div>
    <p>This ensures that if you were born on a leap day (February 29th), your age is still calculated correctly during non-leap years. The tool automatically adjusts to count February 28th or March 1st as the equivalent boundary date, depending on regional calendar rules.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Key Features — Why Use Our Age Calculator?</h2>
    <ul style="list-style:none;padding:0;margin:0;display:flex;flex-direction:column;gap:0.75rem;">
      <li style="display:flex;gap:0.75rem;align-items:flex-start;"><span style="color:#059669;font-weight:900;font-size:1.1rem;flex-shrink:0;">✓</span><span><strong>Exact Age in Years, Months &amp; Days</strong> — Precise chronological age including total days, hours, and minutes you've been alive.</span></li>
      <li style="display:flex;gap:0.75rem;align-items:flex-start;"><span style="color:#059669;font-weight:900;font-size:1.1rem;flex-shrink:0;">✓</span><span><strong>Age Between Any Two Dates</strong> — Calculate age or elapsed time between any start and end date. Great for anniversaries, contracts, and eligibility checks.</span></li>
      <li style="display:flex;gap:0.75rem;align-items:flex-start;"><span style="color:#059669;font-weight:900;font-size:1.1rem;flex-shrink:0;">✓</span><span><strong>Reverse Date of Birth Search</strong> — Know someone's exact age in years and months? Enter it into our "Find DOB" tab to reverse-calculate their birth date.</span></li>
      <li style="display:flex;gap:0.75rem;align-items:flex-start;"><span style="color:#059669;font-weight:900;font-size:1.1rem;flex-shrink:0;">✓</span><span><strong>Real-Time Birthday Countdown</strong> — Find out exactly how many days, hours, minutes, and seconds remain until your next birthday.</span></li>
      <li style="display:flex;gap:0.75rem;align-items:flex-start;"><span style="color:#059669;font-weight:900;font-size:1.1rem;flex-shrink:0;">✓</span><span><strong>Life Milestones &amp; Zodiac Sign</strong> — Know your 10,000th day alive, 25,000th day, next decade birthday, and your Western zodiac sign.</span></li>
      <li style="display:flex;gap:0.75rem;align-items:flex-start;"><span style="color:#059669;font-weight:900;font-size:1.1rem;flex-shrink:0;">✓</span><span><strong>100% Private — Nothing Stored</strong> — All calculations run locally in your browser. Your DOB is never uploaded, tracked, or saved.</span></li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>🆚 Age Calculator vs. Other Online Tools</h2>
    <div style="overflow-x:auto;">
      <table class="compare-table">
        <thead><tr>
          <th>Feature</th>
          <th style="color:#4f46e5;">WorldOfTools</th>
          <th>Other Tools</th>
        </tr></thead>
        <tbody>
          <tr><td>Privacy</td><td class="yes">✓ Browser Only</td><td class="no">Server Upload</td></tr>
          <tr><td>Speed</td><td class="yes">✓ Instant Calculation</td><td class="no">Page Reload Required</td></tr>
          <tr><td>Ads &amp; Popups</td><td class="yes">✓ Zero Intrusive Ads</td><td class="no">Intrusive Popups</td></tr>
          <tr><td>Leap Year Logic</td><td class="yes">✓ Advanced Gregorian</td><td class="no">Basic Approximation</td></tr>
          <tr><td>Birthday Countdown</td><td class="yes">✓ Live Second-by-Second</td><td class="no">Static Days Only</td></tr>
          <tr><td>Life Milestones</td><td class="yes">✓ 10k/25k Day Tracking</td><td class="no">Rarely Available</td></tr>
        </tbody>
      </table>
    </div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>How old am I if I was born in 1990?</summary><p>If born in 1990, you are 36 years old in 2026 (or 35 if your birthday hasn't occurred yet this year). Use this calculator for your exact age with months and days, accounting for leap years.</p></details>
    <details><summary>How do I calculate age from date of birth manually?</summary><p>Subtract your birth year from the current year, then adjust by -1 if your birthday hasn't passed yet this year. For exact months and days, manual calculation is prone to errors due to varying month lengths. It's safer to use this tool, which computes it instantly in your browser.</p></details>
    <details><summary>How many days old am I?</summary><p>Multiply your completed years by 365, add an extra day for each leap year you've lived through, then add the remaining days from your last birthday to today. Or simply enter your DOB above — the tool computes your total days alive instantly.</p></details>
    <details><summary>Can I calculate age between two specific dates?</summary><p>Yes. Use the "Specific Date" tab — enter any start date (as DOB) and any end date to find the exact duration between two dates. This is perfect for calculating contract durations, visa validity periods, and exam eligibility.</p></details>
    <details><summary>Does the calculator handle leap year birthdays (Feb 29)?</summary><p>Yes, absolutely. If you were born on February 29th, the calculator accurately handles your birthday in non-leap years, using the closest valid date according to standard Gregorian calendar conventions.</p></details>
    <details><summary>Is my date of birth stored or shared with anyone?</summary><p>No. Privacy is our top priority. All calculations run entirely locally in your web browser using JavaScript. Your date of birth is never uploaded to any server, never stored in any database, and never shared with anyone.</p></details>
    <details><summary>Can I use this for age verification and legal purposes?</summary><p>Yes. This tool gives a precise mathematical age suitable for filling out forms, age verification, legal documents, Aadhar registration, school admissions, and checking competitive exam eligibility.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Free Tools You Might Need</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/bmi-calculator"><div class="icon">⚖️</div><div class="name">BMI Calculator</div><div class="desc">Check health & fitness stats</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Solve any % problem</div></a>
      <a class="tool-card-mini" href="/word-counter"><div class="icon">📝</div><div class="name">Word Counter</div><div class="desc">Analyze text & reading time</div></a>
      <a class="tool-card-mini" href="/aspect-ratio-calculator"><div class="icon">📐</div><div class="name">Aspect Ratio</div><div class="desc">Maintain image proportions</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST instantly</div></a>
      <a class="tool-card-mini" href="/ip-address-lookup"><div class="icon">🌐</div><div class="name">IP Lookup</div><div class="desc">Find location for any IP</div></a>
    </div>
  </section>

</div>""",

    "percentage-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is a Percentage Calculator?</h2>
    <p>The <strong>Percentage Calculator</strong> by WorldOfTools is a free, comprehensive, and multi-mode online utility that solves any percentage-related problem instantly. From calculating exam scores and shopping discounts to analyzing salary hikes, GST, business margins, and stock market returns — this tool is designed to cover every possible percentage scenario in a single, intuitive interface.</p>
    <p>Our tool integrates six core mathematical formulas: finding the percentage of a number, calculating what percentage one number is of another, determining percentage change (increase or decrease), finding percentage difference, reversing a percentage calculation, and applying discounts. All processing occurs securely within your browser, ensuring lightning-fast results and complete data privacy with no server uploads required.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Calculate Percentages — 6 Modes Explained</h2>
    <p>Mathematics can be complex, but our tool simplifies it into six distinct modes tailored to real-world applications:</p>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>% of Number</strong> — Find out what a specific percentage of a total number is. Example: 20% of 500 = 100. Ideal for calculating tips, specific tax amounts, or finding a portion of a whole.</p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>X is % of Y</strong> — Determine what percentage one number represents compared to another. Example: 30 out of 150 = 20%. Perfect for calculating academic grades, attendance records, or task completion rates.</p></div>
    <div class="step-item"><div class="step-num">3</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>% Change (Increase / Decrease)</strong> — Measure the growth or reduction between two values. Example: A stock goes from 800 to 1000, representing a 25% increase. Essential for salary hikes, inflation, and sales analysis.</p></div>
    <div class="step-item"><div class="step-num">4</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>% Difference</strong> — Compare two independent values symmetrically. Used extensively in scientific experiments, A/B testing, and comparing prices of two different items where neither is a baseline.</p></div>
    <div class="step-item"><div class="step-num">5</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Reverse %</strong> — Work backward to find the original number when you only know a partial value and its corresponding percentage. Example: If 80 is 40% of a number, the original number is 200. Used to reverse-calculate GST or find original pre-tax prices.</p></div>
    <div class="step-item"><div class="step-num">6</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Discount Calculator</strong> — Enter the original price and the discount percentage to instantly get the final sale price and the exact amount you save. Ideal for shopping sales, coupon codes, and e-commerce.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>The Math Behind Percentages: Formulas You Should Know</h2>
    <p>If you need to calculate percentages manually, here are the standard mathematical formulas utilized by our calculator engine:</p>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Basic Percentage:</strong> (P / 100) × Total = Result. (e.g., to find 15% of 200: (15/100) × 200 = 30)</li>
      <li><strong>Finding the Percentage:</strong> (Part / Total) × 100 = Percentage. (e.g., 40 out of 50: (40/50) × 100 = 80%)</li>
      <li><strong>Percentage Change:</strong> ((New Value - Old Value) / |Old Value|) × 100. A positive result indicates an increase, while a negative result indicates a decrease.</li>
      <li><strong>Percentage Difference:</strong> (|Value A - Value B| / ((Value A + Value B) / 2)) × 100. This provides the absolute difference relative to the average of the two numbers.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>How do I calculate 20% of a number quickly?</summary><p>To manually calculate 20% of a number, simply multiply the number by 0.20. For example, 20% of 500 = 500 × 0.20 = 100. Alternatively, divide the number by 5. For instant and error-free results, use the "% of Number" tab in our calculator above.</p></details>
    <details><summary>What is the formula for percentage change?</summary><p>Percentage Change = ((New Value − Old Value) / Old Value) × 100. A positive result means a percentage increase (growth), while a negative result means a percentage decrease (reduction).</p></details>
    <details><summary>How do I calculate a discount percentage while shopping?</summary><p>Discount % = ((Original Price − Sale Price) / Original Price) × 100. For example: If an item was originally ₹1000 and is now on sale for ₹750, the calculation is ((1000 - 750) / 1000) × 100 = 25% off.</p></details>
    <details><summary>How can I reverse calculate GST or tax?</summary><p>If you paid ₹1180 including an 18% GST rate, you can find the original base price by dividing the total amount by (1 + GST rate). So, ₹1180 / 1.18 = ₹1000. Use our Reverse % tab — enter 1180 as the value and 118 (100 + 18) as the "is % of" field.</p></details>
    <details><summary>What is the difference between a percentage and percentage points?</summary><p>Percentage points measure the absolute difference between two percentages (e.g., moving from 5% to 7% is an increase of 2 percentage points). Percentage measures the relative change (moving from 5% to 7% represents a 40% increase). These are fundamentally different mathematical concepts!</p></details>
    <details><summary>How do I calculate my exam percentage or grade?</summary><p>Use the formula: (Marks Obtained ÷ Total Marks) × 100. Example: If you scored 450 out of 500, the calculation is (450 / 500) × 100 = 90%. You can instantly calculate this using the "X is % of Y" tab — just enter your marks as X and the total as Y.</p></details>
    <details><summary>Is this calculator safe for financial calculations?</summary><p>Yes! WorldOfTools never saves, stores, or transmits the numbers you enter. All calculations are executed via local JavaScript in your browser, guaranteeing 100% data privacy for your sensitive financial or business figures.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Free Calculator Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/age-calculator"><div class="icon">🎂</div><div class="name">Age Calculator</div><div class="desc">Exact age in seconds</div></a>
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Calculate home/car loans</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Add or remove GST</div></a>
      <a class="tool-card-mini" href="/random-number-generator"><div class="icon">🎲</div><div class="name">Random Number</div><div class="desc">True random numbers</div></a>
      <a class="tool-card-mini" href="/scientific-calculator"><div class="icon">🔬</div><div class="name">Scientific Calc</div><div class="desc">Advanced math functions</div></a>
      <a class="tool-card-mini" href="/sip-calculator"><div class="icon">📈</div><div class="name">SIP Calculator</div><div class="desc">Mutual fund returns</div></a>
    </div>
  </section>

</div>""",

    "gst-calculator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the GST Calculator India?</h2>
    <p>The <strong>GST Calculator</strong> by WorldOfTools is a free, instant, browser-based financial utility designed to calculate Goods and Services Tax for any price in India. Updated for the 2025-26 fiscal year, it supports all standard Indian GST tax slabs including 0%, 5%, 12%, 18%, and 28%, along with custom percentage inputs.</p>
    <p>Whether you're a business owner generating tax invoices, a freelancer computing service tax, an accountant reconciling books, or a consumer checking if a retail price is properly GST-inclusive — this tool delivers precise results instantly. The calculator provides a complete tax breakdown, automatically splitting the total tax into <strong>CGST (Central GST)</strong> and <strong>SGST (State GST)</strong>, or consolidating it into <strong>IGST (Integrated GST)</strong> for interstate transactions.</p>
    <p>With a strict privacy-first architecture, all mathematical processing happens 100% locally in your web browser. No financial data, invoice amounts, or tax calculations are ever sent to external servers, ensuring absolute confidentiality.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Calculate GST Online — Step by Step</h2>
    <p>Our intuitive interface offers three powerful modes: Add GST, Remove GST, and Bulk Items. Here's how to use them effectively:</p>
    <div class="step-item">
      <div class="step-num">1</div>
      <p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Choose Your Calculation Mode</strong> — Select "Add GST" to calculate the final invoice price from a base amount. Select "Remove GST" to reverse-calculate the base cost and tax amount from an inclusive retail price. Use "Bulk Items" to build a full multi-item invoice.</p>
    </div>
    <div class="step-item">
      <div class="step-num">2</div>
      <p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Enter the Transaction Amount</strong> — Type the price in Indian Rupees (₹). The calculator supports decimal inputs for exact paise accuracy (e.g., 1450.50).</p>
    </div>
    <div class="step-item">
      <div class="step-num">3</div>
      <p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Select the Applicable GST Slab</strong> — Choose the correct government tax slab for your product or service (5%, 12%, 18%, or 28%), or manually enter a custom rate. Toggle the "IGST" switch if the transaction crosses state borders.</p>
    </div>
    <div class="step-item">
      <div class="step-num">4</div>
      <p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Get Instant Tax Breakdown</strong> — Instantly view the Total Amount, the Base Amount, and the exact tax components (CGST & SGST or IGST). You can easily copy or share the results directly to your clipboard or WhatsApp.</p>
    </div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>GST Tax Slabs in India (Updated 2024–25)</h2>
    <p>The Goods and Services Tax council classifies products and services into different tax brackets. Here is a quick reference guide to the current GST structure in India:</p>
    <div style="overflow-x:auto;">
      <table class="compare-table">
        <thead><tr>
          <th>GST Rate</th>
          <th>CGST</th>
          <th>SGST</th>
          <th>IGST</th>
          <th>Example Goods &amp; Services</th>
        </tr></thead>
        <tbody>
          <tr><td><strong>0% (Exempt)</strong></td><td class="yes">0%</td><td class="yes">0%</td><td class="yes">0%</td><td>Fresh vegetables, milk, eggs, unbranded flour, printed books</td></tr>
          <tr><td><strong>5%</strong></td><td class="yes">2.5%</td><td class="yes">2.5%</td><td class="yes">5%</td><td>Edible oils, sugar, tea, coffee, spices, coal, life-saving drugs</td></tr>
          <tr><td><strong>12%</strong></td><td class="yes">6%</td><td class="yes">6%</td><td class="yes">12%</td><td>Butter, cheese, ghee, mobile phones, processed foods, computers</td></tr>
          <tr><td><strong>18%</strong></td><td class="yes">9%</td><td class="yes">9%</td><td class="yes">18%</td><td>Most IT services, software, telecom, financial services, restaurants, electronics</td></tr>
          <tr><td><strong>28%</strong></td><td class="yes">14%</td><td class="yes">14%</td><td class="yes">28%</td><td>Luxury cars, tobacco products, aerated drinks, cement, ACs, casinos</td></tr>
        </tbody>
      </table>
    </div>
    <p style="font-size:0.85rem;color:#666;margin-top:0.75rem;"><em>Note: Tax rates are subject to change based on GST Council meetings. Always verify with official CBIC notifications for specific HSN/SAC codes.</em></p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Understanding CGST, SGST, and IGST</h2>
    <p>India utilizes a dual-GST model. The application of tax depends entirely on the location of the supplier and the place of supply (the buyer's location):</p>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Intra-State Transactions (Within the same state):</strong> When goods or services are sold within the same state (e.g., from Mumbai to Pune), the GST is split equally between the Central and State governments. <strong>CGST (Central GST)</strong> and <strong>SGST (State GST)</strong> are applied. For an 18% slab, 9% is CGST and 9% is SGST.</li>
      <li><strong>Inter-State Transactions (Between two states):</strong> When the transaction crosses state borders (e.g., from Delhi to Bangalore), the Central government collects the entire tax as <strong>IGST (Integrated GST)</strong>. For an 18% slab, the IGST is applied as a flat 18%.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>How do I manually add GST to a base price?</summary><p>To calculate the GST-inclusive price, multiply the base price by (1 + GST%/100). For example, to add 18% GST to ₹1,000: ₹1,000 × 1.18 = ₹1,180. The GST amount is ₹180. Our "Add GST" tab performs this calculation and provides the CGST/SGST split instantly.</p></details>
    <details><summary>How do I remove GST from a total inclusive price?</summary><p>To extract the base price from a GST-inclusive amount, divide the total price by (1 + GST%/100). For example, if you paid ₹1,180 which includes 18% GST, the base price is: ₹1,180 ÷ 1.18 = ₹1,000. Use the "Remove GST" tab to reverse calculate retail prices.</p></details>
    <details><summary>What is the standard GST rate on software and freelance services?</summary><p>Software services (SaaS), IT consulting, freelance digital services, and most professional B2B services attract a standard GST rate of 18% under the SAC (Services Accounting Code) system.</p></details>
    <details><summary>Can I calculate GST for an invoice with multiple items?</summary><p>Yes! WorldOfTools features a dedicated "Bulk Items" tab. You can add multiple line items, each with different prices and varying GST slabs (e.g., one item at 5%, another at 18%). The calculator will compute the individual taxes and provide a grand total for your complete invoice.</p></details>
    <details><summary>Are the calculations rounded off?</summary><p>Yes, as per standard Indian accounting practices, the calculator handles precise decimal inputs and rounds the final tax amounts to two decimal places (paise) for accurate ledger entries and invoicing.</p></details>
    <details><summary>Is my financial data secure when using this calculator?</summary><p>Absolutely. Your privacy is guaranteed. The calculator runs purely on client-side JavaScript. This means your invoice amounts, base prices, and tax data never leave your computer and are never logged on our servers.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Other Free Financial & Utility Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Loan & mortgage EMI</div></a>
      <a class="tool-card-mini" href="/sip-calculator"><div class="icon">📈</div><div class="name">SIP Calculator</div><div class="desc">Mutual fund returns</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Find exact % changes</div></a>
      <a class="tool-card-mini" href="/invoice-generator"><div class="icon">🧾</div><div class="name">Invoice Maker</div><div class="desc">Generate PDF invoices</div></a>
      <a class="tool-card-mini" href="/word-counter"><div class="icon">📝</div><div class="name">Word Counter</div><div class="desc">Analyze text length</div></a>
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
            
        # Find the <div class="seo-section"> ... </div> block at the end of the file
        # We know it starts with <!-- SEO CONTENT --> and ends before <footer>
        
        pattern = re.compile(r'<!-- SEO CONTENT -->\s*<div class="seo-section">.*?</div>\s*</main>', re.DOTALL)
        
        # Check if it matches
        if pattern.search(html):
            new_html = pattern.sub(content + '\n\n</main>', html)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(new_html)
            print(f"Successfully injected content into {filename}")
        else:
            print(f"Could not find SEO section block in {filename}")

if __name__ == "__main__":
    inject_content()
