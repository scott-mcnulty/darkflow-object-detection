.PHONY: help
help:
	@echo "    camera-server-image"
	@echo "         Builds the camera server docker image."



.PHONY: camera-server-image
camera-server-image:
	docker build . -f docker/CameraServerDockerfile -t darkflow-object-detection:camera-server
