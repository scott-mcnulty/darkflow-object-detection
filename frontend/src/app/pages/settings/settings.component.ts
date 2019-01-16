import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';

import { AppSettingsService } from 'src/app/services/app-settings.service';
import { SettingsForm } from './settings-form';

@Component({
  selector: 'app-settings',
  templateUrl: './settings.component.html',
  styleUrls: ['./settings.component.sass']
})
export class SettingsComponent implements OnInit {

  model = new SettingsForm(
      this.appSettingsService.getSetting('cameraServerHostname'),
      this.appSettingsService.getSetting('cameraServerPort'),
      this.appSettingsService.getSetting('inferenceServerHostname'),
      this.appSettingsService.getSetting('inferenceServerPort'));

  constructor(private appSettingsService: AppSettingsService) { }

  ngOnInit() {
  }

  onSubmit(form: NgForm) {
    console.log(form.value);
    this.appSettingsService.setSetting('cameraServerHostname', form.value['cameraServerHostname']);
    this.appSettingsService.setSetting('cameraServerPort', form.value['cameraServerPort']);
    this.appSettingsService.setSetting('inferenceServerHostname', form.value['inferenceServerHostname']);
    this.appSettingsService.setSetting('inferenceServerPort', form.value['inferenceServerPort']);
    this.appSettingsService.generateNewServerUrls();
  }
}
