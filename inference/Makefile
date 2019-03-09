SHELL := /bin/bash

.PHONY: help
help:
	@echo "    clean-images"
	@echo "         Removes detected/labeled images directories."



.PHONY: clean-images
clean-images:
	rm -rf images


.PHONY: init-env
init-env:

	virtualenv venv;\
	source venv/bin/activate;\
	python3 -m pip install tensorflow==1.12.0 numpy==1.15.4 opencv-python==3.4.4.19 Cython==0.29.1 image==1.5.27 requests==2.20.1 flask-cors gunicorn;\
	cd darkflow; pip install .; cd ..;\
	cp -r darkflow/cfg inference;