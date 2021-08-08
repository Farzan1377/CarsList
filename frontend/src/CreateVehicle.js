import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import deleteLogo from './deleteLogo.png';
import editLogo from './editLogo.png';
import { v4 as uuidv4 } from 'uuid';

function CreateVehicle(props) {
    
    const [manufacturer, setManufacturer] = useState()
    const [model, setModel] = useState()
    const [year, setYear] = useState()
    const [type, setType] = useState()
    const [vehicleCondition, setVehicleCondition] = useState()
    const [odometer, setOdometer] = useState()
    const [color, setColor] = useState()
    const [image, setImage] = useState()
    const [description, setDescription] = useState()

    const saveUpdates = () => {
        var imgURL = ''
        const data = new FormData()
            data.append("image", image)
            fetch("https://api.imgur.com/3/image/", {
                method: "post",
                headers: {
                    Authorization: "Client-ID 4d4f9d618c33390"
                },
                body: data
            }).then(data => data.json()).then(data => {
                console.log('success', data)
                imgURL = data.data.link
                var formdata = new FormData();
                formdata.append("vehicle_id", uuidv4());
                formdata.append("user_id", "c016a996-090d-4215-8b42-6a95c2d5cf29");
                formdata.append("manufacturer", manufacturer);
                formdata.append("model", model);
                formdata.append("year", year);
                formdata.append("type", type);
                formdata.append("vehicle_condition", vehicleCondition);
                formdata.append("odometer", odometer);
                formdata.append("paint_color", color);
                formdata.append("image_url", imgURL);
                formdata.append("description", description);
                var requestOptions = {
                    method: 'POST',
                    body: formdata,
                    redirect: 'follow'
                };
        
                fetch("http://127.0.0.1:5000/vehicles/create_user_vehicles", requestOptions)
                    .then(response => response.text())
                    .then(result => console.log(result))
                    .catch(error => console.log('error', error));
            })
   
    }

    return (
        <>
            <div className="EditVehicleContainer">
                <h1>Create a new vehicle</h1>
                <div className="SmallContainer">
                    <div className="VehicleInfoSmall">
                        <h4>Manufacturer</h4>
                        <input type="text" onChange={(val) => setManufacturer(val.target.value)} />
                    </div>
                    <div className="VehicleInfoSmall">
                        <h4>Model</h4>
                        <input type="text" onChange={(val) => setModel(val.target.value)} />
                    </div>
                </div>
                <div className="SmallContainer">
                    <div className="VehicleInfoSmall">
                        <h4>Year</h4>
                        <input type="text" onChange={(val) => setYear(val.target.value)} />
                    </div>
                    <div className="VehicleInfoSmall">
                        <h4>Type</h4>
                        <input type="text" onChange={(val) => setType(val.target.value)} />
                    </div>
                </div>
                <div className="SmallContainer">
                    <div className="VehicleInfoSmall">
                        <h4>Vehicle Condition</h4>
                        <input type="text" onChange={(val) => setVehicleCondition(val.target.value)} />
                    </div>
                    <div className="VehicleInfoSmall">
                        <h4>Odometer</h4>
                        <input type="text" onChange={(val) => setOdometer(val.target.value)} />
                    </div>
                </div>
                <div className="SmallContainer">
                    <div className="VehicleInfoSmall">
                        <h4>Paint Color</h4>
                        <input type="text" onChange={(val) => setColor(val.target.value)} />
                    </div>
                    <div className="VehicleInfoSmall">
                        <h4>Image</h4>
                        <input type="file" onChange={val => setImage(val.target.files[0])} />
                    </div>
                </div>
                <div className="VehicleInfo">
                    <h4>Description</h4>
                    <input type="text" onChange={(val) => setDescription(val.target.value)} />
                </div>
                <Link to="/profile">
                    <div onClick={saveUpdates} className="CreatePostButton"><p>Create</p></div>
                </Link>
            </div>
        </>

    );
}

export default CreateVehicle;