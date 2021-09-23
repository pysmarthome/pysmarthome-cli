from setuptools import setup, find_packages

setup(
    name='pysmarthome-cli',
    description='A command line interface for pysmarthome',
    version='0.0.0',
    author='Filipe Alves',
    author_email='filipe.alvesdefernando@gmail.com',
    install_requires=[
        'gql[aiohttp]',
    ],
    packages=find_packages(),
    scripts=['pysmarthome'],
    url='https://github.com/filipealvesdef/pysmarthome-cli/',
    zip_safe=False,
)
