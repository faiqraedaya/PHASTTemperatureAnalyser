from setuptools import setup, find_packages

setup(
    name="phast-analyzer",
    version="2.0.0",
    packages=find_packages(),
    install_requires=[
        "numpy",
        "pandas",
        "scipy",
        "openpyxl",
        "PyQt5",
    ],
    python_requires=">=3.6",
    author="Your Name",
    author_email="your.email@example.com",
    description="PHAST Temperature Dispersion Analyzer",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
) 