/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{js,jsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        sans: ['"Geist Variable"', 'system-ui', '-apple-system', 'Segoe UI', 'sans-serif'],
        mono: ['"Geist Mono Variable"', 'ui-monospace', 'SFMono-Regular', 'Menlo', 'monospace'],
        // same serif stack as the landing page and the promo film
        display: ['"Hoefler Text"', '"Iowan Old Style"', '"EB Garamond"', 'Palatino', 'Georgia', 'serif'],
      },
      // Astrolab brand (shared with landing + film): night-navy surfaces, warm ink text,
      // brass accent. Components use gray-*/blue-*/white, so remapping these scales
      // re-themes every tab at once; data-viz colours use explicit hex and stay as they are.
      colors: {
        black: '#080a12',
        white: '#f2eee4',
        gray: {
          50: '#f7f4ec',
          100: '#f2eee4',
          200: '#e2dccd',
          300: '#c9c2b2',
          400: '#a9a69c',
          500: '#7f8094',
          600: '#4a5068',
          700: '#2a3145',
          800: '#161c2c',
          900: '#0f1320',
          950: '#0b0e17',
        },
        blue: {
          200: '#f3e2b0',
          300: '#e8c66a',
          400: '#d9b04a',
          500: '#c49a2c',
          600: '#a8831f',
          700: '#8a6a12',
          800: '#5e480c',
          900: '#3a2c08',
          950: '#221a05',
        },
      },
    },
  },
  plugins: [],
}
