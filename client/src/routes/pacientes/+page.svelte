<script>
  // esta sera la vista donde se mostraran todos los pacientes actuales

  import { onMount } from 'svelte';

  // traemos todas las funciones que escribimos en ./api/pacientes.api.js
  import { getPacientes } from './api/pacientes.api.js';

  import TablaPacientes from './components/TablaPacientes.svelte';

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

<h1 class="text-center mt-40 text-3xl font-bold text-gray-800 "
  >Lista de pacientes</h1>

<!-- CONTENEDOR -->
<div
  class="container flex justify-center mt-10 mb-10 rounded-lg shadow-lg  mx-auto bg-white dark:bg-gray-800 dark:text-white"
>

    <!-- llamamos a un componente para que traiga la tabla de pacientes -->
    <!-- recordar que lo qeu se debe exportar en el componente es el nombre del componente y no el archivo .svelte -->
    <div class="relative overflow-x-auto shadow-md sm:rounded-lg w-full"
    > 
      <TablaPacientes {listaTodosPacientes} />
    </div>


</div>
