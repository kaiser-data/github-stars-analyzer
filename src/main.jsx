import React, { Suspense, lazy } from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Link, useLocation } from 'react-router-dom'
import GitHubStarsAnalyzer from './GitHubStarsAnalyzer'
import './index.css'

// Lazy-load the lab — Three.js + force-graph-3d is ~1.3 MB. Don't pay
// the cost on /, only when the user actually visits /lab.
const LabApp = lazy(() => import('./lab/LabApp'))

function NavBar() {
  const { pathname } = useLocation()
  const linkClass = (path) =>
    `px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
      pathname === path
        ? 'bg-blue-600 text-white'
        : 'text-gray-300 hover:bg-gray-700 hover:text-white'
    }`
  return (
    <nav className="bg-gray-900 border-b border-gray-700 px-6 py-3">
      <div className="max-w-[1920px] mx-auto flex items-center gap-2">
        <span className="text-white font-bold mr-4">GitHub Stars</span>
        <Link to="/" className={linkClass('/')}>Live</Link>
        <Link to="/lab" className={linkClass('/lab')}>Lab — Graph</Link>
      </div>
    </nav>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<GitHubStarsAnalyzer />} />
        <Route path="/lab/*" element={
          <Suspense fallback={<div className="min-h-screen bg-gray-900 text-gray-400 flex items-center justify-center">Loading lab…</div>}>
            <LabApp />
          </Suspense>
        } />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
