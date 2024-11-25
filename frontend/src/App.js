import Header from './Components/Header';
import { Link, Routes, Route, BrowserRouter as Router } from "react-router-dom";
import About from './Components/About';
import Login from './Components/Login';
import Browse from './Components/Browse';
import SearchBar from './Components/SearchBar';
import Home from './Components/Home';
import ItemPage from './Components/ItemPage';
import Upload from './Components/Upload';
import Footer from './Components/Footer';
import FAPI from './Components/FAPI';
import Signup from './Components/Signup';
import AdminView from './Components/AdminView';
import { StrictMode } from 'react';
import UserProfilePage from './Components/UserProfilePage';
import 'semantic-ui-css/semantic.min.css'


function App() {
  return (
    <div className=' relative min-h-screen pb-10'>
      <Router>
        <Header />






        <Routes>
          <Route path="/" element={
            <div>
              <SearchBar />
              <Home />
            </div>}>
          </Route>
          <Route path="/browse/:q" element={
            <div>
              <SearchBar />
              <Browse />
            </div>}>
          </Route>
          <Route path="/view/:id" element={<ItemPage />}></Route>
          <Route path="/login" element={<Login />}></Route>
          <Route path="/signup" element= {<Signup />}></Route>
          <Route path="/about" element={<About />}></Route>
          <Route path="/admin" element={<AdminView />}></Route>
          <Route path ="/user_profile" element = {<UserProfilePage />}></Route>
          <Route path ="/upload" element={<Upload />}></Route>
        </Routes>

        <Footer />
      </Router>

    </div>
  );
}

export default App;
