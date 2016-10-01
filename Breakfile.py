from breakable import *
import os

python = which('python')
pyvenv = which('pyvenv') or which('virtualenv')

@entrypoint
def test():
    with_venv = setup_venv()
    with_venv("flake8")
    with_venv("nosetests --with-coverage --cover-min-percentage=100 --cover-html --cover-html-dir=htmlcov")

@entrypoint
def setup_venv():
    pyvenv("venv/")
    with_venv = Executable("source venv/bin/activate && ")
    with_venv("pip install --upgrade pip")
    with_venv("pip install -r requirements.txt")
    return with_venv

@entrypoint
def clean():
    for root, dirs, files in os.walk("."):
        for f in files:
            if f.endswith('.pyc'):
                rm(os.path.join(root, f))
