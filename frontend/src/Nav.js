import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';
import companyLogo from './carLogo.png';

function Nav() {
    return (
        <nav className="navBar">
            <Link to="/">
            <img className="CompanyLogo" src={companyLogo}/>
            </Link>
            
            <ul className="navItems">
                <Link to="/profile">
                <li className="ProfilePicContainer">
                    <img className="ProfilePic" src="https://randomuser.me/api/portraits/men/31.jpg"/>
                </li>
                </Link>
                
            </ul>
        </nav>
    )
}

export default Nav;