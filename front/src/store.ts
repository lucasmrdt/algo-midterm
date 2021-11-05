import { createStore } from "nedux";
import { createStoreHook } from "react-nedux";
import { AlgoChoice, Data } from "./types";

// const BEGIN_DATE = 1634342400; // 2021-10-16

export const store = createStore({
  beginDate: null as null | number,
  endDate: null as null | number,
  algo: AlgoChoice.custom,
  data: null as null | Data[],
});

export const useStore = createStoreHook(store);
