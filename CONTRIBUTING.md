# Contributing

Thank you for your interest in MEIA. This repository accompanies a paper
under peer review; while the core results are frozen for reproducibility,
we welcome contributions that improve code quality, documentation, or
extend the framework.

## Reporting Issues

If you find a discrepancy between this code and the paper, please open an
issue with:
1. The specific section/equation/table in the paper
2. The corresponding file and line number in this repository
3. A minimal reproduction of the discrepancy

## Reproducibility Issues

If you cannot reproduce a reported number within reasonable tolerance
(accounting for hardware-dependent floating-point variation), please
include:
- Your environment (`pip freeze` output or `environment.yml` diff)
- The exact command run
- The full output/error

## Pull Requests

1. Fork the repository and create a feature branch
2. Ensure `pytest tests/` and `python scripts/smoke_test.py` pass
3. Follow the existing code style (we use `black` for formatting)
4. Reference the relevant paper section in your PR description if the
   change affects a method described in the paper

## Code of Conduct

Please be respectful and constructive in all interactions. This is an
academic research repository supporting open science.
