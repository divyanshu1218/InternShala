import api, { storage } from '../config/api';

export const authService = {
    async login(email, password) {
        try {
            const response = await api.post('/auth/login', { email, password });
            if (response.data.token) {
                await storage.setItem('userToken', response.data.token);
            }
            return response.data;
        } catch (error) {
            throw error.response ? error.response.data : error;
        }
    },

    async signup(name, email, password) {
        try {
            const response = await api.post('/auth/signup', { name, email, password });
            return response.data;
        } catch (error) {
            throw error.response ? error.response.data : error;
        }
    },

    async logout() {
        try {
            // Optional: Notify backend
            // await api.post('/auth/logout');
            await storage.deleteItem('userToken');
        } catch (error) {
            console.error('Logout error', error);
        }
    },

    async getProfile() {
        try {
            const response = await api.get('/auth/me');
            return response.data;
        } catch (error) {
            throw error.response ? error.response.data : error;
        }
    },

    async getToken() {
        return await storage.getItem('userToken');
    }
};
