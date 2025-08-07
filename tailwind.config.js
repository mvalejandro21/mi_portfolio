import defaultTheme from 'tailwindcss/defaultTheme';

export default {
  content: [
    "./index.html",
    "./src/**/*.{js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['Inter', ...defaultTheme.fontFamily.sans],
      },
      colors: {
        neutral: {
          light: '#f9f9f9',
          DEFAULT: '#f0f0f0',
          dark: '#d4d4d4',
        },
        primary: '#0a0a0a',
        accent: '#007aff', // azul tipo iOS
      },
    },
  },
  plugins: [],
}
