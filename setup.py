import setuptools

with open("README.md", "r", encoding="utf-8") as file_obj:
    long_description = file_obj.read()


__version__ = "0.0.0"

REPO_NAME = "text_summarization_project"
AUTHOR_USER_NAME = "kiran-narayan1"
SRC_REPO = "TextSummarization"
AUTHOR_EMAIL = "@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    version=__version__,
    description="a pypi package for NLP app",
    long_description=long_description,
    long_description_content = "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)
