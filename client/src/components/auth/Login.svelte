
<script>
  import { goto } from '$app/navigation';
  let username = '';
  let password = '';
  let isUsernameActive = false;
  let isPasswordActive = false;

  // TEMPORAL - Para navegar a la página de pacientes al hacer login solamente redirigimos
  const handleLogin = () => {
    // Aquí puedes agregar la lógica para el login
    console.log("Logging in with:", { username, password });
    goto('/pacientes');
  };
</script>

<section class="gradient-form h-full bg-transparent dark:bg-transparent dark:text-neutral-200"
>
  <div class="container h-full p-10 mx-auto"
  >
    <div class="flex h-full flex-wrap items-center justify-center text-neutral-800 dark:text-neutral-200 shadow-lg"
    >
      <div class="w-full">
        <div class="block rounded-lg bg-white dark:bg-neutral-800 sombreado"
        >
          <div class="g-0 lg:flex lg:flex-wrap">
            <!-- Columna izquierda (formulario de login) -->
            <div class="px-4 md:px-0 lg:w-6/12">
              <div class="md:mx-6 md:p-12">
                <!-- Logo -->
                <div class="text-center">
                  <img class="mx-auto w-48" src="https://tecdn.b-cdn.net/img/Photos/new-templates/bootstrap-login-form/lotus.webp" alt="logo" />
                  <h4 class="mb-12 mt-1 pb-1 text-xl font-semibold">GY-SIS</h4>
                </div>

                <form>
                  <p class="mb-4">Ingrese su cuenta</p>

                  <!-- Input de Username -->
                  <div class="relative mb-4">
                    <input
                      bind:value={username}
                      type="text"
                      class="peer block w-full rounded border-0 bg-transparent px-3 py-2 leading-[1.6] outline-none transition-all duration-200 ease-linear dark:text-white dark:placeholder:text-neutral-300"
                      placeholder=""
                      on:focus={() => isUsernameActive = true}
                      on:blur={() => isUsernameActive = username.length > 0}
                    />
                    <label
                      class="absolute left-3 top-2 transition-all duration-200 ease-out text-neutral-500 dark:text-neutral-400 pointer-events-none transform {isUsernameActive || username.length ? '-translate-y-5 scale-75' : ''}"
                    >
                      Username
                    </label>
                  </div>

                  <!-- Input de Password -->
                  <div class="relative mb-4">
                    <input
                      bind:value={password}
                      type="password"
                      class="peer block w-full rounded border-0 bg-transparent px-3 py-2 leading-[1.6] outline-none transition-all duration-200 ease-linear dark:text-white dark:placeholder:text-neutral-300"
                      placeholder=""
                      on:focus={() => isPasswordActive = true}
                      on:blur={() => isPasswordActive = password.length > 0}
                    />
                    <label
                      class="absolute left-3 top-2 transition-all duration-200 ease-out text-neutral-500 dark:text-neutral-400 pointer-events-none transform {isPasswordActive || password.length ? '-translate-y-5 scale-75' : ''}"
                    >
                      Password
                    </label>
                  </div>

                  <!-- Botón de Login -->
                  <div class="mb-12 pb-1 pt-1 text-center">
                    <button
                      on:click|preventDefault={handleLogin}
                      class="mb-3 inline-block w-full rounded px-6 pb-2 pt-2.5 text-xs font-medium uppercase leading-normal text-white shadow-lg transition duration-150 ease-in-out"
                      style="background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593)"
                    >
                      Log in
                    </button>


                    <!-- por si se olvida la contraseña -->
                    <!-- <a href="#!" class="text-sm text-blue-600">Forgot password?</a> -->



                  </div>


                  <!-- <!-1- Botón de Registro -1-> -->
                  <!-- <div class="flex items-center justify-between pb-6"> -->
                  <!--   <p class="mb-0">Don't have an account?</p> -->
                  <!--   <button -->
                  <!--     class="inline-block rounded border-2 border-red-500 px-6 py-2 text-xs font-medium text-red-500 transition duration-150 ease-in-out hover:bg-red-50 hover:text-red-600 dark:hover:bg-red-800" -->
                  <!--   > -->
                  <!--     Register -->
                  <!--   </button> -->
                  <!-- </div> -->
                </form>
              </div>
            </div>

            <!-- Columna derecha (descripción) -->
            <div
              class="flex items-center rounded-b-lg lg:w-6/12 lg:rounded-e-lg lg:rounded-bl-none"
              style="background: linear-gradient(to right, #ee7724, #d8363a, #dd3675, #b44593)"
            >
              <div class="px-4 py-6 text-white md:mx-6 md:p-12">
                <h4 class="mb-6 text-xl font-semibold">Hola de nuevo !</h4>
                <p class="text-sm">
                  Ingrese sus datos para acceder a la plataforma de GY-SIS.
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</section>

<style>
  .peer:focus ~ label,
  .peer:not(:placeholder-shown) ~ label {
    @apply -translate-y-5 scale-75 text-primary;
  }

  .sombreado {
    box-shadow: 0 10px 20px 4px gray;
  }
</style>
