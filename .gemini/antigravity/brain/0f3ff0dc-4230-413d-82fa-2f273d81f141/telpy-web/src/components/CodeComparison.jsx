import { useState } from 'react'

const CodeComparison = () => {
    const [activeTab, setActiveTab] = useState('telpy')

    const codeSnippets = {
        telpy: `pani factorial(n) nirvachinchu:
    okavela n 1 kanna_chinna_samam ayithe:
        1 phalam_ivvu
    lekapothe:
        n * factorial(n - 1) phalam_ivvu

# Main execution
num = 5
result = factorial(num)
"Factorial is " + result chupinchu()`,
        python: `def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

# Main execution
num = 5
result = factorial(num)
print("Factorial is " + str(result))`
    }

    return (
        <section className="py-20 bg-black/20">
            <div className="container mx-auto px-6">
                <div className="flex flex-col lg:flex-row gap-12 items-center">
                    <div className="lg:w-1/2">
                        <h2 className="text-3xl lg:text-4xl font-bold mb-6">
                            Familiar, Yet <span className="text-secondary">Distinctly Native</span>
                        </h2>
                        <p className="text-text-secondary mb-8 text-lg">
                            Compare the syntax. TelPy re-imagines control flow to match how you speak, using keywords like <code className="bg-accent/10 text-accent px-1 rounded">okavela</code> (if) and <code className="bg-accent/10 text-accent px-1 rounded">nirvachinchu</code> (define).
                        </p>
                        <div className="flex gap-4">
                            <div className="flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-accent"></span>
                                <span>SOV Logic</span>
                            </div>
                            <div className="flex items-center gap-2">
                                <span className="w-2 h-2 rounded-full bg-secondary"></span>
                                <span>Readable</span>
                            </div>
                        </div>
                    </div>

                    <div className="lg:w-1/2 w-full">
                        <div className="glass-card p-0 overflow-hidden shadow-2xl shadow-accent/5">
                            <div className="flex border-b border-white/10">
                                <button
                                    onClick={() => setActiveTab('telpy')}
                                    className={`flex-1 py-3 px-6 text-sm font-semibold transition-colors ${activeTab === 'telpy' ? 'bg-accent/10 text-accent border-b-2 border-accent' : 'text-text-secondary hover:text-white'}`}
                                >
                                    factorial.tel
                                </button>
                                <button
                                    onClick={() => setActiveTab('python')}
                                    className={`flex-1 py-3 px-6 text-sm font-semibold transition-colors ${activeTab === 'python' ? 'bg-secondary/10 text-secondary border-b-2 border-secondary' : 'text-text-secondary hover:text-white'}`}
                                >
                                    factorial.py
                                </button>
                            </div>
                            <div className="p-6 bg-[#0B1120] min-h-[300px]">
                                <pre className="font-mono text-sm leading-relaxed overflow-x-auto">
                                    <code className="language-python">
                                        {codeSnippets[activeTab].split('\n').map((line, i) => (
                                            <div key={i} className="table-row">
                                                <span className="table-cell select-none text-slate-700 text-right w-8 pr-4">{i + 1}</span>
                                                <span className="table-cell">{line}</span>
                                            </div>
                                        ))}
                                    </code>
                                </pre>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </section>
    )
}

export default CodeComparison
