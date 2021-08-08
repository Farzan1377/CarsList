import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import deleteLogo from './deleteLogo.png';
import editLogo from './editLogo.png';

function EditVehicle(props) {
  const [vehicle, setVehicle] = useState([])
  const [manufacturer, setManufacturer] = useState()
  const [model, setModel] = useState()
  const [year, setYear] = useState()
  const [type, setType] = useState()
  const [vehicleCondition, setVehicleCondition] = useState()
  const [odometer, setOdometer] = useState()
  const [color, setColor] = useState()
  const [description, setDescription] = useState()

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
            setVehicle(data.success[0])
            
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
  }, [])

  useEffect(() => {
    setManufacturer(vehicle.manufacturer)
    setModel(vehicle.model)
    setYear(vehicle.year)
    setType(vehicle.type)
    setVehicleCondition(vehicle.vehicle_condition)
    setOdometer(vehicle.odometer)
    setColor(vehicle.paint_color)
    setDescription(vehicle.description)
  }, [vehicle])
  
  const saveUpdates = () => {
    var formdata = new FormData();
    formdata.append("vehicle_id", vehicle.vehicle_id);
    formdata.append("manufacturer", manufacturer);
    formdata.append("model", model);
    formdata.append("year", year);
    formdata.append("type", type);
    formdata.append("vehicle_condition", vehicleCondition);
    formdata.append("odometer", odometer);
    formdata.append("paint_color", color);
    formdata.append("description", description);

    var requestOptions = {
      method: 'PUT',
      body: formdata,
      redirect: 'follow'
    };

    fetch("http://127.0.0.1:5000/vehicles/update_user_vehicles", requestOptions)
      .then(response => response.text())
      .then(result => console.log(result))
      .catch(error => console.log('error', error));
  }

  return (
    <>
      <div className="EditVehicleContainer">
       <h1>Edit your vehicle</h1>
       <div className="SmallContainer">
           <div className="VehicleInfoSmall">
                <h4>Manufacturer</h4>
                <input type="text" placeholder={manufacturer} onChange={(val) => setManufacturer(val.target.value)} />
           </div>
           <div className="VehicleInfoSmall">
                <h4>Model</h4>
                <input type="text" placeholder={model} onChange={(val) => setModel(val.target.value)} />
           </div>
       </div>
       <div className="SmallContainer">
            <div className="VehicleInfoSmall">
                <h4>Year</h4>
                <input type="text" placeholder={year} onChange={(val) => setYear(val.target.value)} />
            </div>
            <div className="VehicleInfoSmall">
                <h4>Type</h4>
                <input type="text" placeholder={type} onChange={(val) => setType(val.target.value)} />
            </div>
        </div>
        <div className="SmallContainer">
            <div className="VehicleInfoSmall">
                <h4>Vehicle Condition</h4>
                <input type="text" placeholder={vehicleCondition} onChange={(val) => setVehicleCondition(val.target.value)} />
            </div>
            <div className="VehicleInfoSmall">
                <h4>Odometer</h4>
                <input type="text" placeholder={odometer} onChange={(val) => setOdometer(val.target.value)} />
            </div>
        </div>
        <div className="LastContainer">
            <div className="VehicleInfoSmall">
                <h4>Paint Color</h4>
                <input type="text" placeholder={color} onChange={(val) => setColor(val.target.value)} />
            </div>
        </div>
       <div className="VehicleInfo">
           <h4>Description</h4>
           <input type="text" placeholder={description} onChange={(val) => setDescription(val.target.value)} />
       </div>
       <Link to="/profile">
            <div onClick={saveUpdates} className="CreatePostButton"><p>Save</p></div>
        </Link>
      </div>
    </>

  );
}

export default EditVehicle;