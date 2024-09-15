
<script>
  import { onMount } from 'svelte';

  import { getHistorias } from './api/historias.api';

  let products = [];
  let searchTerm = '';
  let filterOption = '1';

  onMount(async () => {
    historias = await getHistorias();
  });


  // FILTROS
  //<!-- funcion para filtrar historias clinicas por nombre -->

  function filteredProducts() {
    return products.filter(product => {
      if (searchTerm.length === 0) {
        return true;
      }

      return product.name.toLowerCase().includes(searchTerm.toLowerCase());
    });
  }



</script>


<!-- posiblemente aca quiero traer un header que pueda hacer cosas -->


<!-- Contenedor centrado -->
<div class="flex justify-center py-6 md:py-20 bg-neutral-100 dark:bg-neutral-900
  ">
  <!-- Contenedor de la tabla con bordes redondeados, sombra y soporte para tema oscuro/claro -->
  <div class="w-full max-w-5xl bg-white dark:bg-neutral-800 rounded-lg shadow-lg p-6">
    
    <!-- Controles de búsqueda y filtro -->
    <div class="flex justify-between mb-4">
      
      <!-- Input de búsqueda -->
      <div class="relative">
        <label for="inputSearch" class="sr-only">Search</label>
        <input 
          id="inputSearch" 
          type="text" 
          placeholder="Search..." 
          class="block w-64 rounded-lg border dark:border-none dark:bg-neutral-600 py-2 pl-10 pr-4 text-sm focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-400" 
          bind:value={searchTerm}
        />
        <span class="pointer-events-none absolute left-3 top-1/2 -translate-y-1/2 transform">
          <!-- Icono de búsqueda -->
          <svg xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke-width="1.5" stroke="currentColor" class="h-4 w-4 text-neutral-500 dark:text-neutral-200">
            <path stroke-linecap="round" stroke-linejoin="round" d="M21 21l-5.197-5.197m0 0A7.5 7.5 0 105.196 5.196a7.5 7.5 0 0010.607 10.607z" />
          </svg>
        </span>
      </div>

      <!-- Filtro -->
      <div class="relative hidden sm:block">
        <label for="inputFilter" class="sr-only">Filter</label>
        <select 
          id="inputFilter" 
          class="block w-40 rounded-lg border dark:border-none dark:bg-neutral-600 p-2 text-sm focus:border-blue-400 focus:outline-none focus:ring-1 focus:ring-blue-400" 
          bind:value={filterOption}
        >
          <option value="1" selected>Last week</option>
          <option value="2">Last month</option>
          <option value="3">Yesterday</option>
          <option value="4">Last 7 days</option>
          <option value="5">Last 30 days</option>
        </select>
      </div>
    </div>

    <!-- Tabla -->
    <table class="min-w-full text-left text-sm whitespace-nowrap">
      
      <!-- Encabezado de la tabla -->
      <thead class="uppercase tracking-wider border-b-2 dark:border-neutral-600 bg-neutral-50 dark:bg-neutral-800">
        <tr>
          <th scope="col" class="px-6 py-4">
            Product
            <!-- Icono de ordenación -->
            <a href="" class="inline">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="w-[0.75rem] h-[0.75rem] inline ml-1 text-neutral-500 dark:text-neutral-200 mb-[1px]" fill="currentColor">
                <path d="M137.4 41.4c12.5-12.5 32.8-12.5 45.3 0l128 128c9.2 9.2 11.9 22.9 6.9 34.9s-16.6 19.8-29.6 19.8H32c-12.9 0-24.6-7.8-29.6-19.8s-2.2-25.7 6.9-34.9l128-128zm0 429.3l-128-128c-9.2-9.2-11.9-22.9-6.9-34.9s16.6-19.8 29.6-19.8H288c12.9 0 24.6 7.8 29.6 19.8s2.2 25.7-6.9 34.9l-128 128c-12.5 12.5-32.8 12.5-45.3 0z" />
              </svg>
            </a>
          </th>
          <th scope="col" class="px-6 py-4">
            Price
            <!-- Icono de ordenación -->
            <a href="" class="inline">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="w-[0.75rem] h-[0.75rem] inline ml-1 text-neutral-500 dark:text-neutral-200 mb-[1px]" fill="currentColor">
                <path d="M137.4 41.4c12.5-12.5 32.8-12.5 45.3 0l128 128c9.2 9.2 11.9 22.9 6.9 34.9s-16.6 19.8-29.6 19.8H32c-12.9 0-24.6-7.8-29.6-19.8s-2.2-25.7 6.9-34.9l128-128zm0 429.3l-128-128c-9.2-9.2-11.9-22.9-6.9-34.9s16.6-19.8 29.6-19.8H288c12.9 0 24.6 7.8 29.6 19.8s2.2 25.7-6.9 34.9l-128 128c-12.5 12.5-32.8 12.5-45.3 0z" />
              </svg>
            </a>
          </th>
          <th scope="col" class="px-6 py-4">
            Stock
            <!-- Icono de ordenación -->
            <a href="" class="inline">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="w-[0.75rem] h-[0.75rem] inline ml-1 text-neutral-500 dark:text-neutral-200 mb-[1px]" fill="currentColor">
                <path d="M137.4 41.4c12.5-12.5 32.8-12.5 45.3 0l128 128c9.2 9.2 11.9 22.9 6.9 34.9s-16.6 19.8-29.6 19.8H32c-12.9 0-24.6-7.8-29.6-19.8s-2.2-25.7 6.9-34.9l128-128zm0 429.3l-128-128c-9.2-9.2-11.9-22.9-6.9-34.9s16.6-19.8 29.6-19.8H288c12.9 0 24.6 7.8 29.6 19.8s2.2 25.7-6.9 34.9l-128 128c-12.5 12.5-32.8 12.5-45.3 0z" />
              </svg>
            </a>
          </th>
          <th scope="col" class="px-6 py-4">
            Status
            <!-- Icono de ordenación -->
            <a href="" class="inline">
              <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 320 512" class="w-[0.75rem] h-[0.75rem] inline ml-1 text-neutral-500 dark:text-neutral-200 mb-[1px]" fill="currentColor">
                <path d="M137.4 41.4c12.5-12.5 32.8-12.5 45.3 0l128 128c9.2 9.2 11.9 22.9 6.9 34.9s-16.6 19.8-29.6 19.8H32c-12.9 0-24.6-7.8-29.6-19.8s-2.2-25.7 6.9-34.9l128-128zm0 429.3l-128-128c-9.2-9.2-11.9-22.9-6.9-34.9s16.6-19.8 29.6-19.8H288c12.9 0 24.6 7.8 29.6 19.8s2.2 25.7-6.9 34.9l-128 128c-12.5 12.5-32.8 12.5-45.3 0z" />
              </svg>
            </a>
          </th>
        </tr>
      </thead>

      <!-- Cuerpo de la tabla -->
      <tbody class="divide-y divide-neutral-200 dark:divide-neutral-600">
        {#each filteredProducts() as product}
          <tr>
            <td class="px-6 py-4">{product.name}</td>
            <td class="px-6 py-4">${product.price.toFixed(2)}</td>
            <td class="px-6 py-4">{product.stock}</td>
            <td class="px-6 py-4">{product.status}</td>
          </tr>
        {/each}
      </tbody>
    </table>
  </div>
</div>
