
<script>
  import { onMount } from 'svelte';
  import HistoriesList from './components/HistoriesList.svelte';
  import { fetchHistories } from './api/histories';

  let histories = [];

  // Cargar datos de historias clínicas cuando el componente se monta
  onMount(async () => {
    histories = await fetchHistories();
  });
</script>

<main class="p-6">
  <h1 class="text-2xl font-bold mb-4">Historias Clínicas</h1>
  
  {#if histories.length > 0}
    <HistoriesList {histories} />
  {:else}
    <p>Cargando historias clínicas...</p>
  {/if}
</main>

<style>
  /* Estilos opcionales */
</style>
