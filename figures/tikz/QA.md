# TikZ figure QA

## CLAE architecture

- Updated 2026-09-05: four-panel publication redesign; final preview `clae_architecture_v06.png`, editable source `clae_architecture.tex`, vector output `clae_architecture.pdf`.
- complexity_review: keep; research mode.
- math_logic_review: schematic. Waveforms and activation tiles are illustrative; dimensions, layers, rates, loss coefficients, and branch semantics follow the manuscript.
- checked_invariants: six aligned full-length views; shared encoder; parallel losses on p; first-global z reconstruction; clean x target; frozen probes on z. No target encoder or quantizer is implied.
- verification: native XeLaTeX compilation passed without font warnings; Poppler PNG render inspected; full manuscript compiled with pdfLaTeX and Figure 1 inspected on page 3 at manuscript width. No visible text overlap or clipping.
- check exception: bundled Python safety and automated visual-check scripts were not run because repository instructions require prior permission for Python scripts. Native compilation and manual source and rendered inspection were used instead. The existing clae_architecture-visual-qa.json belongs to the previous design and does not validate this revision.

## VISReg adaptation

- semantic_status: pass after safety check, compilation, automated research-mode visual QA, and manual PNG inspection. The figure distinguishes the project-specific distributed population construction from the standard projection, sorting, and Gaussian-quantile matching sequence.
- complexity_review: keep if space permits; omit before compressing the architecture figure
- mode: research
- communication_job: show the project-specific population construction and the sequence used for projected Gaussian-quantile matching
- caption_text: Project-specific VISReg adaptation. Projector frames from every view and example are gathered into one distributed population, centered and scaled, projected onto 256 freshly sampled normalized directions, sorted, and matched to standard-normal quantiles.
- render_version: `visreg_adaptation.png`
- final_pdf_size: 493.07 x 80.72 pt (paper-safe full width)
- automated_visual_qa: pass
