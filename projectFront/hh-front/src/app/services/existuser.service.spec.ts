import { TestBed } from '@angular/core/testing';

import { ExistuserService } from './existuser.service';

describe('ExistuserService', () => {
  let service: ExistuserService;

  beforeEach(() => {
    TestBed.configureTestingModule({});
    service = TestBed.inject(ExistuserService);
  });

  it('should be created', () => {
    expect(service).toBeTruthy();
  });
});
