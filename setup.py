from distutils.core import setup
from setuptools import find_packages

setup(
    name='twindb_monitoring',
    version='0.1',
    packages=find_packages(),
    include_package_data=True,
    url='https://github.com/twindb/monitoring',
    license='Apache License Version 2.0',
    author='Ovais Tariq',
    author_email='ovaistariq@gmail.com',
    description='Scripts for configuring and setting up monitoring',
    entry_points='''
        [console_scripts]
        dd_generate_dashboards=dd.generate_dashboards:cli
    ''',
)
