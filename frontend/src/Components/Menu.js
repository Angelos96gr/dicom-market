import { Link } from "react-router-dom"


const style = "text-gray text-m rounded-md block px-10 hover:bg-gray-100 hover:text-black  hover:rounded w-full";

function Menu(props) {
    return (
    
    <menu className="fixed bg-white right-0 p-0 m-0 shadow flex rounded-md justify-center">
        <ul>
            <li><Link
                to="/"
                className= {style}
                onClick={props.closeMenu}>
                Home
            </Link></li>
            <li><Link
                to="/login"
                className={style}
                onClick={props.closeMenu}>
                Login
            </Link></li>
            <li><Link
                to="/about"
                className={style}
                onClick={props.closeMenu}>
                About
            </Link></li>
            <li><Link
                to="/FAPI"
                className={style}
                onClick={props.closeMenu}>
                FAPI
            </Link></li>
        </ul>
    </menu>
    
)
}


export default Menu