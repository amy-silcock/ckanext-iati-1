from setuptools import setup, find_packages
import sys, os

version = '0.1'

setup(name='ckanextiati',
      version=version,
      description="CKAN Extension Code for the IATI Registry",
      long_description="""\
""",
      classifiers=[], # Get strings from http://pypi.python.org/pypi?%3Aaction=list_classifiers
      keywords='iati un aid openaid',
      author='Open Knowledge Foundation',
      author_email='info@okfn.org',
      url='http://www.okfn.org',
      license='',
      packages=find_packages(exclude=['ez_setup', 'examples', 'tests']),
      include_package_data=True,
      namespace_packages=['ckanext'],
      zip_safe=False,
      install_requires=[
          # -*- Extra requirements: -*-
          'ckanclient>=0.3',
          'lxml>2.2.6'
      ],
      entry_points="""
      # -*- Entry points: -*-
      
      [ckan.plugins]
      iati = ckanext.iati:IatiPlugin
      
      [ckan.forms]
      iati_package = ckanext.iati.forms:get_iati_package_fieldset
      iati_group = ckanext.iati.forms:get_iati_group_fieldset
      """,
      )