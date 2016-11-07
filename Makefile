project := twindb_monitoring

.PHONY: virtualenv
virtualenv:
	virtualenv env --setuptools --prompt='(twindb_monitoring)'

.PHONY: rebuild-requirements
rebuild-requirements:
	pip-compile --verbose --no-index --output-file requirements.txt requirements.in
	pip-compile --verbose --no-index --output-file requirements-test.txt requirements-test.in

.PHONY: upgrade-requirements
upgrade-requirements:
	pip-compile --upgrade --verbose --no-index --output-file requirements.txt requirements.in
	pip-compile --upgrade --verbose --no-index --output-file requirements-test.txt requirements-test.in

.PHONY: bootstrap
bootstrap:
	pip install -U "setuptools==19.2"
	pip install -U "pip==7.1.2"
	pip install -U "pip-tools>=1.6.0"
	pip-sync requirements.txt requirements-test.txt
	pip install --editable .

.PHONY: test
test:
	py.test --flakes --full-trace --verbose --cache-clear tests/

.PHONY: clean
clean:
	@find . -name "*.pyc" -delete || true

.PHONY: clean-all
clean-all:
	rm -rf env
