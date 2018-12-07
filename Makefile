.PHONY: help
help:
	@echo "    build-camera-server-image"
	@echo "         Builds the camera server docker image."
	@echo "    build-frontend-image"
	@echo "         Builds the frontend docker image."



.PHONY: build-camera-server-image
build-camera-server-image:
	docker build . -f docker/CameraServerDockerfile -t darkflow-object-detection:camera-server


.PHONY: build-frontend-image
build-frontend-image:
	docker build . -f docker/FrontendDockerfile -t darkflow-object-detection:frontend
