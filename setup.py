from setuptools import setup

with open("README.md", 'r') as f:
    long_description = f.read()

setup(
    name="extext",
    version="0.0.1",
    description="Extract text data on the screen",
    url="https://github.com/TrAyZeN/extext",
    author="TrAyZeN",
    author_email="",
    long_description=long_description,
    long_description_content_type="text/markdown",
    license="MIT",
    packages=["extext"],
    install_requires=[
        "packaging==21.3",
        "Pillow==9.0.1",
        "pyparsing==3.0.7",
        "pyperclip==1.8.2",
        "PyQt5==5.15.6",
        "PyQt5-Qt5==5.15.2",
        "PyQt5-sip==12.9.1",
        "pytesseract==0.3.9",
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent"
    ]
)
