# MEIA: Multimodal Ethical Interaction Agent

[![Paper](https://img.shields.io/badge/Paper-SCI--Q1-blue)](#citation)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![DOI](https://img.shields.io/badge/DOI-pending-lightgrey)](#citation)

Official implementation and benchmark release for the paper:

> **Autonomous AI Agents for Enhanced Interactions and Decision-Making in the Metaverse: A Multimodal and Ethically-Aware Framework**
> *(Manuscript under review, SCI Q1)*

MEIA is a unified framework for autonomous AI agents in the metaverse that
jointly optimises user engagement and ethical fairness. It is built on a
formally specified **Ethical Partially Observable Markov Decision Process
(Ethical-POMDP)** and combines a multimodal perception architecture with
two algorithms that enforce demographic parity and equalised odds during
training and at inference.

---

## ⚠️ Important: Scope of Evaluation

All results in this repository and the accompanying paper are derived from
a **calibrated multi-agent simulation study** (the MultiEthic-V benchmark),
not from human-subject experiments. The User Engagement Score (UES), Bias
Reduction Index (BRI), and User Trust Score (UTS) are **computational
behavioural proxies** and should not be interpreted as validated human
outcomes. A human-subjects study (IRB application #IRB-2025-0311, under
review) is planned as the critical next step. Please read this repository
and the paper's Limitations section (6.4) with this scope in mind.

---

## Repository Contents

```
MEIA/
├── src/                      # Core model and algorithm implementations
│   ├── models/                # HMF architecture: MPM, CAFL, BSE, EDE, TRG
│   ├── training/               # ECRL (Algorithm 1) training loop
│   ├── evaluation/             # ABM (Algorithm 2), metrics, baselines
│   └── utils/                  # Shared utilities, config loading, logging
├── configs/                  # YAML configs for all experiments
├── data/
│   ├── datasheets/             # Datasheets for MetaConvo-50K, MetaGesture-30K
│   └── sample_data/            # Small de-identified sample for smoke-testing
├── benchmarks/MultiEthic-V/  # Benchmark generation and scenario definitions
├── results/
│   ├── figures/                 # Reproduction scripts for Figures 1–5
│   └── tables/                  # Reproduction scripts for Tables 1–5
├── supplementary/            # Appendices A–D, Tables S1–S4 (paper materials)
├── scripts/                  # End-to-end reproduction scripts
├── tests/                    # Unit tests for core components
└── checkpoints/              # Released model weights (see Model Weights below)
```

## Quick Start

```bash
git clone https://github.com/<org>/MEIA.git
cd MEIA
conda env create -f environment.yml
conda activate meia
pip install -e .

# Run a smoke test on the sample data (no GPU required, ~2 min)
python scripts/smoke_test.py

# Reproduce Figure 2 (ECRL training dynamics) from released logs
python results/figures/make_figure2.py --logs results/raw_logs/ecrl_s1/

# Reproduce Table 3 (main results) from released evaluation outputs
python results/tables/make_table3.py --eval_dir results/raw_logs/eval/
```

Full training and evaluation reproduction (requires the MultiEthic-V
benchmark and a CUDA-capable GPU, ~72h on 4×A100) is documented in
[`docs/REPRODUCING.md`](docs/REPRODUCING.md).

## Installation

See [`INSTALL.md`](INSTALL.md) for detailed environment setup, including
CUDA version requirements and Unreal Engine 5.3 plugin setup used to
generate the MultiEthic-V benchmark.

## Released Artifacts

| Artifact | Location | Status |
|---|---|---|
| MultiEthic-V benchmark (scenario configs + generation scripts) | `benchmarks/MultiEthic-V/` | ✅ Released |
| MetaConvo-50K datasheet | `data/datasheets/MetaConvo-50K.md` | ✅ Released |
| MetaGesture-30K datasheet | `data/datasheets/MetaGesture-30K.md` | ✅ Released |
| Derived text/gesture embeddings | `data/embeddings/` (Zenodo, see below) | ✅ Released |
| Raw transcripts/motion-capture | — | ❌ Not released (ToS/licensing restriction; see datasheets) |
| Trained model weights (HMF, ECRL policy) | `checkpoints/` (Hugging Face, see below) | ✅ Released |
| GPT-4o prompt logs and outputs (B1/B2 baselines) | `supplementary/B_gpt4o_prompts/` | ✅ Released |
| Demographic-inference confusion matrix | `supplementary/D_confusion_matrix.csv` | ✅ Released |
| Theorem 1 full proof | `supplementary/A_theorem1_proof.pdf` | ✅ Released |

Large binary artifacts (model weights, full embeddings) are hosted externally
due to GitHub file-size limits:

- **Model weights**: [Hugging Face Hub — meia-hmf-ecrl-v1](https://huggingface.co/PLACEHOLDER)
- **Derived embeddings**: [Zenodo DOI — PLACEHOLDER](https://zenodo.org/PLACEHOLDER)

## Citation

If you use this code, benchmark, or model weights, please cite:

```bibtex
@article{meia2026,
  title   = {Autonomous AI Agents for Enhanced Interactions and
             Decision-Making in the Metaverse: A Multimodal and
             Ethically-Aware Framework},
  author  = {[Author names withheld pending double-blind review]},
  journal = {[Journal name pending acceptance]},
  year    = {2026},
  note    = {Manuscript under review}
}
```

## License

Code is released under the [MIT License](LICENSE). The MultiEthic-V
benchmark and datasheets are released under
[CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). See
[`LICENSE`](LICENSE) and [`data/LICENSE_DATA.md`](data/LICENSE_DATA.md).

## Contact

For questions about reproducing results, please open a
[GitHub Issue](../../issues). For questions about the IRB-approved human
study (in preparation), see [`docs/HUMAN_STUDY.md`](docs/HUMAN_STUDY.md).
