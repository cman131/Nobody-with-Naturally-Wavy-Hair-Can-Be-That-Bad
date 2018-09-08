export class DeckSearchResult {
  public id: string;
  public name: string;
  public author: string;
  public cardCount: string;
  public sideCount: string;

  public static fromResponse(obj: any): DeckSearchResult {
    return obj;
  }
}
