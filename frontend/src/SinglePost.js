import { useEffect, useState } from "react";
import carPlaceholder from './carPlaceholder.jpeg';
import Image from './Image'

function SinglePost({match}) {
  
  const id = match.params.id
  const index = id.search(';')
  const vehicle_id = id.substring(0,index)
  const user_id = id.substring(index+1)
  const [post, setPost] = useState([])
  const [poster, setPoster] = useState([])

  useEffect(() => {

    fetch(`http://127.0.0.1:5000/users/get_user_info?user_id=${user_id}`)
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
            setPoster(data.success[0])
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });

    fetch(`http://127.0.0.1:5000/vehicles/get_user_vehicles?user_id=${user_id}`)
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
            setPost(data.success[0])
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
  }, [])
    console.log(post)
    return (
      <div className="SinglePost">
        <h1>{post.manufacturer} {post.model} {post.year}</h1>
        <h1>{post.price}</h1>
        <Image src={post.image_url} className="PostImage" fallbackSource={carPlaceholder} />
        <p>{post.description}</p>
        <div className="SinglePoster">
          
          <Image src={poster.picture} className="PostImage" fallbackSource={carPlaceholder} />
          <p> Contact {poster.name} at {poster.email} or {poster.phone}</p>
        </div>
      </div>
    ); 
  }
  
export default SinglePost;