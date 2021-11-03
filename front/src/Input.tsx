import { useState } from "react";
import { FormInput, FormSelect } from "shards-react";
import Zoom from "react-reveal/Zoom";

export enum InputChoice {
  UniqueDate = "unique_date",
  BetweenDate = "between_date",
}

const CHOICES = [
  { label: "À une date", value: InputChoice.UniqueDate },
  { label: "Entre 2 dates", value: InputChoice.BetweenDate },
];

function Input(props: any) {
  const [selected, setSelected] = useState(InputChoice.UniqueDate);

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
            <FormInput placeholder="My form input" type="date" />
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
          <FormInput placeholder="My form input" type="date" />
        </div>
      </div>
    </div>
  );
}

export default Input;
