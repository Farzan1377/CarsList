import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import carPlaceholder from './carPlaceholder.jpeg';
import Image from './Image'
function Post({ car }) {

  return (
    <Link to={`id=${car.vehicle_id};${car.user_id}`}>
      <div className="Post">
        <Image src={car.image_url} className="PostImage" fallbackSource={carPlaceholder} />
      </div>
    </Link>
  );
}

export default Post;