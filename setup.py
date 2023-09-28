from setuptools import setup, find_packages
from module_structure import _author, __version, __name_

AUTHOR = _author_
VERSION = _version_
NAME = _name_

setup(
    name=NAME,
    version=VERSION,
    description='Machine Learning Classes UFV',
    author=AUTHOR,
    author_email='7900782@alumnos.ufv.es',
    license='MIT',
    python_requires='>=3.9',
    packages=find_packages(),
    include_package_data=False,
    install_requieres= ['pandas', 'torch', 'numpy']
)