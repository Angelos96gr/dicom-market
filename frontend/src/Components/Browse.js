
import axios from "axios"
import { useEffect, useState } from "react"
import { useParams } from "react-router-dom"
import Loader from "./Loader"
import ItemCard from "./ItemCard"
import { useAxiosGet } from "../Hooks/HttpRequestsAxios"
import FilterSideBar from "./FilterSideBar"


function Browse() {
    let content

    // Replace with FastAPI routes
    const { q } = useParams()
    const url = `https://api.thecatapi.com/v1/images/search?limit=10`
    let items = useAxiosGet(url)

    if (items.data) {

        content =
            <div className="justify-center flex flex-col items-center">
                {items.data.map(item => <div key = {item.id}><ItemCard itemCard={item} /></div>)}
            </div>


    }

    if (items.loading) {
        content = <Loader /> //spinner in case of slow item load - implemnt at page level
    }

    if (items.error) {
        content = <div>Error {items.data.status}: Please refresh the page or try again later</div>
    }

    return (
        <div className="flex flex-row">
            <FilterSideBar />
            <div>
                {content}
            </div>
        </div>
    )




}



export default Browse

