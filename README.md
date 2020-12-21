# LexYamlGen

Tool to convert Bot Definition and Bot Template Excel files to Yaml.

## Development

### Dependencies

```bash
# (Optional) Create venv
python -m venv env

# (Optional) Activate venv
source env/bin/activate

# Install Python dependencies
pip install -r requirements-to-freeze.txt

# (Optional) Install Dev requirements
pip install -r requirements-dev.txt
```

### Usage

```bash
python lex_yaml_gen.py
```

### Building

Before building:

- Update `requirements.txt` with current pinned versions
- Ensure you are in a virtualenv with correct dependecies and Python version
- Ensure you are on the correct platform (Windows for Windows executables/msi, linux for linux, mac for mac, etc.)

To build an EXE and associated files:

```bash
python setup.py build
```

To build an MSI installer:

```bash
python setup.py bdist_msi
```
