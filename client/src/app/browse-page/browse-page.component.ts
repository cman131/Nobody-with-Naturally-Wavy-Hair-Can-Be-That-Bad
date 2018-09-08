import {
  Component,
  OnInit
} from '@angular/core';

import {
  DeckSearchResult
} from '../shared/model';
import {
  ProDataService
} from '../shared/services/pro-data.service';
import { Observable } from 'rxjs';

@Component({
  selector: 'browse-page',
  templateUrl: './browse-page.component.html'
})
export class BrowsePageComponent implements OnInit {
  public results: Observable<DeckSearchResult[]>;

  constructor(private dataService: ProDataService) { }

  public ngOnInit() {
    this.results = this.dataService.getAllDecks(undefined);
  }
}
