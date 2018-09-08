import {
  Injectable
} from '@angular/core';
import {
  Http
} from '@angular/http';

import {
  Observable
} from 'rxjs';

import {
  Deck,
  DeckSearchResult
} from '../model';

@Injectable()
export class ProDataService {
  private baseUrl = 'http://127.0.0.1:5000';

  constructor(private http: Http) { }

  public getDeck(id: string): Observable<Deck> {
    return this.http.get(
      this.baseUrl + '/deck',
      {
        params: {'id': id}
      }
    ).take(1).map((response: any) => Deck.fromResponse(response.json().deck));
  }

  public getAllDecks(filterString: string): Observable<DeckSearchResult[]> {
    return this.http.get(
      this.baseUrl + '/decks',
      {
        params: {
          'searchTerm': filterString
        }
      }
    ).take(1).map((response: any) => response.json().results.map((item: any) => DeckSearchResult.fromResponse(item)));
  }

  public createDeck(deck: Deck): Observable<string> {
    return this.http.post(
      this.baseUrl + '/deck/create',
      deck
    ).take(1).map(response => response.json().id);
  }

  public updateDeck(deck: Deck): void {
    this.http.put(
      this.baseUrl + '/deck/update',
      deck
    ).take(1).subscribe((obj) => console.log(obj));
  }
}
