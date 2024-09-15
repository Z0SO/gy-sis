/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{html,js,svelte}",
    "./node_modules/@sveltejs/**/*.svelte"
  ],

  theme: {
    extend: {
      colors: {
        primary: '#3490dc', // Cambia este valor al color que desees
      },
    },
  },


  plugins: [],
}
