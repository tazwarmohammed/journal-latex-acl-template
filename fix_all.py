import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# 1. Title
content = content.replace(
    r'\title{CLAE: Towards a Foundation Model for Bangla Speech using \acf{JEPA} and \acf{VISReg}}',
    r'\title{CLAE: Towards a Foundation Model for Bangla Speech using JEPA and VISReg}'
)

# 2. Add stfloats
content = content.replace(r'\usepackage[nolist]{acronym}', r'\usepackage[nolist]{acronym}' + '\n' + r'\usepackage{stfloats}')

# Helper functions
def extract_float(text, tag, label):
    # Matches \begin{table}[htbp] ... \label{foo} ... \end{table}
    # Be careful, non-greedy match might fail if there's multiple tables. Better to find the one with the label.
    pattern = re.compile(r'\\begin\{' + tag + r'\}' + r'\[.*?\]' + r'.*?' + re.escape(label) + r'.*?' + r'\\end\{' + tag + r'\}', re.DOTALL)
    match = pattern.search(text)
    if match:
        float_content = match.group(0)
        text = text[:match.start()] + text[match.end():]
        return float_content, text
    return None, text

def insert_after(text, target, insertion):
    if not insertion: return text
    idx = text.find(target)
    if idx != -1:
        insert_idx = idx + len(target)
        return text[:insert_idx] + '\n\n' + insertion + '\n' + text[insert_idx:]
    return text

# Extract all floats we want to modify
tab1, content = extract_float(content, r'table\*', r'\label{tab:related_work}')
fig2, content = extract_float(content, r'figure\*', r'\label{fig:detailed_architecture}')
tab2, content = extract_float(content, r'table', r'\label{tab:dataset_stats}')
tab3, content = extract_float(content, r'table', r'\label{tab:architecture_hyperparams}')
fig3, content = extract_float(content, r'figure\*', r'\label{fig:jepa_views}')
tab4, content = extract_float(content, r'table', r'\label{tab:downstream_benchmark}')
tab5, content = extract_float(content, r'table\*', r'\label{tab:ablation_metrics}')
fig6, content = extract_float(content, r'figure\*', r'\label{fig:ablation_bar_chart}')

# 3. Table 1
if tab1:
    tab1 = re.sub(r'\\begin\{table\*\}\[.*?\]', r'\\begin{table*}[t]', tab1)
    content = insert_after(content, r'\section{Related Work}', tab1)

# 4. Figure 2
if fig2:
    fig2 = re.sub(r'\\begin\{figure\*\}\[.*?\]', r'\\begin{figure*}[t]', fig2)
    content = insert_after(content, r'\section{Method}', fig2)

# 5. Table 2
if tab2:
    tab2 = re.sub(r'\\begin\{table\}\[.*?\]', r'\\begin{table}[t]', tab2)
    content = insert_after(content, r'\subsection{Dataset}', tab2)

# 6. Table 3
if tab3:
    tab3 = re.sub(r'\\begin\{table\}\[.*?\]', r'\\begin{table*}[t]', tab3)
    tab3 = tab3.replace(r'\end{table}', r'\end{table*}')
    tab3 = tab3.replace(r'\resizebox{\columnwidth}', r'\resizebox{0.65\textwidth}')
    content = insert_after(content, r'\subsection{Training Objective}', tab3)

# 7. Figure 3
if fig3:
    fig3 = re.sub(r'\\begin\{figure\*\}\[.*?\]', r'\\begin{figure*}[t]', fig3)
    content = insert_after(content, r'\subsection{Pre-processing and View Augmentation Strategy}', fig3)

# 8. Table 4
if tab4:
    tab4 = re.sub(r'\\begin\{table\}\[.*?\]', r'\\begin{table*}[t]', tab4)
    tab4 = tab4.replace(r'\end{table}', r'\end{table*}')
    tab4 = tab4.replace(r'\resizebox{\columnwidth}', r'\resizebox{0.8\textwidth}')
    content = insert_after(content, r'\subsection{Downstream Benchmarking and Comparative Analysis}', tab4)

# 9. Table 5 & Figure 6
if tab5:
    tab5 = re.sub(r'\\begin\{table\*\}\[.*?\]', r'\\begin{table*}[b]', tab5)
if fig6:
    fig6 = re.sub(r'\\begin\{figure\*\}\[.*?\]', r'\\begin{figure*}[b]', fig6)
if tab5 and fig6:
    combined = tab5 + '\n\n' + fig6
    content = insert_after(content, r'\subsection{Effect of the Multi-Head Codebook (MHC)}', combined)

# Clean up multiple newlines
content = re.sub(r'\n{3,}', '\n\n', content)

with open('acl_latex.tex', 'w') as f:
    f.write(content)

print("Restored and modified document perfectly.")
