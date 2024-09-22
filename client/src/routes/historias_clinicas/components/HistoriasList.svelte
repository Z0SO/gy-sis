
<script>
  import { onMount } from 'svelte';
  import { getHistorias } from '../api/historias.api.js';
  import HistoriaItem from './HistoriaItem.svelte';

  let LTHC = [];

  onMount(async () => {
    try {
      LTHC = await getHistorias();
    } catch (error) {
      console.error("Error al obtener las historias clínicas:", error);
    }
  });
</script>

<!-- Tabla de historias clínicas con más espacio y mejor interactividad -->
<div
  class="overflow-x-auto bg-white dark:bg-neutral-800 rounded-lg p-8"
>
  <table
    class="min-w-full bg-white dark:bg-neutral-800 dark:text-neutral-200 shadow-md rounded-lg overflow-hidden"
  >
    <thead>
      <tr class="bg-gray-100 dark:bg-neutral-700 text-gray-600 dark:text-neutral-300 uppercase text-sm leading-normal">
        <th class="py-4 px-6 text-left">Paciente</th>
        <th class="py-4 px-6 text-left">Motivo de Consulta</th>
        <th class="py-4 px-6 text-left">Derivado por</th>
        <th class="py-4 px-6 text-left">Antecedentes Clínicos</th>
        <th class="py-4 px-6 text-left">Diagnóstico Presuntivo</th>
        <th class="py-4 px-6 text-left">Tratamiento Actual</th>
      </tr>
    </thead>
    <tbody class="text-gray-600 dark:text-neutral-300 text-sm font-light">
      {#each LTHC as una_historia}
        <HistoriaItem {una_historia} />
      {/each}
    </tbody>
  </table>
</div>
