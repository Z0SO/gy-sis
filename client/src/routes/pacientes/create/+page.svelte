
<script>
  import { onMount } from 'svelte';
  import { crearPaciente } from '../api/pacientes.api.js'; // Import the function to create a patient

  let pac_dni = '';
  let pac_nombre = '';
  let pac_edad = '';
  let pac_domicilio = '';
  let pac_obrasocial = '';
  let pac_telefono = '';
  let pac_telefono_emergencia = '';
  let pac_ocupacion = '';
  let pac_estadocivil = '';

  const handleSubmit = async () => {
    const paciente = {
      pac_dni,
      pac_nombre,
      pac_edad,
      pac_domicilio,
      pac_obrasocial,
      pac_telefono,
      pac_telefono_emergencia,
      pac_ocupacion,
      pac_estadocivil
    };

    try {
      await crearPaciente(paciente);
      alert('Paciente creado con éxito');
    } catch (error) {
      alert('Error al crear el paciente');
    }
  };
</script>

<div class="container mx-auto px-6 md:px-8 mt-40 bg-white dark:bg-neutral-800 p-8 shadow-lg rounded-lg transition-all duration-200 ease-in-out">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-white mb-6">Crear Paciente</h1>
    <form on:submit|preventDefault={handleSubmit}>
      <div class="grid grid-cols-1 gap-6">
        <div>
          <label for="pac_dni" class="block text-sm font-medium text-gray-700 dark:text-gray-200">DNI</label>
          <input type="text" id="pac_dni" bind:value={pac_dni} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_nombre" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Nombre</label>
          <input type="text" id="pac_nombre" bind:value={pac_nombre} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_edad" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Edad</label>
          <input type="number" id="pac_edad" bind:value={pac_edad} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_domicilio" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Domicilio</label>
          <input type="text" id="pac_domicilio" bind:value={pac_domicilio} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_obrasocial" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Obra Social</label>
          <input type="text" id="pac_obrasocial" bind:value={pac_obrasocial} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_telefono" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Teléfono</label>
          <input type="text" id="pac_telefono" bind:value={pac_telefono} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_telefono_emergencia" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Teléfono de Emergencia</label>
          <input type="text" id="pac_telefono_emergencia" bind:value={pac_telefono_emergencia} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_ocupacion" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Ocupación</label>
          <input type="text" id="pac_ocupacion" bind:value={pac_ocupacion} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="pac_estadocivil" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Estado Civil</label>
          <input type="text" id="pac_estadocivil" bind:value={pac_estadocivil} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
      </div>
      <div class="mt-6">
        <button type="submit" class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-zinc-500 hover:bg-zinc-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-zinc-500 dark:focus:ring-zinc-500 dark:focus:ring-offset-zinc-800">Crear Paciente</button>
      </div>
    </form>
  </div>
</div>

