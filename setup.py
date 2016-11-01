from setuptools import setup, find_packages

setup(name='datascience_utils',
      version='1.0',
      description="Various data analysis scripts, useful for command line data mining and exploration. Most scripts work on csv numeric data with some configurable separator, defaulting to \t, with optional header-handling.",
      author="josh attenberg",
      author_email="jattenbe@stern.nyu.edu",
      url="https://github.com/jattenberg/datascience-utilities",
      packages=find_packages(),
      install_requires=[
        'pandas',
        'scipy',
        'numpy',
        'matplotlib',
        'seaborn'
      ]
      )
