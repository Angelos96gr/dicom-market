import { Link } from "react-router-dom"
import { formElementStyle, formStyle, buttonClass } from "../commonStyling"
import { useEffect, useState } from "react"
import axios from "axios"
import ActionFormResult from "./ActionFormResult"
import { useNavigate } from "react-router-dom"


function Signup() {
    const [email, setEmail] = useState("")
    const [pwd, setPwd] = useState("")
    const [signupMessage, setSignupMessage] = useState("")
    const [submissionStatus, setSubmissionStatus] = useState("pending")
    let enteredEmail, enteredPwd1, enteredPwd2
    let navigate = useNavigate()

    const createUserUrl = "http://localhost:8000/users/"



    useEffect(() => {

        const payload = { "email": email, "password": pwd }
        if (email) {
            axios.post(createUserUrl, payload).then((resp) => {
                setSubmissionStatus("completed")
                setSignupMessage(`You have succesfully created a user account with the credentials ${email}`);
                navigate("/user_profile");

            }).catch(err => {
                if (err.code == "ERR_NETWORK"){
                    setSignupMessage(`Server is down. Please try again later.`)
                    return
                }
                if (submissionStatus == "ready") {
                    setSignupMessage(`${JSON.parse(err.request.response).detail}! `)
                    setEmail("")
                    setPwd("")
                    setSubmissionStatus("pending")
                }
            }

            )
        }

    }, [submissionStatus])



    const readCredentials = () => {
        enteredEmail = document.querySelector("#username_signup").value
        enteredPwd1 = document.querySelector("#pwd_signup").value
        enteredPwd2 = document.querySelector("#pwd2_signup").value
        let emailRegex = /^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$/
        let pwdRegex = /^[a-zA-Z0-9!]{3,12}$/

        if (!emailRegex.test(enteredEmail)) {
            setSignupMessage("You have entered an invalid email")
            return
        }

        if (enteredPwd2 != enteredPwd1) {
            setSignupMessage("The entered passwords do not match")
            return
        }
        if (!(pwdRegex.test(enteredPwd1)) || !pwdRegex.test(enteredPwd2)) {
            setSignupMessage("The passwords must be at least 3 digits long")
            return

        }

        setEmail(enteredEmail)
        setPwd(enteredPwd1)
        setSubmissionStatus("ready")
    }


    return (
        <div className="flex flex-col items-center">
            <div className="flex pt-32 justify-center">
                <form className={formStyle} >
                    <input className={formElementStyle} id="username_signup" type="text" name="username" autoComplete="off" onChange={() => setSubmissionStatus("pending")} placeholder="Enter your email" title="Please enter a valid email address" required />
                    <input className={formElementStyle} id="pwd_signup" type="password" name="pwd" onChange={() => setSubmissionStatus("pending")} placeholder="Enter your password" title="Please enter a password with length between 3 and 12 characters" required />
                    <input className={formElementStyle} id="pwd2_signup" type="password" name="pwd1" onChange={() => setSubmissionStatus("pending")} placeholder="Repeat your password" title="Please enter a password with length between 3 and 12 characters" required />
                    <button className={buttonClass} name="signup" type="button" onClick={readCredentials}>Sign up</button>
                </form>

            </div>
            <ActionFormResult message={signupMessage} />

        </div>)
}


export default Signup