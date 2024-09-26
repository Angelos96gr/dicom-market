import { text } from "@fortawesome/fontawesome-svg-core";
import { useState } from "react";
import { useNavigate } from "react-router-dom";
import { buttonClassGo } from "../commonStyling";

function SearchBar() {


    const [formData, setFormData] = useState({});
    const navigate = useNavigate();


    const handleSubmit = (event) => {
        event.preventDefault(); // Prevents default form submission behavior



      const dataToSubmit = {
        ...formData // Any additional form data object here
      };

      const {searchTerm} = dataToSubmit

      navigate(`/browse/${searchTerm}`);
    }
    
    const handleInputChange = (event) => {
        const { target } = event;
        const { name, value } = target;
        setFormData({
          ...formData, // Keep existing form data
          [name]: value // Update form data for the input field that changed
        });
      }

    return (
        <div>
            <form className="flex p-3 m-1 justify-center items-center block gap-2" onSubmit={handleSubmit}>
                <input className="border rounded-2xl  w-2/5 p-2" type="text" placeholder="Enter a search term" name="searchTerm" onChange={handleInputChange}/>
                <button className={buttonClassGo} type="submit">Go</button>
            </form>
        </div>)

    }

export default SearchBar