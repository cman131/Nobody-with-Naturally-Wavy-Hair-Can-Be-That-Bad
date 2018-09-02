import {
  Card
} from './card';

export class Deck {
  public name: string;
  public cards: Card[];
  public sideboard: Card[];

  constructor() {
    this.name = 'Untitled',
    this.cards = [];
    this.sideboard = [];
  }

  public addCard(card: Card) {
    this.cards.push(card);
  }

  public removeCard(card: Card) {
    const index = this.cards.findIndex((item) => item === card);
    this.cards = this.cards.filter((value: Card, ind: number) => ind !== index);
  }

  public addSideCard(card: Card) {
    this.sideboard.push(card);
  }

  public removeSideCard(card: Card) {
    const index = this.sideboard.findIndex((item) => item === card);
    this.sideboard = this.sideboard.filter((value: Card, ind: number) => ind !== index);
  }
}
