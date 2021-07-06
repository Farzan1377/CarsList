import { useEffect } from "react";

function SinglePost(props) {
    
    return (
      <div className="SinglePost">
        <h1>Ford F15ik0 2018</h1>
        <h1>$20,000</h1>
        <img className="SinglePostImage" src="https://images.craigslist.org/01212_6xRHfNWpFtGz_0CI0t2_600x450.jpg"></img>
        <p>Description</p>
        <button>Contact me.</button>
      </div>
    ); 
  }
  
export default SinglePost;