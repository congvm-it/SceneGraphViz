from setuptools import setup, find_packages
from os import path

__version__ = '1.0.0'

with open('requirements.txt') as f:
    requirements = f.read().splitlines()

setup(
    name='sgraphviz',
    version=__version__,
    description='Scene Graph Visualization',
    packages=find_packages(),
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    author='ranjaykrishna',
    license='MIT',
    zip_safe=False,
    install_requires=requirements,
    classifiers=(
        'Programming Language :: Python :: 3.6',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Topic :: Scientific/Engineering :: Artificial Intelligence',
    ),
)
