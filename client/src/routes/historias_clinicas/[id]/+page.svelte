
<script>
  // /roues/historias_clinicas/[id]/+page.svelte

  import { onMount } from 'svelte';

  // importamos la funcion getHistoriaById que se encarga de traer una historia clinica por su id
  //import { getHistoriaById } from '../api/historias.api.js';

  import { getPacienteById } from '../../pacientes/api/pacientes.api.js';
  // para obtener parametros de la url
  import {page} from '$app/stores';


  let historiaClinica = null;

  let paciente = null;

  let cargando = true;

  let error_page = null;

  onMount(async () => {

    // obtenemos el id de la historia clinica que viene en la url, por ejemplo: /historias_clinicas/1 -> id = 1
    const {id} = $page.params;

    try {
      paciente = await getPacienteById(id);
    } catch (error) {
      error_page = error;
    } finally {
      cargando = false;
    }

    
  });

</script>

<br><br><br><br><br>
{#if cargando}
  <p>Cargando...</p>
{:else}
  {#if error_page}
    <p>{error_page.message}</p>
  {:else}
    
    <ul>
      <li>Nombre: {paciente.pac_nombre}</li>

    </ul>
  {/if}
{/if}

