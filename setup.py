from setuptools import setup

setup(name="epiphany-editor",
      version="0.3.1",
      description="Map Editor for Epiphany (a Boulder-Dash clone).",
      author="teratorn",
      author_email="epiphany-editor /AT/ teratorn /DOT/ net",
      scripts=['epiphany-editor'],
      # depending on pygtk explicitly here is problematic in that it can't
      # just be fetched from pypi and built like most dependencies.
      #install_requires=['pygtk', 'pygame']
      install_requires=['pygame']
      )
