
15 Sep 2024:
- Initial commit including basic setup of home, browse, view, login, about components
- Draft FastApi code and sqlalchemy code
- Currently mock data is pulled through a dummy open source API (to be changed after FastAPI is implemented)


22 Sep 2024
- FastAPI works with sqlite and no response models
- routing, crud, db initialization and models setup


26 Sep 2024
- Backend: Connection with postgreSQL and create user
- Frontend: Factoring out styling and new Signup page component/route

28 Sep 2024
- Backend: Finished apis to manage users (CRUD) & better error handling (HTTP exceptions)
- Frontent: Connection with Backend api to register new user & UserProfilePage placeholder site

10 Oct 2024
- Backend: Admin tools & router splits
- Frontend: Admint tool page displaying all users of the app


13 Oct 2024
- Frontend: 
    - Hompage with sliding images taken from a .json file



23 Nov 2024
- Frontend:
    - Basic functionality (form fill, checking regex and sending request to BE implemented - missing check and request response resolution)
    - Delete user from UserProfilePage component
    - Improved error handling in AdminView component
- Backend:
    - Corrections in hashed password verification
    - New .sh for setting up backend server + README


24 Nov 2024:
- FE error handling for network problems in Login/Signup components
- BE integration for login/authentication functionality (incl. error handling) - pending JWT integration




25 Nov 2024
- Upload component: File upload (user input from local disk)
