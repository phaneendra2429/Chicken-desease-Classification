# This script is used to configure and set up the project for packaging and distribution, providing metadata, and specifying where the packages and modules are located.

import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()



__version__="0.0.0"

REPO_NAME = "Chicken-desease-Classification"
AUTHOR_USER_NAME = "phaneendra2429"
SRC_REPO="cnnClassifier"
AUTHOR_EMAIL = "phaneendraganji3@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small python package for CNN app",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
    
)