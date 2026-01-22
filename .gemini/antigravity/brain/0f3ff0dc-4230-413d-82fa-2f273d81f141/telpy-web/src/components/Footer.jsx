const Footer = () => {
    return (
        <footer className="border-t border-white/10 py-12 bg-bg-secondary">
            <div className="container mx-auto px-6 flex flex-col md:flex-row justify-between items-center gap-6">
                <div className="text-xl font-bold flex items-center gap-2">
                    <span className="text-accent">Tel</span><span className="text-secondary">Py</span>
                </div>

                <div className="text-text-secondary text-sm">
                    &copy; 2026 TelPy Project. Open Source under MIT.
                </div>

                <div className="flex gap-6">
                    <a href="#" className="text-text-secondary hover:text-accent transition-colors">GitHub</a>
                    <a href="#" className="text-text-secondary hover:text-accent transition-colors">Twitter</a>
                    <a href="#" className="text-text-secondary hover:text-accent transition-colors">Discord</a>
                </div>
            </div>
        </footer>
    )
}

export default Footer
