from setuptools import setup, find_packages
setup(
        version=0.1,
        name="pyaqadvisor",
        package_dir={'pyaqadvisor': 'pyaqadvisor'},
        packages=find_packages(),
        install_requires=[
            'fuzzywuzzy',
            'BeautifulSoup',
            'requests',
#'python-Levenshtein',
            ],
        extras_require = {
            }
        )
