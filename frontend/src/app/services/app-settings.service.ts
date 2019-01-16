import { Injectable } from '@angular/core';

import { AppSettings } from '../app-settings';

@Injectable({
  providedIn: 'root'
})
export class AppSettingsService {

  appSettings: AppSettings;

  constructor() {
    this.appSettings = new AppSettings();
  }

  getSettings(): AppSettings {
    return this.appSettings;
  }

  getSetting(key) {
    return this.appSettings[key];
  }

  setSetting(key, value) {
    this.appSettings[key] = value;
  }

  generateNewCameraServerUrl() {
    const newCameraServerUrl = 'http://' +
        this.getSetting('cameraServerHostname') +
        ':' +
        this.getSetting('cameraServerPort');

    this.setSetting('cameraServerUrl', newCameraServerUrl);
  }

  generateNewInferenceServerUrl() {
    const newInferenceServerUrl = 'http://' +
        this.getSetting('inferenceServerHostname') +
        ':' +
        this.getSetting('inferenceServerPort');

    this.setSetting('inferenceServerUrl', newInferenceServerUrl);
  }

  generateNewServerUrls() {
    this.generateNewCameraServerUrl();
    this.generateNewInferenceServerUrl();
  }
}
