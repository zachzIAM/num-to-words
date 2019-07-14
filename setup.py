import pathlib
from setuptools import setup

HERE = pathlib.Path(__file__).parent

README = (HERE / "README.md").read_text()

setup(
    name='num-to-words',
    install_requires=['pytest'],
    version='1.0.0',
    packages=['num2words'],
    url='https://github.com/zachzIAM/num-to-words',
    license='MIT',
    author='Zach Zankov',
    author_email='zach.zankov@investecmail.com',
    description='Convert a number to English numeral',
    long_description=README,
    long_description_content_type="text/markdown",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
    ],
    entry_points={
        "console_scripts": [
            "num2words=num2words.__main__:main",
        ]
    },
)
