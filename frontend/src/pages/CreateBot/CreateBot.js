import { useState, useEffect } from "react";

import "./CreateBot.css";

const API_URL = process.env.REACT_APP_API_URL;

export default function CreateBot() {
    const [redditUsername, setRedditUsername] = useState("");
    const [clientId, setClientId] = useState("");
    const [clientSecret, setClientSecret] = useState("");
    const [username, setUsername] = useState("");
    const [password, setPassword] = useState("");

    const handleSubmit = async (e) => {
        e.preventDefault();
        const requestBody = { redditUsername, clientId, clientSecret, username, password };
        console.log(requestBody);
        const response = await fetch(API_URL + '/bots', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json'
            },
            body: JSON.stringify(requestBody)
        });

        const data = await response.json();
        console.log(data);
    }


    return (<div className="create-bot-page">
        <form onSubmit={handleSubmit} className="create-bot-form card p-4 flex flex-column shadow-sm border-0">
            <h2 className="form-title card-title mt-3">Create New Bot</h2>
            <input className="shadow-sm mt-3" type="text" value={redditUsername} onChange={(e) => setRedditUsername(e.target.value)} name="reddit-username" placeholder="Your Reddit Username" required />
            <input className="shadow-sm mt-3" type="text" value={clientId} onChange={(e) => setClientId(e.target.value)} name="client-id" placeholder="Client ID" required />
            <input className="shadow-sm mt-3" type="password" value={clientSecret} onChange={(e) => setClientSecret(e.target.value)} name="client-secret" placeholder="Client Secret Key" required />
            <input className="shadow-sm mt-3" type="text" value={username} onChange={(e) => setUsername(e.target.value)} name="username" placeholder="Bot Username" required />
            <input className="shadow-sm mt-3" type="password" value={password} onChange={(e) => setPassword(e.target.value)} name="password" placeholder="Password" required />
            <button className="shadow-sm form-submit-button btn btn-primary mt-4">Submit</button>
        </form>
    </div>);
}