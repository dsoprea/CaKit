import setuptools
import os

import ck

app_path = os.path.dirname(ck.__file__)

with open(os.path.join(app_path, 'resources', 'README.rst')) as f:
      long_description = f.read()

with open(os.path.join(app_path, 'resources', 'requirements.txt')) as f:
      install_requires = list(map(lambda s: s.strip(), f.readlines()))

setuptools.setup(
      name='ca_kit',
      version=ck.__version__,
      description="Certificate-authority test harness.",
      long_description=long_description,
      classifiers=[],
      keywords='ssl openssl ca certificate',
      author='Dustin Oprea',
      author_email='myselfasunder@gmail.com',
      url='https://github.com/dsoprea/CaKit',
      license='GPL 2',
      packages=setuptools.find_packages(exclude=['dev']),
      include_package_data=True,
      zip_safe=False,
      install_requires=install_requires,
      package_data={
            'ck': ['resources/README.rst',
                   'resources/requirements.txt'],
      },
      scripts=[
            'ck/resources/scripts/ck_create_ca',
            'ck/resources/scripts/ck_create',
            'ck/resources/scripts/ck_sign',
            'ck/resources/scripts/ck_verify_ca',
      ],
)
