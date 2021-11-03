export enum InputChoice {
  UniqueDate = "unique_date",
  BetweenDate = "between_date",
}

export interface Data {
  x: Date;
  y: [number, number, number, number];
}

export interface APIData {
  date: number;
  opening: number;
  closing: number;
  low: number;
  high: number;
}
