import React, { useState , useEffect} from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome"
import { faBars } from "@fortawesome/free-solid-svg-icons"
import { Link } from "react-router-dom";
import Menu  from "./Menu";

function Navigation() {

    //react hook to know if menu is open or not
    const [showMenu, setShowMenu] = useState(false)
    const closeMenu = ()=>setShowMenu(false)
    let menu

    //conditional rendering

    if (showMenu) {
        menu = <Menu closeMenu = {closeMenu} />
    }
    return (
        <nav>
            <span>
                <FontAwesomeIcon icon={faBars} onClick={() => setShowMenu(!showMenu)} />
            </span>
            {menu}
        </nav>
    )

}


export default Navigation 
