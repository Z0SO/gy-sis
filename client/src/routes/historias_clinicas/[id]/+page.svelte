
<script>
  // /roues/historias_clinicas/[id]/+page.svelte

  import { onMount } from 'svelte';
  import { getPacienteById } from '../../pacientes/api/pacientes.api.js';
  
  import { getHistorias } from '../api/historias.api.js';

  // para obtener parametros de la url
  import { page } from '$app/stores';


  let listaHistoriasClinicas = null;
  
  let historiaClinica = {};


  let un_paciente = null;

  let cargando = true;

  let error_page = null;

  onMount(async () => {

    // obtenemos el id de la historia clinica que viene en la url, por ejemplo: /historias_clinicas/1 -> id = 1
    const {id} = $page.params;

    try {

      listaHistoriasClinicas = await getHistorias();
      un_paciente = await getPacienteById(id);
      
      console.log('ID del paciente de la URL:', id);
      console.log('Lista de historias clínicas:', listaHistoriasClinicas);

      // se filtran las historias clinicas para obtener la que corresponde al paciente de la url que es la id del paciente que se selecciono
      historiaClinica = listaHistoriasClinicas.find(historia => historia.pac_id === un_paciente.pac_id);

    
      console.log('Historia Clínica del paciente:', historiaClinica);
    } catch (error) {
      error_page = error;
    } finally {
      cargando = false;
    }

    
  });

</script>


<br><br><br><br><br>

<!-- esto en definitiva sera un componente que se le pase toda la logica -->
<!-- los campos de Historia Clinica son: -->
<!--     paciente = models.OneToOneField(Paciente, related_name='historia_clinica', on_delete=models.CASCADE) -->


<!--     motivo_consulta = models.TextField() -->
<!--     derivado_por = models.CharField(max_length=50) -->
<!--     antecedentes_clinicos = models.TextField() -->
<!--     hc_laboratorio = models.TextField(blank=True, null=True) -->
<!--     diagnostico_presuntivo = models.TextField() -->
<!--     tratamientos_anteriores = models.TextField() -->
<!--     tratamiento_actual = models.TextField() -->
<!--     fecha_creacion = models.DateTimeField(auto_now_add=True) -->




{#if cargando}
  <p>Cargando...</p>
{:else}
  {#if error_page}
    <p>{error_page.message}</p>
  {:else}
    
    <ul>
      <li>Historia Clinica del paciente: {un_paciente.pac_nombre}</li>

      <li>Motivo de consulta: {historiaClinica.motivo_consulta}</li>
      <li>Derivado por: {historiaClinica.derivado_por}</li>
      <li>Antecedentes clínicos: {historiaClinica.antecedentes_clinicos}</li>
      <li>Historia Clínica de laboratorio: {historiaClinica.hc_laboratorio}</li>
      <li>Diagnóstico presuntivo: {historiaClinica.diagnostico_presuntivo}</li>
      <li>Tratamientos anteriores: {historiaClinica.tratamientos_anteriores}</li>
      <li>Tratamiento actual: {historiaClinica.tratamiento_actual}</li>
    </ul>
  {/if}
{/if}
