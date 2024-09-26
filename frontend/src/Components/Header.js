import React from "react";
import Navigation from "./Navigation";
import { Link } from "react-router-dom";
import { headerClass } from "../commonStyling";

function Header() {

    return (
        <header className={headerClass}>
            <Link to="/">
            <span className="font-bold">DCMarket</span>
            </Link>
            <span>The best DICOM in the market</span>
        
        
        
        <Navigation />
        </header>
    )

}

export default Header