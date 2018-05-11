from setuptools import setup
import sys

assert sys.version_info >= (3, 6, 0), "requires Python 3.6+"
from pathlib import Path  # noqa E402

CURRENT_DIR = Path(__file__).parent

INSTALL_REQUIRES = [
    'black',
    'watchdog>=0.8.3,<0.9',
]

def get_long_description():
    readme_md = CURRENT_DIR / "README.md"
    with open(readme_md, encoding="utf8") as ld_file:
        return ld_file.read()

setup(
    name="blackdaemon",
    version='0.1.0.1',
    description="Daemon to automatically run black, the uncompromising code formatter.",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    keywords="daemon black automation formatter yapf autopep8 pyfmt gofmt rustfmt",
    author="Chad Smith",
    author_email="grassfedcode@gmail.com",
    url="https://github.com/cs01/blackdaemon",
    license="MIT",
    python_requires=">=3.6",
    zip_safe=False,
    install_requires=INSTALL_REQUIRES,
    test_suite="tests.test_black",
    classifiers=[
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3 :: Only",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Quality Assurance",
    ],
    entry_points={"console_scripts": ["blackdaemon=blackdaemon:main"]},
)
