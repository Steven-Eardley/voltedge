from setuptools import setup, find_packages

setup(
    name = 'voltedge',
    version = '0.0.1',
    packages = find_packages(),
    install_requires = [
        "octopus==1.0.0",
        "esprit",
        "Flask"
    ],
    url = 'http://cottagelabs.com/',
    author = 'Steven Eardley',
    author_email = 'steve@cottagelabs.com',
    description = 'An experiment with edges based on UK EV data',
    classifiers = [
        'Development Status :: 3 - Alpha',
        'Environment :: Console',
        'Intended Audience :: Developers',
        'License :: Copyheart',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules'
    ],
)
