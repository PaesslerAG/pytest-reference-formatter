.PHONY: clean-python clean-build docs clean-tox
PYPI_SERVER?=pypi
GIT_REMOTE_NAME?=origin
SHELL=/bin/bash
VERSION=$(shell python -c"import pytest_reference_formatter as m; print(m.__version__)")

clean: clean-build clean-python clean-tox

clean-build:
	rm -fr build/
	rm -fr dist/
	find -name *.egg-info -type d | xargs rm -rf

clean-python:
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f {} +
	find . -name '__pycache__' -type d -exec rm -rf {} +

clean-tox:
	if [[ -d .tox ]]; then rm -r .tox; fi

release: TAG:=v${VERSION}
release: exit_code=$(shell git ls-remote ${GIT_REMOTE_NAME} | grep -q tags/${TAG}; echo $$?)
release:
ifeq ($(exit_code),0)
	@echo "Tag ${TAG} already present"
else
	git tag -a ${TAG} -m"${TAG}"; git push --tags ${GIT_REMOTE_NAME}
endif
