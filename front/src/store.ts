import { createStore } from "nedux";
import { createStoreHook } from "react-nedux";
import { AlgoChoice, Data, InputChoice, MarketChoice } from "./types";

// const BEGIN_DATE = 1634342400; // 2021-10-16

export const store = createStore({
  beginDate: null as null | number,
  endDate: null as null | number,
  k: -1,
  algo: AlgoChoice.custom,
  displayPrediction: false,
  market: MarketChoice.btc,
  data: null as null | Data[],
  selectedInput: InputChoice.UniqueDate,
});

export const useStore = createStoreHook(store);
