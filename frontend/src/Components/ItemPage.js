import { useParams } from "react-router-dom"

function ItemPage(){


    const {id} = useParams()
    console.log(id)
    return(
        <div>This is the itempage for {id}</div>
    )

}


export default ItemPage