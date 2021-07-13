
from setuptools import setup, find_packages
# 已經改為 remoteApi.dll

install_requires=[
    'gym',
    'numpy'
]

setup(name='vrep_env',
      version='0.0.2',
      description='V-REP integrated with OpenAI Gym',
      url='https://github.com/ycps/vrep-env',
      packages=[package for package in find_packages() if package.startswith('vrep_env')],
      install_requires=install_requires,
      package_data={'': ['remoteApi.dll']},
      include_package_data=True
)
