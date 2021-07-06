function CreatePost(props) {
    return (
      <div className="CreatePost">
        <h1>Create new posting</h1>
        <form>
        
        <input placeholder="Title" type="text" name="name" />
        <input placeholder="Description" type="text" name="desc" />
        <input type="file" name="myImage"  />
        <input type="submit" value="Submit" />
        </form>
      </div>
    ); 
  }
  
export default CreatePost;