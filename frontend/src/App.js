import './App.css';
import Main from "./Views/Main";
import Detail from "./Views/Detail";
import Make from "./Views/Make";
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';

function App() {
  return (
    <div className="App">

        <Router>
          <Routes>
            <Route path="/" element={<Main/>}/>     
            <Route path="/detail/:id" element={<Detail/>}/>
            <Route path="/maketts" element={<Make/>}/>
          </Routes>
        </Router>
    </div>
  );
}

export default App;
