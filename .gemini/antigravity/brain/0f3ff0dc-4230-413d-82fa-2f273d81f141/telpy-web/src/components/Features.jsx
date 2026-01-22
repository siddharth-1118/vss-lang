const Features = () => {
    const features = [
        {
            title: "Cognitive Resonance",
            desc: "Syntax designed to align with Telugu SOV (Subject-Object-Verb) grammar structure for intuitive logic flow.",
            icon: "🧠"
        },
        {
            title: "Python Power",
            desc: "Transpiles directly to Python 3, giving you instant access to the entire ecosystem of libraries like NumPy and Pandas.",
            icon: "🐍"
        },
        {
            title: "Production Ready",
            desc: "Includes a robust transpiler, full standard library localization, and helpful error messages in Telugu.",
            icon: "🚀"
        }
    ]

    return (
        <section id="features" className="py-20 relative">
            <div className="container mx-auto px-6">
                <div className="text-center mb-16">
                    <h2 className="text-3xl lg:text-5xl font-bold mb-4">Why <span className="text-accent">TelPy</span>?</h2>
                    <p className="text-text-secondary max-w-2xl mx-auto">
                        Empowering the next billion users by removing the English language barrier from computational thinking.
                    </p>
                </div>

                <div className="grid md:grid-cols-3 gap-8">
                    {features.map((feature, idx) => (
                        <div key={idx} className="glass-card hover:bg-white/5 transition-all cursor-default group">
                            <div className="text-4xl mb-4 group-hover:scale-110 transition-transform duration-300">{feature.icon}</div>
                            <h3 className="text-xl font-bold mb-2">{feature.title}</h3>
                            <p className="text-text-secondary">{feature.desc}</p>
                        </div>
                    ))}
                </div>
            </div>
        </section>
    )
}

export default Features
