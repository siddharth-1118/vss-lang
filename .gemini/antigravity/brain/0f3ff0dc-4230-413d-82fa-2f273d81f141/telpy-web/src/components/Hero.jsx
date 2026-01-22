const Hero = () => {
    return (
        <section className="relative pt-32 pb-20 overflow-hidden">
            <div className="container mx-auto px-6 grid lg:grid-cols-2 gap-12 items-center">
                <div className="z-10">
                    <div className="inline-block px-4 py-2 rounded-full bg-accent/10 border border-accent/20 text-accent mb-6 animate-pulse">
                        v1.0 is now live
                    </div>
                    <h1 className="text-5xl lg:text-7xl font-bold leading-tight mb-6">
                        Coding in Your <br />
                        <span className="gradient-text">Mother Tongue</span>
                    </h1>
                    <p className="text-xl text-text-secondary mb-8 max-w-lg">
                        TelPy breathes life into programming by bridging the gap between Telugu cognition and Python's power. Write code the way you think.
                    </p>
                    <div className="flex flex-col sm:flex-row gap-4">
                        <div className="flex items-center gap-3 bg-white/5 border border-white/10 rounded-full px-6 py-3 font-mono text-sm">
                            <span className="text-accent">$</span>
                            <span>pip install telpy</span>
                            <button
                                onClick={() => navigator.clipboard.writeText('pip install telpy')}
                                className="ml-2 text-text-secondary hover:text-white transition-colors"
                                title="Copy to clipboard"
                            >
                                <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round"><rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2-2v1"></path></svg>
                            </button>
                        </div>
                        <button className="btn btn-primary">
                            Get Started
                        </button>
                    </div>
                    <p className="mt-4 text-sm text-text-secondary">
                        Now available on <a href="https://pypi.org/project/telpy/" target="_blank" rel="noreferrer" className="text-accent hover:underline">PyPI</a>
                    </p>
                </div>

                <div className="relative animate-float">
                    <div className="absolute inset-0 bg-accent/20 blur-[100px] rounded-full pointer-events-none"></div>
                    <div className="glass-card relative z-10 font-mono text-sm leading-relaxed border-l-4 border-accent">
                        <div className="flex gap-2 mb-4">
                            <div className="w-3 h-3 rounded-full bg-red-500"></div>
                            <div className="w-3 h-3 rounded-full bg-yellow-500"></div>
                            <div className="w-3 h-3 rounded-full bg-green-500"></div>
                        </div>
                        <p className="text-text-secondary"># TelPy Example</p>
                        <p className="mt-2"><span className="text-accent">pani</span> greet(name) <span className="text-secondary">nirvachinchu</span>:</p>
                        <p className="pl-4"><span className="text-green-400">"Namaskaram "</span> <span className="text-secondary">+</span> name <span className="text-accent">chupinchu</span>()</p>
                        <p className="mt-4"><span className="text-accent">okavela</span> time <span className="text-secondary">12 kanna_chinna</span> <span className="text-accent">ayithe</span>:</p>
                        <p className="pl-4"><span className="text-green-400">"Subhodayam"</span> <span className="text-accent">chupinchu</span>()</p>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default Hero
