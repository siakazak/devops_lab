from setuptools import setup, find_packages

setup(
    name="snapshot",
    packages=find_packages(),
    scripts=["snapshot.py", "timer.py", "snapshot"],
    version="0.1",
    author="Siarhei Kazak",
    author_email="siarhei_kazak@epam.com",
    description="Take system snapshot every 5 mins",
    license="MIT"
)
