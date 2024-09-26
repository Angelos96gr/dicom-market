import {formElementStyle, formStyle, buttonClass}  from "../commonStyling"


function Login() {
    return (
        <div className="flex pt-32 justify-center">
            <form action="/login" method="post" className={formStyle}>
                <input className= {formElementStyle} type="text" name="username" autoComplete="off" placeholder="Enter your email" pattern="^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$" title="Please enter a valid email address" required />
                <input className= {formElementStyle} type="password" name="pwd" placeholder="Enter your password" pattern="^[a-zA-Z0-9!]{3,12}$" title="Please enter a password with length between 3 and 12 characters" required />
                <button className={buttonClass} name="login" type="submit">Login</button>
                <button className={buttonClass} name="signup" type="button">Sign up</button>

            </form>
        </div>
    )
}



export default Login