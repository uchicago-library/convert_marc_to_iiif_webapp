from setuptools import setup, find_packages


def readme():
    with open("README.md", 'r') as f:
        return f.read()


setup(
    name="convert_marc_to_iiif_webapp",
    description="A web application intended to be able to a) extract a MARC record from the Solr index and b) generate IIIF record",
    version="1.0.0",
    long_description=readme(),
    author="Tyler Danstrom",
    author_email="tdanstrom@uchicago.edu",
    packages=find_packages(
        exclude=[
        ]
    ),
    include_package_data=True,
    url='https://github.com/verbalhanglider/convert_marc_to_iiif_webapp',
    dependency_links = [
        'https://github.com/uchicago-library/marc2iiif/tarball/master#egg=marc2iiif',
        'https://github.com/uchicago-library/extract_marc_from_vufind/tarball/master#egg=marcExtraction'
   ],
    install_requires=[
    ],
    tests_require=[
        'pytest'
    ],
    test_suite='tests',
    entry_points = {
        'console_scripts': [
            'find_records=OLEMarcMigration.search.__main__:main'
        ]
    }
)
