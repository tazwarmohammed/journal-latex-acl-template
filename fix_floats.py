import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# 1. Add stfloats package
if r'\usepackage{stfloats}' not in content:
    content = content.replace(r'\usepackage[nolist]{acronym}', r'\usepackage[nolist]{acronym}' + '\n' + r'\usepackage{stfloats}')

# 2. Table 3 (architecture_hyperparams)
def fix_table(text, label, new_width):
    # Find the table containing the label
    pattern = re.compile(r'\\begin\{table\}\[htbp\].*?' + re.escape(label) + r'.*?\\end\{table\}', re.DOTALL)
    match = pattern.search(text)
    if match:
        table_content = match.group(0)
        table_content = table_content.replace(r'\begin{table}[htbp]', r'\begin{table*}[t]')
        table_content = table_content.replace(r'\end{table}', r'\end{table*}')
        table_content = table_content.replace(r'\resizebox{\columnwidth}', f'\\resizebox{{{new_width}}}')
        return text[:match.start()] + table_content + text[match.end():]
    return text

content = fix_table(content, r'\label{tab:architecture_hyperparams}', r'0.8\textwidth')
# 3. Table 4 (downstream_benchmark)
content = fix_table(content, r'\label{tab:downstream_benchmark}', r'0.8\textwidth')


# 4. Move Table 5 and Figure 6 to the top of the appendix and change to [b]
def extract_float(text, begin_tag, end_tag):
    pattern = re.compile(re.escape(begin_tag) + r'.*?' + re.escape(end_tag), re.DOTALL)
    match = pattern.search(text)
    if match:
        float_content = match.group(0)
        text = text[:match.start()] + text[match.end():]
        return float_content, text
    return None, text

table5, content = extract_float(content, r'\begin{table*}[h]', r'\end{table*}')
fig6, content = extract_float(content, r'\begin{figure*}[htbp]', r'\end{figure*}')

if table5:
    table5 = table5.replace(r'\begin{table*}[h]', r'\begin{table*}[b]')
if fig6:
    fig6 = fig6.replace(r'\begin{figure*}[htbp]', r'\begin{figure*}[b]')

# Insert after \subsection{Summary of Ablation Configurations}
insert_target = r'\subsection{Summary of Ablation Configurations}'
if table5 and fig6:
    idx = content.find(insert_target)
    if idx != -1:
        insert_idx = idx + len(insert_target)
        # Put them right after the subsection declaration
        insertion = "\n\n" + table5 + "\n\n" + fig6 + "\n\n"
        content = content[:insert_idx] + insertion + content[insert_idx:]

with open('acl_latex.tex', 'w') as f:
    f.write(content)

print("Done")
