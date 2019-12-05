from distutils.core import setup

setup(
  name = 'package',
  packages = ['package'], 
  version = '0.1',
  license='MIT',
  description = 'TYPE YOUR DESCRIPTION HERE',
  author = 'YOUR NAME',
  author_email = 'your.email@domain.com',
  url = 'https://github.com/Yabudabi/package',
  download_url = 'https://github.com/Yabudabi/package/archive/v_01.zip',
  keywords = ['SOME', 'MEANINGFULL', 'KEYWORDS'],   # Keywords that define your package best
  install_requires=[
          'numpy',
          'scrapeasy',
      ],
  dependency_links=['https://github.com/Yabudabi/package/tarball/master#egg=gearman-2.0.0beta'],
)