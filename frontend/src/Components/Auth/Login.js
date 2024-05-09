import React, { useEffect } from 'react'
import { useForm } from 'react-hook-form'
import { useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useState } from 'react'

function Login({setIsLoggedIn}) {

    const {register,handleSubmit}=useForm()
    const navigate = useNavigate()
    const [error, setError] = useState('');
    

        async function saveData(data){
            console.log(data)
            await axios.post('http://localhost:8000/users/login/',data,
            {headers:{"content-Type":"application/x-www-form-urlencoded"}}).then(response=>{
                console.log(response.data)
                sessionStorage.setItem('access',response.data.access)  
                /*sessionStorage.setItem('role',response.data.redirectURL)   
                sessionStorage.setItem('email',response.data.email)*/
                setError(response.data.message)
                /*const redirectURL = response.data.redirectURL
                setUserRole(sessionStorage.getItem('role'))
                setUserEmail(sessionStorage.getItem('email'))*/
                setIsLoggedIn(sessionStorage.getItem('access'))

                navigate('/home') ;
                   
            }).catch(error=>{
                
                setError(error.response.data.detail)
                console.log(error.response)
                   
            }
            )
           
          //console.log(sessionStorage.getItem('access'))  
    }

  return (
    <>
        <hr style={{color:'white'}}/>
        <div style={{ display: 'flex'}}>
            <div className ="col-6" style={{ marginTop:30}} >
               

            </div>
            <div className='container' style={{backgroundColor:'thistle',borderRadius:20,padding:40,width:500,height:600,marginTop:120,marginLeft:350}}>
                <center style={{color:'midnightblue'}}>
                
                <h1 style={{color:'black'}}>Login</h1>
                {error && <h3>{error}</h3>}
                </center><hr/>
                
                            
                
                <form onSubmit={handleSubmit(saveData)}>

                    <label htmlFor='un'>Email id</label>
                    <input type='username' id='un' style={{padding:20}} placeholder='Enter user registered email id' className='form-control' {...register('username')}/><br/><br/>

                    <label htmlFor='pw'>Password</label>
                    <input type='password' id='pw' style={{padding:20}} placeholder='Enter user password' className='form-control' {...register('password')}/><br/><br/>

                    
                    <input type='submit' value='Login me' className='btn btn-success col-4'/><br/><br/>


                </form>
            </div>
            </div>
    </>
  )
}

export default Login
