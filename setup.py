from distutils.core import setup

setup(
    name='MarkdownBlankLine',
    version='0.1.3',
    packages=['MarkdownBlankLine',],
    license='Apache License 2.0',
    long_description=open('README.txt').read(),
    url='https://github.com/ribalba/markdown.blankline',
    description='A markdown extension that enables you to add blank lines',
    author='Didi Hoffmann',
    author_email='didi@ribalba.de',
    install_requires=[
        "Markdown >= 2.3.1",
    ],
)