import re

with open('acl_latex.tex', 'r') as f:
    content = f.read()

# Remove the current single-column floats
# First find Table 5
tab_pattern = re.compile(r'\\begin\{table\}\[htbp\].*?\\label\{tab:ablation_metrics\}\s*\\end\{table\}', re.DOTALL)
match_tab = tab_pattern.search(content)
if match_tab:
    content = content[:match_tab.start()] + content[match_tab.end():]

# Find Figure 6
fig_pattern = re.compile(r'\\begin\{figure\}\[htbp\].*?\\label\{fig:ablation_bar_chart\}\s*\\end\{figure\}', re.DOTALL)
match_fig = fig_pattern.search(content)
if match_fig:
    content = content[:match_fig.start()] + content[match_fig.end():]

# Now insert the double-column version right before the last subsection
insertion = r"""
\begin{table*}[b]
\centering
\resizebox{0.9\textwidth}{!}{%
\begin{tabular}{@{}lcccc@{}}
\toprule
\textbf{Configuration} & \textbf{Mel Loss} & \textbf{STFT Loss} & \textbf{JEPA Loss} & \textbf{VISReg Loss} \\ \midrule
\textbf{Baseline (12.5 Hz)} & 1.541 & 9.927 & 0.0088 & 0.0248 \\
No Decoder Corruption & \textbf{1.034} & \textbf{8.234} & 0.0086 & 0.0243 \\
25 Hz Bottleneck & 1.338 & 9.204 & \textbf{0.0082} & 0.0143 \\
No Multi-Head (MHC) & 1.557 & 9.933 & 0.0089 & 0.0247 \\
Representation Only & 5.084 & 25.918 & 0.0122 & \textbf{0.0085} \\ \bottomrule
\end{tabular}%
}
\caption{Training metrics at 25,000 steps across various ablation configurations. The baseline utilizes a 12.5 Hz bottleneck, decoder corruption, and a hybrid reconstruction-representation objective.}
\label{tab:ablation_metrics}
\end{table*}

\begin{figure*}[b]
\centering
\resizebox{0.75\textwidth}{!}{%
\begin{tikzpicture}
\begin{axis}[
    ybar,
    bar width=20pt,
    width=14cm,
    height=8cm,
    enlarge x limits=0.15,
    legend style={at={(0.5,1.15)}, anchor=north,legend columns=-1},
    ylabel={Mel Reconstruction Loss},
    symbolic x coords={Baseline, No Corrupt, 25 Hz, No MHC, Repr Only},
    xtick=data,
    nodes near coords,
    nodes near coords align={vertical},
    x tick label style={rotate=20,anchor=east},
    ymin=0, ymax=6,
    grid=major,
]
\addplot[fill=blue!40, draw=black] coordinates {(Baseline, 1.541) (No Corrupt, 1.034) (25 Hz, 1.338) (No MHC, 1.557) (Repr Only, 5.084)};
\end{axis}
\end{tikzpicture}%
}
\caption{Visual comparison of the Mel-spectrogram Reconstruction Loss at 25,000 steps. Disabling reconstruction grounding (Repr Only) results in catastrophic acoustic loss, while removing decoder corruption (No Corrupt) artificially depresses the loss at the risk of overfitting.}
\label{fig:ablation_bar_chart}
\end{figure*}
"""

# Insert right before \subsection{Effect of the Multi-Head Codebook (MHC)}
target = r'\subsection{Effect of the Multi-Head Codebook (MHC)}'
idx = content.find(target)
if idx != -1:
    content = content[:idx] + insertion + '\n' + content[idx:]

# Clean up empty lines
content = re.sub(r'\n{3,}', '\n\n', content)

with open('acl_latex.tex', 'w') as f:
    f.write(content)

print("Restored double-column floats at the end.")
