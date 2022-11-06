import "./Navbar.css";
import { useState } from "react";
import { Link, useNavigate } from "react-router-dom";

import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faGripHorizontal, faUser, faQuestion } from "@fortawesome/free-solid-svg-icons";

export default function Navbar() {
    const [links, setLinks] = useState(["Dashboard", "Account", "FAQ"])

    return(<nav className="shadow-sm">
        <Link to="/"><FontAwesomeIcon icon={faGripHorizontal} className="nav-icon" size="2x" /></Link>
        <FontAwesomeIcon icon={faUser} className="nav-icon" size="2x" />
        <FontAwesomeIcon icon={faQuestion} className="nav-icon" size="2x" />
    
    </nav>);
}