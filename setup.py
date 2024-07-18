from setuptools import setup, find_packages

setup(
    name="rickrollprinter",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        'pygame',  # Add pygame as a dependency
    ],
    author="jayoungh",
    author_email="juanandresyounghoyos@gmail.com",
    description="A Python package that prints Rickroll and plays the song.",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/yourusername/rickrollprinter",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
