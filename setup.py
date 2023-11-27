from setuptools import setup, find_packages

with open("README.md", encoding="utf-8") as f:
    long_des = str(f.read())

setup(
    name='FletDesigner',
    version='1.0',
    author='<AUTHOR>',
    description='A Drag Drop UI builder For Flet python',
    long_description=long_des,
    long_description_content_type='text/markdown',
    url='https://github.com/normalentity/FletDesigner',
    install_requires=["flet"],
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X"
    ],
    include_dirs=[],
    package_data={"":[]},
    include_package_data=True
)