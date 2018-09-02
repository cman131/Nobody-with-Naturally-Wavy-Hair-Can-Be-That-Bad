export class Card {
    public id: string;
    public name: string;
    public description: string;
    public type: string;
    public cmc: number;
    public imageUrl: string;
    public subtypes?: string[];
    public power?: number | string;
    public toughness?: number | string;

    public static fromResponse(cardBody: any): Card {
        return {
            id: cardBody.id,
            name: cardBody.name,
            description: cardBody.oracle_text,
            imageUrl: cardBody.image_uris.large,
            cmc: cardBody.cmc,
            type: cardBody.type_line,
            power: cardBody.power,
            toughness: cardBody.toughness
        };
    }
}
