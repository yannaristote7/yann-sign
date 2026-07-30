"use client";


import { useEffect, useState } from "react";
import { getProfile } from "@/services/profile.service";


interface UserProfile {

    id:number;
    username:string;
    email:string;
    role:string;

}



export default function Dashboard(){

    const [user,setUser] = useState<UserProfile | null>(null);


    useEffect(()=>{


        async function loadProfile(){

            try {

                const data = await getProfile();

                setUser(data);


            } catch(error){

                console.error(
                    "Erreur récupération profil",
                    error
                );

            }

        }


        loadProfile();


    },[]);



    if(!user){

        return (
            <main className="flex min-h-screen items-center justify-center">

                Chargement...

            </main>
        );

    }



    return (

        <main className="p-10">


            <h1 className="text-4xl font-bold">

                Bienvenue {user.username}

            </h1>


            <div className="mt-5">


                <p>
                    Email :
                    {user.email}
                </p>


                <p>
                    Rôle :
                    {user.role}
                </p>


            </div>


        </main>

    );

}