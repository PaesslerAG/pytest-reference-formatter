.PHONY: clean-python clean-build docs clean-tox
PYPI_SERVER?=pypi
GIT_REMOTE_NAME?=origin
SHELL=/bin/bash
VERSION=$(shell python -c"import pytest_reference_formatter as m; print(m.__version__)")

release: TAG:=v${VERSION}
release: exit_code=$(shell git ls-remote ${GIT_REMOTE_NAME} | grep -q tags/${TAG}; echo $$?)
release:
ifeq ($(exit_code),0)
	@echo "Tag ${TAG} already present"
else
	git tag -a ${TAG} -m"${TAG}"; git push --tags ${GIT_REMOTE_NAME}
endif
