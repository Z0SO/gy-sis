
<script>
  import Login from '../components/auth/Login.svelte';
</script>

<main class="flex flex-col min-h-screen bg-gradient-light dark:bg-gradient-dark justify-center items-center">
  <Login />
</main>

<style>
  /* Estilos globales para el tema claro */
  .bg-gradient-light {
    background: linear-gradient(to bottom, #f5f5f5, #ffffff);
  }

  /* Estilos para el tema oscuro */
  .bg-gradient-dark {
    background: linear-gradient(to bottom, #1a202c, #2d3748);
  }
</style>
