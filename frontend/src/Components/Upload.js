import { useState } from "react"
import { formElementStyle, formStyle, buttonClass } from "../commonStyling"



function Upload() {

    const [selectedFile, setSelectedFile] = useState("")

    const formData = new FormData()

    const getFileName = (event) =>
    {
        const fileName = event.target.files[0]
        console.log(fileName)
        setSelectedFile(fileName)

    }

    const showFileName = () =>
    {if (selectedFile){
        return(
            <div>
                <div>Selected file:</div>
                <div>{selectedFile.name}</div>
            </div>
        )
    }}


    return (


        <div>
            <label>Select a file to upload</label><br></br>
            <input type="file" id="filename" accept = ".dcm" onChange={getFileName}></input>
            <button className = {buttonClass} type="button">Upload</button>
            {showFileName()}
        </div>


    )
}

export default Upload