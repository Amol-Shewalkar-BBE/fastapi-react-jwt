import './App.css';
import '../node_modules/bootstrap/dist/css/bootstrap.min.css'
import {BrowserRouter,Routes,Route} from 'react-router-dom';
import GuestNavbar from './Components/Navbar/GuestNavbar';
import Signup from './Components/Auth/Signup';
import Login from './Components/Auth/Login';
import Home from './Components/Home';
import Profile from './Components/Customer/Profile';
import Logout from './Components/Auth/Logout';
import { useState } from 'react';
import About from './Components/About';

function App() {

  const [isLoggedIn,setIsLoggedIn]=useState(sessionStorage.getItem('access'))

  return (
  <>
    <BrowserRouter>
      <GuestNavbar isLoggedIn={isLoggedIn}/>
      <Routes>
        <Route path='/signup' element={<Signup/>}/>
        <Route path='/login' element={<Login setIsLoggedIn={setIsLoggedIn}/>}/>
        <Route path='/logout' element={<Logout setIsLoggedIn={setIsLoggedIn}/>}/>

        <Route path='/' element={<Home/>}/>
        <Route path='/about' element={<About/>}/>
        <Route path='/profile' element={<Profile/>}/>

      </Routes>
    </BrowserRouter>
  </>
  );
}

export default App;
