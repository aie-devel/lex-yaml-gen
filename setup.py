import os
import sys
from cx_Freeze import setup, Executable

BASE_DIR = os.path.abspath(os.path.dirname(__file__))
details = {}
with open(os.path.join(BASE_DIR, 'lex_yaml_gen.py'), mode='r', encoding='utf-8') as in_file:
    for line in in_file:
        if line.startswith('__title__'):
            details['__title__'] = line.split("'")[1]
        if line.startswith('__description__'):
            details['__description__'] = line.split("'")[1]
        if line.startswith('__version__'):
            details['__version__'] = line.split("'")[1]

BASE = None
# Comment out the following for access to the console when running the applcation
if sys.platform == 'win32':
    BASE = 'Win32GUI'

includes = []
include_files = ['sample_bot_definition.xlsx', 'sample_bot_template.xlsx']
excludes = []
packages = [
    'openpyxl',
    'ruamel.yaml',
]
path = []

EXECUTABLES = [
    Executable(
        script='lex_yaml_gen.py',
        base=BASE,
        icon='welocalize.ico',
        shortcutName="Lex Yaml Gen",
        shortcutDir="StartMenuFolder")
]

setup(
    name=details['__title__'],
    version=details['__version__'],
    description=details['__description__'],
    author='Welocalize',
    options={
        'build_exe': {
            'includes': includes,
            'include_files': include_files,
            'excludes': excludes,
            'packages': packages,
            'path': path
        }
    },
    executables=EXECUTABLES)
