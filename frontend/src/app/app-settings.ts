export class AppSettings {

    // Camera server settings
    cameraServerHostname = '192.168.1.3';
    cameraServerPort = '8000';
    cameraServerUrl = 'http://' + this.cameraServerHostname + ':' + this.cameraServerPort;

    // Inference server settings
    inferenceServerHostname = '192.168.1.3';
    inferenceServerPort = '8001';
    inferenceServerUrl = 'http://' + this.inferenceServerHostname + ':' + this.inferenceServerPort;
}
