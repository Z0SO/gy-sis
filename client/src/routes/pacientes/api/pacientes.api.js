
import axios from 'axios';

const API_URL = 'http://localhost:8000/api/pacientes';


// Obtener todos los pacientes
export const getPacientes = async () => {
    try {
        const response = await axios.get(API_URL);
        return response.data;
    }
    catch (error) {
        console.error(error);
    }

}

// Función para obtener un paciente por su id
export const getPacienteById = async (id) => {
    try {
        const response = await axios.get(`${API_URL}/${id}`);
        return response.data;
    }
    catch (error) {
        console.error(error);
    }
}

// Función para crear un paciente

export const crearPaciente = async (paciente) => {
    try {
        const response = await axios.post(API_URL, paciente);
        return response.data;
    }
    catch (error) {
        console.error(error);
    }
}

// Función para actualizar un paciente

export const actualizarPaciente = async (id, paciente) => {
    try {
        const response = await axios.put(`${API_URL}/${id}`, paciente);
        return response.data;
    }
    catch (error) {
        console.error(error);
    }
}

// Función para eliminar un paciente

export const eliminarPaciente = async (id) => {
    try {
        const response = await axios.delete(`${API_URL}/${id}`);
        return response.data;
    }
    catch (error) {
        console.error(error);
    }
}



