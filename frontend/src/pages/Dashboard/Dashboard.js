import { useState } from "react";

import "./Dashboard.css";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPen, faPlusCircle } from "@fortawesome/free-solid-svg-icons";

export default function Dashboard() {
    const [bots, setBots] = useState([
        {
            name: "Bot 1",
            active: true
        },
        {
            name: "Bot 2",
            active: false
        },
        {
            name: "Bot 3",
            active: true
        },
        {
            name: "Bot 4",
            active: true
        }
    ]);

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
                    <h3 className="bot-name">{bot.name}</h3>
                    <div className="bot-actions d-flex align-items-center gap-3">
                        <FontAwesomeIcon icon={faPen} />   
                    </div>
                </div>)}

                <div className="create-bot-icon-div">
                    <FontAwesomeIcon icon={faPlusCircle} size="2x" className="create-bot-icon mt-3" />   
                </div>
            </div> 
              
        </section>  
    </div>);
}