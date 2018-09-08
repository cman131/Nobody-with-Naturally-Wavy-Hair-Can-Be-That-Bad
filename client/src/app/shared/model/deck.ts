import {
  Card
} from './card';

export class Deck {
  public id?: string;
  public name: string;
  public author: string;
  public cards: Card[];
  public sideboard: Card[];

  constructor(
    id: string = undefined,
    name = 'Untitled',
    author = 'Anonymous',
    cards: Card[] = [],
    sideboard: Card[] = []
  ) {
    this.id = id;
    this.name = name,
    this.author = author,
    this.cards = cards;
    this.sideboard = sideboard;
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

  public static fromResponse(obj: any): Deck {
    return new Deck(
      obj.id,
      obj.name,
      obj.author,
      obj.cards.map((card: any) => Card.fromResponse(card, false)),
      obj.sideboard.map((card: any) => Card.fromResponse(card, false))
    );
  }
}
