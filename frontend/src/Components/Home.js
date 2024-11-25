import React, { useState, useEffect } from "react";
import {
    Icon
} from 'semantic-ui-react'

import imageFiles from "./imageFiles.json"


function Home() {

    const imageArray = imageFiles.files
    const [img, setImg] = useState(imageArray[0])
    const getCurrentImage = (el) => el === img;

    const updateImagePrevious = () => {

        const currIndex = imageArray.findIndex(getCurrentImage)

        if (currIndex > 0) {
            setImg(imageArray[currIndex - 1])
        }
        else {
            setImg(imageArray[imageArray.length - 1])
        }


    }

    const updateImageNext = () => {

        const currIndex = imageArray.findIndex(getCurrentImage)
        if (currIndex < (imageArray.length - 1)) {
            setImg(imageArray[currIndex + 1])
        }
        else {
            setImg(imageArray[0])

        }


    }


    /* ToDo periodic image update
    useEffect(() => {
        console.log("Setting timer")
        const regularUpdate = setInterval(updateImageNext, 8000)
    }
        , [])

    */


    return (
        <div className="flex justify-center items-center px-10 pt-12">
            <Icon name="chevron left" className="cursor-pointer" onClick={updateImagePrevious}></Icon>
            <img src={img} alt="HomePage" className="w-2/5 h-96" />
            <Icon name="chevron right" className="cursor-pointer" onClick={updateImageNext}></Icon>
        </div>)
}


export default Home