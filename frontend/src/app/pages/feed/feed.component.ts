import { Component, OnInit, OnDestroy } from '@angular/core';
import { Subscription, interval } from 'rxjs';

import { ImageService } from '../../services/image.service';
import { AppSettingsService } from '../../services/app-settings.service';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.sass']
})
export class FeedComponent implements OnInit, OnDestroy {

  imageToShow: any;
  imageRefresh = 100;
  sub: Subscription;

  constructor(private imageService: ImageService, private appSettingsService: AppSettingsService ) { }

  ngOnInit() {
    this.sub = interval(this.imageRefresh).subscribe(() => this.getImageFromService());
  }

  ngOnDestroy() {
      this.sub.unsubscribe();
  }

  createImageFromBlob(image: Blob) {
    const reader = new FileReader();

    reader.addEventListener('load', () => {
        this.imageToShow = reader.result;
    }, false);

    if (image) {
        reader.readAsDataURL(image);
    }
  }

  getImageFromService() {
    this.imageService.getImage(this.appSettingsService.getSetting('cameraServerUrl') + '/image').subscribe(data => {
      this.createImageFromBlob(data);
    }, error => {
      this.sub.unsubscribe();
      console.log(error);
    });
  }
}
