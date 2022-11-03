import logo from './logo.svg';
import './App.css';
import { BrowserRouter, Routes, Route } from "react-router-dom";
import LandingPage from "./components/LandingPage";
import SignIn from './components/SignIn';
import NavBar from './components/NavBar';
import Profile from './components/Profile';
import {MyList} from "./components/MyList";
import {Search} from "./components/Search";
import {MediaPage} from "./components/MediaPage";
import Home from './components/Home';
import './lib/font-awesome/css/all.min.css';
import { Header } from './components/Header';



function App() {
  return (
  <BrowserRouter>
  <Header />
    <Routes>
      <Route path="/" element={<LandingPage></LandingPage>}></Route>
      <Route path="/home" element={<Home />}></Route>
      <Route path="/login" element={<SignIn />}></Route>
      <Route path="/Profile" element={<Profile />}/>
      <Route path="/my-list" element={<MyList />}/>
      <Route path="/search" element={<Search />}/>
      <Route path="/media-page/:id" element={<MediaPage />}/>
    </Routes>
  </BrowserRouter>
    );

}
 
export default App;