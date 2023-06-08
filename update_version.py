import os
import re

version = f"{os.getenv('MAJOR', 0)}.{os.getenv('MINOR', 0)}.{os.getenv('PATCH', 0)}"
build_number = os.getenv('BUILD_NUMBER')

if version:
    with open('version.py', 'r') as file:
        filedata = file.read()

    filedata = re.sub(r'APP_VERSION = "[^"]*"', 'APP_VERSION = "{}"'.format(version), filedata)

    with open('version.py', 'w') as file:
        file.write(filedata)

if build_number:
    with open('version.py', 'r') as file:
        filedata = file.read()

    filedata = re.sub(r'BUILD_NUMBER = "[^"]*"', 'BUILD_NUMBER = "{}"'.format(build_number), filedata)

    with open('version.py', 'w') as file:
        file.write(filedata)
