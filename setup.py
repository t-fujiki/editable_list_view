from setuptools import setup, find_packages
import pathlib

here = pathlib.Path(__file__).parent.resolve()

long_description = (here / 'README.md').read_text(encoding='utf-8')

# Arguments marked as "Required" below must be included for upload to PyPI.
# Fields marked as "Optional" may be commented out.

setup(
    name='editable_list_view',  
    version='1.0.0', 
    description='Editable list view for Django', 
    long_description=long_description, 
    long_description_content_type='text/markdown',  
    url='https://github.com/t-fujiki/editable_list_view', 
    author='Takaaki Fujiki',  
    author_email='',  
    classifiers=[ 
        'License :: OSI Approved :: MIT License',

        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        "Programming Language :: Python :: 3.10",
        'Programming Language :: Python :: 3 :: Only',
    ],

    keywords='django, python, listview', 
    package_dir={'': 'src'}, 
    packages=find_packages(where='src'),
    python_requires='>=3.6, <4',
    install_requires=['django'],  

)
