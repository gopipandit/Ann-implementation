from setuptools import setup

with open("README.MD", "r", encoding="utf-8") as f:
    long_description = f.read()


setup(
    name="src",
    version="0.0.1",
    author="Gopi Pandit",
    description="A small package for ANN Implementation.",
    long_description=long_description,
    url="https://github.com/gopipandit/Ann-implementation",
    author_email="gopi_pandit@yahoo.com",
    packages=["src"],
    python_requires=">3.8",
    install_requires=["dvc",
                      "matplotlib",
                      "seaborn",
                      "numpy",
                      "pandas",
                      "scikit-learn"],
)
