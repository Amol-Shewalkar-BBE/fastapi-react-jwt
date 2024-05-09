import React from 'react'
import { Navigate } from 'react-router-dom'

function Logincheck(OriginalComponent) {

    function NewComponent(props){
        if(sessionStorage.getItem('access')){
            return <OriginalComponent/>
        }
        else
        {
            return <Navigate to='/login'/>
        }
    }
  return NewComponent
}

export default Logincheck
