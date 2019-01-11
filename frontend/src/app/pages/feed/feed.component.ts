import { Component, OnInit, OnDestroy } from '@angular/core';

import { ImageService } from '../../services/image.service';
import { Subscription, interval } from 'rxjs';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.sass']
})
export class FeedComponent implements OnInit, OnDestroy {

  imageToShow: any;
  isImageLoading: boolean;
//   yourImageUrl = 'http://localhost:8000/video_feed';
  yourImageUrl = 'http://localhost:8001/image';
  sub: Subscription;

  constructor(private imageService: ImageService ) { }

  ngOnInit() {
    this.sub = interval(400).subscribe(() => this.getImageFromService());
    this.getImageFromService();
    setInterval(() => {
        this.getImageFromService();
    }, 400);
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
    this.isImageLoading = true;
    this.imageService.getImage(this.yourImageUrl).subscribe(data => {
      this.createImageFromBlob(data);
      this.isImageLoading = false;
    }, error => {
      this.isImageLoading = false;
      console.log(error);
    });
  }
}
