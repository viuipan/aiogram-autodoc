from setuptools import setup, find_packages

setup(
    name='aiogram_autodoc',
    version='0.0.1',
    url='https://github.com/viuipan/aiogram_autodoc',
    license='MIT',
    description='Generates command documentation from handlers',
    packages=['aiogram_autodoc'],
    setup_requires=['aiogram<3']
)