from setuptools import setup, find_packages

setup(name='datascience-utilities',
      version='1.1',
      description="Various data analysis scripts, useful for command line data mining and exploration. Most scripts work on csv numeric data with some configurable separator, defaulting to \t, with optional header-handling.",
      author="josh attenberg",
      author_email="jattenbe@stern.nyu.edu",
      url="https://github.com/jattenberg/datascience-utilities",
      download_utl="https://github.com/jattenberg/datascience-utilities/archive/0.1.1.tar.gz",
      packages=find_packages(),
      install_requires=[
          'pandas',
          'scipy',
          'numpy',
          'matplotlib',
          'seaborn',
          "statsmodels",
      ],
      extras_require={
          "iterm":["itermplot"]
      },
      entry_points={
          'console_scripts': [
              "plot_hist=datascience_utilities.plotHist:main",
              "plot_xy=datascience_utilities.plotXY:main",
              "plot_hex=datascience_utilities.plotHex:main",
              "describe=datascience_utilities.describe:main",
              "ztest=datascience_utilities.ztest:main",
              "normal=datascience_utilities.normal:main",
              "exponential=datascience_utilities.exponential:main",
              "poisson=datascience_utilities.poisson:main",
              "reservoir_sample=datascience_utilities.reservoirSampling:main",
              "csv_to_json=datascience_utilities.csv_to_json:main",
              "json_to_csv=datascience_utilities.json_to_csv:main",
          ]
      }
)
