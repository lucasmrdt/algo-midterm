import { useState } from "react";
import { FormInput, FormSelect } from "shards-react";
import Zoom from "react-reveal/Zoom";
import { InputChoice } from "./types";
import { useStore } from "./store";

const CHOICES = [
  { label: "À une date", value: InputChoice.UniqueDate },
  { label: "Entre 2 dates", value: InputChoice.BetweenDate },
];

const formatInputDate = (e: any) =>
  new Date(e.currentTarget.value).getTime() / 1000;

function Input() {
  const [selected, setSelected] = useState(InputChoice.UniqueDate);
  const [, setBeginDate] = useStore("beginDate");
  const [, setEndDate] = useStore("endDate");

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
              onChange={(e: any) => setBeginDate(formatInputDate(e))}
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
            onChange={(e: any) => setEndDate(formatInputDate(e))}
          />
        </div>
      </div>
    </div>
  );
}

export default Input;
