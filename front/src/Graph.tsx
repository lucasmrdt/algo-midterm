import { useCallback, useEffect, useState } from "react";
import { renderToString } from "react-dom/server";
import Chart, { Props } from "react-apexcharts";
import Loader from "react-js-loader";
import { ENDPOINT } from "./constants";
import { useStore } from "./store";
import { APIData } from "./types";

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
  const [data, setData] = useStore("data");
  const [loading, setLoading] = useState(false);

  const fetchData = useCallback(async () => {
    setLoading(true);
    if (data && data.length > MAX_ITEMS) {
      setData([]);
    }
    try {
      const res = await fetch(
        `${ENDPOINT}/data?begin=${beginDate}&end=${endDate}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
          },
        }
      );
      const data: APIData[] = await res.json();
      setData(
        data.map((d) => ({
          x: new Date(d.date),
          y: [d.opening, d.high, d.low, d.closing],
        }))
      );
    } catch {}
    setLoading(false);
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, [beginDate, endDate, setData]);

  useEffect(() => {
    fetchData();
  }, [fetchData]);

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
        height="90%"
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
    </>
  );
}

export default Graph;
