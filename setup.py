from setuptools import setup
import sys

required = []
long_description = ""
with open('README.md') as f:
    long_description += f.read()

setup(
    name='bad_words_plus',
    version='1.0.0',
    description='Unofficial API for Eksi Sozluk.',
    long_description=long_description,
    author='Yusuf Usta',
    author_email='yusuf@usta.email',
    maintainer='Yusuf Usta',
    maintainer_email='yusuf@usta.email',
    url='https://github.com/yusufusta/bad_words_plus',
    license='GPL3',
    packages=['bad_words_plus'],
    install_requires=required,
    keywords=['bad words'],
    long_description_content_type="text/markdown",
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 (GPLv3)',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9'
    ],
)
