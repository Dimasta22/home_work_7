from setuptools import  setup, find_namespace_packages

setup(
    name='clean_folder',
    version='0.0.1',
    description='Clean folder project with previous dev(Home work 7)',
    author='Dima Serdiuk',
    author_email='serdyuk0002@gmail.com',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    packages=find_namespace_packages(),
    entry_points={'console_scripts': [
        'clean_folder=clean_folder.clean:start']}
)