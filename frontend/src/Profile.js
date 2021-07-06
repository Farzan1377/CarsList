import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';

function Profile(props) {
    return (
      <div className="Profile">
        <h1>Welcome back John!</h1>
        <Link to="/createPost">
            <p>Create Posting</p>
        </Link>
        
      </div>
    ); 
  }
  
export default Profile;