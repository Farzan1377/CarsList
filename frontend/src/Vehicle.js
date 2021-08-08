import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import deleteLogo from './deleteLogo.png';
import editLogo from './editLogo.png';

function Vehicle(props) {
  const car = props.car
  const tesst = () => {
    console.log('propss', props)
    props.getID(car.vehicle_id)
  }

  const deleteVehicle = () => {

    console.log('delete')
    
    fetch(`http://127.0.0.1:5000/vehicles/delete_user_vehicles?vehicle_id=${car.vehicle_id}`)
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
            tesst()
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
  }

  return (
    
    <Link to={`makePost=${car.vehicle_id}`}>
      <div className="Vehicle">
        <img className="VehicleImage" src={car.image_url} />
        <Link to="/editVehicle">
          <div className="VehicleEdit">
            <img className="Logo" src={editLogo} />
          </div>
        </Link>
        <div onClick={deleteVehicle} className="VehicleDelete">
          <img className="Logo" src={deleteLogo} />
        </div>
      </div>
    </Link>
    

  );
}

export default Vehicle;