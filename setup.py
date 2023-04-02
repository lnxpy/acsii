#!/usr/bin/env python

"""The setup script."""

from setuptools import setup, find_packages

with open('README.md') as readme_file:
    readme = readme_file.read()

requirements = [
    'opencv-python<=4.7.0',
]

test_requirements = [ ]

setup(
    author="Sadra Yahyapour",
    author_email='lnxpylnxpy@gmail.com',
    python_requires='>=3.6',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Natural Language :: English',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="ACSII (not ASCII) is an image processing project that is capable of turning real images into ASCII arts.",
    entry_points={
        'console_scripts': [
            'acsii=acsii.cli:main',
        ],
    },
    install_requires=requirements,
    license="MIT license",
    long_description=readme,
    include_package_data=True,
    keywords='acsii',
    name='acsii',
    packages=find_packages(include=['acsii', 'acsii.*']),
    test_suite='tests',
    tests_require=test_requirements,
    url='https://github.com/lnxpy/acsii',
    version='0.1.0',
    zip_safe=False,
)
