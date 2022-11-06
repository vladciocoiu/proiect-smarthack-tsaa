import { useState, useEffect } from "react";
import { useParams } from "react-router-dom";
import Dropdown from "react-bootstrap/Dropdown";
import DropdownButton from "react-bootstrap/DropdownButton";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faX } from "@fortawesome/free-solid-svg-icons";

import "./EditBot.css";

const API_URL = "http://192.168.22.162:8000/api";

export default function EditBot() {
    const { botId } = useParams();
    const [active, setActive] = useState(false);
    const [username, setUsername] = useState("");
    const [actions, setActions] = useState([]);
    const [subreddit, setSubreddit] = useState("tsaa");
    const [action, setAction] = useState({});
    const [keywords, setKeywords] = useState([]);
    const [findIn, setFindIn] = useState("");
    const [notify, setNotify] = useState(false);
    const [showNewAction, setShowNewAction] = useState(false);
    const [reqData, setReqData] = useState({});
    const [showUpdateSuccessful, setShowUpdateSuccessful] = useState(false);

    useEffect(() => {
        const fetchBotData = async() => {
            const response = await fetch(API_URL + "/bots/" + botId);
            const data = await response.json();

            console.log(data);
            setActive(data?.active);
            setSubreddit(data?.taskQueue[0].params?.subreddit);
            setKeywords(data?.taskQueue[0].params.keywords);
            setUsername(data.username);
            setActions(data?.taskQueue);
            setReqData(data);
        }
        fetchBotData();
    }, []);

    const updateBot = async (newActions) => {
        // e.preventDefault();
        const requestBody = { ...reqData, taskQueue: newActions };
        console.log(requestBody);
        const response = await fetch(API_URL + '/bots/' + botId, {
            method: 'PUT',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();

        setShowUpdateSuccessful(true);
        setTimeout(() => setShowUpdateSuccessful(false), 5000);
        console.log(data);
    }

    const saveFindIn = async () => {
        const newFindIn = {
            type: "find",
            params: {
                keywords,
                findIn: findIn.toLowerCase(),
                subreddit
            }
        };

        const newActions = [...actions];
        newActions.shift();
        newActions.unshift(newFindIn);
        setActions(newActions);

        updateBot(newActions);
    }

    const addKeyword = (e) => {
        e.preventDefault();
        const word = e.target[0].value;
        if(keywords.includes(word)) return;

        const newKeywords = [...keywords];
        newKeywords.push(word);
        setKeywords(newKeywords);
    }

    const removeWord = (word) => {
        const newKeywords = keywords.filter(w => w != word);
        setKeywords(newKeywords);
    }

    return (<div className="edit-bot-page">
        <div className="edit-bot-form">
            <h1 className="bot-name">{username}</h1>
            <div className="find-in-div border-0 shadow-sm">
                <p className="find-in-text find">FIND</p>
                <form className="add-keyword-form" onSubmit={addKeyword}>
                    <input type="text" placeholder="Keyword" className="keyword-input" />
                </form>
                <p className="find-in-text in">IN</p>
                <DropdownButton id="dropdown-button" title={findIn}>
                    {["Comments", "Posts"].map(el => <Dropdown.Item onClick={() => setFindIn(el)}>{el}</Dropdown.Item> )}
                </DropdownButton>
                <div className="keyword-list shadow-sm border-0 p-2">
                    {(keywords.length 
                        ? keywords.map(word => <div className="keyword shadow-sm">
                            <p>{word}</p>
                            <FontAwesomeIcon onClick={() => removeWord(word)} icon={faX} size="xs" className="delete-keyword-icon" />
                        </div>)
                        : <p className="no-keywords">No keywords...</p>
                    )}
                </div>
                <div className="actions-list">
                    {actions.slice(1).map(action => <ListAction action={action} />)}
                </div>

                <p className={"update-successful-message " + (showUpdateSuccessful ? "opaque" : "transparent")}>Bot Updated Successfully!</p>
                <button className="save-find-in shadow-sm" onClick={saveFindIn}>Save</button>
            </div>
            {showNewAction && <ActionForm actions={actions} setActions={setActions} setShowNewAction={setShowNewAction} updateBot={updateBot} />}
            <button className="create-action shadow-sm p-3" onClick={() => setShowNewAction(true)}>Create Action</button>
        </div>
    </div>);
}

function ListAction({ action }) {

    const transformInterval = interval => {
        if(interval <= 60 * 60) return "Hourly";
        if(interval == 60 * 60 * 24) return "Daily";
        return "Weekly";
    }

    return (<div className="action shadow-sm p-2 border-0">
        <p className="type">{action.type[0].toUpperCase() + action.type.slice(1)}</p>
        {action.type == "notify" ? <p className="interval-p">{transformInterval(action.params?.interval)}</p> : ""}
        {action.type == "reply" ? <p className="message-p">{"'" + action.params?.message + "'"}</p> : ""}
    </div>);
}

function ActionForm({ actions, setActions, setShowNewAction, updateBot }) {
    const [type, setType] = useState("");
    const [interval, setInterval] = useState("");
    const [message, setMessage] = useState("");

    const transformTime = interval => {
        if(interval == "Hourly") return 60 * 60;
        if(interval == "Daily") return 60 * 60 * 24;
        if(interval == "Weekly") return 60 * 60 * 24 * 7;
    }

    const handleSubmit = async e => {
        e.preventDefault();
        const action = {
            type: type.toLowerCase(),
            params: {}
        }
        if(type == "Reply") action.params = { message };
        else if(type == "Notify") action.params = { interval: transformTime(interval) };
        
        const newActions = [...actions];
        newActions.push(action);
        setActions(newActions);

        setShowNewAction(false);
    }

    return (<form onSubmit={handleSubmit} className={"new-action-form border-0 shadow-sm m-3 p-3 " + (type ? "action-form-" + type : "")}>
        <h2 className="new-action-title mt-4">New Action</h2>
        <DropdownButton id="action-form-dropdown" title={type || "Type"}>
            {["Reply", "Delete", "Notify"].map(el => <Dropdown.Item onClick={() => setType(el)}>{el}</Dropdown.Item> )}
        </DropdownButton>  
        {(type == "Reply" ? <input className="mesasge-input" name="message" value={message} onChange={(e) => setMessage(e.target.value)} placeholder="Message" /> : '')}
        {(type == "Notify" 
            ? <DropdownButton id="time-dropdown" title={interval || "Time Interval"}>
                {["Hourly", "Daily", "Weekly"].map(el => <Dropdown.Item onClick={() => setInterval(el)}>{el}</Dropdown.Item> )}
            </DropdownButton>
            : '')}

        <button className="submit-action shadow-sm">Submit</button>
    </form>);
}