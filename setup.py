from setuptools import setup

setup(name="epiphany-editor",
      version="0.4.2",
      description="Map Editor for Epiphany (a Boulder-Dash clone).",
      author="teratorn",
      author_email="epiphany-editor /AT/ teratorn /DOT/ net",
      url='https://github.org/teratorn/epiphany-editor',
      license='MIT',
      scripts=['epiphany-editor'],
      install_requires=['pygame', 'PyGObject'],
      classifiers=[
          'Development Status :: 5 - Production/Stable',
          'Environment :: X11 Applications :: GTK',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3 :: Only',
      ]
      )
