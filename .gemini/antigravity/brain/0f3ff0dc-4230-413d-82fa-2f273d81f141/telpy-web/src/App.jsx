import { useState } from 'react'
import Navbar from './components/Navbar'
import Hero from './components/Hero'
import Features from './components/Features'
import CodeComparison from './components/CodeComparison'
import Footer from './components/Footer'
import './index.css'

function App() {
  return (
    <div className="min-h-screen bg-bg-primary">
      <div className="fixed inset-0 z-0 opacity-20 pointer-events-none" 
           style={{
             backgroundImage: 'radial-gradient(circle at 10% 20%, rgba(245, 158, 11, 0.15) 0%, transparent 40%), radial-gradient(circle at 90% 80%, rgba(6, 182, 212, 0.15) 0%, transparent 40%)'
           }}>
      </div>
      
      <div className="relative z-10">
        <Navbar />
        <main>
          <Hero />
          <Features />
          <CodeComparison />
        </main>
        <Footer />
      </div>
    </div>
  )
}

export default App
