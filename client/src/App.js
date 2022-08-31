import React from "react";
import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import {Header} from "./components/Header";
import {Home} from "./components/Home";
import {MyList} from "./components/MyList";
import {Add} from "./components/Add";
import './lib/font-awesome/css/all.min.css';

function App() {
  return (
  <Router>
      <Header/>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/my-list" element={<MyList />}/>
        <Route path="/add" element={<Add />}/>
      </Routes>
    </Router>
  
  );
}

export default App;
