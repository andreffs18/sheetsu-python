from setuptools import setup, find_packages

setup(
    name='sheetsu',
    version='0.0.5',
    description='Sheetsu Python client',
    url='http://github.com/andreffs18/sheetsu-python',
    author='Andre Silva',
    author_email='andreffs18@gmail.com',
    license='MIT',
    keywords='sheetsu api client sdk spreadsheet',
    packages=find_packages(),
    zip_safe=False,
    install_requires=['requests']
)
