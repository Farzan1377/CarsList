import { useEffect, useState } from 'react';
import { BrowserRouter as Router, Switch, Route, Link } from 'react-router-dom';
import Vehicle from './Vehicle';

function MakePost({ match }) {
    console.log(match)
    const id = match.params.id
    const [price, setPrice] = useState()
    const [isPosted, setPosted] = useState(false)

    useEffect(() => {
        fetch(`http://127.0.0.1:5000/posts/get_post?post_id=${id+'c016a996-090d-4215-8b42-6a95c2d5cf29'}`)
      .then(
        function (response) {
          if (response.status !== 200) {
            console.log('Looks like there was a problem. Status Code: ' +
              response.status)
            return
          }

          // Examine the text in the response
          response.json().then(function (data) {
            console.log(data.success.length)
            if (data.success.length != 0) {
                setPosted(true)
                setPrice(data.success[0].price)
            } 
          });
        }
      )
      .catch(function (err) {
        console.log('Fetch Error :-S', err)
      });
    }, [])

    const upload = () => {
        var formdata = new FormData();
                formdata.append("post_id", id+'c016a996-090d-4215-8b42-6a95c2d5cf29');
                formdata.append("vehicle_id", id);
                formdata.append("user_id", 'c016a996-090d-4215-8b42-6a95c2d5cf29');
                formdata.append("price", price);
                var requestOptions = {
                    method: 'POST',
                    body: formdata,
                    redirect: 'follow'
                };
        
                fetch("http://127.0.0.1:5000/posts/create_post", requestOptions)
                    .then(response => response.text())
                    .then(result => console.log(result))
                    .catch(error => console.log('error', error));
            
    }

    const deletePost = () => {

    }

    return (
        <div className="MakePostContainer">
            <h3>{isPosted ? 'Edit posting' : 'Create posting'}</h3>
            <input type="text" placeholder={isPosted ? price : 'price'} onChange={(val) => setPrice(val)} />
            <Link to="/profile">
            <div onClick={upload} className="CreatePostButton"><p>Upload</p></div>
            </Link>
            {isPosted ? <Link to="/profile">
            <div onClick={deletePost} className="CreatePostButton"><p>Delete</p></div>
            </Link> : null}
        </div>
    );
}

export default MakePost;