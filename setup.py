from distutils.core import setup

setup(
    name='radio',
    version='0.0.6',
    author='Santiago Pestarini',
    author_email='santiagonob@gmail.com',
    packages=['radio'],
    package_data={'radio': ['data/*.json']},
    scripts=['bin/radio'],
    url='http://pypi.python.org/pypi/radio/',
    license='LICENSE.txt',
    description='Just listen to the radio.',
    long_description=open('README.rst').read(),
)
