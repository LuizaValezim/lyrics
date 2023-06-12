import sys

reserved_word=['print', 'while', 'if', 'else', 'def', 'use']

class PrePo:

    def removeComments(argv):
        if '#' not in argv:
            return argv
        lines = argv.split('\n')
        for i in range(len(lines)):
            for j in range(len(lines[i])):
                if lines[i][j] == '#':
                    lines[i] = lines[i][:j]
                    break
        return '\n'.join(lines)

    
class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value


class Tokenizer:
    def __init__(self, source):
        self.source = source
        self.position = 0
        self.next = None

    def selectNext(self):
        if self.position >= len(self.source):
            self.next = None
            return
        c = self.source[self.position]
        if c.isdigit():
            value = ''
            while self.position < len(self.source) and self.source[self.position].isdigit():
                value += self.source[self.position]
                self.position += 1
            if self.source[self.position].isalpha():
                raise Exception('Unexpected character: ' + self.source[self.position])
            self.next = Token('NUMBER', int(value))
        elif c.isalpha() or c == '_':
            value = ''
            value += self.source[self.position]
            self.position += 1
            if self.source[self.position].isdigit():
                while self.position < len(self.source) and self.source[self.position].isdigit():
                    value += self.source[self.position]
                    self.position += 1
                if self.position < len(self.source) and (self.source[self.position].isalpha() or self.source[self.position] == '_'):
                    while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                        value += self.source[self.position]
                        self.position += 1
                    self.next = Token('IDEN', value)
                else:
                    self.next = Token('NAME', value)
            else:
                while self.position < len(self.source) and (self.source[self.position].isalnum() or self.source[self.position] == '_'):
                    value += self.source[self.position]
                    self.position += 1
                if value in reserved_word:
                    self.next = Token('RESERVED', value)
                else:
                    self.next = Token('IDEN', value)

        elif c == ' ':
            self.position += 1
            self.selectNext()
        elif c == '+':
            self.next = Token('PLUS', c)
            self.position += 1
        elif c == '-':
            self.next = Token('MINUS', c)
            self.position += 1
        elif c == '*':
            self.next = Token('MULT', c)
            self.position += 1
        elif c == '/':
            self.next = Token('DIV', c)
            self.position += 1
        elif c == '(':
            self.next = Token('LPAREN', c)
            self.position += 1
        elif c == ')':
            self.next = Token('RPAREN', c)
            self.position += 1
        elif c == '\n':
            self.next = Token('NEWLINE', c)
            self.position += 1
        elif c == '{':
            self.next = Token('LBRACE', c)
            self.position += 1
        elif c == '}':
            self.next = Token('RBRACE', c)
            self.position += 1
        elif c == '=':
            if self.source[self.position + 1] == '=':
                self.next = Token('EQ', c)
                self.position += 2
            else:
                self.next = Token('ASSIGN', c)
                self.position += 1
        elif c == '<':
            self.next = Token('LT', c)
            self.position += 1
        elif c == '>':
            self.next = Token('GT', c)
            self.position += 1
        elif c == '!':
            self.next = Token('NOT', c)
            self.position += 1
        elif c == '&':
            if self.source[self.position + 1] == '&':
                self.next = Token('AND', c)
                self.position += 2
            else:
                raise Exception('Unexpected character: ' + c)
        elif c == '|':
            if self.source[self.position + 1] == '|':
                self.next = Token('OR', c)
                self.position += 2
            else:
                raise Exception('Unexpected character: ' + c)
        elif c == ':':
            self.next = Token('COLON', c)
            self.position += 1
        elif c == '"':
            value = ''
            self.position += 1
            while self.position < len(self.source) and self.source[self.position] != '"':
                value += self.source[self.position]
                self.position += 1
            if self.source[self.position] == '"':    
                self.position += 1
                self.next = Token('STRING', value)
            else:
                raise Exception('Unexpected character: ' + c)
        elif c == ',':
            self.next = Token('COMMA', c)
            self.position += 1
        else:
            raise Exception('Unexpected character: ' + c)
        return self.next

class SymbolTable:
    def __init__(self):
        self.table = {}
    
    def get(self, name):
        if name not in self.table:
            raise Exception('Variable not declared')
        return self.table[name]
    
    def get_key_by_value(self, value):
        for key, val in self.table.items():
            if value in val:
                return key
        return None
    
    
    def set(self, name, value):
        self.table[name] = value
    


class FuncTable:
    def __init__(self):
        self.table = {}
    
    def get(self, name):
        return self.table[name]
    
    def create (self, name, value):
        if name in self.table:
            raise Exception('Function already declared')
        self.table[name] = value
    


class Node:
    def __init__(self, value):
        self.value = value
        self.children = []

    def evaluate(self, st):
        pass


class UnOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, st):
        if self.value == '-':
            return ["Int",-self.children[0].evaluate(st)[1]]
        if self.value == '!':
            return ["Int",not self.children[0].evaluate(st)[1]]
        return ["Int", self.children[0].evaluate(st)[1]]

class intVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return ["Int", self.value]
    
class nameVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return ["Name", self.value]

class strVal(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self, st):
        return ['String', self.value]
    
    
class NoOp(Node):
    def __init__(self):
        pass

    def evaluate(self,st):
        return None

class BinOp(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, st):
        x = self.children[0].evaluate(st)[1]
        y = self.children[1].evaluate(st)[1]
        if self.children[0].evaluate(st)[0] == "String" or self.children[1].evaluate(st)[0] == "String":
            if self.value == '+':
                return ["String", str(x) + str(y)]
            if self.value == '&&':
                if x and y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '||':
                if x or y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '==':
                if x == y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '<':
                if x < y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '>':
                if x > y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            else:
                raise Exception('Unexpected token: String')
        else:
            if self.value == '+':
                return ["Int", x + y]
            if self.value == '-':
                return ["Int", x - y]
            if self.value == '*':
                return ["Int", x * y]
            if self.value == '/':
                return ["Int", x // y]
            if self.value == '&&':
                if x and y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '||':
                if x or y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '==':
                if x == y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '<':
                if x < y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            if self.value == '>':
                if x > y:
                    return ["Int", 1]
                else:
                    return ["Int", 0]
            
class Print(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, st):
        for child in self.children:
            value = child.evaluate(st)[1]
            print(value)

class Assign(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self,st):
        st.set(self.children[0].value, self.children[1].evaluate(st))
    
class Iden(Node):
    def __init__(self, value):
        self.value = value

    def evaluate(self,st):
        return st.get(self.value)
    
class Block(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self,st):
        for child in self.children:
            if hasattr(child, 'value'):
                child.evaluate(st)
                if child.value == 'return':
                    return child.evaluate(st)

class If(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self,st):
        if self.children[0].evaluate(st)[1]:
            self.children[1].evaluate(st)
        elif len(self.children) == 3:
            self.children[2].evaluate(st)

class While(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self,st):
        while self.children[0].evaluate(st)[1]:
            self.children[1].evaluate(st)


         
class ReadLine(Node):
    def __init__(self, value):
        pass

    def evaluate(self, st):
        return ["Int", int(input())]
    
class FuncDec(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, st):
        ft.create(self.children[0], self)

class FunCall(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, st):
        func = ft.get(self.value)
        if len(func.children[1]) != len(self.children):
            raise Exception('Wrong number of arguments')
        func_st = SymbolTable()

        if len(self.children) != 0:
            for i in range(len(func.children[1])):
                func_st.set(func.children[1][i].value, self.children[i].evaluate(st)) 
        return func.children[2].evaluate(func_st)
    
class Return(Node):
    def __init__(self, value, children):
        self.value = value
        self.children = children

    def evaluate(self, st):
        return self.children[0].evaluate(st)
    
class Parser:
    def __init__(self, tokenizer):
        self.tokenizer = tokenizer
        self.tokenizer.selectNext()

    def parseBlock(self):
        result = Block('Block', [])
        while self.tokenizer.next is not None:
            result.children.append(self.parseStatement())
        return result
    
    def parseStatement(self):
        if self.tokenizer.next.type == 'NEWLINE':
            self.tokenizer.selectNext()
            return NoOp()
        elif self.tokenizer.next.value == 'use':
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'IDEN':
                name = self.tokenizer.next.value
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'LPAREN':
                    self.tokenizer.selectNext()
                    args = []
                    if self.tokenizer.next.type == 'RPAREN':
                        self.tokenizer.selectNext()
                        return FunCall(name, args)
                    else:
                        args.append(self.parseRelExpr())
                        while self.tokenizer.next.type == 'COMMA':
                            self.tokenizer.selectNext()
                            args.append(self.parseRelExpr())
                        if self.tokenizer.next.type == 'RPAREN':
                            self.tokenizer.selectNext()
                            return FunCall(name, args)
                        else:
                            raise Exception('Unexpected token: ' + self.tokenizer.next.type)
            else:
                raise Exception('Unexpected token: ' + self.tokenizer.next.type)
        elif self.tokenizer.next.type == 'IDEN':
            name = self.tokenizer.next.value
        
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'ASSIGN':
                self.tokenizer.selectNext()
                return Assign('ASSIGN', [Iden(name), self.parseExpression()])
            else:
                raise Exception('Unexpected token: ' + self.tokenizer.next.type)
            
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'item':
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'IDEN':
                name = self.tokenizer.next.value
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'COLON':
                    self.tokenizer.selectNext()
                    return Assign('ASSIGN', [Iden(name), self.parseExpression()])
            
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'print':
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'LPAREN':
                self.tokenizer.selectNext()
                to_print = self.parseRelExpr()
                print_args = [to_print]
                while self.tokenizer.next.type == 'COMMA':
                    self.tokenizer.selectNext()
                    to_print = self.parseRelExpr()
                    print_args.append(to_print)
                if self.tokenizer.next.type == 'RPAREN':
                    self.tokenizer.selectNext()
                    return Print('Print', print_args)
                else:
                    raise Exception('Unexpected token: ' + self.tokenizer.next.type)
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'while':
            self.tokenizer.selectNext()
            condition = self.parseRelExpr()
            if self.tokenizer.next.type == 'LBRACE':
                self.tokenizer.selectNext()
                body = Block('Block', [])
                while self.tokenizer.next.type != 'RBRACE':
                    body.children.append(self.parseStatement())
                if self.tokenizer.next.type == 'RBRACE':
                    self.tokenizer.selectNext()
                    return While('While', [condition, body])    
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'if':
            self.tokenizer.selectNext()
            condition = self.parseRelExpr()
            if self.tokenizer.next.type == 'LBRACE':
                self.tokenizer.selectNext()
                body = Block('Block', [])
                while self.tokenizer.next.type != 'RBRACE':
                    body.children.append(self.parseStatement())
                if self.tokenizer.next.type == 'RBRACE':
                    self.tokenizer.selectNext()
                if self.tokenizer.next is not None and self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'else':
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == 'LBRACE':
                        self.tokenizer.selectNext()
                        else_body = Block('Block', [])
                        while self.tokenizer.next.type != 'RBRACE':
                            else_body.children.append(self.parseStatement())
                        if self.tokenizer.next.type == 'RBRACE':
                            self.tokenizer.selectNext()
                            return If('If', [condition, body, else_body])
                    else:
                        raise Exception('Unexpected token: ' + self.tokenizer.next.type)
                else:
                    self.tokenizer.selectNext()
                    return If('If', [condition, body])
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'def':
            self.tokenizer.selectNext()
            name = self.tokenizer.next.value
            self.tokenizer.selectNext()
            if self.tokenizer.next.type == 'LPAREN':
                self.tokenizer.selectNext()
                args = []
                if self.tokenizer.next.type == 'IDEN':
                    args.append(self.parseRelExpr())
                    while self.tokenizer.next.type == 'COMMA':
                        self.tokenizer.selectNext()
                        args.append(self.parseRelExpr())
                if self.tokenizer.next.type == 'RPAREN':
                    self.tokenizer.selectNext()
                    if self.tokenizer.next.type == 'LBRACE':
                        self.tokenizer.selectNext()
                        body = Block('Block', [])
                        while self.tokenizer.next.type != 'RBRACE':
                            body.children.append(self.parseStatement())
                        if self.tokenizer.next.type == 'RBRACE':
                            self.tokenizer.selectNext()
                            return FuncDec('Function', [name, args, body])
                    else:
                        raise Exception('Unexpected token: ' + self.tokenizer.next.type)
                else:
                    raise Exception('Unexpected token: ' + self.tokenizer.next.type)
        else:
            raise Exception('Unexpected token: ' + self.tokenizer.next.type)
        
    def parseTerm(self):
        result = self.parseFactor()
        while self.tokenizer.next is not None and self.tokenizer.next.type in ('MULT', 'DIV', 'AND'):
            if self.tokenizer.next.type == 'MULT':
                self.tokenizer.selectNext()
                result = BinOp('*', [result, self.parseFactor()])
            if self.tokenizer.next.type == 'DIV':
                self.tokenizer.selectNext()
                result = BinOp('/', [result, self.parseFactor()])
            if self.tokenizer.next.type == 'AND':
                self.tokenizer.selectNext()
                result = BinOp('&&', [result, self.parseFactor()])
        return result
        
    def parseExpression(self):
        
        result = self.parseTerm()
        while self.tokenizer.next is not None and self.tokenizer.next.type in ('PLUS', 'MINUS', 'OR'):
            if self.tokenizer.next.type == 'PLUS':
                self.tokenizer.selectNext()
                result = BinOp('+', [result, self.parseTerm()])
            elif self.tokenizer.next.type == 'MINUS':
                self.tokenizer.selectNext()
                result = BinOp('-', [result, self.parseTerm()])
            elif self.tokenizer.next.type == 'OR':
                self.tokenizer.selectNext()
                result = BinOp('||', [result, self.parseTerm()])
        return result
    
    def parseRelExpr(self):
        result = self.parseExpression()
        while self.tokenizer.next is not None and self.tokenizer.next.type in ('EQ', 'LT', 'GT'):
            if self.tokenizer.next.type == 'EQ':
                self.tokenizer.selectNext()
                result = BinOp('==', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'LT':
                self.tokenizer.selectNext()
                result = BinOp('<', [result, self.parseExpression()])
            elif self.tokenizer.next.type == 'GT':
                self.tokenizer.selectNext()
                result = BinOp('>', [result, self.parseExpression()])

        return result

    def parseFactor(self):
        if self.tokenizer.next.type == "NUMBER":
            result = self.tokenizer.next.value
            self.tokenizer.selectNext()
            return intVal(result)
        elif self.tokenizer.next.type == 'NAME':
            result = self.tokenizer.next.value
            self.tokenizer.selectNext()
            return nameVal(result)
        elif self.tokenizer.next.type == 'STRING':
            result = self.tokenizer.next.value
            self.tokenizer.selectNext()
            return strVal(result)
        elif self.tokenizer.next.type == 'MINUS':
            self.tokenizer.selectNext()
            return UnOp('-', [self.parseFactor()])
        elif self.tokenizer.next.type == 'PLUS':
            self.tokenizer.selectNext()
            return UnOp('+', [self.parseFactor()])
        elif self.tokenizer.next.type == 'NOT':
            self.tokenizer.selectNext()
            return UnOp('!', [self.parseFactor()])
        elif self.tokenizer.next.type == 'LPAREN':
            self.tokenizer.selectNext()
            result = self.parseRelExpr()
            if self.tokenizer.next.type == 'RPAREN':
                self.tokenizer.selectNext()
                return result
            else:
                raise Exception('Unexpected token: ' + self.tokenizer.next.type)
        elif self.tokenizer.next.type == 'IDEN':
            result = self.tokenizer.next.value
            
            self.tokenizer.selectNext()
            return Iden(result)
        elif self.tokenizer.next.type == 'RESERVED' and self.tokenizer.next.value == 'use':
            if self.tokenizer.next.type == 'IDEN':
                result = self.tokenizer.next.value
                self.tokenizer.selectNext()
                if self.tokenizer.next.type == 'LPAREN':
                    self.tokenizer.selectNext()
                    args = []
                    if self.tokenizer.next.type == 'RPAREN':
                        self.tokenizer.selectNext()
                        return FunCall(result, args)
                    else:
                        args.append(self.parseRelExpr())
                        while self.tokenizer.next.type == 'COMMA':
                            self.tokenizer.selectNext()
                            args.append(self.parseRelExpr())
                        if self.tokenizer.next.type == 'RPAREN':
                            self.tokenizer.selectNext()
                            return FunCall(result, args)
                        else:
                            raise Exception('Unexpected token: ' + self.tokenizer.next.type)
                else:
                    raise Exception('Unexpected token: ' + self.tokenizer.next.type)
                
        else:
            raise Exception('Unexpected token: ' + self.tokenizer.next.type)


    @staticmethod
    def run(code,st):
        tokenizer = Tokenizer(code)
        parser = Parser(tokenizer)
        result = parser.parseBlock()
        if tokenizer.next is not None:
            raise Exception('Unexpected token: ' + tokenizer.next.type)
        return result.evaluate(st)


global ft 
ft = FuncTable()

def main():
    filename = sys.argv[1]
    with open (filename, "r") as myfile:
        data=myfile.read()

    code = PrePo.removeComments(data)
    st = SymbolTable()
    Parser.run(code,st)


if __name__ == '__main__':
    main()