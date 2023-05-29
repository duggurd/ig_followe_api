import os
from setuptools import setup

directory = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(directory, 'README.md'), encoding='utf-8') as f:
  long_description = f.read()

setup(name='ig-follower-api',
      version='0.0.1',
      description='Python wrapper for Instagram API targeting followers of users',
      author='Alexander Haugerud',
      license='MIT',
      long_description=long_description,
      long_description_content_type='text/markdown',
      packages = ['ig_follower_api'],
      classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License"
      ],
      install_requires=['requests'],
      python_requires='>=3.8',
      include_package_data=True
)