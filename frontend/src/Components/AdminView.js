import { useAxiosGet } from "../Hooks/HttpRequestsAxios"

function AdminView() {

    const adminUrl = "http://localhost:8000/admin/1/user_overview"
    let usersRendered

    const userList = useAxiosGet(adminUrl).data
    console.log(userList)

    if (userList) {
        usersRendered = userList.map(d => (<li key={d.id}>{d.email}</li>))
    }

    return (
        <h1> List of app users
            {usersRendered}
        </h1>
    )
}


export default AdminView