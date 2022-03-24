from setuptools import setup, find_packages


setup(
    name='willit',
    version='0.0.1',
    description="A command-line tool for the hacker in you",
    author="Casey Reid",
    aurthor_email="itprofguru@gmail.com",
    url="https://github.com/packetchaos/willit",
    license="GNUv3",
    keywords='command and control',
    packages=find_packages(exclude=['docs', 'tests']),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'Click>=7.0.0',
        'requests>=2.26.0',
        'pexpect>=4.8.0'
    ],
    python_requires='>=3.0',
    extras_require={},
    entry_points={
        'console_scripts': [
            'will=will.cli:cli'
        ],
    },
)
