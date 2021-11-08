export enum InputChoice {
  UniqueDate = "unique_date",
  BetweenDate = "between_date",
  BetweenDateWithK = "between_date_with_k",
  BestKBetweenDateWithQueue = "best_k_between_date_queue",
  BestKBetweenDateWithSort = "best_k_between_date_sort",
}

export enum AlgoChoice {
  custom = "algo",
  db = "db",
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
