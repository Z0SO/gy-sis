
<script>
  import { onMount } from 'svelte';

  import { getHistorias } from '../api/historias.api.js';


  import HistoriaItem from './HistoriaItem.svelte';
  
  // generamos la lista de todas las historias clinicas
  let LTHC = [];


  onMount( async () => {
    LTHC = await getHistorias();
  });


</script>


{#each LTHC as una_historia}

<a href="/historias_clinicas/{una_historia.paciente}" >
    <HistoriaItem {una_historia} />
  </a>
{/each}

