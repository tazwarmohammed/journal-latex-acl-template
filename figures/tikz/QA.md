# TikZ figure QA

## CLAE architecture

- Updated 2026-09-05: four-panel publication redesign; final preview `clae_architecture_v06.png`, editable source `clae_architecture.tex`, vector output `clae_architecture.pdf`.
- complexity_review: keep; research mode.
- math_logic_review: schematic. Waveforms and activation tiles are illustrative; dimensions, layers, rates, loss coefficients, and branch semantics follow the manuscript.
- checked_invariants: six aligned full-length views; shared encoder; parallel losses on p; first-global z reconstruction; clean x target; frozen probes on z. No target encoder or quantizer is implied.
- verification: native XeLaTeX compilation passed without font warnings; Poppler PNG render inspected; full manuscript compiled with pdfLaTeX and Figure 1 inspected on page 3 at manuscript width. No visible text overlap or clipping.
- check exception: bundled Python safety and automated visual-check scripts were not run because repository instructions require prior permission for Python scripts. Native compilation and manual source and rendered inspection were used instead. The existing clae_architecture-visual-qa.json belongs to the previous design and does not validate this revision.

## VISReg adaptation

- Updated 2026-09-05: retained and redrawn in the architecture figure's navy,
  teal, and gold palette with matching typography. Four panels show population
  construction, detached normalization, random projections, and quantile
  matching; the bottom strip gives the three component losses.
- complexity_review: keep; research schematic, with distinct explanatory value
  beyond the architecture overview. Tiles and the direction sketch are not data.
- math_logic_review: compared with `models/visreg.py`; population mean, RMS
  scale plus epsilon, detached divisor, normalized Gaussian directions, sorted
  projections, normal quantiles, and component averaging agree with the code.
- render_version: `visreg_adaptation_editorial.png`; editable source and vector
  PDF retain `visreg_adaptation` as their basename.
- verification: balanced-environment and unsafe-command checks in Node,
  XeLaTeX compilation, Poppler rendering, and manual figure/manuscript inspection.
  Old automated visual-QA files apply to the preceding figure, not this revision.

## Matched training trajectories

- Updated 2026-09-05: retained as Appendix Figure 3. Updated sans-serif labels,
  restrained palette, grid, and step units to match the manuscript figures.
- render_version: `ablation_training_curves_editorial.png`.
- data_integrity: all 24 CSV paths and x/y column mappings match the preceding
  source exactly. No smoothing, additional evaluation, or changed plotted data.
- semantic_review: attempted training steps on x; weighted objectives in (a),
  raw components in (b–d); dashed components have zero objective weight. Total
  objective values cannot rank models trained with different losses.
- verification: Node source checks, two XeLaTeX passes for the shared legend,
  Poppler rendering, and manual standalone/manuscript inspection.
- Python check exception for both figures: repository instructions require
  prior permission for Python scripts. Native compilation and direct source /
  rendered inspection were used instead; no Python, training, or model
  evaluation was run.
