from setuptools import find_packages, setup

with open('README.me', 'r') as f:
	long_description = f.read()

setup(
	name='pgbackup',
	version='0.1.0',
	author='Tadas Narbutas',
	author_email='narbutas.tadas@gmail.com',
	descrption='CLI tool for PostgreSQL backup'
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/narbutas/pgbackup',
	packages=find_packages('src')
	)