from setuptools import setup
import os

setup(name='PyFreelingApi',
      version='0.1.3',
      url='https://github.com/PaulBreugnot/PyFreeling',
      author="Paul Breugnot",
      author_email='paul.breugnot@etu.emse.fr',
      packages=["pyFreelingApi", "pyFreelingApi.windows_api", "pyFreelingApi.linux_api"],
      package_data={"pyFreelingApi.windows_api": ["_pyfreeling.pyd"]},
      description="Freeling Python APIs",
      long_description=open('README.md').read())
