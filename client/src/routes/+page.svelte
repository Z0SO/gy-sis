
<script>
  import Login from '../components/auth/Login.svelte';
</script>

<main 
  class="flex flex-col bg-gradient-to-b from-zinc-300 to-white justify-center items-center"
>


  <Login />



</main>

<style>
  /* Estilos globales */
  main {
    min-height: 100vh; /* Asegura que el footer quede al final */
  }
  .input-field {
    width: 100%;
    padding: 0.5rem;
    border: 1px solid #ccc;
    border-radius: 0.375rem;
  }



</style>
