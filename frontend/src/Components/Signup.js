import { Link } from "react-router-dom"
import { formElementStyle, formStyle, buttonClass } from "../commonStyling"

function Signup() {


    return (<div className="flex pt-32 justify-center">
        <form action="/signup" method="post" className={formStyle}>
            <input className={formElementStyle} type="text" name="username" autoComplete="off" placeholder="Enter your email" pattern="^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$" title="Please enter a valid email address" required />
            <input className={formElementStyle} type="text" name="firstname" autoComplete="off" placeholder="Enter your first name" pattern="^[a-zA-Z]+$" required />
            <input className={formElementStyle} type="text" name="lastname" autoComplete="off" placeholder="Enter your last name" pattern="^[a-zA-Z]+$" required />
            <input className={formElementStyle} type="text" name="address" autoComplete="off" placeholder="Enter your address" required />
            <Link className={buttonClass} to={`/signup`}>Sign up</Link>
        </form>
    </div>)
}


export default Signup