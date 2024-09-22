
<script>



</script>


<!-- Componente dedicado a la creación de una historia clínica. Este componente se encarga de recoger los datos de un formulario y enviarlos a la API para que se cree una historia clínica en la base de datos. -->
<div class="container mx-auto px-6 md:px-8 mt-40 bg-white dark:bg-neutral-800 p-8">
  <div class="max-w-4xl mx-auto">
    <h1 class="text-2xl font-bold text-black dark:text-white">Crear Historia Clínica</h1>
    <form class="mt-6" on:submit|preventDefault={handleSubmit}>
      <div class="grid grid-cols-1 gap-6">
        <div>
          <label for="nombre" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Nombre</label>
          <input type="text" id="nombre" name="nombre" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="apellido" class="block text-sm font-medium text-gray-700 dark:text-gray-200">Apellido</label>
          <input type="text" id="apellido" name="apellido" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="dni"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">DNI</label>
          <input type="text" id="dni" name="dni" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="fecha_nacimiento"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Fecha de Nacimiento</label>
          <input type="date" id="fecha_nacimiento" name="fecha_nacimiento" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="telefono"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Teléfono</label>
          <input type="text" id="telefono" name="telefono" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="email"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Email</label>
          <input type="email" id="email" name="email" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="direccion"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Dirección</label>
          <input type="text" id="direccion" name="direccion" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="localidad"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Localidad</label>
          <input type="text" id="localidad" name="localidad" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="provincia"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Provincia</label>
          <input type="text" id="provincia" name="provincia" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>
        <div>
          <label for="codigo_postal"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Código Postal</label>
          <input type="text" id="codigo_postal" name="codigo_postal" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm" />
        </div>

        <div>
          <label for="antecedentes"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Antecedentes</label>
          <textarea id="antecedentes" name="antecedentes" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="alergias"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Alergias</label>
          <textarea id="alergias" name="alergias" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="medicamentos"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Medicamentos</label>
          <textarea id="medicamentos" name="medicamentos" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
        <div>
          <label for="observaciones"
            class="block text-sm font-medium text-gray-700 dark:text-gray-200">Observaciones</label>
          <textarea id="observaciones" name="observaciones" class="mt-1 block w-full px-3 py-2 border border-gray-300 dark:border-neutral-700 rounded-md shadow-sm focus:outline-none focus:ring-zinc-300 dark:focus:ring-zinc-500 focus:border-zinc-300 dark:focus:border-zinc-500 sm:text-sm"></textarea>
        </div>
      </div>
      <div class="mt-6">
        <button type="submit" class="w-full py-2 px-4 border border-transparent rounded-md shadow-sm text-sm font-medium text-white bg-zinc-500 hover:bg-zinc-600 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-zinc-500 dark:focus:ring-zinc-500 dark:focus:ring-offset-zinc-800">Crear Historia Clínica</button>      </div>
    </form>
  </div>
</div>


