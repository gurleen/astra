import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="Astra",
    version="0.0.1",
    author="Gurleen Singh",
    author_email="gs585@drexel.edu",
    description="A small web framework",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/gurleens2000/astra-web",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)