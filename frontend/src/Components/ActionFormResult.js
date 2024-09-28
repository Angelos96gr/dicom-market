import { useEffect, useState } from "react"


function ActionFormResult(props) {
    return (
        <div className="dlex flex-col justify-center text-center">

            <div id="resultMessage" className="item-center w-80 m-4">
                {props.message}
            </div>
        </div>
    )
}


export default ActionFormResult