import { ToastContainer } from "react-toastify";
import Graph from "./Graph";
import Input from "./Input";

function App() {
  return (
    <div className="w-full h-full relative overflow-hidden">
      <Input />
      <p>test</p>
      <Graph />
      <ToastContainer />
    </div>
  );
}

export default App;
