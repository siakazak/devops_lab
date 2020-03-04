from setuptools import setup, find_packages

setup(
    name="pr-stats",
    packages=find_packages(),
    scripts=["pr-stats", "githubuser.py"],
    version="0.2.8",
    author="Siarhei Kazak",
    author_email="siarhei_kazak@epam.com",
    description="Demo GitHub REST API script",
    license="MIT"
)
