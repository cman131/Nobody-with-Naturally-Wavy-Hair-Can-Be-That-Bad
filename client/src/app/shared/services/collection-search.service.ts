import {
  Injectable
} from '@angular/core';
import {
  Http
} from '@angular/http';

import {
  BehaviorSubject,
  Observable
} from 'rxjs';

import {
  Card
} from '../model/card';

@Injectable()
export class CollectionSearchService {
  private baseUrl = 'https://api.scryfall.com/cards/search';

  constructor(private http: Http) { }

  public getCards(searchData: Partial<Card>): Observable<Card[]> {
    // No search criteria
    if (!searchData.name && !searchData.description && !searchData.type) {
      return new BehaviorSubject([]);
    }

    // Build filters
    let filterString = this.addFilter('', '', searchData.name);
    filterString = this.addFilter(filterString, 'o:', searchData.description);
    filterString = this.addFilter(filterString, 't:', searchData.type);

    // Query scryfall
    let params: any = { q: filterString };
    return this.http.get(
      this.baseUrl,
      {
        params: params
      }
    ).take(1).map((value) => {
      if (value.status >= 300) {
        return [];
      }

      let cards: any[] = value.json().data;
      return cards.map(card => Card.fromResponse(card));
    }).catch(err => {
      return [];
    });
  }

  private addFilter(filterString: string, filter: string, query: string) {
    if (query) {
      return (!filterString ? '' : filterString + '+') + filter + query;
    }
    return filterString;
  }
}
