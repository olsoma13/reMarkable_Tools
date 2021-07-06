import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="reMarkable_tools",
    version="0.0.1",
    author="Matt Olson",
    author_email="matt@olsonmatthew.com",
    description="A set of utilities for managing my reMarkable Tablet.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/olsoma13/reMarkable_Tools",
    project_urls={
        "Bug Tracker": "https://github.com/olsoma13/reMarkable_Tools/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Unix"
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
)