import { Link } from "react-router-dom"


const buttonClass = "bg-blue-400 hover:bg-blue-500 text-white py-2 px-4 rounded-xl"


function ItemCard(props) {

    return (
        <div>
            <Link to={`/view/${props.itemCard.id}`}>
                <img className="w-full h-100 p-2 overflow-hidden" src={props.itemCard.url} alt={props.itemCard.id} />
            </Link>
            <div className="p-3 flex justify-center">
                <Link className={buttonClass} to={`/view/${props.itemCard.id}`}>
                    View

                </Link>
            </div>
        </div>
    )
}

export default ItemCard