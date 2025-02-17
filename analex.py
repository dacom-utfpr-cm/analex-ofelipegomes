from automata.fa.Moore import Moore
import sys, os
import re

from myerror import MyError

error_handler = MyError('LexerErrors')

global check_cm
global check_key

moore = Moore(
# Estados
['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 
 'q11', 'q12','q012', 'q13', 'q14', 'q15', 'q16', 'q17', 'q18', 'q19', 'q20', 
 'q21', 'q22', 'q23', 'q24', 'q25', 'q26', 'q27', 'q28', 'q29', 'q30', 
 'q31', 'q32', 'q33', 'q34', 'q35', 'q36', 'q37', 'q38', 'q39', 'q40', 
 'q41', 'q42', 'q43', 'q44', 'q45', 'q46', 'q47', 'q48', 'q49', 'q50', 
 'q51', 'q52', 'q53', 'q54', 'q55', 'q56', 'q57', 'q58', 'q59', 'q60', 
 'q61', 'q62', 'q63', 'q64', 'q65', 'q66', 'q67', 'q68', 'q69', 'q70', 
 'q71', 'q72', 'q73', 'q74', 'q75', 'q76', 'q77', 'q78', 'q79', 'q80', 
 'q81', 'q82', 'q83', 'q84', 'q85', 'q86', 'q87', 'q88', 'q89', 'q90', 
 'q91', 'q92', 'q93', 'q94', 'q95', 'q96', 'q97', 'q98', 'q99', 'q100', 'q101', 'q102', 'q103'],

# Alfabeto
[
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
    'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z',
    '(', ')', '{', '}', ' ', '\n', '\t', '_', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ',', '+', '=',';',','
],
    # Saídas possíveis (tokens)
  ['INT', 'MAIN', 'VOID', 'LPAREN', 'RPAREN', 'LBRACES', 'RBRACES', 'RETURN','DIFFERENT',
   'NUMBER', 'SEMICOLON', 'FLOAT', 'COMMA', 'ATTRIBUTION', 'PLUS', 'IF', 'ELSE', 'EQUALS',
   'LBRACKETS', 'RBRACKETS'],

    # Transições
    {
        # INT
        'q0': {
            'i': 'q1',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            '0': 'q19',  
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'f': 'q40',
            '/': 'q101',
        },
        'q1': {'n': 'q2',
               'f':'q58',
               },
        'q2': {'t': 'q3',
               'p': 'q42',
        },
        'q3': {
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'm': 'q4',
            '0': 'q19',
        },

        # MAIN
        'q4': {'a': 'q5'},
        'q5': {'i': 'q6'},
        'q6': {'n': 'q7'},
        
        #ID
        'q7': {
            ')': 'q12',
            '(': 'q11',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            '0': 'q19',
            ';': 'q30',
            ',': 'q60',
            '+': 'q50',
            '-':'q70',
            '/':'q75',
            '*':'q76',
            '[':'q85',
            ']':'q86',
            
        },
        'q77':{
            ')': 'q78',
               'o': 'q9',
                ';': 'q79',
                ' ': 'q82',
                ',': 'q83',
        },
        
        'q78':{'{': 'q13'},
        'q79':{'\n': 'q15'},
        'q82':{
            '/': 'q101',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',
        },
        
        'q83':{
            'y': 'q7',
            'u': 'q7',
            'v':'q7',
            ',': 'q60',  
            ' ': 'q15',
            '\n': 'q0',  
            ')': 'q12',  
            '}': 'q14',  
        },
        
        # lparen
        'q11': {
            'a': 'q7',  
            'c': 'q7',
            'v': 'q77',
            'g': 'q55',
            ')': 'q12',
            '0': 'q19',
            'i': 'q1',
            'u': 'q7',
            'x': 'q7',
            'z': 'q7',
            'r': 'q21',
        },
        'q8': {'o': 'q9',
               ' ': 'q15',
               ',':'q60',
               },
        'q9': {'i': 'q10'},
        'q10': {'d': 'q012'},
        'q012': {')': 'q12',
                 ' ': 'q15',
                 },
        
        # RPAREN transitions
        'q12': {
            ')': 'q12',
            '{': 'q13',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            '}': 'q14',  # Aceitar diretamente uma chave após RPAREN
            ';': 'q30',
            '0': 'q19',
        },

        # Chaves e espaço em branco
        'q13': {
            '}': 'q14',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
        },
        'q14': {
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            '0': 'q19',
        },
        #space
        'q15': {
            '!': 'q90',
            '-': 'q70',
            '/': 'q101',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'c':'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',
        },


        # RETURN
        'q21': {'e': 'q22'},
        'q22': {'t': 'q23',
                's':'q7',},#res
        'q23': {'u': 'q24'},
        'q24': {'r': 'q25'},
        'q25': {'n': 'q26'},
        'q26': {
            '(': 'q11',
            ' ': 'q15',
            ';': 'q30',
        },
        # NUMBERS
        'q19': {
            '0': 'q99',
            ' ': 'q15',
            ')': 'q12',
            '\n': 'q15',
            '\t': 'q15',
            ';': 'q30',
            '}': 'q14',
            '[':'q85',
            ']':'q86',
        },
        #BIG NUMBER
        'q99':{'/': 'q101',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',
            ';': 'q30',
            ']':'q86',},
        
        'q30':{
            ' ':'q15',
            ';':'q30',
            '\n':'q0',
            ')': 'q12',
            '}': 'q14',
        },
        
        #FUNC
        'q87':{'n':'q88'},
        'q88':{'c':'q7'},
        
        #FLOAT
        
        'q40':{'l':'q31',
               'u':'q87',
               },
        'q31':{'o':'q32'},
        'q32':{'a':'q33'},
        'q33':{'t':'q34'},
        'q34':{' ':'q15'},
        
        #soma
        'q27':{'o': 'q28'},
        'q28':{'m': 'q29'},
        'q29':{'a': 'q7'},
        
        #plus
        'q50':{' ': 'q15',
               '+':'q50',
               },
        
        #minus
        'q95':{
            '-':'q70',
            '/': 'q75',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',
            
        },
        
        'q96':{
            '-':'q70',
            '/': 'q75',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',},
        
        'q70':{'-':'q70',
               'u':'q96',
               ' ':'q95',
               '1':'q19'
               },
        #DIVIDE
        'q75':{'/':'q75',
               'v':'q7',
               },
        
        #TIMES
        'q76':{'*': 'q76',
               'v':'q7',
               },
        
        #ATTRIBUTION
        'q41':{
            '=':'q80',
            ' ': 'q81',
        },        
        
        #EQUALS
        'q80':{'=':'q80',
                ' ': 'q15',},
        
        'q81':{
            '-':'q70',
            '/': 'q101',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',

        },
        
        #INPUT
        'q42': {'u': 'q43'},
        'q43': {'t':'q7'},
        
        #OUT
        'q51': {'u':'q52'},
        'q52': {'t':'q2'},
    
        #COMMA
        'q60': {
            'b': 'q7',
            'y': 'q7',
            'u': 'q7',
            'v':'q7',
            ',': 'q60',  
            ' ': 'q15',
            '\n': 'q0',  
            ')': 'q12',  
            '}': 'q14',  
        },
        
        
        #gcd
        'q55':{'g':'q55',
               'c':'q56',
               },
        'q56':{'d':'q7'},
    #IF
    'q58':{'f':'q58',
           ' ': 'q15',
           '(': 'q11',
           },
    
    #ELSE 
    'q61':{'e':'q61',
           'l':'q62'},
    'q62':{'s':'q63'},
    'q63':{'e':'q64'},
    'q64':{' ': 'q15'},
    
    #comentario
    
    'q101':{'*': 'q102',
            '\n': 'q0',
            ' ': 'q101',
            },
    
    'q102': {'\n': 'q102',
             '*': 'q103',
             ' ': 'q102',
             'u': 'q102',
             '-': 'q102',
             '/': 'q102',
             'v': 'q102',
             '=': 'q102',
             'm': 'q102',
             'o': 'q102',
             'd': 'q102'
            
    },
    'q103': { '/': 'q0',
             '*': 'q103',
             'v': 'q103',
             ' ':'q103',
             '=':'q103',
             'i':'q103',
             '\t': 'q102',
             'u': 'q102',
             },
    
    #LBRACKETS
    'q85':{ 
            '/': 'q101',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',
            ';': 'q30',
        
    },
    
    #RBRACKETS
    
    'q86':{ 
            '/': 'q101',
            '=': 'q41',
            '+':'q50',
            ' ': 'q15',
            '\n': 'q15',
            '\t': 'q15',
            'i': 'q1',
            'm': 'q4',
            '(': 'q11',
            ')': 'q12',
            '{': 'q13',
            '}': 'q14',
            'r': 'q21',
            '0': 'q19',  # Transições para números
            '1': 'q19',
            '2': 'q19',
            '3': 'q19',
            '4': 'q19',
            '5': 'q19',
            '6': 'q19',
            '7': 'q19',
            '8': 'q19',
            '9': 'q19',
            'a': 'q7',
            'b': 'q7',
            'g': 'q55',
            'x':'q7',
            'y':'q7',
            'u': 'q7',
            'v': 'q77',
            'z': 'q7',
            'f':'q40',
            's':'q27',
            'o':'q51',
            'e': 'q61',
            ';': 'q30',
            '[':'q85',
        
    },
    
    #different
    
    'q90':{'=':'q91'},
    'q91':{' ':'q15'},
    },
    

    # Estado inicial
    'q0',

    # Saídas associadas a cada estado
    {
        'q0': '',
        'q1': '',
        'q2': '',
        'q3': 'INT',
        'q4': '',
        'q5': '',
        'q6': '',
        'q7': 'ID',
        'q8': '',
        'q9': '',
        'q10': 'VOID',
        'q11': 'LPAREN',
        'q12': 'RPAREN',
        'q012': '',
        'q13': 'LBRACES',
        'q14': 'RBRACES',
        'q15': '',
        'q19': 'NUMBER',  # Novo token para números
        'q30': 'SEMICOLON',
        'q21': '',
        'q22': '',
        'q23': '',
        'q24': '',
        'q25': '',
        'q26': 'RETURN',
        'q27': '',
        'q28': '',
        'q29': '',
        'q34': '',
        'q40':'',
        'q42': '',
        'q43': '',
        'q41':'',
        'q31':'',
        'q32':'',
        'q33':'FLOAT',
        'q34':'',
        'q35':'',
        'q50':'PLUS',
        'q51': '',
        'q52': '',
        'q55':'',
        'q56':'',
        'q57':'',
        'q58':'IF',
        'q60':'COMMA',
        'q61':'',
        'q62':'',
        'q63':'',
        'q64': 'ELSE',
        'q70':'',
        'q75':'DIVIDE',
        'q76':'TIMES',
        'q77': '',
        'q78':'ID' 'RPAREN',
        'q79': 'ID' 'SEMICOLON',
        'q101':'',
        'q102':'',
        'q103': '',
        'q80': 'EQUALS',
        'q81': 'ATTRIBUTION',
        'q82': 'ID',
        'q83':'ID''COMMA',
        'q85':'LBRACKETS',
        'q86':'RBRACKETS',
        'q87':'',
        'q88':'',
        'q90':'',
        'q91':'DIFFERENT',
        'q95':'MINUS',
        'q96':'MINUS''ID',
        'q99':'',
    }
)


def main():
    check_cm = False
    check_key = False

    for idx, arg in enumerate(sys.argv):
        aux = arg.split('.')
        if aux[-1] == 'cm':
            check_cm = True
            idx_cm = idx

        if arg == "-k":
            check_key = True

    if len(sys.argv) < 3:
        raise TypeError(error_handler.newError(check_key, 'ERR-LEX-USE'))

    if not check_cm:
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-NOT-CM'))
    elif not os.path.exists(sys.argv[idx_cm]):
        raise IOError(error_handler.newError(check_key, 'ERR-LEX-FILE-NOT-EXISTS'))
    else:
        with open(sys.argv[idx_cm], 'r', encoding='utf-8') as data:  # Read with UTF-8 encoding
            source_file = data.read()

        if not check_cm:
            print("Definição da Máquina")
            print(moore)
            print("Entrada:")
            print(source_file)
            print("Lista de Tokens:")

        tokens = moore.get_output_from_string(source_file)

        separated_tokens = re.findall(r'INT|ID|IF|ELSE|DIFFERENT|LPAREN|LBRACKETS|RBRACKETS|VOID|RPAREN|COMMA|LBRACES|FLOAT|RBRACES|NUMBER|RETURN|ATTRIBUTION|PLUS|SEMICOLON|MINUS|TIMES|DIVIDE|EQUALS', tokens)

        separated_tokens = [token.replace('\r', '') for token in separated_tokens]

        output = '\n'.join(separated_tokens)

        print(output)

if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)