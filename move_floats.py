import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# Helper function to extract and remove a float
def extract_float(text, begin_tag, end_tag):
    pattern = re.compile(re.escape(begin_tag) + r'.*?' + re.escape(end_tag), re.DOTALL)
    match = pattern.search(text)
    if match:
        float_content = match.group(0)
        # Fix placement specifier to [t] to prevent awkward gaps
        float_content = re.sub(r'\\begin\{(figure|table)\*?\}\[[^\]]+\]', r'\\begin{\1*}[t]' if '*' in begin_tag else r'\\begin{\1}[t]', float_content)
        text = text[:match.start()] + text[match.end():]
        return float_content, text
    return None, text

# Extract floats
table1, content = extract_float(content, r'\begin{table*}[t]', r'\end{table*}') # It's currently [t]
fig2, content = extract_float(content, r'\begin{figure*}[t]', r'\end{figure*}') # It's currently [t]
table2, content = extract_float(content, r'\begin{table}[htbp]', r'\end{table}')
table3, content = extract_float(content, r'\begin{table}[htbp]', r'\end{table}')
fig3, content = extract_float(content, r'\begin{figure*}[htbp]', r'\end{figure*}')

# Now insert them after their respective section headers
def insert_after(text, search_str, insert_str):
    if insert_str is None: return text
    idx = text.find(search_str)
    if idx != -1:
        insert_idx = idx + len(search_str)
        return text[:insert_idx] + '\n' + insert_str + '\n' + text[insert_idx:]
    return text

content = insert_after(content, r'\section{Related Work}', table1)
content = insert_after(content, r'\section{Method}', fig2)
content = insert_after(content, r'\subsection{Dataset}', table2)
content = insert_after(content, r'\subsection{Experimental Setup}', table3)
content = insert_after(content, r'\subsection{Pre-processing and View Augmentation Strategy}', fig3)

# Fix double newlines
content = re.sub(r'\n{3,}', '\n\n', content)

with open('acl_latex.tex', 'w') as f:
    f.write(content)

print("Done")
