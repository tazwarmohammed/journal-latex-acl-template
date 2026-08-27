import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# Extract the strip block
strip_pattern = re.compile(r'\\begin\{strip\}.*?\\end\{strip\}', re.DOTALL)
match = strip_pattern.search(content)

if match:
    strip_text = match.group(0)
    
    # We will manually rebuild the tables as single-column environments
    # First, let's extract the inner parts
    
    # Extract Table 5 tabular part
    tab_inner_pattern = re.compile(r'\\begin\{tabular\}.*?\\end\{tabular\}%', re.DOTALL)
    tab_match = tab_inner_pattern.search(strip_text)
    tab_inner = tab_match.group(0) if tab_match else ""
    
    # Extract Table 5 caption
    tab_cap_pattern = re.compile(r'\\captionof\{table\}\{(.*?)\}', re.DOTALL)
    tab_cap_match = tab_cap_pattern.search(strip_text)
    tab_cap = tab_cap_match.group(1) if tab_cap_match else "Training metrics at 25,000 steps across various ablation configurations. The baseline utilizes a 12.5 Hz bottleneck, decoder corruption, and a hybrid reconstruction-representation objective."
    
    # Extract Figure 6 tikz part
    fig_inner_pattern = re.compile(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}%', re.DOTALL)
    fig_match = fig_inner_pattern.search(strip_text)
    fig_inner = fig_match.group(0) if fig_match else ""
    
    # Extract Figure 6 caption
    fig_cap_pattern = re.compile(r'\\captionof\{figure\}\{(.*?)\}', re.DOTALL)
    fig_cap_match = fig_cap_pattern.search(strip_text)
    fig_cap = fig_cap_match.group(1) if fig_cap_match else "Visual comparison of the Mel-spectrogram Reconstruction Loss at 25,000 steps. Disabling reconstruction grounding (Repr Only) results in catastrophic acoustic loss, while removing decoder corruption (No Corrupt) artificially depresses the loss at the risk of overfitting."
    
    new_tab = f"""\\begin{{table}}[htbp]
\\centering
\\resizebox{{\\columnwidth}}{{!}}{{%
{tab_inner}
}}
\\caption{{{tab_cap}}}
\\label{{tab:ablation_metrics}}
\\end{{table}}"""

    new_fig = f"""\\begin{{figure}}[htbp]
\\centering
\\resizebox{{\\columnwidth}}{{!}}{{%
{fig_inner}
}}
\\caption{{{fig_cap}}}
\\label{{fig:ablation_bar_chart}}
\\end{{figure}}"""

    replacement = new_tab + '\n\n' + new_fig + '\n'
    
    content = content[:match.start()] + replacement + content[match.end():]
    
    with open('acl_latex.tex', 'w') as f:
        f.write(content)
    print("Replaced strip with single-column floats.")
else:
    print("Could not find strip block.")

