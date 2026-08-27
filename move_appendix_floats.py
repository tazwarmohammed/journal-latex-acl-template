import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

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

# Insert them before \end{document}
insertion = ""
if table5: insertion += table5 + "\n\n"
if fig6: insertion += fig6 + "\n\n"

# Remove double newlines
content = re.sub(r'\n{3,}', '\n\n', content)

content = content.replace('\\end{document}', insertion + '\\end{document}')

with open('acl_latex.tex', 'w') as f:
    f.write(content)

print("Done")
