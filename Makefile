SRC=$(shell find vidsrc/ -name "*.py")


dist/vidsrc-?.?.?-*.whl: $(SRC)
	python3 setup.py bdist_wheel


build: dist/vidsrc-?.?.?-*.whl
	python3 setup.py bdist_wheel


clean:
	rm -rf dist build vidsrc.egg-info
