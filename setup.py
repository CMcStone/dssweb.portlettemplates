from setuptools import setup, find_packages
import os

version = '0.1'

setup(name='dssweb.portlettemplates',
      version=version,
      description="add on templates for quintagroup NGCollection Portlet",
      long_description=open("README.rst").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?:action=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['dssweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          'collective.portlet.ngcollection',
          # -*- Extra requirements: -*-
      ],
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )