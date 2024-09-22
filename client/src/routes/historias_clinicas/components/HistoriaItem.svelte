
<script>
  import { onMount } from 'svelte';
  import { getPacienteById } from '../../pacientes/api/pacientes.api.js';
  import { goto } from '$app/navigation';

  export let una_historia = {};
  let un_paciente = {};

  const gotoHistoriaClinica = () => {
    goto(`/historias_clinicas/${una_historia.id}`);
  };

  onMount(async () => {
    try {
      un_paciente = await getPacienteById(una_historia.paciente);
    } catch (error) {
      console.error("Error al obtener el paciente:", error);
    }
  });
</script>

<!-- Fila de la tabla con mejor espaciado, interactividad y transiciones -->
<tr on:click={gotoHistoriaClinica} 
  class="border-b border-gray-200 dark:border-neutral-700 hover:bg-gray-100 dark:hover:bg-neutral-700 cursor-pointer transition-all duration-200 ease-linear">
  <!-- Paciente -->
  <td class="py-4 px-6 text-left whitespace-nowrap">
    <div class="flex items-center">
      <span class="font-medium text-gray-800 dark:text-neutral-200">{un_paciente?.pac_nombre || 'Cargando...'}</span>
    </div>
  </td>
  
  <!-- Motivo de consulta -->
  <td class="py-4 px-6 text-left">
    <div class="flex items-center">
      <span>{una_historia.motivo_consulta}</span>
    </div>
  </td>

  <!-- Derivado por -->
  <td class="py-4 px-6 text-left">
    <span>{una_historia.derivado_por}</span>
  </td>

  <!-- Antecedentes clínicos -->
  <td class="py-4 px-6 text-left">
    <span>{una_historia.antecedentes_clinicos}</span>
  </td>

  <!-- Diagnóstico presuntivo -->
  <td class="py-4 px-6 text-left">
    <span>{una_historia.diagnostico_presuntivo}</span>
  </td>

  <!-- Tratamiento actual -->
  <td class="py-4 px-6 text-left">
    <span>{una_historia.tratamiento_actual}</span>
  </td>
</tr>
