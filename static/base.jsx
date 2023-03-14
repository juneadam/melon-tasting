// React components to handle melon-tasting as a 1-page app

import Root from "./static/root";

const router = createBrowserRouter([
    {
      path: "/",
      element: <Root />,
    },
  ]);

ReactDOM.createRoot(document.getElementById("root")).render(
    <React.StrictMode>
      <RouterProvider router={router} />
    </React.StrictMode>
  );

// const LoginForm = (props) => {
    
//     return (
//         <div className="container">
//             <form>
//                 <div className="mb-3">
//                     <label for="emailInput" className="form-label">Email</label>
//                     <input type="email" className="form-control" id="emailInput"></input>
//                 </div>
//                 <div className="mb-3">
//                     <label for="passwordInput" className="form-label">Password</label>
//                     <input type="password" className="form-control" id="passwordInput"></input>
//                 </div>
//                 <button type="submit" className="btn btn-primary">Submit</button>
//             </form>
//         </div>
//     );
  
// }

// const NotLoginForm = (props) => {
//     return (
//         <div className="container">
//             <p>
//                 Hello world.
//             </p>
//         </div>
//     )
// }

// const LoginContainer = (props) => {
//     // const [loginStatus, updateLoginStatus] = React.useState(0);
//     loginStatus = props.loginStatus

//     // const fetchStatus = () => {
//     //     fetch('/login-check.json')
//     //     .then((response) => response.json())
//     //     .then((statusJSON) => {
//     //         updateLoginStatus(statusJSON['data'])
//     //     });
//     // }

//     // React.useEffect(fetchStatus, []);

//     // if (this.state.loginStatus) {
//     //     return <MelonScheduler />;
//     // }
//     if (loginStatus){
//         return <NotLoginForm />
//     }
//     return <LoginForm />;
// }

// ReactDOM.render(<LoginContainer loginStatus={false} />, document.querySelector('#content'));