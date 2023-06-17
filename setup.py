from os.path import join, dirname, realpath
from setuptools import setup
import sys

assert sys.version_info.major == 3 and sys.version_info.minor >= 6, \
    "You should have Python 3.6 and greater." 

setup(
    name='thrifty',
    py_modules=['thrifty'],
    version='0.0.1',
    install_requires=[
        'mujoco-py==2.1.2.14',
        'cloudpickle',
        'gym',
        'joblib',
        'matplotlib',
        'numpy',
        'pandas',
        'pytest',
        'psutil',
        'scipy',
        'seaborn==0.8.1',
        'torch==1.13.1',
        'tqdm',
        'moviepy',
        'opencv-python',
        'torchvision',
        'robosuite==1.3.1',
        'h5py',
        'hidapi',
        'pygame'
    ],
    description="Code for ThriftyDAgger.",
    author="Ryan Hoque",
)