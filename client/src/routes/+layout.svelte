
<!-- src/routes/+layout.svelte -->
<script>
  import Navbar from '../components/layout/Navbar.svelte';
  import Footer from '../components/layout/Footer.svelte';
</script>

<main class="flex flex-col min-h-screen">
  <Navbar />
  
  <!-- El contenido de las páginas hijas -->
  <div class="flex-grow">
    <slot></slot> <!-- Aquí se renderizan las páginas hijas -->
  </div>

  <Footer />
</main>

<style>
  @tailwind base;
  @tailwind components;
  @tailwind utilities;

  :global(body) {
    font-family: 'Roboto', sans-serif;
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  main {
    min-height: 100vh; /* Asegura que el footer siempre esté al final */
  }

  /* Estilos para Navbar y Footer si es necesario pueden ir aquí */
</style>
