from setuptools import setup, find_packages

VERSION = '0.1.0'
DESCRIPTION = 'PySteganography - A simple toolset for image encoding and decoding using steganography.'
LONG_DESCRIPTION = 'A package that provides developers the necessary functions to implement steganography in image files through the least significant bit (LSB) technique.\nView examples and features on github: https://github.com/deetsadi/pysteganography'

setup(
    name="pysteganography",
    version=VERSION,
    author="deetsadi (Aditya Sridhar)",
    author_email="<deetsadi@gmail.com>",
    description=DESCRIPTION,
    long_description_content_type="text/markdown",
    long_description=LONG_DESCRIPTION,
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    download_url="https://github.com/deetsadi/pysteganography/archive/refs/tags/v_01.tar.gz",
    install_requires=['opencv-python', 'numpy'],
    keywords=['python', 'steganography', 'cybersecurity', 'images', 'sound', 'security'],
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    python_requires=">=3.6"
)
