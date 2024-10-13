
<script>
  import { onMount } from 'svelte';
  import { crearHistoria } from '../api/historias.api.js';
  import { getPacientes } from '../../pacientes/api/pacientes.api.js';

  let motivo_consulta = '';
  let derivado_por = '';
  let antecedentes_clinicos = '';
  let hc_laboratorio = '';
  let diagnostico_presuntivo = '';
  let tratamientos_anteriores = '';
  let tratamiento_actual = '';
  let paciente = null; // Selected patient ID
  let pacientes = []; // List of patients

  // Fetch patients on component mount
  onMount(async () => {
    pacientes = await getPacientes();
  });

  const handleSubmit = async () => {
    const historia = {
      motivo_consulta,
      derivado_por,
      antecedentes_clinicos,
      hc_laboratorio,
      diagnostico_presuntivo,
      tratamientos_anteriores,
      tratamiento_actual,
      paciente // Ensure this is the patient ID
    };

    try {
      await createHistoriaClinica(historia);
      alert('Historia clínica creada con éxito');
    } catch (error) {
      alert('Error al crear la historia clínica');
    }
  };
</script>

<div class="container mx-auto px-6 md:px-8 mt-40 bg-white dark:bg-neutral-800 p-8 shadow-lg rounded-lg transition-all duration-200 ease-in-out">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-3xl font-bold text-gray-800 dark:text-white mb-6">Crear Historia Clínica</h1>
    <form on:submit|preventDefault={handleSubmit}>
      <div class="grid grid-cols-1 gap-6">
        <!-- Patient selection field -->
        <div>
          <label for="paciente" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Paciente</label>
          <select id="paciente" bind:value={paciente} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required>
            <option value="" disabled selected>Seleccione un paciente</option>
            {#each pacientes as paciente}
              <option value={paciente.id}>{paciente.pac_nombre}</option>
            {/each}
          </select>
        </div>

        <!-- Rest of the form fields -->
        <div>
          <label for="motivo_consulta" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Motivo de Consulta</label>
          <textarea id="motivo_consulta" bind:value={motivo_consulta} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="derivado_por" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Derivado Por</label>
          <input type="text" id="derivado_por" bind:value={derivado_por} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" required />
        </div>
        <div>
          <label for="antecedentes_clinicos" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Antecedentes Clínicos</label>
          <textarea id="antecedentes_clinicos" bind:value={antecedentes_clinicos} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="hc_laboratorio" class="block text-sm font-medium text-gray-700 dark:text-gray-200">HC Laboratorio</label>
          <textarea id="hc_laboratorio" bind:value={hc_laboratorio} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="diagnostico_presuntivo" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Diagnóstico Presuntivo</label>
          <textarea id="diagnostico_presuntivo" bind:value={diagnostico_presuntivo} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="tratamientos_anteriores" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Tratamientos Anteriores</label>
          <textarea id="tratamientos_anteriores" bind:value={tratamientos_anteriores} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="tratamiento_actual" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Tratamiento Actual</label>
          <textarea id="tratamiento_actual" bind:value={tratamiento_actual} class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
      </div>
      <div class="mt-6">
        <button type="submit" class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-zinc-500 hover:bg-zinc-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-zinc-500 dark:focus:ring-zinc-500 dark:focus:ring-offset-zinc-800">Crear Historia Clínica</button>
      </div>
    </form>
  </div>
</div>
