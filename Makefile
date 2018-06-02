PYTHON	= $(shell which python)

TOPDIR  = $(shell pwd)
PYDIR	= kokudaka

OC_SOURCE	= registry.access.redhat.com/openshift3/ose
OC_VERSION	= v3.7
OC_DATA_DIR	= ${HOME}/.oc/openshift.local.data

OS := $(shell uname)
ifeq ($(OS),Darwin)
	PREFIX	=
else
	PREFIX	= sudo
endif

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  clean                    to clean the project directory of any scratch files, bytecode, logs, etc."
	@echo "  help                     to show this message"
	@echo "  lint                     to run linting against the project"
	@echo "  serve                    to run the Flask dev server locally"
	@echo "  unittest                 to run unittests"

clean:
	git clean -fdx -e .idea/ -e *env/

lint:
	tox -elint

unittest:
	tox -e py36

serve:
	export FLASK_APP=kokudaka; export FLASK_ENV=development; flask run