import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';

function Post() {
    return (
    
        <Link to="/abc">
        <div className="Post">
        <img className="PostImage" src="https://images.craigslist.org/01212_6xRHfNWpFtGz_0CI0t2_600x450.jpg"/>
      </div>
        </Link>
   
    
      
    );
  }
  
export default Post;