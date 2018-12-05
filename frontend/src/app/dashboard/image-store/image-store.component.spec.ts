import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { ImageStoreComponent } from './image-store.component';

describe('ImageStoreComponent', () => {
  let component: ImageStoreComponent;
  let fixture: ComponentFixture<ImageStoreComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ ImageStoreComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(ImageStoreComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
