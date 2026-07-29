"use client";

import { useState } from "react";
import { login } from "@/services/auth.service";
import { saveTokens } from "@/lib/auth";


export default function LoginPage(){

    const [username,setUsername] = useState("");
    const [password,setPassword] = useState("");


    async function handleLogin(){

        try {

            const data = await login({
                username,
                password
            });


            saveTokens(
                data.access,
                data.refresh
            );


            alert("Connexion réussie");


        } catch(error){

            alert("Erreur de connexion");

        }

    }


    return (

        <main className="flex min-h-screen items-center justify-center">

            <div>

                <h1 className="text-3xl font-bold mb-5">
                    Connexion YANN Sign
                </h1>


                <input
                    className="border p-2 block mb-3"
                    placeholder="Username"
                    onChange={
                        e => setUsername(e.target.value)
                    }
                />


                <input
                    className="border p-2 block mb-3"
                    type="password"
                    placeholder="Password"
                    onChange={
                        e => setPassword(e.target.value)
                    }
                />


                <button
                    className="bg-black text-white px-4 py-2"
                    onClick={handleLogin}
                >
                    Se connecter
                </button>

            </div>

        </main>

    );
}