# --------------------------------
# lexicalAnalyzer.py
# 
# A lexical analyzer developed by
# me for the compilers discipline
# from 09/19/2023 until
# 09/20/2023.
# --------------------------------

import ply.lex as lex

# Reserved words
reserved = {
    'array': 'ARRAY',
    'begin': 'BEGIN',
    'const': 'CONST',
    'do': 'DO',
    'else': 'ELSE',
    'end': 'END',
    'function': 'FUNCTION',
    'id': 'ID',
    'if': 'IF',
    'integer': 'INTEGER',
    'of': 'OF',
    'procedure': 'PROCEDURE',
    'read': 'READ',
    'real': 'REAL',
    'record': 'RECORD',
    'return': 'RETURN',
    'then': 'THEN',
    'type': 'TYPE',
    'var': 'VAR',
    'while': 'WHILE',
    'write': 'WRITE'
}

# List of token names
tokens = [
    'ATRIBUTION',
    'CLOSING_ROUND_BRACKET',
    'CLOSING_SQUARE_BRACKET',
    'COLON',
    'COMMA',
    'COMMENT',
    'CONST_VALUE',
    'EQUAL',
    'FULL_POINT',
    'LOGICAL_OPERATOR',
    'MATHEMATICAL_OPERATOR',
    'NUMBER',
    'OPENING_ROUND_BRACKET',
    'OPENING_SQUARE_BRACKET',
    'SEMICOLON'
 ] + list(reserved.values())

# Regular expression rules
t_ATRIBUTION = r':='
t_CLOSING_ROUND_BRACKET = r'\)'
t_CLOSING_SQUARE_BRACKET = r'\]'
t_COLON = r':'
t_COMMA = r','
t_CONST_VALUE = r'"(\s|\w)*"'
t_FULL_POINT = r'\.'
t_LOGICAL_OPERATOR = r'(>|<|=|!)'
t_MATHEMATICAL_OPERATOR = r'(\+|-|\*|/)'
t_NUMBER = r'\d+(\.\d+)?'
t_OPENING_ROUND_BRACKET = r'\('
t_OPENING_SQUARE_BRACKET = r'\['
t_SEMICOLON = r';'

def t_COMMENT(t):
    r'<!--(\s|\w)*-->'
    pass

def t_EQUAL(t):
    r'=='
    t.type = reserved.get(t.value, 'EQUAL')
    return t

def t_ID(t):
    r'([a-z]|[A-Z])([a-z]|[A-Z]|\d)*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Define a rule so we can track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# A string containing ignored characters (spaces and tabs)
t_ignore  = ' \t'

# Error handling rule
def t_error(t):
    print("Illegal character " + "'" +  t.value[0] + "'")
    t.lexer.skip(1)

# Building the lexer
lexer = lex.lex()

# Loading the source code file
try:
    filePath = str(input('Enter the file path: '))
    file = open(filePath, 'r')
except:
    print('Error: the file does not exist.')
else:
    sourceCode = file.read()
    file.close()

# Giving the input to the lexer
lexer.input(sourceCode)

# Declaring the token list
tokenList = []

# Tokenizing
for tok in lexer:
    tokenList.append({'lexem': tok.value,
                      'token': tok.type,
                      'line': tok.lineno})

print(lexer)

# Printing the token list
printOpt = input('Do you want to print the token list (y/s): ')

if printOpt == "y":
    for t in tokenList:
        print('Lexem:\t' + t['lexem'])
        print('Token:\t' + t['token'])
        print('Line:\t' + str(t['line']) + '\n')