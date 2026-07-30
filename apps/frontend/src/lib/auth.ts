export function saveTokens(
    access: string,
    refresh: string
) {

    localStorage.setItem(
        "access_token",
        access
    );

    localStorage.setItem(
        "refresh_token",
        refresh
    );
}



export function getAccessToken() {

    return localStorage.getItem(
        "access_token"
    );

}



export function logout() {

    localStorage.removeItem(
        "access_token"
    );

    localStorage.removeItem(
        "refresh_token"
    );

}