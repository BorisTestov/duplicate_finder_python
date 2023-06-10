import os
import re

version = os.getenv('GITHUB_REF')
version = version.replace('refs/tags/', '')
version_parts = re.findall(r'\d+', version)
major = version_parts[0]
minor = version_parts[1]
patch_with_suffix = version_parts[2]
patch = patch_with_suffix.split('_')[0]
build_number = os.getenv('BUILD_NUMBER')

with open('version.py', 'w') as f:
    f.write(f'APP_VERSION = "{major}.{minor}.{patch}"\n')
    f.write(f'BUILD_NUMBER = "{build_number}"\n')

with open('version.py', 'r') as f:
    print(f.read())
