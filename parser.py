from lexicalAnalyzer import tokenList

class Parser:
    def __init__(self, tokenList):
        self.tokenList = tokenList
        self.index = 0
    
    def parse(self):
        return self.program()
    
    def program(self):
        node0 = self.declarations()
        node1 = self.block()
        return ('PROGRAM', (node0, node1))
    
    def declarations(self):
        node0 = self.constant_definition()
        node1 = self.type_definition()
        node2 = self.variable_definition()
        node3 = self.routine_definition()
        return ('DECLARATIONS', (node0, node1, node2, node3))
    
    def constant_definition(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'CONST':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.constant()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'SEMICOLON':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.constant_list()
                        return ('CONSTANT_DEFINITION', (node0, node1, node2, node3))
                    else:
                        print(f'Error (CONSTANT_DEFINITION): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (CONSTANT_DEFINITION): It was expected a ";".')
                    return None
            else:
                return None
        return None
    
    def constant_list(self):
        node0 = self.constant()
        if node0 != None:
            if self.index < len(self.tokenList):
                if self.tokenList[self.index]['type'] == 'SEMICOLON':
                    node1 = self.tokenList[self.index]
                    self.index = self.index + 1
                    node2 = self.constant_list()
                    return ('CONSTANT_LIST', (node0, node1, node2))
                else:
                    print(f'Error (CONSTANT_LIST): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                    return None
            else:
                print(f'Error (CONSTANT_LIST): It was expected a ";".')
                return None
        else:
            return None
    
    def constant(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'EQUAL':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.constant_value()
                        return ('CONSTANT', (node0, node1, node2))
                    else:
                        print(f'Error (CONSTANT): It was expected an "==" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (CONSTANT): It was expected an "==".')
                    return None
            else:
                print(f'Error (CONSTANT): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                return None
        else:
            return None
    
    def constant_value(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'CONST_VALUE':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                return ('CONSTANT_VALUE', (node0))
            else:
                node0 = self.mathematical_expression()
                return ('CONSTANT_VALUE', (node0))
        else:
            return None
    
    def type_definition(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'TYPE':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.types()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'SEMICOLON':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.type_list()
                        return ('TYPE_DEFINITION', (node0, node1, node2, node3))
                    else:
                        print(f'Error (TYPE_DEFINITION): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (TYPE_DEFINITION): It was expected a ";".')
                    return None
            else:
                return None
        else:
            return None
    
    def type_list(self):
        node0 = self.types()
        if node0 != None:
            if self.index < len(self.tokenList):
                if self.tokenList[self.index]['type'] == 'SEMICOLON':
                    node1 = self.tokenList[self.index]
                    self.index = self.index + 1
                    node2 = self.type_list()
                    return ('TYPE_LIST', (node0, node1, node2))
                else:
                    print(f'Error (TYPE_LIST): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                    return None
            else:
                print(f'Error (TYPE_LIST): It was expected a ";".')
                return None
        else:
            return None
    
    def types(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'EQUAL':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.data_type()
                        return ('TYPES', (node0, node1, node2))
                    else:
                        print(f'Error (TYPE): It was expected an "==" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (TYPE): It was expected an "==".')
                    return None
            else:
                print(f'Error (TYPE): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                return None
        else:
            return None
    
    def data_type(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'INTEGER':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                return ('DATA_TYPE', (node0))
            elif self.tokenList[self.index]['type'] == 'REAL':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                return ('DATA_TYPE', (node0))
            elif self.tokenList[self.index]['type'] == 'ARRAY':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'OPENING_SQUARE_BRACKET':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        if self.index < len(self.tokenList):
                            if self.tokenList[self.index]['type'] == 'NUMBER':
                                node2 = self.tokenList[self.index]
                                self.index = self.index + 1
                                if self.index < len(self.tokenList):
                                    if self.tokenList[self.index]['type'] == 'CLOSING_SQUARE_BRACKET':
                                        node3 = self.tokenList[self.index]
                                        self.index = self.index + 1
                                        if self.index < len(self.tokenList):
                                            if self.tokenList[self.index]['type'] == 'OF':
                                                node4 = self.tokenList[self.index]
                                                self.index = self.index + 1
                                                node5 = self.data_type()
                                                return ('DATA_TYPE', (node0, node1, node2, node3, node4, node5))
                                            else:
                                                print(f'Error (DATA_TYPE): It was expected an "of" on line {self.tokenList[self.index]["line"]}.')
                                                return None
                                        else:
                                            print(f'Error (DATA_TYPE): It was expected an "of".')
                                            return None
                                    else:
                                        print(f'Error (DATA_TYPE): It was expected a "]" on line {self.tokenList[self.index]["line"]}.')
                                        return None
                                else:
                                    print(f'Error (DATA_TYPE): It was expected a "]".')
                                    return None
                            else:
                                print(f'Error (DATA_TYPE): It was expected a "number" on line {self.tokenList[self.index]["line"]}.')
                                return None
                        else:
                            print(f'Error (DATA_TYPE): It was expected a "number".')
                            return None
                    else:
                        print(f'Error (DATA_TYPE): It was expected an "[" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (DATA_TYPE): It was expected an "[".')
                    return None
            elif self.tokenList[self.index]['type'] == 'RECORD':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.field()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'END':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        return ('DATA_TYPE', (node0, node1, node2))
                    else:
                        print(f'Error (DATA_TYPE): It was expected an "end" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (DATA_TYPE): It was expected an "end".')
                    return None
            elif self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                return ('DATA_TYPE', (node0))
            else:
                print(f'Error (DATA_TYPE): It was expected an "integer", "real", "array", "record" or "id"  on line {self.tokenList[self.index]["line"]}.')
                return None
        else:
            return None
    
    def field(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'COLON':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.data_type()
                        node3 = self.field_list()
                        return ('FIELD', (node0, node1, node2, node3))
                    else:
                        print(f'Error (FIELD): It was expected a ":" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (FIELD): It was expected a ":".')
                    return None
            else:
                print(f'Error (FIELD): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                return None
        else:
            return None
    
    def field_list(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'SEMICOLON':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.field()
                node2 = self.field_list()
                return ('FIELD_LIST', (node0, node1, node2))
            else:
                return None
        return None
    
    def variable_definition(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'VAR':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.variable()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'SEMICOLON':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.variable_list
                        return ('VARIABLE_DEFINITION', (node0, node1, node2, node3))
                    else:
                        print(f'Error (VARIABLE_DEFINITION): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (VARIABLE_DEFINITION): It was expected a ";".')
                    return None
            else:
                return None
        return None
    
    def variable_list(self):
        node0 = self.variable()
        if node0 != None:
            if self.tokenList[self.index]['type'] == 'SEMICOLON':
                node1 = self.tokenList[self.index]
                self.index = self.index + 1
                node2 = self.variable_list()
                return ('VARIABLE_LIST', (node0, node1, node2))
            else:
                print(f'Error (VARIABLE_LIST): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                return None
        else:
            return None
    
    def variable(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.id_list()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'COLON':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.data_type()
                        return ('VARIABLE', (node0, node1, node2, node3))
                    else:
                        print(f'Error (VARIABLE): It was expected a ":" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (VARIABLE): It was expected a ":".')
                    return None
            else:
                print(f'Error (VARIABLE): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                return None
        else:
            return None
    
    def id_list(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'COMMA':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'ID':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.id_list()
                        return ('ID_LIST', (node0, node1, node2))
                    else:
                        print(f'Error (ID_LIST): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (ID_LIST): It was expected an "id".')
                    return None
            else:
                return None
        else:
            return None
    
    def routine_definition(self):
        node0 = self.routine_name()
        if node0 != None:
            node1 = self.variable_definition()
            node2 = self.block()
            node3 = self.routine_definition()
            return ('ROUTINE_DEFINITION', (node0, node1, node2, node3))
        else:
            return None
    
    def routine_name(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'FUNCTION':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'ID':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.routine_parameter()
                        if self.index < len(self.tokenList):
                            if self.tokenList[self.index]['type'] == 'COLON':
                                node3 = self.tokenList[self.index]
                                self.index = self.index + 1
                                node4 = self.data_type()
                                return ('ROUTINE_NAME', (node0, node1, node2, node3, node4))
                            else:
                                print(f'Error (ROUTINE_NAME): It was expected a ":" on line {self.tokenList[self.index]["line"]}.')
                                return None
                        else:
                            print(f'Error (ROUTINE_NAME): It was expected a ":".')
                            return None
                    else:
                        print(f'Error (ROUTINE_NAME): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (ROUTINE_NAME): It was expected an "id".')
                    return None
            elif self.tokenList[self.index]['type'] == 'PROCEDURE':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'ID':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.routine_parameter()
                        return ('ROUTINE_NAME', (node0, node1, node2))
                    else:
                        print(f'Error (ROUTINE_NAME): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (ROUTINE_NAME): It was expected an "id".')
                    return None
            else:
                print(f'Error (ROUTINE_NAME): It was expected a "function" or "procedure" on line {self.tokenList[self.index]["line"]}.')
                return None
        return None
    
    def routine_parameter(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'OPENING_ROUND_BRACKET':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.field()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'CLOSING_ROUND_BRACKET':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        return ('ROUTINE_PARAMETER', (node0, node1, node2))
                    else:
                        print(f'Error (ROUTINE_PARAMETER): It was expected a ")" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (ROUTINE_PARAMETER): It was expected a ")".')
                    return None
            else:
                return None
        return None
    
    def block(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'BEGIN':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.command()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'SEMICOLON':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.command_list()
                        if self.index < len(self.tokenList):
                            if self.tokenList[self.index]['type'] == 'END':
                                node4 = self.tokenList[self.index]
                                self.index = self.index + 1
                                return ('BLOCK', (node0, node1, node2, node3, node4))
                            else:
                                print(f'Error (BLOCK): It was expected an "end" on line {self.tokenList[self.index]["line"]}.')
                                return None
                        else:
                            print(f'Error (BLOCK): It was expected an "end".')
                            return None
                    else:
                        print(f'Error (BLOCK): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (BLOCK): It was expected a ";".')
                    return None
            elif self.tokenList[self.index]['type'] == 'COLON':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.command()
                return ('BLOCK', (node0, node1))
            else:
                print(f'Error (BLOCK): It was expected a "begin" or ":" on line {self.tokenList[self.index]["line"]}.')
                return None
        return None
    
    def command_list(self):
        node0 = self.command()
        if node0 != None:
            if self.index < len(self.tokenList):
                if self.tokenList[self.index]['type'] == 'SEMICOLON':
                    node1 = self.tokenList[self.index]
                    self.index = self.index + 1
                    node2 = self.command_list()
                    return ('COMMAND_LIST', (node0, node1, node2))
                else:
                    print(f'Error (COMMAND_LIST): It was expected a ";" on line {self.tokenList[self.index]["line"]}.')
                    return None
            else:
                print(f'Error (COMMAND_LIST): It was expected a ";".')
                return None
        else:
            return None
    
    def command(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.name()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'ATRIBUTION':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.mathematical_expression()
                        return ('COMMAND', (node0, node1, node2, node3))
                    else:
                        print(f'Error (COMMAND): It was expected a ":=" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (COMMAND): It was expected a ":=".')
                    return None
            elif self.tokenList[self.index]['type'] == 'WHILE':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.logical_expression()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'DO':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.block()
                        return ('COMMAND', (node0, node1, node2, node3))
                    else:
                        print(f'Error (COMMAND): It was expected a "do" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (COMMAND): It was expected a "do".')
                    return None
            elif self.tokenList[self.index]['type'] == 'IF':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.logical_expression()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'THEN':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node3 = self.block()
                        node4 = self.else_r()
                        return ('COMMAND', (node0, node1, node2, node3, node4))
                    else:
                        print(f'Error (COMMAND): It was expected a "then" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (COMMAND): It was expected a "then".')
                    return None
            elif self.tokenList[self.index]['type'] == 'RETURN':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.logical_expression()
                return ('COMMAND', (node0, node1))
            elif self.tokenList[self.index]['type'] == 'WRITE':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.mathematical_expression()
                return ('COMMAND', (node0, node1))
            elif self.tokenList[self.index]['type'] == 'READ':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'ID':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.name()
                        return ('COMMAND', (node0, node1, node2))
                    else:
                        print(f'Error (COMMAND): It was expected aN "id" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (COMMAND): It was expected aN "id".')
                    return None
            else:
                print(f'Error (COMMAND): It was expected an "id", "while", "if", "return", "write" or "read" on line {self.tokenList[self.index]["line"]}.')
                return None
        return None
    
    def else_r(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ELSE':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.block()
                return ('ELSE_R', (node0, node1))
            else:
                return None
        return None
    
    def parameter_list(self):
        node0 = self.parameter()
        if node0 != None:
            if self.index < len(self.tokenList):
                if self.tokenList[self.index]['type'] == 'COMMA':
                    node1 = self.tokenList[self.index]
                    self.index = self.index + 1
                    node2 = self.parameter_list()
                    return ('PARAMETER_LIST', (node0, node1, node2))
                else:
                    return ('PARAMETER_LIST', (node0))
            else:
                return None
        else:
            return None
    
    def logical_expression(self):
        node0 = self.mathematical_expression()
        node1 = self.tokenList[self.index]
        if node1['type'] == 'LOGICAL_OPERATOR':
            self.index = self.index + 1
            node2 = self.logical_expression()
            return ('LOGICAL_EXPRESSION', (node0, node1, node2))
        else:
            return ('LOGICAL_EXPRESSION', (node0))
    
    def mathematical_expression(self):
        node0 = self.parameter()
        node1 = self.tokenList[self.index]
        if node1['type'] == 'MATHEMATICAL_OPERATOR':
            self.index = self.index + 1
            node2 = self.mathematical_expression()
            return ('MATHEMATICAL_EXPRESSION', (node0, node1, node2))
        else:
            return ('MATHEMATICAL_EXPRESSION', (node0))
    
    def parameter(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'ID':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.name()
                return ('PARAMETER', (node0, node1))
            elif self.tokenList[self.index]['type'] == 'NUMBER':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                return ('PARAMETER', (node0))
            else:
                print(f'Error (PARAMETER): It was expected an "id" or "number" on line {self.tokenList[self.index]["line"]}.')
                return None
        return None
    
    def name(self):
        if self.index < len(self.tokenList):
            if self.tokenList[self.index]['type'] == 'FULL_POINT':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'ID':
                        node1 = self.tokenList[self.index]
                        self.index = self.index + 1
                        node2 = self.name()
                        return ('NAME', (node0, node1, node2))
                    else:
                        print(f'Error (NAME): It was expected an "id" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (NAME): It was expected an "id".')
                    return None
            elif self.tokenList[self.index]['type'] == 'OPENING_SQUARE_BRACKET':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.parameter()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'CLOSING_SQUARE_BRACKET':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        return ('NAME', (node0, node1, node2))
                    else:
                        print(f'Error (NAME): It was expected an "]" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (NAME): It was expected an "]".')
                    return None
            elif self.tokenList[self.index]['type'] == 'OPENING_ROUND_BRACKET':
                node0 = self.tokenList[self.index]
                self.index = self.index + 1
                node1 = self.parameter_list()
                if self.index < len(self.tokenList):
                    if self.tokenList[self.index]['type'] == 'CLOSING_ROUND_BRACKET':
                        node2 = self.tokenList[self.index]
                        self.index = self.index + 1
                        return ('NAME', (node0, node1, node2))
                    else:
                        print(f'Error (NAME): It was expected an ")" on line {self.tokenList[self.index]["line"]}.')
                        return None
                else:
                    print(f'Error (NAME): It was expected an ")".')
                    return None
            else:
                return None
        return None

parser = Parser(tokenList)

print(parser.parse())