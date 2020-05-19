import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { OtherUserProfileComponent } from './other-user-profile.component';

describe('OtherUserProfileComponent', () => {
  let component: OtherUserProfileComponent;
  let fixture: ComponentFixture<OtherUserProfileComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ OtherUserProfileComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(OtherUserProfileComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
