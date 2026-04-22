import os

BASE_DIR = r"c:\Users\HP\Desktop\Projects Folder\world_of_tools"

content_map = {
    "random-number-generator.html": """<!-- SEO CONTENT -->
<div class="seo-section">

  <section style="margin-bottom:3rem;">
    <h2>What is a Random Number Generator?</h2>
    <p>The <strong>Random Number Generator</strong> by WorldOfTools is a high-precision, cryptographically secure utility designed to provide true randomness for developers, researchers, and everyday users. Unlike standard calculators that use predictable math formulas (pseudo-randomness), our tool leverages the <code>window.crypto.getRandomValues()</code> API, which is the same technology used in bank-level security and secure session management.</p>
    <p>Whether you are picking a winner for a lucky draw, generating secure testing data for a web app, playing tabletop RPGs, or simply making a fair decision between friends, our tool ensures that every result is mathematically unbiased and impossible to predict.</p>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>How to Use the Random Number Generator</h2>
    <div class="step-item"><div class="step-num">1</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Set the Range:</strong> Enter your minimum and maximum values (e.g., 1 to 100). The tool supports negative numbers and large integers.</p></div>
    <div class="step-item"><div class="step-num">2</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Choose Quantity:</strong> Decide if you need a single number or a list of multiple random numbers generated at once.</p></div>
    <div class="step-item"><div class="step-num">3</div><p style="margin:0;line-height:1.6;padding-top:0.25rem;"><strong>Allow Duplicates?</strong> Toggle whether the same number can appear more than once in your results (useful for draws where a participant can only win once).</p></div>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Use Cases for Randomness</h2>
    <ul style="line-height:1.7;color:#444;margin-bottom:1rem;padding-left:1.5rem;">
      <li><strong>Contests & Raffles:</strong> Conduct fair giveaways for social media or corporate events without any manual bias.</li>
      <li><strong>Development & Testing:</strong> Generate random IDs, port numbers, or mock data for software testing and QA.</li>
      <li><strong>Gaming & Sports:</strong> Use as a digital dice for board games (D&D) or to randomize teams for local sports matches.</li>
      <li><strong>Scientific Sampling:</strong> Select a truly random subset of data from a larger population for statistical research.</li>
    </ul>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Frequently Asked Questions</h2>
    <details><summary>What is the difference between PRNG and TRNG?</summary><p>A Pseudo-Random Number Generator (PRNG) uses a formula to generate a sequence that <em>looks</em> random but will eventually repeat. A True Random Number Generator (TRNG) or Cryptographically Secure PRNG (CSPRNG)—like the one we use—utilizes physical entropy (system noise, timing) to ensure the numbers cannot be predicted even if the algorithm is known.</p></details>
    <details><summary>Is this tool suitable for generating passwords?</summary><p>While the randomness is secure, we recommend using our dedicated <a href="/password-generator">Password Generator</a> for creating logins, as it includes character complexity settings (symbols, caps) specifically designed for security.</p></details>
    <details><summary>Can I generate random numbers from a list of names?</summary><p>Yes! Our tool includes a mode to pick a random item from a list. Just paste your names or items, and it will shuffle and pick one fairly.</p></details>
  </section>

  <section style="margin-bottom:3rem;">
    <h2>Explore More Utility Tools</h2>
    <div class="tools-grid">
      <a class="tool-card-mini" href="/unit-converter"><div class="icon">📏</div><div class="name">Unit Converter</div><div class="desc">Convert metrics</div></a>
      <a class="tool-card-mini" href="/password-generator"><div class="icon">🛡️</div><div class="name">Password Gen</div><div class="desc">Secure pass</div></a>
      <a class="tool-card-mini" href="/qr-code-generator"><div class="icon">📱</div><div class="name">QR Generator</div><div class="desc">Create QR codes</div></a>
      <a class="tool-card-mini" href="/scientific-calculator"><div class="icon">🔬</div><div class="name">Scientific Calc</div><div class="desc">Advanced math</div></a>
      <a class="tool-card-mini" href="/percentage-calculator"><div class="icon">💯</div><div class="name">Percentage Calc</div><div class="desc">Find X% of Y</div></a>
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
            
        # Find where to inject
        # Looking for existing seo-section to replace it
        start_pattern = r'<!-- SEO CONTENT -->.*?</div>'
        # Or look for <div class="seo-section">...</div>
        
        # Simplified replacement: find <div class="seo-section"> and the next </div> that closes it
        # Actually our script previously used <!-- SEO CONTENT --> as a marker
        
        if '<!-- SEO CONTENT -->' in html:
            # Replace the whole block
            new_html = re.sub(r'<!-- SEO CONTENT -->.*?</div>', content, html, flags=re.DOTALL)
        else:
            # Fallback to finding <div class="seo-section">
            new_html = re.sub(r'<div class="seo-section">.*?</div>', content, html, flags=re.DOTALL)

        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(new_html)
        print(f"Successfully updated content in {filename}")

if __name__ == "__main__":
    import re
    inject_content()
