import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ImageStoreComponent } from './image-store/image-store.component';
import { AboutComponent } from './about/about.component';
import { SettingsComponent } from './settings/settings.component';

@NgModule({
  declarations: [ImageStoreComponent, AboutComponent, SettingsComponent],
  imports: [
    CommonModule
  ]
})
export class DashboardModule { }
