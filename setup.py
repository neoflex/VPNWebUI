#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

requirements = [
    'Flask', 'Flask-Assets', 'Jinja2', 'Werkzeug', 'closure',
    'cssmin', 'webassets', 'Flask-Testing', 'requests', 'Flask-Script'
]

test_requirements = [
    'coverage'
]

setup(
    name='expressvpn-web',
    version='0.0.1',
    description="Web interface to the expressvpn linux client",
    author="Valentin Grouès",
    author_email='neoflexx@gmail.com',
    packages=find_packages(exclude=['contrib', 'docs', 'tests*']),
    package_dir={'expressvpn-web':
                     'expressvpn_web'},
    include_package_data=True,
    install_requires=requirements,
    zip_safe=False,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        # 'Intended Audience :: Developers',
        # 'License :: OSI Approved :: ISC License (ISCL)',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
    ],
    test_suite='tests',
    tests_require=test_requirements,
    package_data={
        'expressvpn-web': ['expressvpn_web/resources/*'],
    }
)
