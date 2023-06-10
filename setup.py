import glob
import os
import setuptools

with open("pypi.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(name = 'smashpy',
                 version = open("smashpy/_version.py").readlines()[-1].split()[-1].strip("\"'"),
                 description = 'SMaSH: A scalable, general marker gene identification framework for single-cell RNA sequencing and Spatial Transcriptomics',
                 long_description=long_description,
                 author = 'Simone Riva',
                 author_email = 'sgr34@cam.ac.uk',
                 url = 'https://gitlab.com/cvejic-group/smash',
                 license='LICENSE',
                 classifiers = ['Programming Language :: Python :: 3.6'],
                 python_requires='>=3.6',
                 packages=setuptools.find_packages(where='smashpy'),
                 package_dir={'': 'smashpy'},
                 py_modules=[os.path.splitext(os.path.basename(path))[0] for path in glob.glob('smashpy/*.py')],
                 install_requires=[ 'shap>=0.37.0',
                                    'matplotlib>=3.3.2',
                                    'scanpy>=1.7.1',
                                    'pandas>=0.25.2',
                                    'seaborn>=0.11.0',
                                    'tensorflow==2.5.0',
                                    'numpy>=1.19.2',
                                    'scikit-learn>=0.23.1',
                                    'xgboost>=1.3.3',
                                    'keras>=2.4.3',
                                    'imbalanced-learn>=0.7.0',
                                    'numba>=0.51.2', 
                                    'harmonypy>=0.0.5',
                                    'plotly>=4.0.0']
                )
