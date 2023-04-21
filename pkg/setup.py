"""A package for bibtex utilities."""

from setuptools import setup

setup(
    name="s23oa",
    version="0.0.1",
    description="OpenAlex utilities",
    maintainer="John Kitchin",
    maintainer_email="jkitchin@andrew.cmu.edu",
    license="MIT",
    packages=["s23oa"],
    entry_points={"console_scripts": ["oa = s23oa.main:main"]},
    scripts=[],
    long_description="""A set of OpenAlex utilities""",
)
