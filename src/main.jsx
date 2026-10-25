import React, { Suspense, lazy } from 'react'
import ReactDOM from 'react-dom/client'
import { BrowserRouter, Routes, Route, Navigate, Link } from 'react-router-dom'
import './index.css'

const LabApp = lazy(() => import('./lab/LabApp'))

function NavBar() {
  return (
    <nav className="bg-black border-b border-gray-700 px-4 h-14 flex items-center">
      <div className="max-w-[1920px] w-full mx-auto flex items-center justify-between">
        <Link to="/lab?tab=map" className="flex items-center gap-2 text-white font-semibold tracking-tight">
          <span className="text-lg leading-none">✦</span> GitHub Stars
        </Link>
        <a href="/" className="text-sm text-gray-400 hover:text-white transition-colors">About</a>
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
          <Suspense fallback={<div className="min-h-screen bg-black text-gray-400 flex items-center justify-center">Loading…</div>}>
            <LabApp />
          </Suspense>
        } />
      </Routes>
    </BrowserRouter>
  </React.StrictMode>,
)
