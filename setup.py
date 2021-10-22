#
# pkmodel setuptools script
#
from setuptools import setup, find_packages


def get_version():
    """
    Get version number from the pkmodel module.
    """
    from pkmodel.version_info import VERSION as version
    return version


def get_readme():
    """
    Load README.md text for use as description.
    """
    with open('README.md') as f:
        return f.read()


# Go!
setup(
    # Module name (lowercase)
    name='pkmodel',

    # Version
    version=get_version(),

    description='Pharmokinetics Modelling Library.',

    long_description=get_readme(),

    license='MIT license',

    author=("Elliot Barbeary, "
            "Mona Furukawa, "
            "Hazel Wee Ling, "
            "Ian McFarlane, "
            "Oliver Turnbull"),

    author_email=("elliot.barbeary@dtc.ox.ac.uk, "
                  "mona.furukawa@dtc.ox.ac.uk, "
                  "hazel.wee@dtc.ox.ac.uk, "
                  "ian.mcfarlane@dtc.ox.ac.uk, "
                  "oliver.turnbull@dtc.ox.ac.uk"),

    maintainer='Ian McFarlane',

    maintainer_email='ian.mcfarlane@dtc.ox.ac.uk',

    url='https://github.com/ian-mcfarlane/pk-modelling/',

    # Packages to include
    packages=find_packages(include=('pkmodel', 'pkmodel.*')),

    # List of dependencies
    install_requires=[
        # Dependencies go here!
        'numpy',
        'matplotlib',
        'scipy',
        'abc',
        'datetime'
    ],
    extras_require={
        'docs': [
            # Sphinx for doc generation. Version 1.7.3 has a bug:
            'sphinx>=1.5, !=1.7.3',
            # Nice theme for docs
            'sphinx_rtd_theme',
        ],
        'dev': [
            # Flake8 for code style checking
            'flake8>=3', 
            # Unittest for testing main codes: testsolution, testprotocol, testmodel.
            'unittest'
        ],
    },
)
