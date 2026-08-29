# Training-diagnostics figure audit

complexity_review: keep

reason: Four small multiples preserve the distinct W&B record identities for one continuous 210k checkpoint trajectory and make the overlap, resume boundaries, and manual schedule changes visible without stitching or interpolating histories. The figure has one grammar (time-series diagnostics) and one job (show the logged objective and learning-rate trajectory).

evidence:

- `20260717_124435`: 1,185 unsmoothed `loss` samples, steps 50--59,250; no logged `lr`; W&B state `finished`; configured base LR 1e-3, scheduler horizon 100k, maximum 100k.
- `large-2kh-packed-recovery-lr-half`: 1,000 unsmoothed `loss` and `lr` samples, steps 50,050--100,000; W&B state `finished`; configured base LR 5e-4, scheduler horizon 100k, maximum 100k.
- `large-2kh-packed-300k-tail-lr-1e4`: 1,414 unsmoothed `loss` and `lr` samples, steps 100,050--170,700; configured base LR 1e-4, scheduler horizon 300k, maximum 300k. W&B records terminal state `failed`, but the author confirms that the training segment completed successfully; the figure therefore does not label the segment as a failure.
- `large-2kh-packed-210k-tail-lr-1e4`: 786 unsmoothed `loss` and `lr` samples, steps 170,750--210,000; W&B state `finished`; configured base LR 1e-4, scheduler horizon 300k, maximum 210k.

math_logic_review: exact

model_or_equations: Plotted coordinates are the exact exported W&B scalar histories for `loss` and `lr`. The only transforms are step/1000 on the horizontal axis and LR times 1e4 on the right axis.

checked_invariants: The four W&B records are identified as one checkpoint lineage; no smoothing; no interpolation; no cross-record line; panel-specific objective ranges are explicit; the 50,050--59,250 overlap remains visible in separate panels; the 170,700/170,750 resume boundary is visible; the third segment is identified as successful despite inaccurate W&B terminal metadata; the graph is called a training diagnostic, not validation, convergence, or generalization evidence.

remaining_risks: W&B did not log `lr` for the first record, so only its configured base LR is annotated. Panel-specific objective ranges support readability but preclude comparing vertical displacement by eye; the caption states this. The final resume path uses the renamed `runs/bengali-210k/checkpoints/last.pt` directory, and the author confirms that it continues the same trajectory.

automated_visual_qa: The research-mode checker now reports only title-band collisions. This standalone multi-panel plot has no document-level internal title; the detector treats upper-panel axis text as occupying a protected title band. It reports no text-overlap or edge-clipping finding. Manual inspection confirms that removing the redundant panel-(c) right-axis title eliminated its collision with panel-(d) ticks. The optional pixel-level text-over-plot check remains unavailable because NumPy is not installed in the project `.venv`; the only in-plot annotation has an opaque white backing box and was manually inspected.

manuscript_fit: pass after rerender; manuscript page 5 was rendered at 180 dpi and manually inspected. Panel titles, tick labels, axis labels, legend, and shortened caption are readable at full text width, with no clipping or central-axis collision. The detailed overlap and lineage caveats appear in the preceding body paragraph on page 4. The manuscript remains seven pages and its log contains no overfull boxes or unresolved citation/reference warnings.

caption_text: Four relevant W&B training histories under the documented schedule changes. Curves are unsmoothed, panels are not joined across runs, and objective-axis ranges differ by panel. These diagnostics are not validation or convergence evidence.

render_version: `training_diagnostics.png`
