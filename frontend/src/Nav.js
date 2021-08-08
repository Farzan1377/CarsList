import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';
import companyLogo from './carLogo.png';

function Nav() {
    return (
        <nav className="navBar">
            <Link to="/">
            <img className="CompanyLogo" src={companyLogo}/>
            </Link>
            
            <Link to="/profile">
                <div className="ProfilePicContainer">
                    <img className="ProfilePic" src="https://randomuser.me/api/portraits/men/31.jpg"/>
                </div>
            </Link>

           
        </nav>
    )
}

export default Nav;