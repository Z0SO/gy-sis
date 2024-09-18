import axios from 'axios';

const API_URL = 'http://localhost:8000/api/historias_clinicas'; // Cambia esto a la URL correcta de tu API.


// Configuración básica de Axios para manejar las peticiones a la API
const api = axios.create({
    baseURL: API_URL,
    headers: {
        'Content-Type': 'application/json',
    },
});


// Función para obtener todas las historias
export const getHistorias = async () => {
    try {
        const response = await api.get('/');
        return response.data;
    } catch (error) {
        console.error('Error al obtener las historias:', error);
        return [];
    }
}

// Función para obtener una historia por su ID
export getHistoriaById = async (id) => {
    try {
        const response = await api.get(`/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error al obtener la historia:', error);
        return null;
    }
}

// Función para crear una historia

export const crearHistoria = async (historia) => {
    try {
        const response = await api.post('/', historia);
        return response.data;
    } catch (error) {
        console.error('Error al crear la historia:', error);
        return null;
    }
}

// Función para actualizar una historia

export const actualizarHistoria = async (id, historia) => {
    try {
        const response = await api.put(`/${id}`, historia);
        return response.data;
    } catch (error) {
        console.error('Error al actualizar la historia:', error);
        return null;
    }
}

// Función para eliminar una historia

export const eliminarHistoria = async (id) => {
    try {
        const response = await api.delete(`/${id}`);
        return response.data;
    } catch (error) {
        console.error('Error al eliminar la historia:', error);
        return null;
    }
}
