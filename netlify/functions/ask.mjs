// Netlify entry point, kept while the site moves to Vercel. The handler lives
// in api/ask.mjs, which Vercel serves at the same path.
export { handler as default } from '../../api/ask.mjs';

export const config = { path: '/api/ask' };
