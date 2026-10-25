import { Route, Routes } from "react-router";
import SearchPage from "./pages/SearchPage";

const App = () => {
  return (
    <Routes>
      <Route path="/" element={<SearchPage/>}/>
    </Routes>
  );
};

export default App;