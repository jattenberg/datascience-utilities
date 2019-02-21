from setuptools import setup, find_packages

setup(name='datascience-utilities',
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
          'seaborn',
          "statsmodels"
      ],
      entry_points={
          'console_scripts': [
              "plot_hist=datascience_utilities.plotHist:main",
              "plot_xy=datascience_utilities.plotXY:main",
              "plot_hex=datascience_utilities.plotHex:main",
              "describe=datascience_utilities.describe:main",
              "ztest=datascience_utilities.ztest:main",
              "normal=datascience_utilities.normal:main",
              "reservoir_sample=datascience_utilities.reservoirSampling"
          ]
      }
)
