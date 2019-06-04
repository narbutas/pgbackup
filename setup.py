from setuptools import find_packages, setup

with open('README.md', 'r') as f:
	long_description = f.read()

setup(
	name='pgbackup',
	version='1.0.0',
	author='Tadas Narbutas',
	author_email='narbutas.tadas@gmail.com',
	descrption='CLI tool for PostgreSQL backup',
	summary='CLI tool for PostgreSQL backup',
	license='Apache License 2.0',
	long_description=long_description,
	long_description_content_type='text/markdown',
	url='https://github.com/narbutas/pgbackup',
	packages=find_packages('src'),
	package_dir={'': 'src'},
	install_requires=['boto3'],
	python_requires='>=3.6',
	entry_points={
		'console_Scripts': [
			'pgbackup=pgbackup.cli.main'
		]
	}
)