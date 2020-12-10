import os
import sys
from setuptools import setup, find_packages



if os.getuid() != 0:
    print("ERROR : need run as root")
    sys.exit(0)

print("INFO: checking and installing requirement")
os.system('! dpkg -S python-imaging-tk && apt-get -y install-python-imaging-tk')


packages = []
print('INFO : generating the requirements from requirements.txt')

for line in open('requirements.txt'):
    if not line.startswith('#'):
        packages.append(line.strip())


setup(
    name ='modern mirror',
    version = '1.0.0',
    description = 'modern mirror with raspberry pi device for home smarthome',
    author = 'slowy07',
    url = 'https://www.github.com/slowy07',
    installRequires = packages,
    packages = find_packages()
)



#---------------
# if some error on wikipedia
# try install by command pip install wikipedia
#---------------