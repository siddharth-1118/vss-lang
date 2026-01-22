# TelPy to Python Lexicon Mapping

KEYWORDS = {
    # Control Flow
    'okavela': 'if',
    'lekapothe_okavela': 'elif',
    'lekapothe': 'else',
    'prathi': 'for',
    'varaku': 'while',
    'aapu': 'break',
    'konasagu': 'continue',
    'vadhiley': 'pass',
    'phalam_ivvu': 'return',
    'ivvu': 'return', # Alias?
    'ippatiki_ivvu': 'yield',
    
    # Logic
    'mariyu': 'and',
    'leka': 'or',
    'kaadu': 'not',
    'undi': 'is',
    'lo': 'in',
    
    # Definitions
    'nirvachinchu': 'def', # Suffix-style often, but mapped to def
    'pani': 'def',         # Prefix-style 'pani foo():' -> 'def foo():'
    'thargathi': 'class',
    'chinna_pani': 'lambda',
    
    # Data/Types
    'emiledu': 'None',
    'nizam': 'True',
    'abaddham': 'False',
    'laaga': 'as',
    'nundi': 'from',
    'thechuko': 'import',
    
    # Exceptions
    'prayatninchu': 'try',
    'thappu_ayithe': 'except',
    'chivariga': 'finally',
    'leppu': 'raise',
    'srustinchu': 'raise',
}

OPERATORS = {
    'kooda': '+',
    'theesiveyi': '-',
    'hechinchu': '*',
    'bhaginchu': '/',
    'sesham': '%',
    'samam': '==',
    'ki_samam': '==',
    'asamam': '!=',
    'samam_kaadu': '!=',
    'kanna_pedda': '>',
    'kanna_chinna': '<',
    'pedda_leka_samam': '>=',
    'chinna_leka_samam': '<=',
}

BUILTINS = {
    'chupinchu': 'print',
    'adugu': 'input',
    'podavu': 'len',
    'shreni': 'range',
    'theruvu': 'open',
    'rakam': 'type',
    'anke': 'int',
    'dashaamsam': 'float',
    'padam': 'str',
    'jaabitha': 'list',
    'nighantuvu': 'dict',
    'samithi': 'set',
    'sahayam': 'help',
}
