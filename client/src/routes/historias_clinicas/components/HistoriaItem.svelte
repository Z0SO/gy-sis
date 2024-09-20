<script>
  import { onMount } from 'svelte';

  // pedimos la funcion que nos traera el paciente por id
  import { getPacienteById } from '../../pacientes/api/pacientes.api.js';

  // exportamos la historia clinica para poder usarla en el componente HistoriasList.svelte
  export let una_historia = {};

  // en la historia clinica esta el id del paciente guardamos el id del paciente
  const id_paciente = una_historia.paciente;

  // creamos un objeto paciente vacio para guardar la informacion del paciente
  let un_paciente = {};

  // Una vez que se monta el componente, traemos el paciente con el id correspondiente a su historia clínica
  onMount(async () => {
    try {
      
      const pac = await getPacienteById(id_paciente);

      // guardamos el paciente en la variable un_paciente
      un_paciente = pac;
    } catch (error) {
      console.error("Error al obtener el paciente:", error);
    }
  });


</script>


<div class="bg-white shadow-lg rounded-lg px-8 pt-8 pb-8 mb-8 flex flex-col my-4 max-w-4xl mx-auto border border-gray-200">
  <!-- Título con el nombre del paciente --> 
  <h2 class="text-3xl font-extrabold text-gray-800 text-center mb-6">Historia Clínica de {un_paciente.pac_nombre}</h2>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
    <!-- Motivo de consulta -->
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">Motivo de consulta</label>
      <p class="text-base text-gray-800">{una_historia.motivo_consulta}</p>
    </div>

    <!-- Derivado por -->
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">Derivado por</label>
      <p class="text-base text-gray-800">{una_historia.derivado_por}</p>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
    <!-- Antecedentes clínicos -->
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">Antecedentes clínicos</label>
      <p class="text-base text-gray-800">{una_historia.antecedentes_clinicos}</p>
    </div>

    <!-- HC Laboratorio -->
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">HC Laboratorio</label>
      <p class="text-base text-gray-800">{una_historia.hc_laboratorio}</p>
    </div>
  </div>

  <div class="grid grid-cols-1 md:grid-cols-2 gap-6 mb-8">
    <!-- Diagnóstico presuntivo -->
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">Diagnóstico presuntivo</label>
      <p class="text-base text-gray-800">{una_historia.diagnostico_presuntivo}</p>
    </div>

    <!-- Tratamientos anteriores -->
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">Tratamientos anteriores</label>
      <p class="text-base text-gray-800">{una_historia.tratamientos_anteriores}</p>
    </div>
  </div>

  <!-- Tratamiento actual -->
  <div class="grid grid-cols-1 mb-8">
    <div>
      <label class="block text-sm font-semibold text-gray-600 uppercase mb-2">Tratamiento actual</label>
      <p class="text-base text-gray-800">{una_historia.tratamiento_actual}</p>
    </div>
  </div>
</div>
