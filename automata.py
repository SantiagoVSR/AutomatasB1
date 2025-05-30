def es_letra(c):
    return c.isalpha()

def es_digito(c):
    return c.isdigit()

def es_espacio(c):
    return c.isspace()

palabras_reservadas = {
    'string': 'TIPO_DATO',
    'int': 'TIPO_DATO',
    'double': 'TIPO_DATO',
    'boolean': 'TIPO_DATO',
    'if': 'CONDICIONAL',
    'else': 'CONDICIONAL',
    'for': 'BUCLE',
    'while': 'BUCLE',
    'list': 'BUCLE',
    'texto.imp': 'IMPRIMIR',
    'and': 'OPERADOR_LOGICO',
    'or': 'OPERADOR_LOGICO',
    'not': 'OPERADOR_LOGICO'
}

def clasificar_identificador(token):
    token_lower = token.lower()
    return palabras_reservadas.get(token_lower, 'IDENTIFICADOR')

def reconocer_tokens(cadena):
    estado = 0
    i = 0
    token = ''
    tokens = []

    while i < len(cadena):
        c = cadena[i]

        match estado:
            case 0:
                if es_letra(c):
                    estado = 1
                    token += c
                elif c == '.':
                    estado = 2
                    token += c
                elif es_digito(c):
                    estado = 4
                    token += c
                elif c in [',', '.', ';', ':']:
                    estado = 6
                    token += c
                elif c in ['[', ']', '(', ')', '{', '}']:
                    estado = 7
                    token += c
                elif c == '%':
                    estado = 8
                    token += c
                elif c in ['>', '<', '!', '=']:
                    estado = 9
                    token += c
                elif c == '|':
                    estado = 11
                    token += c
                elif c == '&':
                    estado = 13
                    token += c
                elif c in ["'", '"']:
                    estado = 15
                    token += c
                elif c == '/' or c == '\\':
                    estado = 16
                    token += c
                elif c == '*':
                    estado = 18
                    token += c
                elif c == '-':
                    estado = 20
                    token += c
                elif c == '+':
                    estado = 22
                    token += c
                elif es_espacio(c) or c == '\n':
                    estado = 0
                else:
                    tokens.append(("ERROR", c, "❌"))
            case 1:
                if es_letra(c) or es_digito(c) or c == '.':
                    token += c
                elif es_espacio(c) or c == '\n':
                    tipo = clasificar_identificador(token)
                    tokens.append((tipo, token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tipo = clasificar_identificador(token)
                    tokens.append((tipo, token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 2:
                if es_digito(c):
                    token += c
                    estado = 3
                else:
                    tokens.append(("ERROR", token + c, "❌"))
                    token = ''
                    estado = 0
            case 3:
                if es_digito(c):
                    token += c
                elif es_espacio(c) or c == '\n':
                    tokens.append(('DECIMAL', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('DECIMAL', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 4:
                if es_digito(c):
                    token += c
                elif c == '.':
                    token += c
                    estado = 5
                elif es_espacio(c) or c == '\n':
                    tokens.append(('ENTERO', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('ENTERO', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 5:
                if es_digito(c):
                    token += c
                    estado = 3
                else:
                    tokens.append(("ERROR", token + c, "❌"))
                    token = ''
                    estado = 0
            case 6 | 7 | 8 | 10 | 12 | 14 | 15 | 17 | 19 | 21 | 23:
                if es_espacio(c) or c == '\n':
                    tokens.append(('SIMBOLO', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('SIMBOLO', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 9:
                if c == '=':
                    token += c
                    estado = 10
                elif es_espacio(c) or c == '\n':
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 11:
                if c == '|':
                    token += c
                    estado = 12
                else:
                    tokens.append(("ERROR", token + c, "❌"))
                    token = ''
                    estado = 0
            case 13:
                if c == '&':
                    token += c
                    estado = 14
                else:
                    tokens.append(("ERROR", token + c, "❌"))
                    token = ''
                    estado = 0
            case 16:
                if c == '=':
                    token += c
                    estado = 17
                elif c == '/' or c == '\\':
                    token += c
                    estado = 24  # Comentario de línea
                elif es_espacio(c) or c == '\n':
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 24:
                if c == '\n':
                    tokens.append(('COMENTARIO', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    token += c
            case 18:
                if c == '=':
                    token += c
                    estado = 17
                elif c == '*':
                    token += c
                    estado = 19
                elif es_espacio(c) or c == '\n':
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 20:
                if c == '=':
                    token += c
                    estado = 17
                elif c == '-':
                    token += c
                    estado = 21
                elif es_espacio(c) or c == '\n':
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                    continue
            case 22:
                if c == '=':
                    token += c
                    estado = 17
                elif c == '+':
                    token += c
                    estado = 23
                elif es_espacio(c) or c == '\n':
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                else:
                    tokens.append(('OPERADOR', token, "✅"))
                    token = ''
                    estado = 0
                    continue
        i += 1

    if token:
        tipo = clasificar_identificador(token)
        tokens.append((tipo, token, "✅"))

    return tokens

# ============================
# LECTURA DEL ARCHIVO .TXT
# ============================

try:
    with open("Prueba.txt", "r", encoding="utf-8") as archivo:
        contenido = archivo.read()
    resultado = reconocer_tokens(contenido)

    for tipo, valor, estado in resultado:
        print(f"{estado} {tipo}: {valor}")

except FileNotFoundError:
    print("❌ El archivo 'entrada.txt' no se encuentra en el directorio actual.")
