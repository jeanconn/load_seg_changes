from distutils.core import setup

setup(name='load_seg_changes',
      version='0.1',
      description='display changes in ingested load segments over time',
      author='Jean Connelly',
      author_email='jeanconn@head.cfa.harvard.edu',
      packages=['load_seg_changes', 'load_seg_changes.web'],
      package_data={'load_seg_changes.web':
                        ['templates/*/*.html', 'templates/*.html']},
      license='BSD',
      )
