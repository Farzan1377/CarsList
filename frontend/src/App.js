import logo from './logo.svg';
import './App.css';
import Post from './Post';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';
import SinglePost from './SinglePost';
import CreatePost from './CreatePost';
import Profile from './Profile';
import Nav from './Nav';
import { useEffect } from 'react';

function App() {
  
  return (
    <Router>
      <div className="App">
      <Nav />
      <Switch>
        <Route path="/" exact component={Home} />
        <Route path="/abc"  component={SinglePost} />
        <Route path="/createPost"  component={CreatePost} />
        <Route path="/profile"  component={Profile} />
      </Switch>
       
    
      
      </div>
    </Router>
    
  );
}

const Home = () => 
   (
    <>
  <form className="SearchArea">
        
        <input className="SearchBar" type="text" name="name" placeholder="Search..." />
        <button>
        Filter
      </button>
       
      </form>
      
    
    <div className="Postings">
       <Post/>
       
      
        
    </div>
    </>
);


export default App;
