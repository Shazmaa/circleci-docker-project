from setuptools import setup, find_packages

setup(
    name='DevSecOps_Project',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'pytest',
        'requests',
        'flask',
    ],
)

