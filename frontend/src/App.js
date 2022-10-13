import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./Pages/LandingPage";
import SignIn from './Pages/SignIn';
import NavBar from './Pages/NavBar';
import Profile from './Pages/Profile';


function App() {
  return (
  <BrowserRouter>
  <NavBar />
    <Routes>
      <Route path="/" element={<LandingPage></LandingPage>}></Route>
      <Route path="/login" element={<SignIn />}></Route>
      <Route path="/:id" element={<Profile />}></Route>
    </Routes>

  </BrowserRouter>
    );
}

export default App;
