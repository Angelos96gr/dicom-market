

function UserProfilePage(props) {

    return (
        <div>
            This is the user profile area
            <div className="flex flex-row bg-red-100 h-screen p-5 justify-between">
                <div className="flex flex-col bg-green-100 m-10">Here we have the user info for user {props.user}
                    <div className="bg-yellow-100 m-5 w-80 h-80">
                        the photo
                    </div>
                </div>
                <div className="flex flex-col bg-blue-100 m-10 w-screen">Here are the items
                    <div>Item 1
                    </div>
                    <div>Item 2
                    </div>

                </div>
            </div>
        </div>
    )

}



export default UserProfilePage