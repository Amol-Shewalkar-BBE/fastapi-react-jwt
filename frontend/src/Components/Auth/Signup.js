import React from 'react'
import { useForm } from 'react-hook-form'
import { NavLink, useNavigate } from 'react-router-dom'
import axios from 'axios'
import { useState } from 'react'

function Signup() {

    const {register,handleSubmit}=useForm()
        const navigate = useNavigate()
        const [message, setMessage] = useState(' ');
        const [error,setError]=useState([])
        async function saveData(data){
                console.log(data)
                
               await axios.post('http://localhost:8000/users/signup/',data,
               {headers:{"content-Type":"application/json"}}).then(response=>{
                    setMessage(response.data.message)
                    navigate('/login')
               }).catch(error=>{
                
                    console.log(error.response.data)
                    setError(error.response.data)
               })
               
        }
  return (
    <>
        <hr style={{color:'white'}}/>
            <div className='container' style={{backgroundColor:'palegoldenrod',borderRadius:20,padding:40, width:700, marginLeft:900}}>
                <center style={{color:'midnightblue'}}>
                <h1>Create your Account</h1><hr/>
                  {message && <h3>{message}</h3>}
                  
                </center>
                <form onSubmit={handleSubmit(saveData)}>

                    <label htmlFor='fn'>First Name</label>
                    <input type='text' id='fn' className='form-control' {...register('first_name',{required : 'first_name is required'})}/><br/>
                    <p style={{'color':'red'}}>{error.first_name && error.first_name.message}</p><br/>

                    <label htmlFor='ln'>Last Name</label>
                    <input type='text' id='ln' className='form-control' {...register('last_name',{required : 'last_name is required'})}/><br/>
                    <p style={{'color':'red'}}>{error.last_name && error.last_name.message}</p><br/>

                    <label htmlFor='ps'>Password</label>
                    <input type='password' id='psd' className='form-control' {...register('password',{required : 'password is required'})}/><br/>
                    {error.password && <h4 style={{color:'red'}}>{error.password}</h4>}<br/>
                    
                    <label htmlFor='em'>Email Id</label>
                    <input type='email' id='em' className='form-control' {...register('email',{required : 'Email id is required',
                                                                        pattern:{value:/^[a-zA-Z0-9.!#$%&’*+/=?^_`{|}~-]+@[a-zA-Z0-9-]+(?:\.[a-zA-Z0-9-]+)*$/,message:'Enter valid email'}})}/><br/>
                    <p style={{color:'red'}}>{error.email}</p><br/>
                    
                   
                    <label htmlFor='ro'>User Role</label>&nbsp;&nbsp;
                    <select className='btn btn-outline-dark' {...register('role',{required : 'User Role is required'})}>
                        <option disabled selected>Select Role</option>
                        <option value='customer'>customer</option>
                        <option value='admin'>admin</option>
                    </select>
                    <p style={{'color':'red'}}>{error.role && error.role.message}</p><br/>

                    
                    <input type='submit' value='Register' style={{padding:10,fontSize:20}} className='btn btn-success col-6'/><br/><br/>
                    
                   
                </form>
            </div>
    </>
  )
}

export default Signup
