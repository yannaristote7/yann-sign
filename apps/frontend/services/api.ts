import axios from "axios";
import { getAccessToken } from "@/lib/auth";


const api = axios.create({

    baseURL:
        process.env.NEXT_PUBLIC_API_URL ||
        "http://127.0.0.1:8000/api",

    headers: {
        "Content-Type": "application/json",
    },

});


api.interceptors.request.use(
    (config) => {

        const token = getAccessToken();


        if (token) {

            config.headers.Authorization =
                `Bearer ${token}`;

        }


        return config;

    }
);


export default api;