/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        primary: "#853BCE",
        gray: "#827D7D",
        secondary: "#181622",
      },
      backgroundColor: {
        primary: "#853BCE",
        secondary: "#181622",
        main: "#13111C"
      }
    },
  },
  plugins: [],
}
