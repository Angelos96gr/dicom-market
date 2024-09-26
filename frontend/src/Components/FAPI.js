
import { useAxiosGet } from "../Hooks/HttpRequestsAxios"





function FAPI(){

    let content = null
    const url = "http://localhost:8000/"
    const response = useAxiosGet(url)

    if (response.data){
        content = response.data.message
    }



    return (
        <div>
            <h1>Axios request temp</h1>
            <h2>{content}</h2>

        </div>
    )
}


export default FAPI