import { useState, useEffect } from "react";
import { Link } from "react-router-dom";

import "./Dashboard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen, faPlusCircle } from "@fortawesome/free-solid-svg-icons";

const API_URL = process.env.REACT_APP_API_URL;

export default function Dashboard() {


    const [bots, setBots] = useState([]);

    useEffect(() => {
        const getBots = async () => {
            const response = await fetch(API_URL + "/bots");
            const data = await response.json();
            console.log(data);
            setBots(data);
        }
        getBots();
    }, []);

    const handleCheck = (e, idx) => {
        const newBots = [...bots];
        const bot = newBots[idx];
        bot.active = !bot.active;
        newBots[idx] = bot;

        setBots(newBots);

    }

    return (<div className="dashboard">
        <div className="title-div"><h1 className="title">Dashboard</h1></div>
        <section className="my-bots-section card p-4 flex flex-column shadow-sm border-0">
            <h2 className="card-title mt-3">My Bots</h2>
            <div className="card-body bots-list mt-2">
                {bots.map( (bot, idx) => <div key={bot.name} className={"bot mb-3 mt-3 shadow-sm border-0 d-flex" + (!bot.active ? " bot-transparent " : "")}>
                    <h3 className="bot-name">{bot.username}</h3>
                    <div className="bot-actions d-flex align-items-center gap-3">
                        <Link to={"/bots/" + bot.id + "/edit"}><FontAwesomeIcon className="edit-bot-icon" icon={faPen} /></Link>   
                    </div>
                </div>)}
            </div> 
            <div className="create-bot-icon-div">
                <Link to="/create-bot"><FontAwesomeIcon icon={faPlusCircle} size="2x" className="create-bot-icon mt-3" /></Link>
            </div>
              
        </section>  
    </div>);
}