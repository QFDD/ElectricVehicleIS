import axios from 'axios';

const API_URL = 'http://10.193.160.177:5000/api'; 

export const getPendingServiceRecords = (page = 1, limit = 10) => {
    return axios.get(`${API_URL}/pending_services`, {
        params: { page, limit }
    });
};
export const getProcessedServiceRecords = (page = 1, limit = 10) => {
    return axios.get(`${API_URL}/processed_services`, {
        params: { page, limit }
    });
};
export const fetchTotalRecords = () => {
    return axios.get(`${API_URL}/total_records`)
}

export const fetchProcessedTotalRecords = () => {
    return axios.get(`${API_URL}/processed_total_records`)
}
export const getParts = (page = 1, limit = 10) => {
    return axios.get(`${API_URL}/parts`, {
        params: { page, limit }
    });
}