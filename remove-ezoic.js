const fs = require('fs');
const path = require('path');

const dir = 'c:\\Users\\HP\\Desktop\\Projects Folder\\world_of_tools';

function removeEzoic(filePath) {
    let content = fs.readFileSync(filePath, 'utf8');
    
    // We want to remove lines containing ezoic or gatekeeper references
    const lines = content.split('\n');
    const newLines = lines.filter(line => {
        if (line.includes('cmp.gatekeeperconsent.com')) return false;
        if (line.includes('the.gatekeeperconsent.com')) return false;
        if (line.includes('ezojs.com/ezoic')) return false;
        if (line.includes('ezstandalone')) return false;
        if (line.includes('ezoicanalytics.com')) return false;
        if (line.includes('<!-- Ezoic CMP and Header Scripts -->')) return false;
        if (line.includes('<!-- End Ezoic Scripts -->')) return false;
        return true;
    });

    const newContent = newLines.join('\n');
    if (content !== newContent) {
        fs.writeFileSync(filePath, newContent, 'utf8');
        console.log('Removed Ezoic from: ' + path.basename(filePath));
    }
}

function walkDir(currentPath) {
    const files = fs.readdirSync(currentPath);
    for (const file of files) {
        const fullPath = path.join(currentPath, file);
        const stat = fs.statSync(fullPath);
        if (stat.isDirectory()) {
            if (file !== 'node_modules' && file !== '.git' && file !== 'tmp_report') {
                walkDir(fullPath);
            }
        } else if (file.endsWith('.html')) {
            removeEzoic(fullPath);
        }
    }
}

walkDir(dir);
console.log('Done scanning for Ezoic.');
