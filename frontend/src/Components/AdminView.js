import { isAxiosError } from "axios"
import { useAxiosGet } from "../Hooks/HttpRequestsAxios"

function AdminView() {

    const adminUrl = "http://localhost:8000/admin/users"
    let usersRendered
    let tableRendered = <div></div>
    let responseResult
    let len = "0"

    const userListResponse = useAxiosGet(adminUrl).data
    console.log(userListResponse)

    if (userListResponse) {
        if (isAxiosError(userListResponse)) {

            console.log("message to print", userListResponse.message)
            responseResult = <div> {userListResponse.message}: There seems to be an issue with retrieving the requested information. Check the server works as expected.</div>
        }
        else {
            usersRendered = userListResponse.map(d => (<tr key={d.id}><td className="border-2">{d.id}</td><td className="border-2">{d.email}</td><td className="border-2">{d.hashed_password}</td></tr>))
            tableRendered = (<table className="border-2 table-auto">
                <thead>
                    <tr>
                        <th>ID</th>
                        <th>Username</th>
                        <th>Hashed password</th>
                    </tr>
                </thead>
                <tbody>
                    {usersRendered}
                </tbody>
            </table>)
            len = Object.keys(userListResponse).length
            responseResult = <div>There are currently {len} users</div>
        }

    }



    return (
        <div>
            {responseResult}
            {tableRendered}
        </div>
    )
}


export default AdminView