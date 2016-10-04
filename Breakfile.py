from breakable import *
import os

class BreakTasks(object):
    def clean(self):
        """ Recursively remove *.pyc files """
        rm("-r venv/")
        for pyc in find_files(r".*\.pyc"):
            rm(pyc)

    def test(self):
        """ Run all tests """
        self.check_style()
        self.unittests()

    def clean_branches(self):
        """ Remove all merged branches """
        git = which("git")
        for branch in git.collect("branch --merged | grep -v '*' | grep -v master"):
            git("branch -d %s" % branch)

    def check_style(self):
        self.install_requirements()
        self.setup_venv()
        self.with_venv("flake8")

    def unittests(self):
        self.install_requirements()
        self.setup_venv()
        self.with_venv("nosetests --with-coverage --cover-min-percentage=100 --cover-html --cover-html-dir=htmlcov")

    def install_requirements(self):
        if not path("venv/").exists:
            needs("requirements.txt")
            self.setup_venv()
            self.with_venv("pip install --upgrade pip")
            self.with_venv("pip install -r requirements.txt")

    def setup_venv(self):
        if not hasattr(self, 'with_venv'):
            self.find_pyvenv()
            if not os.path.exists("venv/"):
                self.pyvenv("venv/")
            self.with_venv = Executable("source venv/bin/activate && ")

    def find_pyvenv(self):
        if not hasattr(self, 'pyvenv'):
            self.pyvenv = which('pyvenv') or which('virtualenv')
