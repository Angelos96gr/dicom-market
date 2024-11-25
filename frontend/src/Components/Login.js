import { useEffect, useState } from "react"
import { formElementStyle, formStyle, buttonClass } from "../commonStyling"
import { useNavigate } from "react-router-dom"
import axios from "axios"
import ActionFormResult from "./ActionFormResult"



function Login() {
    const [email, setEmail] = useState("")
    const [pwd, setPwd] = useState("")
    const [loginMessage, setLoginMessage] = useState("")
    const [logSubmissionStatus, setLoginSubmissionStatus] = useState("pending")
    let enteredEmail, enteredPwd
    let navigate = useNavigate()
    const loginUrl = "http://localhost:8000/user/"




    useEffect(() => {
        console.log("rendering useEffect")
        const payload = { "email": email, "password": pwd }
        if (email) {
            axios.post(loginUrl, payload).then((resp) => {
                setLoginSubmissionStatus("completed")
                setLoginMessage(`You have succesfully created a user account with the credentials ${email}`);
                navigate("/user_profile");

            }).catch(err => {
                console.log(err)
                if (err.code == "ERR_NETWORK"){
                    setLoginMessage(`Server is down. Please try again later.`)
                    return
                }
                if (logSubmissionStatus == "ready") {
                    setLoginMessage(`${JSON.parse(err.request.response).detail}`)
                    setEmail("")
                    setPwd("")
                    setLoginSubmissionStatus("pending")
                }
                    
            }

            )
        }

    }, [logSubmissionStatus])


    // enter data in form
    const readCredentials = () => {

        enteredEmail = document.querySelector("#username_login").value
        console.log("enteredEmail", enteredEmail)
        enteredPwd = document.querySelector("#pwd_login").value
        let emailRegex = /^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$/
        let pwdRegex = /^[a-zA-Z0-9!]{3,12}$/

        if (!emailRegex.test(enteredEmail)) {
            setLoginMessage("You have entered an invalid email")
            return
        }
        if (!(pwdRegex.test(enteredPwd))) {
            setLoginMessage("The passwords must be at least 3 digits long")
            return

        }

        setEmail(enteredEmail)
        setPwd(enteredPwd)
        setLoginSubmissionStatus("ready")
    }



    return (
        <div className="flex pt-32 justify-center">
            <div>
                <form className={formStyle}>
                    <input className={formElementStyle} id="username_login" type="text" name="username" autoComplete="off" onClick={() => setLoginSubmissionStatus("pending")} placeholder="Enter your email" pattern="^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$" title="Please enter a valid email address" required />
                    <input className={formElementStyle} id="pwd_login" type="password" name="pwd" placeholder="Enter your password" onClick={() => setLoginSubmissionStatus("pending")} pattern="^[a-zA-Z0-9!]{3,12}$" title="Please enter a password with length between 3 and 12 characters" required />
                    <button className={buttonClass} name="login" type="button" onClick={readCredentials}>Login</button>
                    <button className={buttonClass} name="signup" type="button" onClick={() => navigate("/signup")}>Sign up</button>

                </form>
                <ActionFormResult message={loginMessage} />

            </div>

        </div>
    )
}



export default Login