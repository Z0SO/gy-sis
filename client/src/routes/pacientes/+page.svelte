<script>
  // esta sera la vista donde se mostraran todos los pacientes actuales

  import { onMount } from 'svelte';

  // traemos todas las funciones que escribimos en ./api/pacientes.api.js
  import { getPacientes } from './api/pacientes.api.js';

  // creamos una variable para guardar los pacientes
  let listaTodosPacientes = [];

  // creamos una funcion para traer los pacientes
  async function obtenerPacientes() {
    
    const pacientes = await getPacientes();
    listaTodosPacientes = pacientes;
 
  }

  // llamamos a la funcion obtenerPacientes() cuando la pagina se monte
  onMount(() => {
    obtenerPacientes();
  });

</script>

<h1 class="text-center mt-20"
  >Lista de pacientes</h1>

{#if listaTodosPacientes.length > 0}
  <ul>
    {#each listaTodosPacientes as paciente}
      <li>{paciente.pac_nombre} con DNI -> {paciente.pac_dni}</li>
    {/each}
  </ul>
{:else}
  <p>No hay pacientes</p>
{/if}

