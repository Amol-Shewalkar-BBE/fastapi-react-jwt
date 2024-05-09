import React from 'react'
import { NavLink } from 'react-router-dom'

function GuestNavbar({isLoggedIn}) {
  return (
    <>
        <nav className="navbar navbar-expand-lg navbar bg Navbar_element" style={{borderRadius:20,marginTop:30, border:1, backgroundColor:'lightblue'}}>
         
         <div className="container-fluid">
            
             
             <button className="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarNavAltMarkup" aria-controls="navbarNavAltMarkup" aria-expanded="false" aria-label="Toggle navigation">
             <span className="navbar-toggler-icon"></span>
             </button>
             <div className="collapse navbar-collapse" id="navbarNavAltMarkup">
             <div className="navbar-nav">
                    <NavLink style={{marginLeft:80,borderRadius:10,padding:20,color:'brown',fontSize:30}} className="nav-link active" aria-current="page" to="/"><b>Home</b></NavLink>
                    <NavLink style={{marginLeft:80,borderRadius:10,padding:20,color:'brown',fontSize:30}} className="nav-link active" to="/about"><b>About</b></NavLink>
                {isLoggedIn ?(
                    <>
                        
                        <NavLink style={{marginLeft:80,borderRadius:10,padding:20,color:'brown',fontSize:30}} className="nav-link active" to="/profile"><b>Profile</b></NavLink>
                        <NavLink style={{marginLeft:1000,borderRadius:10,padding:20,color:'brown',fontSize:30}} className="nav-link active" to="/logout"><b>Logout</b></NavLink>
                    </>
                ):
                (
                    <>
                        
                        <NavLink style={{marginLeft:1000,borderRadius:10,padding:20,color:'brown',fontSize:30}} className="nav-link active" to="/login"><b>Login</b></NavLink>
                        <NavLink style={{marginLeft:80,borderRadius:10,padding:20,color:'brown',fontSize:30}} className="nav-link active" to="/signup"><b>Signup</b></NavLink>
                    </>
                )
                 
                 
                }
             </div>
             </div>
         </div>
         </nav>
    
    </>
  )
}

export default GuestNavbar
