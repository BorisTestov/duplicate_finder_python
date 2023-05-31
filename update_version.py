import os
import re

# Get the version and build number from the environment variables
version = f"{os.getenv('MAJOR', 0)}.{os.getenv('MINOR', 0)}.{os.getenv('PATCH', 0)}"
build_number = os.getenv('APPVEYOR_BUILD_NUMBER')

if version:
    # Read in the file
    with open('version.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub(r'APP_VERSION = "[^"]*"', 'APP_VERSION = "{}"'.format(version), filedata)

    # Write the file out again
    with open('version.py', 'w') as file:
        file.write(filedata)

if build_number:
    # Read in the file again (in case it was rewritten above)
    with open('version.py', 'r') as file:
        filedata = file.read()

    # Replace the target string
    filedata = re.sub(r'BUILD_NUMBER = "[^"]*"', 'BUILD_NUMBER = "{}"'.format(build_number), filedata)

    # Write the file out again
    with open('version.py', 'w') as file:
        file.write(filedata)
