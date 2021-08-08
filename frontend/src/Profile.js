import { useEffect, useState } from 'react';
import {BrowserRouter as Router, Switch, Route, Link} from 'react-router-dom';
import Vehicle from './Vehicle';

function Profile(props) {

    const [user, setUser] = useState({"gender":"male","name":{"title":"Mr","first":"Carter","last":"Steward"},"location":{"street":{"number":7250,"name":"W Dallas St"},"city":"Albury","state":"Australian Capital Territory","country":"Australia","postcode":7574,"coordinates":{"latitude":"-79.5399","longitude":"-9.7348"},"timezone":{"offset":"+5:00","description":"Ekaterinburg, Islamabad, Karachi, Tashkent"}},"email":"carter.steward@example.com","login":{"uuid":"2dabe015-9780-45dc-9911-d576dd520f2e","username":"bigcat859","password":"marlene","salt":"IBHbtZWh","md5":"97144981ed1b30c9287b63adabd55a4f","sha1":"3b6a6d88aa415883813c2be6eadefa1f37312c12","sha256":"a2bee5f4ab6b294319329f28e639c338c9ebf0f019e48b3edb41cd832e33c823"},"dob":{"date":"1963-08-08T14:03:27.910Z","age":58},"registered":{"date":"2010-09-22T02:58:30.214Z","age":11},"phone":"08-8310-9198","cell":"0447-513-801","id":{"name":"TFN","value":"182050953"},"picture":{"large":"https://randomuser.me/api/portraits/men/42.jpg","medium":"https://randomuser.me/api/portraits/med/men/42.jpg","thumbnail":"https://randomuser.me/api/portraits/thumb/men/42.jpg"},"nat":"AU"})
    const [userVehicles, setUserVehicles] = useState([])
   
    useEffect(() => {
      fetch('http://127.0.0.1:5000/vehicles/get_user_vehicles?user_id=c016a996-090d-4215-8b42-6a95c2d5cf29')
      .then(
        function (response) {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
              response.status)
            return
          }

          // Examine the text in the response
          response.json().then(function (data) {
            console.log(data)
            setUserVehicles(data.success)
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
    }, [])

    const removeCar = (id) => {
      console.log('id', id)
      setUserVehicles(vehicles.filter(vehicle => vehicle.vehicle_id != id))
    }

    const vehicles = userVehicles.map((car) => <Vehicle key={car.vehicle_id} car={car} getID={removeCar} />)
    console.log(user)
    return (
      <div className="Profile">
        
        <h1 className="Font">{user.name.first} {user.name.last}</h1>
        <h3 className="ProfileInfo Font">{user.login.username}</h3>
        <h3 className="ProfileInfo Font">{user.email}</h3>
        <div className="CreatePostSection">
          <Link to="/createPost">
            <div className="CreatePostButton"><p>Create Vehicle</p></div>
          </Link>
        </div>
        <h3 className="VehiclesTitle">My vehicles</h3>
        <div className="VehiclesSection">
          {vehicles}
        </div>
        
        
      </div>
    ); 
  }
  
export default Profile;