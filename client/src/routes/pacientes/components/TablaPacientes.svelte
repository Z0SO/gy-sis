
<script>

  // este componente lo llamara +page.svelte y cuando lo llama le pasa {listaTodosPacientes}
  import ItemPacientes from './ItemPacientes.svelte';

  // exportamos la variable pacientes para que el componente ItemPacientes.svelte pueda acceder a ella
  export let listaTodosPacientes = [];
 

  // creamos una funcion para buscar un paciente por su dni
  async function buscarPaciente(dni) {
    const res = await fetch(`http://localhost:3000/api/pacientes/${dni}`);
    const paciente = await res.json();
    return paciente;
  }

  // creamos una funcion para ordenar los pacientes por su dni
  function ordenarPacientesPorDni() {
    listaTodosPacientes.sort((a, b) => a.pac_dni - b.pac_dni);
  }

  


</script>

  <!-- TABLA -->
  <!-- esta va a armar la estructura de la tabla de pacientes. asi que vamos a llamar a un componente que se encargue de traer un item de la tabla de pacientes -->

  <!-- ademas de la tabla de pacientes, vamos a agregar un boton para ordenar los pacientes por su dni y un input para buscar un paciente por su dni -->
 

<!--    <input type="text" class="border border-gray-200 p-2 rounded-lg" placeholder="Buscar paciente por DNI" /> -->
<!--     <button class="bg-blue-500 text-white p-2 rounded-lg mt-2">Buscar</button> -->
<!--     <button class="bg-blue-500 text-white p-2 rounded-lg mt-2">Ordenar por DNI</button> -->

    <table class="w-full text-sm text-left rtl:text-right text-gray-500 dark:text-gray-400">
    
      <thead class="text-xs text-gray-700 uppercase bg-gray-50 dark:bg-gray-700 dark:text-gray-400">
        <tr>
          <th scope="col" class="px-6 py-3">Nombre</th>
          <th scope="col" class="px-6 py-3">DNI</th>
          <th scope="col" class="px-6 py-3">Edad</th>
          <th scope="col" class="px-6 py-3">Domicilio</th>
          <th scope="col" class="px-6 py-3">Obra social</th>
          <th scope="col" class="px-6 py-3">Telefono</th>
          <th scope="col" class="px-6 py-3">Telefono de emergencia</th>
          <th scope="col" class="px-6 py-3">Ocupacion</th>
          <th scope="col" class="px-6 py-3">Estado civil</th>
        </tr>
      </thead>
      <tbody>
        {#each listaTodosPacientes as paciente}
          <ItemPacientes {paciente} />
        {/each}
      </tbody>
    </table>
  

