from setuptools import setup

setup(
	name = 'Package',
	url = 'https://github.com/Yabudabi/Package',
	author = 'Yannick Bertschy',
	author_email = 'byannick@ethz.ch',
	packages = ['package'],
	install_requires = ['numpy'],
	version = '0.1',
	license = 'MIT',
	description = 'Python package'
	dependency_links=[
        'git+ssh://git@github.com/Yabudabi/Package/tree/master/package']
)