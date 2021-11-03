import { useEffect, useRef, useState } from "react";
import { FormInput, FormSelect } from "shards-react";
import Zoom from "react-reveal/Zoom";
import { InputChoice } from "./types";
import { useStore } from "./store";

const CHOICES = [
  { label: "À une date", value: InputChoice.UniqueDate },
  { label: "Entre 2 dates", value: InputChoice.BetweenDate },
];

const BEGIN_DATE = "2021-10-01";
const END_DATE = "2021-10-16";

const formatInputDate = (value: string) => new Date(value).getTime() / 1000;

function Input() {
  const [selected, setSelected] = useState(InputChoice.UniqueDate);
  const [, setBeginDate] = useStore("beginDate");
  const [, setEndDate] = useStore("endDate");
  const [beginValue, setBeginValue] = useState(BEGIN_DATE);
  const [endValue, setEndValue] = useState(END_DATE);

  const beginRef = useRef<HTMLInputElement>(null);
  const endRef = useRef<HTMLInputElement>(null);

  useEffect(() => {
    if (beginRef.current && endRef.current) {
      setBeginDate(formatInputDate(BEGIN_DATE));
      setEndDate(formatInputDate(END_DATE));
    }
  }, [setBeginDate, setEndDate]);

  return (
    <div className="flex px-10 py-20 items-center">
      <div className="mr-20">
        <Zoom>
          <FormSelect onChange={(e: any) => setSelected(e.currentTarget.value)}>
            {CHOICES.map((choice) => (
              <option key={choice.value} value={choice.value}>
                {choice.label}
              </option>
            ))}
          </FormSelect>
        </Zoom>
      </div>
      <div className="flex-1 flex">
        <div className="flex-1">
          <Zoom>
            <FormInput
              type="date"
              value={beginValue}
              onChange={(e: any) => {
                setBeginValue(e.currentTarget.value);
                setBeginDate(formatInputDate(e.currentTarget.value));
              }}
              ref={beginRef}
            />
          </Zoom>
        </div>
        <div
          className="flex-1 ml-10"
          style={{
            transition: "all 1s",
            maxWidth: selected === InputChoice.BetweenDate ? "100%" : 0,
            overflow: "hidden",
          }}
        >
          <FormInput
            type="date"
            value={endValue}
            onChange={(e: any) => {
              setEndValue(e.currentTarget.value);
              setEndDate(formatInputDate(e.currentTarget.value));
            }}
            ref={endRef}
          />
        </div>
      </div>
    </div>
  );
}

export default Input;
