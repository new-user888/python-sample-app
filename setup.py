from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="python-sample-app",
    version="1.1",
    description="A starter template for new Python applications",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Benjamin Costa",
    author_email="benjamin.costa.75@gmail.com",
    license="MIT",
    url="https://github.com/becosta/python-sample-app",
    packages=find_packages(),
    entry_points={
        "console_scripts": [
            "sample-app=python_sample_app.main:main",
        ],
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
