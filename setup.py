from pathlib import Path
from setuptools import setup, find_packages

# put the contents of your README file into the long_description


this_directory = Path(__file__).parent
long_description = (this_directory / "README.RST").read_text()

setup(
    long_description=long_description
)
