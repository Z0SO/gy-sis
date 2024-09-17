<script>
  // este componente es llamado por tablaPacientes.svelte y le pasamos {pacienteItem=paciente}

  // debemos exportar la variable pacienteItem para que el componente ItemPaciente.svelte pueda acceder a ella

  export let paciente= {};


</script>

<tr class="odd:bg-white odd:dark:bg-gray-900 even:bg-gray-50 even:dark:bg-gray-800 border-b dark:border-gray-700 hover:bg-gray-100 hover:dark:bg-gray-700" 
>
  <th  scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white dark:bg-gray-800"
  >{paciente.pac_nombre}</th>
  <td class="border px-6 py-4">{paciente.pac_dni}</td>
  <td class="border px-6 py-4">{paciente.pac_edad}</td>
  <td class="border px-6 py-4">{paciente.pac_domicilio}</td>
  <td class="border px-6 py-4">{paciente.pac_obrasocial}</td>
  <td class="border px-6 py-4">{paciente.pac_telefono}</td>
  <td class="border px-6 py-4">{paciente.pac_telefono_emergencia}</td>
  <td class="border px-6 py-4">{paciente.pac_ocupacion}</td>
  <td class="border px-6 py-4">{paciente.pac_estadocivil}</td>

</tr>
