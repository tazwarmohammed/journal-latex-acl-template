import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# Extract Table 3
pattern = re.compile(r'\\begin\{table\*\}\[t\].*?\\label\{tab:architecture_hyperparams\}\s*\\end\{table\*\}', re.DOTALL)
match = pattern.search(content)

if match:
    table_content = match.group(0)
    # Remove from current location
    content = content[:match.start()] + content[match.end():]
    
    # Insert after \subsection{Training Objective}
    insert_target = r'\subsection{Training Objective}'
    idx = content.find(insert_target)
    if idx != -1:
        insert_idx = idx + len(insert_target)
        content = content[:insert_idx] + '\n' + table_content + '\n' + content[insert_idx:]
        
    with open('acl_latex.tex', 'w') as f:
        f.write(content)
    print("Moved Table 3")
else:
    print("Could not find Table 3")
