import logo from './logo.svg';
import DropdownButton from 'react-bootstrap/DropdownButton';
import Dropdown from 'react-bootstrap/Dropdown';
import './App.css';
import Post from './Post';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import SinglePost from './SinglePost';
import CreatePost from './CreatePost';
import Profile from './Profile';
import Nav from './Nav';
import { useEffect, useState } from 'react';
import Myvehicles from './CreatePost';
import EditVehicle from './EditVehicle';
import CreateVehicle from './CreateVehicle';
import MakePost from './MakePost';

function App() {
  return (
    <Router>
      <div className="App">
        <Nav />
        <Switch>
          <Route path='/' exact component={Home} />
          <Route path="/id=:id" component={SinglePost} />
          <Route path="/createPost" component={CreateVehicle} />
          <Route path="/profile" component={Profile} />
          <Route path="/editVehicle" component={EditVehicle} />
          <Route path="/makePost=:id" component={MakePost} />
        </Switch>
      </div>
    </Router>
  );
}

const Home = () => {
  const [pageNum, setPageNum] = useState(1)
  const [shownCars, setShownCars] = useState([])
  const [manufacturer, setManufacturer] = useState('')
  const [lowPrice, setPriceLow] = useState('')
  const [highPrice, setPriceHigh] = useState('')
  const manufacturers = ['all','ford', 'mercedes-benz', 'chevrolet', 'honda', 'nissan', 'jeep', 'toyota', 'buick', 'lexus', 'volkswagen', 'acura', 'mini', 'rover', 'chrysler', 'ram', 'cadillac', 'volvo', 'kia', 'porsche', 'gmc', 'dodge', 'infiniti', 'hyundai', 'subaru', 'mazda', 'audi', 'pontiac', 'bmw', 'fiat', 'saturn', 'jaguar', 'lincoln', 'mitsubishi', 'tesla', 'mercury', 'harley-davidson', 'alfa-romeo']
  const priceLow = ['all','0', '500', '1000', '1500', '2000', '5000', '8000', '10000', '15000']
  const priceHigh = ['all','500', '1000', '2000', '8000', '10000', '15000', '25000', '50000', '70000', '120000']
  const manufacturerItems = manufacturers.map((manufacturer) => <Dropdown.Item key={manufacturer} onClick={() => setManufacturer(manufacturer)}>{manufacturer}</Dropdown.Item>)
  const priceLowItems = priceLow.map((price) => <Dropdown.Item key={price} onClick={() => setPriceLow(price)}>{price}</Dropdown.Item>)
  const priceHighItems = priceHigh.map((price) => <Dropdown.Item key={price} onClick={() => setPriceHigh(price)}>{price}</Dropdown.Item>)
  const randomData = [1,2,3,4,5,6,7,8,9,10]
  const pageItems = randomData.map((data) => <div key={data} onClick={() => changePage(data)} className="dot"></div>)
  console.log('HEERE', shownCars)

  const changePage = (data) => {
    console.log('page changed', data)
    fetch(`http://127.0.0.1:5000/posts/recent_posts?start_index=${data*48-47}&end_index=${data*48}`)
      .then(
        function (response) {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
              response.status)
            return
          }

          // Examine the text in the response
          response.json().then(function (data) {
            setShownCars(data.success)
            
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
  }

  useEffect(() => {
    changePage(1)
  }, [])
  useEffect(() => {
    console.log(`changed ${manufacturer} ${lowPrice} ${highPrice}`)
      // fetch filtering api
      fetch(`http://127.0.0.1:5000/search/select_vehicles?manufacturer=${manufacturer == 'all' ? '' : manufacturer}&price_low=${lowPrice == 'all' ? '' : lowPrice}&price_high=${highPrice == 'all' ? '' : highPrice}`)
      .then(
        function (response) {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
              response.status)
            return
          }

          // Examine the text in the response
          response.json().then(function (data) {
            console.log('gfgfg',data)
            setShownCars(data.data)
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
  }, [lowPrice, manufacturer, highPrice])
  
  
  const cars = shownCars.map((car) => <Post key={car.vehicle_id+car.user_id}  car={car}/>)

  
  
  return (
    <>
      <div className="Dropdowns">
        <DropdownButton className="ManuDropButton" id="Manufacturer" title={`Manufacturer ${manufacturer}`}>
          {manufacturerItems}
        </DropdownButton>
        <DropdownButton className="ManuDropButton" title={`Price Low ${lowPrice}`}>
          {priceLowItems}
        </DropdownButton>
        <DropdownButton className="ManuDropButton" id="PriceHigh" title={`Price High ${highPrice}`}>
          {priceHighItems}
        </DropdownButton>
      </div>


      <div className="Postings">
        {cars}
        <div className="Paging">
        {pageItems}
      </div>
      </div>
      
    </>
  );
}

export default App;
