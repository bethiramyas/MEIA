from setuptools import setup, find_packages

setup(
    name="meia",
    version="1.0.0",
    description="MEIA: Multimodal Ethical Interaction Agent",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.11",
    install_requires=[
        "torch>=2.2",
        "transformers>=4.38",
        "shap>=0.45",
        "numpy>=1.26",
        "scipy>=1.11",
        "pandas>=2.1",
        "matplotlib>=3.8",
        "statsmodels>=0.14",
        "scikit-learn>=1.4",
        "pyyaml>=6.0",
    ],
    extras_require={
        "dev": ["pytest>=8.0", "black", "flake8"],
    },
)
