import { createStore } from "nedux";
import { createStoreHook } from "react-nedux";
import { Data } from "./types";

export const store = createStore({
  beginDate: null as null | number,
  endDate: null as null | number,
  data: null as null | Data[],
});

export const useStore = createStoreHook(store);
