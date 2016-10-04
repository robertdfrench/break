from breakable import *

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
        """ Enforce PEP8 guidelines """
        self.install_requirements()
        self.setup_venv()
        self.with_venv("flake8")

    def unittests(self):
        """ Run all unittests and measure coverage """
        self.install_requirements()
        self.setup_venv()
        self.with_venv("nosetests --with-coverage --cover-min-percentage=100 --cover-html --cover-html-dir=htmlcov")

    def install_requirements(self):
        """ Install packages into virtual environment """
        if not path("venv/").exists:
            needs("requirements.txt")
            self.setup_venv()
            self.with_venv("pip install --upgrade pip")
            self.with_venv("pip install -r requirements.txt")

    def setup_venv(self):
        """ Create empty virtual environment """
        if not hasattr(self, 'with_venv'):
            self.find_pyvenv()
            if not path("venv/").exists:
                self.pyvenv("venv/")
            self.with_venv = Executable("source venv/bin/activate && ")

    def find_pyvenv(self):
        """ Find pyvenv or virtualenv commands """
        if not hasattr(self, 'pyvenv'):
            self.pyvenv = which('pyvenv') or which('virtualenv')
