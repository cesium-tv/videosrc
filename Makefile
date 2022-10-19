SRC=$(shell find vidsrc/ -name "*.py")


/usr/bin/virtualenv:
	sudo apt install python3-virtualenv


dist/vidsrc-?.?.?-*.whl: $(SRC)
	python3 setup.py bdist_wheel


build: dist/vidsrc-?.?.?-*.whl
	python3 setup.py bdist_wheel


.venv: requirements.txt /usr/bin/virtualenv
	virtualenv -p python3 .venv
	.venv/local/bin/pip install -r requirements.txt
	.venv/local/bin/pip install flake8 responses-server
	touch .venv


.PHONY: test
test: .venv
	.venv/local/bin/python3 -m unittest tests/test_*.py


.PHONY: lint
lint: .venv
	.venv/local/bin/python3 -m flake8 vidsrc/


.PHONY: ci
ci: lint test


.PHONY: clean
clean:
	rm -rf dist build vidsrc.egg-info .venv