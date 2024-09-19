
<script>
  
  // aca vamos a pedir todas las historias clinicas
  
  import { onMount } from 'svelte';

  import { getHistorias } from './api/historias.api';


  // esta es la variable que va a contener todas las historias clinicas
  let LTHC = [];
  
  onMount(async () => {
    LTHC = await getHistorias();
  });

</script>


<br><br><br><br><br>

<!-- hagamos un buen contenedor bien estilizado -->
<!-- el div debe ser bien estilizado con tailwind, de manera profesional -->
<!-- el estilo de cada etiqueta debe ser congruente con toda la pagina y debe mostrarse muy lindo y profesional -->
<div
  class="grid grid-cols-1 gap-4 md:grid-cols-2 lg:grid-cols-3"
>
  <!-- lo mismo para todos los divs, h2 y p -->
  {#each LTHC as una_historia}
    <div
      class="bg-white shadow-lg rounded-lg p-4"
    >
      <h2 
        class="text-xl font-semibold"
      >{una_historia.paciente}</h2>
      <p 
        class="text-gray-600"
      >{una_historia.diagnostico_presuntivo}</p>
    </div>
  {/each}

</div>

