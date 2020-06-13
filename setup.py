from setuptools import setup
import os

VERSION = "0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="datasette-psutil",
    description="Datasette plugin adding a /-/psutil debugging endpoint",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Simon Willison",
    url="https://github.com/simonw/datasette-psutil",
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["datasette_psutil"],
    entry_points={"datasette": ["psutil = datasette_psutil"]},
    install_requires=["datasette>=0.44", "psutil"],
    extras_require={"test": ["pytest", "pytest-asyncio", "httpx"]},
    tests_require=["datasette-psutil[test]"],
)
