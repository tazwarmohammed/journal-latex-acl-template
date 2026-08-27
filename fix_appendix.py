import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# Add packages
if r'\usepackage{cuted}' not in content:
    content = content.replace(r'\usepackage{stfloats}', r'\usepackage{stfloats}' + '\n' + r'\usepackage{cuted}' + '\n' + r'\usepackage{caption}')

# Extract table 5
tab5_pattern = re.compile(r'\\begin\{table\*\}\[b\].*?\\label\{tab:ablation_metrics\}\s*\\end\{table\*\}', re.DOTALL)
match_tab5 = tab5_pattern.search(content)
if match_tab5:
    tab5_str = match_tab5.group(0)
    content = content[:match_tab5.start()] + content[match_tab5.end():]
else:
    tab5_str = ""
    print("Could not find table 5")

# Extract figure 6
fig6_pattern = re.compile(r'\\begin\{figure\*\}\[b\].*?\\label\{fig:ablation_bar_chart\}\s*\\end\{figure\*\}', re.DOTALL)
match_fig6 = fig6_pattern.search(content)
if match_fig6:
    fig6_str = match_fig6.group(0)
    content = content[:match_fig6.start()] + content[match_fig6.end():]
else:
    fig6_str = ""
    print("Could not find figure 6")

# Reformat them into a strip block
if tab5_str and fig6_str:
    # Modify Table 5
    tab5_str = tab5_str.replace(r'\begin{table*}[b]', '')
    tab5_str = tab5_str.replace(r'\end{table*}', '')
    tab5_str = re.sub(r'\\caption\{(.*?)\}', r'\\captionof{table}{\1}', tab5_str, flags=re.DOTALL)
    
    # Modify Figure 6
    fig6_str = fig6_str.replace(r'\begin{figure*}[b]', '')
    fig6_str = fig6_str.replace(r'\end{figure*}', '')
    fig6_str = re.sub(r'\\caption\{(.*?)\}', r'\\captionof{figure}{\1}', fig6_str, flags=re.DOTALL)
    
    strip_block = r'\begin{strip}' + '\n' + tab5_str + '\n' + r'\vspace{2em}' + '\n' + fig6_str + '\n' + r'\end{strip}' + '\n'
    
    # Insert right before \end{document}
    content = content.replace(r'\end{document}', strip_block + r'\end{document}')

with open('acl_latex.tex', 'w') as f:
    f.write(content)

print("Applied strip formatting.")
