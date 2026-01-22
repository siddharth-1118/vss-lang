import { useState, useEffect } from 'react'

const Navbar = () => {
    const [scrolled, setScrolled] = useState(false)

    useEffect(() => {
        const handleScroll = () => {
            setScrolled(window.scrollY > 50)
        }
        window.addEventListener('scroll', handleScroll)
        return () => window.removeEventListener('scroll', handleScroll)
    }, [])

    return (
        <nav className={`fixed top-0 left-0 right-0 z-50 transition-all duration-300 ${scrolled ? 'bg-bg-primary/80 backdrop-blur-md border-b border-white/5' : 'bg-transparent'}`}>
            <div className="container mx-auto px-6 h-20 flex items-center justify-between">
                <a href="#" className="text-2xl font-bold flex items-center gap-2">
                    <span className="text-accent">Tel</span><span className="text-secondary">Py</span>
                </a>

                <div className="hidden md:flex items-center gap-8">
                    <a href="#features" className="text-text-secondary hover:text-white transition-colors">Features</a>
                    <a href="#docs" className="text-text-secondary hover:text-white transition-colors">Documentation</a>
                    <a href="#playground" className="text-text-secondary hover:text-white transition-colors">Playground</a>
                    <a href="https://github.com/telpy" target="_blank" rel="noreferrer" className="btn btn-primary text-sm px-6 py-2">
                        GitHub
                    </a>
                </div>
            </div>
        </nav>
    )
}

export default Navbar
