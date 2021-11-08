import { useEffect, useRef, useState } from "react";
import { FormInput, FormSelect, Slider } from "shards-react";
import Zoom from "react-reveal/Zoom";
import { AlgoChoice, InputChoice } from "./types";
import { useStore } from "./store";

const ALGO_CHOICES = [
  { label: "Custom", value: AlgoChoice.custom },
  { label: "SQLite", value: AlgoChoice.db },
];

const DATE_CHOICES = [
  { label: "À une date", value: InputChoice.UniqueDate },
  { label: "Entre 2 dates", value: InputChoice.BetweenDate },
  { label: "Entre 2 dates (avec k)", value: InputChoice.BetweenDateWithK },
  {
    label: "Meilleur entre 2 dates (queue)",
    value: InputChoice.BestKBetweenDateWithQueue,
  },
  {
    label: "Meilleur entre 2 dates (sort)",
    value: InputChoice.BestKBetweenDateWithSort,
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
  const [k, setK] = useStore("k");
  const [, setAlgoChoice] = useStore("algo");
  const [beginValue, setBeginValue] = useState(BEGIN_DATE);
  const [endValue, setEndValue] = useState<string | null>(null);

  const beginRef = useRef<HTMLInputElement>(null);
  const endRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (
      selected === InputChoice.BetweenDate ||
      selected === InputChoice.BetweenDateWithK ||
      selected === InputChoice.BestKBetweenDateWithQueue ||
      selected === InputChoice.BestKBetweenDateWithSort
    ) {
      setEndValue(END_DATE);
    } else {
      setEndValue(null);
    }
    if (
      selected === InputChoice.BetweenDateWithK ||
      selected === InputChoice.BestKBetweenDateWithQueue ||
      selected === InputChoice.BestKBetweenDateWithSort
    ) {
      setK(100);
    } else {
      setK(-1);
    }
  }, [selected, setEndDate, setK]);

  useEffect(() => {
    setBeginDate(formatInputDate(beginValue));
    setEndDate(formatInputDate(endValue));
  }, [beginValue, endValue, setBeginDate, setEndDate]);

  return (
    <div className="flex px-10 my-20 items-center">
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
          <FormSelect onChange={(e: any) => setSelected(e.currentTarget.value)}>
            {DATE_CHOICES.map((choice) => (
              <option key={choice.value} value={choice.value}>
                {choice.label}
              </option>
            ))}
          </FormSelect>
        </Zoom>
      </div>
      <div className="flex-1 flex items-center h-full">
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
    </div>
  );
}

export default Input;
