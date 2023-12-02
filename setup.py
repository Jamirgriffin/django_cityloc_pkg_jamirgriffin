from setuptools import setup, find_packages
from pathlib import Path

# put the contents of your README file into the long_description
this_directory = Path(__file__).parent
readme_path = this_directory / "README.RST"
long_description = readme_path.read_text()

setup(
    # other setup parameters...

    long_description=long_description,
    # other setup parameters...
)
