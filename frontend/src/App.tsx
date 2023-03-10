import { Route, Routes, Link } from 'react-router-dom'
import { HomePage } from './pages/Home/home'
//import { Private } from './pages/Private/index'
import { LoginPage } from './pages/Login/login'
import './App.css';
import * as C from './App.styles';
import { RequireAuth } from './contexts/Auth/RequireAuth';
import { AuthContext } from './contexts/Auth/AuthContext';
import { useContext } from 'react';


const App = () => {
    const auth = useContext(AuthContext)


    //const storageData = JSON.parse(localStorage.getItem('authToken'));
    //
    //if (storageData.access) {
    //    var b64 = window.btoa(storageData.access);
    //    var b65 = window.btoa(jwtDecode(storageData.access));
    //    alert("Codificado: " + b64);
    //    alert("Decodificado: " + window.atob(b65));
    //}

    //const userID = auth.user?.user_id;
    //console.log(userID)


    const handleLogout = async () => {
        await auth.signout();
        window.location.href = window.location.href;
    }

    return (
        <div className="App container">
            <C.Header>
                <C.HeaderText>
                    <h2>Finances</h2>
                </C.HeaderText>
            </C.Header>
            <br />
            <C.Body>
                <nav className="navbar navbar-expand-sm bg-light navbar-dark">
                    <ul className="navbar-nav">
                        <li className="nav-item- m-1">
                            <Link className="btn btn-light btn-outline-primary" to="/">
                                Home
                            </Link>
                        </li>
                        <li className='nav-item- m-1'>
                            {!auth.user ?
                                (<Link className="btn btn-light btn-outline-primary" to="/private">Login</Link>) : (
                                    <Link className="btn btn-light btn-outline-primary" to="/private" onClick={handleLogout} >Sair</Link>
                                )}
                        </li>
                        <li className='nav-item- m-1'>
                            {auth.user ?
                                (<p> Ol?? {auth.user?.username}, tudo bem ? </p>) : (
                                    <p></p>
                                )}
                        </li>
                    </ul>
                </nav>
            </C.Body>

            <Routes>
                <Route path="/" element={<RequireAuth><HomePage /></RequireAuth>} />
                <Route path="/private" element={<LoginPage />} />
            </Routes>
        </div>
    );
}

export default App;