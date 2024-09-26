

const formElementStyle = "w-80 px-2 py-2 m-2 border rounded-md "
const buttonClass = "w-40 py-2 m-2 bg-blue-400 hover:bg-blue-500 text-white py-2 px-4 rounded-xl"

function Login() {
    return (
        <div className="flex pt-32 justify-center  ">
            <form action="/login" method="post" className="flex flex-col bg-blue-100 p-4 rounded-md items-center">
                <input className= {formElementStyle} type="text" name="username" autoComplete="off" placeholder="Enter your email" pattern="^[a-zA-Z0-9]+@[a-zA-Z]+\.[a-z]+$" title="Please enter a valid email address" required />
                <input className= {formElementStyle} type="password" name="pwd" placeholder="Enter your password" pattern="^[a-zA-Z0-9!]{3,12}$" title="Please enter a password with length between 3 and 12 characters" required />
                <button className={buttonClass} name="login" type="submit">Login</button>
                <button className={buttonClass} name="signup" type="button">Signup</button>

            </form>
        </div>
    )
}



export default Login