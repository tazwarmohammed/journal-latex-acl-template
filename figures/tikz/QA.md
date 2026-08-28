# TikZ figure QA

## CLAE architecture v01

- semantic_status: rejected after manual inspection; connector routing encoded the wrong relationship
- complexity_review: reject
- mode: research
- communication_job: distinguish the shared encoder path, the loss-only projector branch, reconstruction from `z`, and evaluation from `z`
- caption_text: Implemented training and evaluation paths. Two global and four full-length local views share the frontend, encoder, and projector. Representation objectives act on per-frame projector outputs `p`; decoder corruption, waveform reconstruction, and frozen-feature probes consume encoder latents `z`.
- render_version: `clae_architecture_v01.png`

First-render critique: reject. The reconstruction connector visually passed through the probe node, and the representation branch encoded consistency followed by VISReg rather than parallel objectives.

## CLAE architecture v02

- semantic_status: pass after safety check, compilation, and manual PNG inspection. The shared path is explicit; `z` independently feeds the projector, decoder-corruption, and probe paths; view consistency and VISReg are parallel objectives on `p`; the clean waveform is only the reconstruction target. No EMA, target encoder, predictor, pooled VISReg, or FastConformer equivalence appears.
- complexity_review: keep
- mode: research
- communication_job: distinguish the shared encoder path, parallel loss-only projector objectives, reconstruction from `z`, and evaluation from `z`
- caption_text: Implemented training and evaluation paths. Two global and four full-length local views share the frontend, encoder, and projector. Parallel representation objectives act on per-frame projector outputs `p`; decoder corruption, waveform reconstruction, and frozen-feature probes consume encoder latents `z`.
- render_version: `clae_architecture_v02.png`
- final_pdf_size: 493.32 x 192.46 pt (paper-safe full width)
- automated_visual_qa: The checker reports `title_band_collision` because it treats the top-row process nodes as competing title text. This standalone paper figure intentionally has no internal title; manual inspection confirms that the top row is evenly spaced, fully visible, and non-overlapping. No clipping or text overlap is present. This is a detector false positive, not an unresolved layout defect.

## VISReg adaptation v01

- semantic_status: superseded by v02, which reserves safer page-edge whitespace
- complexity_review: keep
- mode: research
- communication_job: show the project-specific population construction and the sequence used for projected Gaussian-quantile matching
- caption_text: Project-specific VISReg adaptation. Projector frames from every view and example are gathered into one distributed population, centered and scaled, projected onto 256 freshly sampled normalized directions, sorted, and matched to standard-normal quantiles.
- render_version: `visreg_adaptation_v01.png`

## VISReg adaptation v02

- semantic_status: pass after safety check, compilation, automated research-mode visual QA, and manual PNG inspection. The figure distinguishes the project-specific distributed population construction from the standard projection, sorting, and Gaussian-quantile matching sequence.
- complexity_review: keep if space permits; omit before compressing the architecture figure
- mode: research
- communication_job: show the project-specific population construction and the sequence used for projected Gaussian-quantile matching
- caption_text: Project-specific VISReg adaptation. Projector frames from every view and example are gathered into one distributed population, centered and scaled, projected onto 256 freshly sampled normalized directions, sorted, and matched to standard-normal quantiles.
- render_version: `visreg_adaptation_v02.png`
- final_pdf_size: 493.07 x 80.72 pt (paper-safe full width)
- automated_visual_qa: pass
