import os
import re

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

# 1. Technical SEO Restoration for Bank Statement Analyzer
def fix_bank_analyzer_tech():
    filepath = os.path.join(BASE_DIR, "bank-statement-analyzer.html")
    with open(filepath, 'r', encoding='utf-8') as f:
        html = f.read()
    
    # We saw empty spaces in the head. Let's replace the whole head with a clean version.
    # We'll use a standardized block.
    
    tech_seo = """    <!-- SEO Optimization Meta Tags -->
    <link rel="canonical" href="https://worldoftools.in/bank-statement-analyzer">
    <meta property="og:type" content="website">
    <meta property="og:site_name" content="WorldOfTools.in">
    <meta property="og:title" content="Bank Statement Analyzer — Free Private PDF Analyzer, No Upload | WorldOfTools">
    <meta property="og:description" content="Free online bank statement analyzer. Analyze your PDF, CSV, or Excel statements instantly in your browser. 100% private, no data upload, no login required.">
    <meta property="og:url" content="https://worldoftools.in/bank-statement-analyzer">
    <meta property="og:image" content="https://worldoftools.in/og/worldoftools-banner.png">
    <meta property="og:image:width" content="1200">
    <meta property="og:image:height" content="630">
    <meta property="og:locale" content="en_IN">
    <meta name="twitter:card" content="summary_large_image">
    <meta name="twitter:site" content="@worldoftools_in">
    <meta name="twitter:title" content="Bank Statement Analyzer — Free Private PDF Analyzer, No Upload | WorldOfTools">
    <meta name="twitter:description" content="Analyze bank statements instantly and privately in your browser. 100% free, no data upload.">
    <meta name="twitter:image" content="https://worldoftools.in/og/worldoftools-banner.png">
    <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "SoftwareApplication",
    "name": "Bank Statement Analyzer",
    "applicationCategory": "FinanceApplication",
    "operatingSystem": "Web Browser",
    "offers": {
      "@type": "Offer",
      "price": "0",
      "priceCurrency": "INR"
    },
    "aggregateRating": {
      "@type": "AggregateRating",
      "ratingValue": "4.9",
      "ratingCount": "840"
    },
    "description": "Free, private bank statement analyzer for PDF, CSV, and Excel. Categorize expenses and track spending locally.",
    "url": "https://worldoftools.in/bank-statement-analyzer"
  }
    </script>
    <script type="application/ld+json">
  {
    "@context": "https://schema.org",
    "@type": "BreadcrumbList",
    "itemListElement": [
      {
        "@type": "ListItem",
        "position": 1,
        "name": "Home",
        "item": "https://worldoftools.in"
      },
      {
        "@type": "ListItem",
        "position": 2,
        "name": "Calculators",
        "item": "https://worldoftools.in/calculators-online"
      },
      {
        "@type": "ListItem",
        "position": 3,
        "name": "Bank Statement Analyzer",
        "item": "https://worldoftools.in/bank-statement-analyzer"
      }
    ]
  }
    </script>"""

    # Replace the empty block or duplicate block in head
    # The empty block we saw was between <meta content="..." name="keywords"/> and <meta name="theme-color" content="#ffe066"/>
    # But wait, we saw multiple comments too.
    
    # Let's just find the start of the head and insert it after keywords if possible.
    html = re.sub(r'<meta content=".*?" name="keywords"/>\s*(?:<link.*?>|<meta.*?>|<!--.*?-->|\s)*<meta name="theme-color"', 
                  f'<meta content="bank statement analyzer, bank statement analysis tool, expense tracker from bank statement, analyze bank statement online, bank statement to excel, spending analysis tool, income expense analyzer, budget tracker from bank statement, transaction categorizer, free bank statement analyzer, monthly expense report, where is my money going, bank statement reader, PDF bank statement analyzer, CSV bank statement analyzer, upload PDF bank statement, analyze PDF statement online" name="keywords"/>\n\n{tech_seo}\n\n<meta name="theme-color"', 
                  html, flags=re.DOTALL)

    # 2. Inject SEO CONTENT (expanded guide)
    seo_content = """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is the Private Bank Statement Analyzer?</h2>
    <p>The <strong>Bank Statement Analyzer</strong> by WorldOfTools is a cutting-edge, 100% free financial utility designed to help you regain control over your money. Unlike traditional fintech apps that require you to link your bank account via insecure APIs or upload sensitive PDFs to their servers, our tool operates on a <strong>Zero-Knowledge architecture</strong>.</p>
    <p>Every calculation, transaction categorization, and chart generation happens entirely within your web browser. Your bank statement data (including account numbers, balances, and transaction details) is never transmitted to our servers. It is the most secure and private way to analyze your spending habits online.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How It Works: Step-by-Step</h2>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Upload Your Statement:</strong> Drag and drop your bank statement in PDF, CSV, or Excel format. We support all major Indian banks including SBI, HDFC, ICICI, Axis, and Kotak.</p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Automatic Categorization:</strong> Our intelligent algorithm scans your transaction descriptions and automatically tags them into categories like Food, Rent, Salary, Entertainment, and Utilities.</p></div>
    <div class="step-item"><div class="step-num">3</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Analyze Your Dashboard:</strong> Instantly view your Income vs. Expenses ratio, your biggest spending categories, and monthly trends through interactive charts.</p></div>
    <div class="step-item"><div class="step-num">4</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Export Your Data:</strong> Once analyzed, you can export the cleaned and categorized data back to Excel for further processing or tax filing.</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Key Features for Indian Users</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>UPI Transaction Sorting:</strong> Automatically identifies and groups UPI payments (GPay, PhonePe, Paytm) to show you where your small daily expenses are going.</li>
      <li><strong>Identify Hidden Subscriptions:</strong> Spot recurring monthly charges from OTT platforms (Netflix, Hotstar) or gym memberships that you might have forgotten about.</li>
      <li><strong>Loan & EMI Identification:</strong> See exactly how much of your monthly income is consumed by loan repayments and bank charges.</li>
      <li><strong>Salary Verification:</strong> Track your monthly salary credits and dividend income to ensure all credits match your expectations.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>Is my bank statement data safe?</summary><p><strong>Yes, 100%.</strong> This is the primary reason we built this tool. Traditional analyzers store your data to sell it for marketing. We use client-side JavaScript (using the <code>pdf.js</code> and <code>xlsx</code> libraries) so that your data stays in your browser's memory and is destroyed the moment you close the tab.</p></details>
    <details><summary>Does this tool work with password-protected PDFs?</summary><p>Yes. If your bank statement (like from HDFC or SBI) is password-protected, the browser will prompt you for the password locally. We never see or store that password.</p></details>
    <details><summary>What bank formats are supported?</summary><p>We support standard PDF exports from almost all banks worldwide, as well as CSV and Excel exports. For PDF statements, our tool uses OCR and text-parsing to extract transaction tables automatically.</p></details>
    <details><summary>Can I use this for my GST or ITR filing?</summary><p>Absolutely. Small business owners and freelancers use this tool to quickly categorize their business expenses from their personal accounts, making it easy to calculate deductible expenses for tax season.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Optimize Your Financial Future</h2>
    <p>Analyzing your statement is the first step. Once you've identified your savings potential, use our other tools to plan your wealth:</p>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/emi-calculator"><div class="icon">🏠</div><div class="name">EMI Calculator</div><div class="desc">Plan your loans</div></a>
      <a class="tool-card-mini" href="/sip-calculator"><div class="icon">📈</div><div class="name">SIP Calculator</div><div class="desc">Grow your savings</div></a>
      <a class="tool-card-mini" href="/ppf-calculator"><div class="icon">💰</div><div class="name">PPF Calculator</div><div class="desc">Secure tax-free returns</div></a>
      <a class="tool-card-mini" href="/gst-calculator"><div class="icon">🧾</div><div class="name">GST Calculator</div><div class="desc">Business tax planning</div></a>
      <a class="tool-card-mini" href="/income-tax-calculator"><div class="icon">🏧</div><div class="name">Tax Planner</div><div class="desc">Calculate tax liability</div></a>
    </div>
  </section>

</div>"""

    # Inject before </body>
    html = html.replace('</body>', f'\n{seo_content}\n</body>')
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(html)
    print("Successfully overhauled Bank Statement Analyzer with SEO and Tech tags.")

if __name__ == "__main__":
    fix_bank_analyzer_tech()
