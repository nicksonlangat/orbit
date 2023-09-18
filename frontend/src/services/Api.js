import axios from 'axios'

export default (use_token = true) => {

    let headers = {
        Accept: 'application/json',
        'Content-Type': 'application/json',
    }

    if (use_token) {
        headers['Authorization'] = `Bearer ${localStorage.getItem('orbit')}` 
    }
    const Api = axios.create({
        baseURL: process.env.VUE_APP_BASE_URL,
        withCredentials: false,
        headers: headers
    })
    return Api
}
