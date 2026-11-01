import React, { Suspense, lazy } from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom'
import './index.css'

const LabApp = lazy(() => import('./lab/LabApp'))

function NavBar() {
  return (
    <nav className="bg-black/80 backdrop-blur border-b border-gray-700 px-4 h-14 flex items-center sticky top-0 z-40">
      <div className="max-w-[1920px] w-full mx-auto flex items-center justify-between">
        <Link to="/lab?tab=map" className="flex items-baseline gap-2 text-white">
          <span className="text-blue-300 text-lg leading-none">✦</span>
          <span className="font-mono text-[11px] tracking-[0.3em] uppercase text-blue-400">GitHub</span>
          <span className="font-display text-xl leading-none">Astrolab</span>
        </Link>
        <a href="/" className="text-sm text-gray-400 hover:text-white transition-colors">About</a>
      </div>
    </nav>
  )
}

function Footer() {
  return (
    <footer className="border-t border-gray-700 px-4 py-6 mt-10">
      <div className="max-w-[1920px] mx-auto flex flex-wrap items-baseline justify-between gap-3 text-sm">
        <span className="font-display italic text-blue-300">Don't rebuild. Build on the stars.</span>
        <span className="text-gray-400">
          Made by <span className="font-display text-white text-base">Kaiser Data &amp; AI</span>
          <span className="text-gray-600"> · </span>
          <a href="https://github.com/kaiser-data" target="_blank" rel="noreferrer"
             className="font-mono text-blue-400 hover:text-blue-300">github.com/kaiser-data</a>
        </span>
      </div>
    </footer>
  )
}

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <BrowserRouter>
      <NavBar />
      <Routes>
        <Route path="/" element={<Navigate to="/lab?tab=map" replace />} />
        <Route path="/lab/*" element={
          <Suspense fallback={<div className="min-h-screen bg-black text-gray-400 flex items-center justify-center">Loading…</div>}>
            <LabApp />
          </Suspense>
        } />
      </Routes>
      <Footer />
    </BrowserRouter>
  </React.StrictMode>,
)
