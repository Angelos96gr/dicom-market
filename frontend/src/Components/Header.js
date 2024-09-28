import React, { useState } from "react";
import Navigation from "./Navigation";
import { Link } from "react-router-dom";
import { headerClass } from "../commonStyling";

function Header(props) {


    return (
        <header className={headerClass}>
            <Link to="/">
            <span className="font-bold">DCMarket</span>
            </Link>
            <span>The best DICOM in the market</span>
        
        
        <div className="flex flex-row w-60 bg-blue-100 justify-between">
            <div className="pr-5">{props.user}</div>
        <Navigation />

        </div>
        </header>
    )

}

export default Header