from setuptools import setup
import os.path

current_dir = os.path.abspath(os.path.dirname(__file__))
with open(os.path.join(current_dir, 'README.md')) as rdr:
    long_description = rdr.read()

setup(name='pymonkey',
      version='0.1.0',
      description='Monkey interpreter',
      long_description=long_description,
      url='http://github.com/adamvinueza/pymonkey',
      author='Adam Vinueza',
      author_email='adamvinueza@pm.me',
      license='Apache 2.0',
      packages=['pymonkey'],
      classifiers=[
          'Development Status :: 1 - Planning',
          'Intended Audience :: Developers',
          'License :: OSI Approved :: MIT License',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7'
      ],
      zip_safe=False)
