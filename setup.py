#!/usr/bin/env python
from setuptools import setup, find_packages

setup(
    name='i3history',
    version='0.0.1',
    description='A navigation history for i3wm',
    author='Paul Baecher',
    author_email='pbaecher@gmail.com',
    url='https://github.com/pb-/i3history',
    packages=find_packages('.'),
    license='MIT',
    install_requires=[
        'i3ipc >=1.2.0',
    ],
    entry_points={
        'console_scripts': [
            'i3history = i3history:run',
        ],
    },
)
