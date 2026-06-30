# Installation

## Requirements

- Python 3.11
- CUDA 12.1-capable GPU (training only; CPU sufficient for smoke tests
  and metric reproduction from released logs)
- ~20 GB disk space for pretrained checkpoints (RoBERTa-large, ViT-B/16,
  LLaMA-3-8B-Instruct 4-bit GPTQ)
- Unreal Engine 5.3 with the MetaHuman plugin (only required to regenerate
  the MultiEthic-V benchmark from scratch; not required to reproduce
  metrics/figures/tables from released logs)

## Standard Installation (recommended)

```bash
git clone https://github.com/<org>/MEIA.git
cd MEIA
conda env create -f environment.yml
conda activate meia
pip install -e .
```

## Verify Installation

```bash
python scripts/smoke_test.py
```

Expected output:
```
==================================================
MEIA Repository Smoke Test
==================================================
[1/5] Testing imports... OK
[2/5] Testing CAFL forward pass (Eq. 3)... OK
[3/5] Testing BSE particle filter (Eq. 1)... OK
[4/5] Testing UES/BRI/UTS metrics... OK
[5/5] Testing ABM bias mitigation logic... OK

All smoke tests passed. Repository is correctly installed.
```

## GPU Setup for Full Training Reproduction

Training the full ECRL policy (Algorithm 1, K=1200 episodes x 5 seeds)
was run on 4x NVIDIA A100-80GB and takes approximately 72 hours per seed
group. See `docs/REPRODUCING.md` for the full training pipeline.

```bash
# Verify CUDA availability
python -c "import torch; print(torch.cuda.is_available(), torch.cuda.device_count())"
```

## Unreal Engine 5.3 Setup (optional — only for benchmark regeneration)

The MultiEthic-V benchmark's avatar rendering and interaction simulation
requires Unreal Engine 5.3 with the MetaHuman plugin. See
`benchmarks/MultiEthic-V/unreal_project/README.md` for the project file
and plugin installation instructions. This step is **not required** if you
only wish to reproduce the published figures and tables from released
interaction logs.

## Common Issues

**`ImportError: cannot import name 'ViTModel' from 'transformers'`**
Ensure `transformers==4.38.2` exactly — newer versions changed the ViT API.

**CUDA out-of-memory during Stage 3 fine-tuning**
Reduce `n_steps_per_episode` in `configs/main_config.yaml` or enable
gradient checkpointing (see `docs/REPRODUCING.md` Section 4).

**`shap.TreeExplainer` errors with the ABM module**
Ensure `shap==0.45.0` exactly; the TreeSHAP API used in
`src/evaluation/abm.py` is version-sensitive.
