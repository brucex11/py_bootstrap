# Python Production Project Bootstrap

The goal here is to provide a somewhat production ready python project bootstrap. 
Simply put, clone it and have ready starting point for your python project.

Here is the GitHub source: https://github.com/fgka/python-bootstrap.git

## File Sturcture and Test Access
Here is a basic python project file structure: https://docs.python-guide.org/writing/structure/

```
Once a test suite grows, you can move your tests to a directory, like so:

tests/test_basic.py
tests/test_advanced.py
Obviously, these test modules must import your packaged module to test it. You
can do this a few ways:

Expect the package to be installed in site-packages.
Use a simple (but explicit) path modification to resolve the package properly.
I highly recommend the latter. Requiring a developer to run setup.py develop
to test an actively changing codebase also requires them to have an isolated
environment setup for each instance of the codebase.

To give the individual tests import context, create a tests/context.py file:

    import os
    import sys
    sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
    import sample
```

## Get Started After Initial Clone
1. Rename 'my_prog.py' to the name of the binary/executable.
2. In 'setup.py' change NAME and DESCRIPTION.
3. Changes for testing TBD.

See project here for a simple example: https://gitlab.nist.gov/gitlab/projectsoftware/nfract/nfract_xml.git

### TODO List
27Oct2022
 'my_prog.py' has been removed so step 1 above in (still) not correct.
This should be corrected/updated after the next few (new) python projects are
generated.

XXxxx2022

## Development 

### Development Environments Using Pyenv and Virtualenv

#### Windows

#### Linux


#### Pyenv


Set python 3.10 as default:
```basn
pyenv install 3.10.8
```

Set pyenv defaults:
```bash
pyenv global 3.10.8
pyenv local 3.10.8
```

#### Virtualenv

Install Virtualenv and update `pip`:
```bash
pip3 install -U pip virtualenv
```

Create virtualenv:
```bash
cd <Your project root dir>

virtualenv -p python3 -q .venv
```

To activate your python virtualenv:
```bash
. .venv/bin/activate
```

Validate with:
```bash
python --version
python3 --version
```

### Install all dependencies

Install packages:
```bash
pip install ".[dev]"
```

### Auto-formatting with black

In this project black was chosen for the auto-formatter.

[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/python/black)

#### Install black with vim

After following the instructions I have in my ``~/.vimrc`` the following:

```vimrc
" black formatter
let g:black_linelength=79
let g:black_skip_string_normalization=1
autocmd BufWritePre *.py execute ':Black'
```

