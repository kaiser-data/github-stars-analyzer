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
      },
      // Vercel-style neutral scale: no blue tint, near-black surfaces
      colors: {
        gray: {
          50: '#fafafa',
          100: '#ededed',
          200: '#e0e0e0',
          300: '#c7c7c7',
          400: '#a1a1a1',
          500: '#7d7d7d',
          600: '#454545',
          700: '#2e2e2e',
          800: '#1a1a1a',
          900: '#0a0a0a',
          950: '#050505',
        },
        blue: {
          200: '#c2dcff',
          300: '#8ec5ff',
          400: '#52a8ff',
          500: '#3291ff',
          600: '#0070f3',
          700: '#0761d1',
          800: '#0a4a9e',
          900: '#0a2a4d',
          950: '#06172b',
        },
      },
    },
  },
  plugins: [],
}
