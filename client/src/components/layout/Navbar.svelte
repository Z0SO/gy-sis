
<script>
  import { goto } from '$app/navigation';

  const is_login = true;
  const ruta_historia_clinica = '/historias_clinicas';
  const ruta_crear_historia_clinica = '/historias_clinicas/create';
  const ruta_nuevo_paciente = '/pacientes/create';


  const ruta_logout = '/';

</script>

<nav class="fixed top-0 left-0 w-full flex items-center justify-between bg-zinc-50 dark:bg-neutral-700 py-2 px-4 shadow-md z-50">
  <div class="flex justify-between w-full lg:items-center">
    <!-- Logo / Home -->
    <a href="/" class="text-xl font-bold text-black dark:text-white">Home</a>

    <!-- Mobile menu button -->
    <button class="lg:hidden text-black dark:text-white" aria-label="Toggle Menu">
      <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="currentColor" class="w-6 h-6">
        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16m-7 6h7" />
      </svg>
    </button>

    <!-- Links -->
    <ul class="hidden lg:flex space-x-4">
      <li><a href={ruta_historia_clinica} class="text-black dark:text-white hover:text-gray-700 dark:hover:text-gray-300">Historias Clínicas</a></li>
      {#if is_login}
        <li><a href={ruta_crear_historia_clinica} class="text-black dark:text-white hover:text-gray-700 dark:hover:text-gray-300">Crear Historia Clínica</a></li>
        <!-- para añadir nuevo paciente -->
        <li><a href={ruta_nuevo_paciente} class="text-black dark:text-white hover:text-gray-700 dark:hover:text-gray-300">Nuevo Paciente</a></li>
        <li><a href={ruta_logout} class="text-black dark:text-white hover:text-gray-700 dark:hover:text-gray-300">Cerrar Sesión</a></li>
      {/if}
    </ul>
  </div>
</nav>

