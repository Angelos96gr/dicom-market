import { useAxiosGet } from "../Hooks/HttpRequestsAxios"

function AdminView() {

    const adminUrl = "http://localhost:8000/admin/users"
    let usersRendered
    let tableRendered
    let len = "0"

    const userList = useAxiosGet(adminUrl).data
    console.log(typeof (userList))

    if (userList) {
        usersRendered = userList.map(d => (<tr key = {d.id}><td className="border-2">{d.id}</td><td className="border-2">{d.email}</td><td className="border-2">{d.hashed_password}</td></tr>))
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
        len = Object.keys(userList).length
    }



    return (
        <h1> There are currently {len} users
            {tableRendered}
        </h1>
    )
}


export default AdminView