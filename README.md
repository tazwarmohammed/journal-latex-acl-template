# CLAE TACL manuscript

The manuscript source is `acl_latex.tex`; the compiled anonymous review PDF is `acl_latex.pdf`. The directory name is historical: this manuscript now uses the official TACL submission style, not the ACL conference template.

Build from this directory with `latexmk -pdf -interaction=nonstopmode -halt-on-error acl_latex.tex`. This compiles LaTeX only; it does not run training, Python, or evaluation. Existing figure PDFs are reused. Figure sources in `figures/tikz/` are compiled separately with XeLaTeX from that directory; the training-curve figure needs two passes for its shared legend.

## Submission preparation

Use the [official TACL submission guidelines](https://transacl.org/ojs/index.php/tacl/about/submissions) and [March 2024 appendix policy](https://transacl.org/index.php/tacl/announcement/view/105). The final reviewed layout has eight main-content pages (references begin on page 8), references through page 11, two replication pages (12–13), and two complementary-result pages (14–15). The appendix categories have separate limits, not a pooled allowance. Recheck these page boundaries after every substantive edit.

The unmodified official `tacl2021v1.sty` was downloaded from https://transacl.org/tacl-submission-templates/tacl2021v1.sty. Its SHA-256 is `7c71ede112ccb3711c7073c4b1c60abfb076b83945e0e9d14ed79caa37dca3b6`. The manuscript places the style's confidentiality text in the modern foreground shipout hook with explicit point dimensions, independent of the current picture unit length; the official style file is unchanged. Do not activate an accepted-paper option for review.

The author-approved release intent is code, evaluation recipes, and checkpoints; no dataset manifests. The manuscript makes that limitation explicit. Review submission is the anonymous PDF, not this source directory or a link to its evidence repositories. Rename the PDF with the assigned submission number and the first one to three title words when uploading. Confirm author profiles, prior-review eligibility, concurrent-submission status, and any required preprint disclosure in the submission portal.

## Evidence and remaining scientific limits

The selected 210k full-data evaluation, earlier matched 25k common-400 study, and reduced fixed-subset FP32 study remain separate. The historical 170k appendix removed by the author remains removed. Main comparisons use probe seed 0; additional neural-probe aggregates use seeds 0/1/2, with SD distinguished from confidence intervals and encoder-training replication. Reduced ASR is not evaluated. Missing and failed results are never replaced by measurements from another protocol.

Two main evaluation tables replace the former four: full-data main-run comparison and reduced fixed-subset comparison, each with reconstruction and frozen-feature panels. The reduced table includes ESTOI and all available Mimi reconstruction proxies. The earlier incomplete 400-clip ablation table remains in the complementary appendix; additional full-data results share one two-panel table. Classification/F1/EER are percentages throughout tables; CER/WER/minDCF remain ratios. All conversions are rounded directly from raw JSON, never from rounded Markdown values. The editorial check verified 264 numerical evaluation entries, including means and SDs separately. The generic pooling description includes final-window padding, and both demographic heads use balanced class weights.

The abstract is 122 words and citation-free. Citations remain in the body. The reader-facing condition name is “main pretraining run”; its endpoint and the matched-ablation budget remain in the experimental description. Figure 2 is retained as a vector explanation of the frame-level VISReg computation. Appendix Figure 3 retains the unsmoothed matched training trajectories; all 24 CSV/column mappings are unchanged. Training losses are optimization diagnostics, not validation evidence or a ranking across different objectives.

`../reports/demographic_label_audit.json` records a result-only label inventory and training-fold majority reference, source identities/hashes, and fold scores. Full-data source predictions were read from the pinned evaluation2 revision `7b8f8c3be6e6d183f655854fed1e5fcad12f1275`; reduced predictions came from the existing TAR (SHA-256 `5663ecb2a2d4f486be4c55fde151c0eb96c8f5d6893e5ca9899c249b3dbdd8e0`). The calculation reproduces saved CLAE macro-F1 from the predictions and independently checks the constant-predictor formula. It performs no fitting or feature extraction. Full age has five labels, including only two fifties clips; reduced age has four. The 210k full-data and all reduced CLAE age macro-F1 scores are below the majority reference. The main text reflects this.

Per-item reconstruction paths in the selected full and reduced raw reconstruction JSON identify Common Voice 26.0 (2026-06-12). Full reconstruction source: the same pinned evaluation2 revision, `conditions/packed-210k-last/step_210000/reconstruction.json`. Reduced source: `full_evaluations_small_fp32/conditions/packed-210k-last/step_210000/reconstruction.json` inside the TAR. These records do not establish pretraining disjointness or waveform identity.

Before claiming exact reproducibility or stronger generalization, recover the selected run's resolved configuration and immutable checkpoint digests; verify historical execution settings and dataset releases; audit pretraining overlap and applicable corpus terms; and investigate the SI-SDR/alignment discrepancy using original/reconstructed waveforms. The manuscript discloses these unresolved limits. No new training or evaluation was run during submission preparation.

## Machine-readable identities moved out of the manuscript

External adapters pin the following Hub revisions: WavLM-base-plus, `4c66d4806a428f2e922ccfa1a962776e232d487b`; Whisper-tiny, `169d4a4341b33bc18d8881c4b69c2e104e1cc0af`; ECAPA, `0f99f2d0ebe89ac095bcc5903c4dd8f72b367286`; emotion2vec, `0c9a3152734f9d7a7a05b4ee6bfb3c109d288664`; Mimi, `89091b3e466eb6a9d11e537bf26b144f194978f7`; and `bosonai/higgs-audio-v2-tokenizer`, `403fbacf2f60caaa102f893fdfabb694619b2417`.

For identifying the demographic partitions, full age/gender split fingerprints are, respectively, `ef5a12b66a66c4a61a1f9e5a4b907a7e53f3b08bef5e5147ae607f2e2a2def62` and `5f13ef4da550a470843e5124017092104c06c4cef98db732a05b700d927172c7`. Reduced age/gender fingerprints are `08d489be6927530a6fc144df52e514daf6a5598ee03c42a4c908bb5fa41d4daa` and `cc898ed272c53ec29ed85919bbddd4dada217281507534edef4d55a59905b639`. Fingerprints identify the saved partitions but cannot reconstruct unreleased manifests.

The manuscript name “main pretraining run” maps to `large-2kh-packed-210k-tail-lr-1e4`, terminal step 210000. Matched ablations stop at 25000; legacy `50k` filenames are identifiers rather than evaluated budgets. These identifiers support artifact tracing and are not experimental prose.
