import { useCallback, useEffect, useMemo, useRef, useState } from "react";
import { renderToString } from "react-dom/server";
import Chart, { Props } from "react-apexcharts";
import Loader from "react-js-loader";
import _ from "lodash";
import { ENDPOINT } from "./constants";
import { useStore } from "./store";
import { APIData, InputChoice } from "./types";

const MAX_ITEMS = 365;

const options: Props["options"] = {
  xaxis: {
    type: "datetime",
  },
  yaxis: {
    labels: {
      formatter: (value: number) => `${value.toLocaleString("fr-FR")}€`,
    },
  },
  tooltip: {
    custom: function ({ seriesIndex, dataPointIndex, w }) {
      const o = w.globals.seriesCandleO[seriesIndex][dataPointIndex];
      const h = w.globals.seriesCandleH[seriesIndex][dataPointIndex];
      const l = w.globals.seriesCandleL[seriesIndex][dataPointIndex];
      const c = w.globals.seriesCandleC[seriesIndex][dataPointIndex];
      return renderToString(
        <div className="apexcharts-tooltip-candlestick p-10">
          <div>Open: {o.toLocaleString("fr-FR")}€</div>
          <div>High: {h.toLocaleString("fr-FR")}€</div>
          <div>Low: {l.toLocaleString("fr-FR")}€</div>
          <div>Close: {c.toLocaleString("fr-FR")}€</div>
        </div>
      );
    },
  },
};

function Graph() {
  const [beginDate] = useStore("beginDate");
  const [endDate] = useStore("endDate");
  const [algo] = useStore("algo");
  const [selected] = useStore("selectedInput");
  const [k] = useStore("k");
  const [data, setData] = useStore("data");
  const [loading, setLoading] = useState(false);
  const [time, setTime] = useState<null | number>(null);
  const firstFetch = useRef(true);

  const fetchData = useCallback(
    async (begin, end, algo, k, selected, shouldClearData) => {
      setLoading(true);
      let baseUrl = `${ENDPOINT}/data/${algo}`;
      if (selected === InputChoice.BestKBetweenDateWithQueue) {
        baseUrl += "/best-with-queue";
      } else if (selected === InputChoice.BestKBetweenDateWithSort) {
        baseUrl += "/best-with-sort";
      }
      try {
        const res = await fetch(`${baseUrl}?begin=${begin}&end=${end}&k=${k}`, {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        });
        const {
          data: newData,
          time: newTime,
        }: { data: APIData[]; time: number } = await res.json();
        if (shouldClearData) {
          setData([]);
        }
        setTime(newTime);
        setData(
          newData.map((d) => ({
            x: new Date(d.date),
            y: [d.opening, d.high, d.low, d.closing],
          }))
        );
      } catch {}
      setLoading(false);
    },
    [setData]
  );

  const debouncedFetchData = useMemo(
    () => _.debounce(fetchData, 1000),
    [fetchData]
  );

  const reloadData = useCallback(async () => {
    const shouldClearData = data && data.length > MAX_ITEMS;
    if (beginDate) {
      if (firstFetch.current) {
        firstFetch.current = false;
        fetchData(beginDate, endDate, algo, k, selected, shouldClearData);
      } else {
        debouncedFetchData(
          beginDate,
          endDate,
          algo,
          k,
          selected,
          shouldClearData
        );
      }
    }
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [beginDate, debouncedFetchData, endDate, algo, k, selected, fetchData]);

  useEffect(() => {
    reloadData();
  }, [reloadData]);

  return (
    <>
      <Chart
        options={{
          ...options,
          chart: {
            toolbar: {
              show: !!data && data.length <= MAX_ITEMS,
            },
            animations: {
              enabled: !!data && data.length <= MAX_ITEMS,
            },
          },
        }}
        series={[{ data: data || [] }]}
        type="candlestick"
        height="80%"
      />
      {loading && (
        <div
          className="fixed tranform top-50% left-50%"
          style={{ transform: "translate(-50%, -50%)" }}
        >
          <Loader
            type="box-rotate-y"
            bgColor={"#666"}
            title={"Chargement ..."}
            color={"#666"}
            size={100}
          />
        </div>
      )}
      {time !== null && (
        <div className="fixed top-130 right-0 p-15 text-right">
          Temps d'exécution
          <br />
          {(time * 1000).toFixed(3)}ms
        </div>
      )}
    </>
  );
}

export default Graph;
