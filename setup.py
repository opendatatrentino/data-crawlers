from setuptools import setup, find_packages

version = '0.1a'

install_requires = [
    'stevedore',
    'pymongo',
]

entry_points = {
    'harvester.ext.crawlers': [

        'pat_statistica = harvester.ext.crawlers.odt'
        '.pat_statistica:Statistica',

        'pat_statistica_subpro = harvester.ext.crawlers.odt'
        '.pat_statistica:StatisticaSubPro',
    ],
    'harvester.ext.storage': [
        "jsondir = harvester.ext.storage.jsondir:JsonDirStorage",
        "memory = harvester.ext.storage.memory:MemoryStorage",
        "mongodb = harvester.ext.storage.mongodb:MongodbStorage",
        "sqlite = harvester.ext.storage.sqlite:SQLiteStorage",
    ],
}

setup(
    name='ckan-api-client',
    version=version,
    packages=find_packages(),
    url='http://rshk.github.io/ckan-api-client',
    license='BSD License',
    author='Samuele Santi',
    author_email='s.santi@trentorise.eu',
    description='',
    long_description='',
    install_requires=install_requires,
    # tests_require=tests_require,
    test_suite='ckan_api_client.tests',
    classifiers=[
        "License :: OSI Approved :: BSD License",
        "Development Status :: 3 - Alpha",
        "Programming Language :: Python :: 2.7",
    ],
    package_data={'': ['README.md', 'LICENSE']},
    # cmdclass={'test': PyTest},
    entry_points=entry_points)
