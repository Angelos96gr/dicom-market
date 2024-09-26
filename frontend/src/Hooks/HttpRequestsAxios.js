import axios from "axios"
import { useEffect, useState } from "react"


export function useAxiosGet(url){
    
const [items, setItems] = useState({
    loading: false,
    data: null,
    error: false
})

useEffect(() => {
    setItems({
        loading: true,
        data: null,
        error: false
    })

    axios.get(url).then((resp) => {
        console.log(resp.data)

        setItems({
            loading: false,
            data: resp.data,
            error: false
        })
    }).catch(err =>

        setItems({
            loading: false,
            data: err,
            error: true
        }))


}, [url])//effect function will rerun once the url changes\

return items

}
