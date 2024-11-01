
/** @type {import('tailwindcss').Config} */
export default {
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
};

