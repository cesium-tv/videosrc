SRC=$(shell find videosrc/ -name "*.py")


/usr/bin/virtualenv:
	sudo apt install python3-virtualenv


dist/videosrc-?.?.?-*.whl: $(SRC)
	python3 setup.py bdist_wheel


build: dist/videosrc-?.?.?-*.whl
	python3 setup.py bdist_wheel


.venv: requirements.txt /usr/bin/virtualenv
	virtualenv -p python3 .venv
	.venv/bin/pip install -r requirements.txt
	.venv/bin/pip install flake8 ../responses-server
	touch .venv


.PHONY: test
test: .venv
	.venv/bin/python3 -m unittest tests


.PHONY: lint
lint: .venv
	.venv/bin/python3 -m flake8 videosrc/


.PHONY: ci
ci: lint test


.PHONY: clean
clean:
	rm -rf dist build videosrc.egg-info .venv
