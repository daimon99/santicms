#!/usr/bin/env python
# -*- coding: utf-8 -*-

from setuptools import setup, find_packages


def fread(filename):
    with open(filename) as f:
        return f.read()


setup(
    name='santicms',
    version='0.1',
    author='Daimon',
    author_email='daijian1@qq.com',
    packages=find_packages(exclude=['tests', 'tests.*']),
    description="Santi Cms app.",
    zip_safe=False,
    include_package_data=True,
    # entry_points={'console_scripts': [
    #     'JQR = manage',
    # ]},
    platforms='any',
    long_description=fread('../README.md'),
    license='MIT',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'Operating System :: MacOS',
        'Operating System :: POSIX',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ], install_requires=[
        'django',
        'pymysql',
        'djangorestframework',
        'markdown',
        'django-filter',
        'jsonpickle',
        'wechat',
        'django-cors-headers',
        'pycrypto',
        'requests',
        'docutils',
        'simplejson',
        'django-debug-toolbar',
        'networkx'
    ]
)
