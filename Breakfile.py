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
        self.with_venv("flake8")

    def unittests(self):
        """ Run all unittests and measure coverage """
        self.install_requirements()
        self.with_venv("nosetests --with-coverage --cover-min-percentage=100 --cover-html --cover-html-dir=htmlcov")

    @only_if_modified("requirements.txt")
    def install_requirements(self):
        """ Install packages into virtual environment """
        self.pip("install --upgrade pip")
        self.pip("install -r requirements.txt")

    @belhorn_property
    def pip(self):
        return lambda x: self.with_venv("pip %s" % x)

    @belhorn_property
    def with_venv(self):
        if not path("venv/").exists:
            self.pyvenv("venv/")
        return Executable("source venv/bin/activate && ")

    @belhorn_property
    def pyvenv(self):
        return which('pyvenv') or which('virtualenv')
