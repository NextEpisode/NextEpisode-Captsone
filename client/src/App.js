import React from "react";
import './App.css';
import {BrowserRouter as Router, Routes, Route} from "react-router-dom";
import {Header} from "./components/Header";
import {Home} from "./components/Home";
import {Profile} from "./components/Profile";
import {Search} from "./components/Search";
import {MediaPage} from "./components/MediaPage";
import './lib/font-awesome/css/all.min.css';
 
function App() {
  return (
  <Router>
      <Header/>
      <Routes>
        <Route path="/" element={<Home />}/>
        <Route path="/Profile" element={<Profile />}/>
        <Route path="/search" element={<Search />}/>
        <Route path="/media-page/:id" element={<MediaPage />}/>
      </Routes>
    </Router>
 
  );
}
 
export default App;