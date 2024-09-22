
<script>
  // /roues/historias_clinicas/[id]/+page.svelte

  import { onMount } from 'svelte';
  import { getPacienteById } from '../../pacientes/api/pacientes.api.js';
  
  import { getHistorias } from '../api/historias.api.js';

  // para obtener parametros de la url
  import { page } from '$app/stores';


  let listaHistoriasClinicas = null;
  
  let historiaClinica = {};


  let un_paciente = {};

  let cargando = true;

  let error_page = null;

  onMount(async () => {

    // obtenemos el id de la historia clinica que viene en la url, por ejemplo: /historias_clinicas/1 -> id = 1
    const {id} = $page.params;

    try {

      listaHistoriasClinicas = await getHistorias();
      un_paciente = await getPacienteById(id);
      
      console.log('ID del paciente de la URL:', id);
      console.log('Lista de historias clínicas:', listaHistoriasClinicas);

      // se filtran las historias clinicas para obtener la que corresponde al paciente de la url que es la id del paciente que se selecciono
      historiaClinica = listaHistoriasClinicas.find(historia => historia.pac_id === un_paciente.pac_id);

    
      console.log('Historia Clínica del paciente:', historiaClinica);
    } catch (error) {
      error_page = error;
    } finally {
      cargando = false;
    }

    
  });

</script>


<br><br><br><br><br>

<!-- importamos el componente de navegación -->
<div
  class="container mx-auto px-4 sm:px-8 max-w-3xl mt-8"
>

  <div
    class="bg-white dark:bg-neutral-800  shadow-lg rounded-lg p-6"
  >
    <h1
      class="text-2xl font-semibold text-neutral-800 dark:text-neutral-200"
    >
      Historia Clínica de {un_paciente.pac_nombre}
    </h1>

    {#if cargando}
      <p>Cargando...</p>
    {:else}
      {#if error_page}
        <p>{error_page.message}</p>
      {:else}
        <div
          class="mt-4"
        >
          <div
            class="flex flex-col"
          >
            <div
              class="flex flex-col"
            >
              <label
                for="motivo_consulta"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Motivo de consulta
              </label>
              <p
                class="text-neutral-800 dark:text-neutral-200"
              >
                {historiaClinica.motivo_consulta}
              </p>
            </div>

            <div
              class="flex flex-col mt-4"
            >
              <label
                for="derivado_por"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Derivado por
              </label>
              <p
                class="text-neutral-800 dark:text-neutral-200"
              >
                {historiaClinica.derivado_por}
              </p>
            </div>

            <div
              class="flex flex-col mt-4"
            >
              <label
                for="antecedentes_clinicos"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Antecedentes clínicos
              </label>
              <p
                class="text-neutral-800 dark:text-neutral-200"
              >
                {historiaClinica.antecedentes_clinicos}
              </p>
            </div>

            <div
              class="flex flex-col mt-4"
            >
              <label
                for="hc_laboratorio"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Historia Clínica de laboratorio
              </label>
              <p class="text-neutral-800 dark:text-neutral-200">
                {historiaClinica.hc_laboratorio}
              </p>
            </div>

            <div
              class="flex flex-col mt-4"
            >
              <label
                for="diagnostico_presuntivo"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Diagnóstico presuntivo
              </label>
              <p
                class="text-neutral-800 dark:text-neutral-200"
              >
                {historiaClinica.diagnostico_presuntivo}
              </p>
            </div>

            <div
              class="flex flex-col mt-4"
            >
              <label
                for="tratamientos_anteriores"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Tratamientos anteriores
              </label>
              <p
                class="text-neutral-800 dark:text-neutral-200"
              >
                {historiaClinica.tratamientos_anteriores}
              </p>
            </div>

            <div
              class="flex flex-col mt-4"
            >
              <label
                for="tratamiento_actual"
                class="text-sm font-semibold text-neutral-600 dark:text-neutral-300"
              >
                Tratamiento actual
              </label>
              <p
                class="text-neutral-800 dark:text-neutral-200"
              >
                {historiaClinica.tratamiento_actual}
              </p>
            </div>
          
            <!-- aqui estaran botones para. editar la historia clinica, agregar una nueva consulta ya que un paciente puede tener una o mas consultas -->
            <div
              class="flex justify-end mt-8"
            >
              <button
                class="bg-blue-500 hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded-lg"
              >
                Editar
              </button>
            
              <button
                class="bg-green-500 hover:bg-green-600 text-white font-semibold px-4 py-2 rounded-lg ml-4"
              >
                Nueva Consulta
              </button>
              
            </div>

          </div>
        </div>
      {/if}
    {/if}
  </div>
</div>
