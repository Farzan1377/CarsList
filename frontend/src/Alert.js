import { useEffect, useState } from 'react';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';

function Alert(props) {
    
    return (
        <div className="AlertContainer">
            <h3>Are you sure want to proceed?</h3>
            <div className="ActionButton">Yes</div>
            <div className="ActionButton">No</div>
        </div>
    ); 
  }
  
export default Alert;