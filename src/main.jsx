import React, { Suspense, lazy } from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Navigate, Link, useLocation } from 'react-router-dom'
import './index.css'

const LabApp = lazy(() => import('./lab/LabApp'))

function NavBar() {
  const { pathname } = useLocation()
  const linkClass = (path) =>
    `px-4 py-2 rounded-lg text-sm font-medium transition-colors ${
      pathname.startsWith(path)
        ? 'bg-blue-600 text-white'
        : 'text-gray-300 hover:bg-gray-700 hover:text-white'
    }`
  return (
    <nav className="bg-gray-900 border-b border-gray-700 px-6 py-3">
      <div className="max-w-[1920px] mx-auto flex items-center gap-2">
        <span className="text-white font-bold mr-4">GitHub Stars</span>
        <Link to="/lab?tab=map" className={linkClass('/lab')}>Map</Link>
        <Link to="/lab?tab=topics" className={linkClass('/lab?tab=topics')}>Topics</Link>
        <Link to="/lab?tab=insights" className={linkClass('/lab?tab=insights')}>Insights</Link>
        <Link to="/lab?tab=all" className={linkClass('/lab?tab=all')}>Browse</Link>
        <Link to="/lab?tab=compare" className={linkClass('/lab?tab=compare')}>Compare</Link>
      </div>
    </nav>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Navigate to="/lab?tab=map" replace />} />
        <Route path="/lab/*" element={
          <Suspense fallback={<div className="min-h-screen bg-gray-900 text-gray-400 flex items-center justify-center">Loading…</div>}>
            <LabApp />
          </Suspense>
        } />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
