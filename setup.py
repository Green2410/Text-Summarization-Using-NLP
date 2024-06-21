import setuptools

with open("README.md", "r", encoding = "utf-8") as f:
    detail_description = f.read()

__version__ = "0.0.0"

REPO_NAME = "Text-Summarization-Using-NLP"
AUTH_USER_NAME = "Green2410"
SOURCE_REPO = "TextSummarizer"
AUTH_MAIL = "abhirupguhathakurta5@gmail.com"


setuptools.setup(
    name = SOURCE_REPO,
    version = __version__,
    author = AUTH_USER_NAME,
    author_email = AUTH_MAIL,
    description = "A small Python package for an application leveraging NLP",
    long_description = detail_description,
    long_description_content = "text/markdown",
    url = f"https://github.com/{AUTH_USER_NAME}/{REPO_NAME}",
    project_urls = {
        "Bug Tracker": f"https://github.com/{AUTH_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir = {"":"src"},
    packages = setuptools.find_packages(where = "src")
)
    
    