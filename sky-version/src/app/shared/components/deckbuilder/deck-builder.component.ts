import {
  Component
} from '@angular/core';

import {
  Card,
  Deck
} from '../../model';

import {
  CollectionSearchService
} from '../../services/collection-search.service';

@Component({
  selector: 'deck-builder',
  templateUrl: './deck-builder.component.html',
  styleUrls: ['./deck-builder.component.scss']
})
export class DeckBuilderComponent {
  // Custom data
  public deck = new Deck();
  public searchResults: Card[] = [];
  public selectedCard = new Card();

  // Forms
  public searchName = '';
  public searchDescription = '';
  public searchType = '';
  public currentPage = 1;

  public get searchResultPage(): Card[] {
    let firstIndex = (this.currentPage - 1) * 20;
    return this.searchResults.slice(firstIndex, firstIndex + 20);
  }

  constructor(private searchService: CollectionSearchService) { }

  public drag(event: DragEvent, card: Card) {
    event.dataTransfer.setData('id', card.id);
  }

  public drop(event: DragEvent, isSide = false) {
    event.preventDefault();
    let id = event.dataTransfer.getData('id');
    let card = this.searchResults.filter(item => item.id === id);
    if (isSide && card.length > 0) {
      this.deck.addSideCard(card[0]);
    } else if (card.length > 0) {
      this.deck.addCard(card[0]);
    }
  }

  public addCard(card: Card) {
    this.deck.addCard(card);
  }

  public removeCard(card: Card) {
    this.deck.removeCard(card);
  }

  public removeSideCard(card: Card) {
    this.deck.removeSideCard(card);
  }

  public formKeyDown(event: KeyboardEvent) {
    if (event.key.toLowerCase() === 'enter') {
      this.search();
    }
  }

  public search(): void {
    const searchData: Partial<Card> = {
      name: this.searchName,
      description: this.searchDescription,
      type: this.searchType
    };
    this.searchService.getCards(searchData).take(1).subscribe(results => {
      this.searchResults = results;
      this.currentPage = 1;
    }, err => {
      this.searchResults = [];
      this.currentPage = 1;
    });
  }

  public updateSelected(card: Card) {
    if (this.selectedCard !== card) {
      this.selectedCard = card;
    }
  }
}
