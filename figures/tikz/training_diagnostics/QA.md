# Training-diagnostics figure audit

complexity_review: reject

reason: The available exports do not support a conservative, self-contained diagnostic of the selected 210k checkpoint without either plotting an explicitly excluded run or creating a misleading gap. The runs must not be stitched: they are distinct W&B histories with manual learning-rate and configuration changes. Separate panels would preserve that distinction, but the admissible panels still do not form an interpretable account of the selected checkpoint's training history.

evidence:

- `20260717_124435` (manifest label `Pretraining segment 1`) contains unsmoothed objective samples every 50 steps from 50 through 59,250. It has no exported `lr` series.
- `large-2kh-packed-recovery-lr-half` (manifest label `Pretraining segment 2 (LR halved)`) contains unsmoothed objective and learning-rate samples every 50 steps from 50,050 through 100,000. It therefore overlaps segment 1 over 50,050--59,250; the two histories cannot be treated as adjacent pieces of one curve. Repository prose says this recovery started from the step-50,000 checkpoint with a manually reduced base learning rate of 5e-4 and reconstructed scheduler state.
- `large-2kh-packed-300k-tail-lr-1e4` (manifest label `Pretraining segment 3 (interrupted after valid logging)`) contains samples from 100,050 through 170,700, is marked `failed`, and is explicitly out of scope for visualization.
- `large-2kh-packed-210k-tail-lr-1e4` (manifest label `Pretraining segment 4`) contains samples from 170,750 through 210,000. It starts immediately after excluded segment 3, so showing it beside segments 1 and 2 while suppressing segment 3 would hide the actual continuation path.
- The manuscript states that the tail used base LR 1e-4 with a 300k scheduler horizon before the maximum was set to 210k, and that the scheduler was reconstructed at resumes rather than restored as independent state. This rules out presenting the histories as one uninterrupted cosine schedule.

math_logic_review: needs_source

model_or_equations: Exact CSV samples exist for `loss`, `l_jepa`, `l_vis`, `l_wav`, and `l_mel`; `lr` is absent only for segment 1. The selected objective is `1.0 L_mel + 0.3 L_view + 0.7 L_VISReg`, so differently scaled raw components would require separate axes or log scaling and careful naming. That layout issue is solvable; provenance is the blocker.

checked_invariants: No smoothing; no cross-run interpolation; no line connecting run boundaries; no relabeling as validation, convergence, or generalization evidence; no use of rank, gradient, memory, or bookkeeping metrics.

remaining_risks: A three-panel plot of only segments 1, 2, and 4 would be formally separated but materially incomplete. A four-panel plot would violate the explicit exclusion of the 170k/failed run. A one-panel plot would additionally conceal the overlap and schedule reconstruction.

recommendation: Do not include a training-diagnostics figure in the manuscript under the current evidence constraints. Retain the raw W&B catalog as provenance. Reconsider only if the experiment owner explicitly authorizes the failed-but-valid-logging segment for a provenance-only diagnostic and supplies/approves exact run-boundary and configuration annotations; otherwise prose is more accurate than a plot.

caption_text: None; figure rejected.

render_version: None; no TikZ source, PDF, or PNG was generated because the evidence gate failed before rendering.
