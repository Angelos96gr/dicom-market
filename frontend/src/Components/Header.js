import React from "react";
import Navigation from "./Navigation";
import { Link } from "react-router-dom";


function Header() {

    return (
        <header className="bg-blue-100 border-b p-5 flex justify-between items-center">
            <Link to="/">
            <span className="font-bold">DCMarket</span>
            </Link>
            <span>The best DICOM in the market</span>
        
        
        
        <Navigation />
        </header>
    )

}

export default Header