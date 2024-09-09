from setuptools import setup, find_packages

# Load the README file for the long description
with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="NeuroMod",  
    version="0.1.0",  # Versioning convention: major.minor.patch
    author="Bharath Kumar Nagaraj",  
    author_email="bharathkumarnlp@gmail.com",  # Replace with your email
    description="A Python library to simulate brain regions and integrate them with LLMs for enhanced cognitive capabilities.",  # Short description of your project
    long_description=long_description,  # Long description read from the README file
    long_description_content_type="text/markdown",  # README is in Markdown
    url="https://github.com/yourusername/NeuroMod",  # Replace with your GitHub repo URL
    packages=find_packages(),  # Automatically find packages in the project
    classifiers=[
        "Programming Language :: Python :: 3",  # Supports Python 3
        "License :: OSI Approved :: MIT License",  # License type
        "Operating System :: OS Independent",  # OS compatibility
    ],
    python_requires='>=3.6',  # Minimum Python version required
    install_requires=[
        "torch>=1.10.0",  # Core ML framework
        "transformers>=4.20.0",  # For LLMs and transformers
        "scikit-learn>=1.0",  # ML utilities
        "numpy>=1.21.0",  # Numerical operations
        "pandas>=1.3.0",  # Data manipulation
        "brian2>=2.4.2",  # Neural simulation
        "spacy>=3.1.0",  # NLP utilities
        "nltk>=3.6.0",  # Additional NLP tools
        "pytorch-lightning>=1.5.0",  # PyTorch utilities
        "mlflow>=1.20.0",  # Experiment tracking
        "optuna>=2.10.0",  # Hyperparameter optimization
        "fastapi>=0.75.0",  # API development
        "uvicorn>=0.15.0",  # ASGI server
        "tensorboard>=2.7.0",  # Model monitoring
        "matplotlib>=3.4.0",  # Visualization
        "seaborn>=0.11.0",  # Statistical visualization
        "loguru>=0.5.0",  # Logging
    ],  # Required dependencies listed here
    entry_points={
        "console_scripts": [
            "neuromod=neuromod.cli:main",  # Replace with actual CLI interface if needed
        ],
    },
    include_package_data=True,  # Include non-Python files specified in MANIFEST.in
)

