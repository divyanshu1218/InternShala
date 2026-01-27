import api from '../config/api';

export const videoService = {
    async fetchDashboard() {
        try {
            const response = await api.get('/dashboard/');
            return response.data;
        } catch (error) {
            throw error.response ? error.response.data : error;
        }
    },

    async getStreamUrl(videoId, token) {
        try {
            const response = await api.get(`/video/${videoId}/stream?token=${token}`);
            return response.data;
        } catch (error) {
            throw error.response ? error.response.data : error;
        }
    }
};
