from setuptools import setup

setup(
    name='serverbrowser',
    version='1.0.0',
    packages=['serverbrowser'],
    package_dir={'serverbrowser': 'trame'},
    package_data={'serverbrowser': ['build/*']},
    include_package_data=True,
)
