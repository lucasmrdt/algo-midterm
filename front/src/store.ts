import { createStore } from "nedux";
import { createStoreHook } from "react-nedux";
import { Data } from "./types";

const BEGIN_DATE = 1634342400; // 2021-10-16

export const store = createStore({
  beginDate: BEGIN_DATE,
  endDate: null as null | number,
  data: null as null | Data[],
});

export const useStore = createStoreHook(store);
