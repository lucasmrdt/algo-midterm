import { useEffect, useRef, useState } from "react";
import { FormInput, FormSelect, Slider, FormCheckbox } from "shards-react";
import Zoom from "react-reveal/Zoom";
import { AlgoChoice, InputChoice, MarketChoice } from "./types";
import { useStore } from "./store";

const MARKET_CHOICES = [
  { label: "BTC", value: MarketChoice.btc },
  { label: "EUR_USD", value: MarketChoice.eur_usd },
  { label: "Nasdaq", value: MarketChoice.nasdaq },
  { label: "VIX", value: MarketChoice.vix },
  { label: "TSLA", value: MarketChoice.tsla },
  { label: "Gold", value: MarketChoice.gold },
  { label: "SP500", value: MarketChoice.sp500 },
];

const ALGO_CHOICES = [
  { label: "Custom", value: AlgoChoice.custom },
  { label: "SQLite", value: AlgoChoice.db },
];

const DATE_CHOICES = [
  { label: "À une date", value: InputChoice.UniqueDate, enabled: () => true },
  {
    label: "Entre 2 dates",
    value: InputChoice.BetweenDate,
    enabled: () => true,
  },
  {
    label: "Entre 2 dates (avec k)",
    value: InputChoice.BetweenDateWithK,
    enabled: () => true,
  },
  {
    label: "Meilleur entre 2 dates (priority queue)",
    value: InputChoice.BestKBetweenDateWithQueue,
    enabled: (algo: AlgoChoice) => algo === AlgoChoice.custom,
  },
  {
    label: "Meilleur entre 2 dates (sort)",
    value: InputChoice.BestKBetweenDateWithSort,
    enabled: () => true,
  },
];

const BEGIN_DATE = "2021-10-01";
const END_DATE = "2021-10-16";

const formatInputDate = (value: string | null) =>
  value ? new Date(value).getTime() / 1000 : null;

function Input() {
  const [selected, setSelected] = useStore("selectedInput");
  const [, setBeginDate] = useStore("beginDate");
  const [, setEndDate] = useStore("endDate");
  const [market, setMarket] = useStore("market");
  const [k, setK] = useStore("k");
  const [algo, setAlgoChoice] = useStore("algo");
  const [displayPrediction, setDisplayPrediction] =
    useStore("displayPrediction");
  const [beginValue, setBeginValue] = useState(BEGIN_DATE);
  const [endValue, setEndValue] = useState<string | null>(null);
  const prevSelected = useRef(selected);

  const beginRef = useRef<HTMLInputElement>(null);
  const endRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (
      selected === InputChoice.BetweenDate ||
      selected === InputChoice.BetweenDateWithK ||
      selected === InputChoice.BestKBetweenDateWithQueue ||
      selected === InputChoice.BestKBetweenDateWithSort ||
      displayPrediction
    ) {
      if (prevSelected.current === InputChoice.UniqueDate) {
        setEndValue(END_DATE);
      }
    } else {
      setEndValue(null);
    }
    if (
      selected === InputChoice.BetweenDateWithK ||
      selected === InputChoice.BestKBetweenDateWithQueue ||
      selected === InputChoice.BestKBetweenDateWithSort
    ) {
      if (
        prevSelected.current === InputChoice.UniqueDate ||
        prevSelected.current === InputChoice.BetweenDate
      ) {
        setK(10);
      }
    } else {
      setK(-1);
    }
    prevSelected.current = selected;
  }, [displayPrediction, selected, setEndDate, setK]);

  useEffect(() => {
    if (
      algo === AlgoChoice.db &&
      selected === InputChoice.BestKBetweenDateWithQueue
    ) {
      setSelected(InputChoice.BestKBetweenDateWithSort);
    }
  }, [algo, selected, setSelected]);

  useEffect(() => {
    setBeginDate(formatInputDate(beginValue));
    setEndDate(formatInputDate(endValue));
  }, [beginValue, endValue, setBeginDate, setEndDate]);

  return (
    <>
      <div className="flex px-10 h-60 items-center">
        {displayPrediction ? (
          <>
            <div className="mr-20">
              <Zoom>
                <FormSelect
                  value={market}
                  onChange={(e: any) => setMarket(e.currentTarget.value)}
                >
                  {MARKET_CHOICES.map((choice) => (
                    <option key={choice.value} value={choice.value}>
                      {choice.label}
                    </option>
                  ))}
                </FormSelect>
              </Zoom>
            </div>
            <div className="flex-1 flex items-center">
              <div className="flex-1">
                <Zoom>
                  <FormInput
                    type="date"
                    value={beginValue}
                    onChange={(e: any) => setBeginValue(e.currentTarget.value)}
                    ref={beginRef}
                  />
                </Zoom>
              </div>
              <div className="flex-1 ml-10">
                <Zoom>
                  <FormInput
                    type="date"
                    value={endValue}
                    onChange={(e: any) => setEndValue(e.currentTarget.value)}
                    ref={endRef}
                  />
                </Zoom>
              </div>
            </div>
          </>
        ) : (
          <>
            <div className="mr-20">
              <Zoom>
                <FormSelect
                  onChange={(e: any) => setAlgoChoice(e.currentTarget.value)}
                >
                  {ALGO_CHOICES.map((choice) => (
                    <option key={choice.value} value={choice.value}>
                      {choice.label}
                    </option>
                  ))}
                </FormSelect>
              </Zoom>
            </div>
            <div className="mr-20">
              <Zoom>
                <FormSelect
                  value={market}
                  onChange={(e: any) => setMarket(e.currentTarget.value)}
                >
                  {MARKET_CHOICES.map((choice) => (
                    <option key={choice.value} value={choice.value}>
                      {choice.label}
                    </option>
                  ))}
                </FormSelect>
              </Zoom>
            </div>
            <div className="mr-20">
              <Zoom>
                <FormSelect
                  value={selected}
                  onChange={(e: any) => setSelected(e.currentTarget.value)}
                >
                  {DATE_CHOICES.filter((d) => d.enabled(algo)).map((choice) => (
                    <option key={choice.value} value={choice.value}>
                      {choice.label}
                    </option>
                  ))}
                </FormSelect>
              </Zoom>
            </div>
            <div className="flex-1 flex items-center">
              <div className="flex-1">
                <Zoom>
                  <FormInput
                    type="date"
                    value={beginValue}
                    onChange={(e: any) => setBeginValue(e.currentTarget.value)}
                    ref={beginRef}
                  />
                </Zoom>
              </div>
              <div
                className="flex-1 ml-10"
                style={{
                  transition: "max-width 1s",
                  maxWidth:
                    selected === InputChoice.BetweenDate ||
                    selected === InputChoice.BetweenDateWithK ||
                    selected === InputChoice.BestKBetweenDateWithQueue ||
                    selected === InputChoice.BestKBetweenDateWithSort
                      ? "100%"
                      : 0,
                  overflow: "hidden",
                }}
              >
                <FormInput
                  type="date"
                  value={endValue}
                  onChange={(e: any) => setEndValue(e.currentTarget.value)}
                  ref={endRef}
                />
              </div>
              <div
                className="flex-1 flex flex-col relative items-center"
                style={{
                  transition: "max-width 1s",
                  maxWidth:
                    selected === InputChoice.BetweenDateWithK ||
                    selected === InputChoice.BestKBetweenDateWithQueue ||
                    selected === InputChoice.BestKBetweenDateWithSort
                      ? "100%"
                      : 0,
                  overflow: "hidden",
                }}
              >
                <p className="absolute">K: {k}</p>
                <div className="self-start w-full px-20">
                  <Slider
                    onSlide={(e: any) => setK(parseInt(e[0]))}
                    connect={[true, false]}
                    start={[k]}
                    range={{ min: 1, max: 100 }}
                  />
                </div>
              </div>
            </div>
          </>
        )}
      </div>
      <div className="flex py-10 px-10 items-center">
        <FormCheckbox
          checked={displayPrediction}
          onChange={() => setDisplayPrediction(!displayPrediction)}
        >
          Prédiction
        </FormCheckbox>
      </div>
    </>
  );
}

export default Input;
