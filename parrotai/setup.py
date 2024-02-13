from setuptools import setup, find_packages
setup(
name='parrotai',
version='0.1.0',
author='Andy Tran',
author_email='andy@joinparrot.ai',
description='API for Parrot AI - a decentralized AI.',
packages=find_packages(),
classifiers=[
'Programming Language :: Python :: 3',
'License :: OSI Approved :: MIT License',
'Operating System :: OS Independent',
],
python_requires='>=3.6',
)