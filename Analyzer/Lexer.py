import re
from enum import Enum, auto
from Analyzer.Token import Token


class Lexer:

    identifier_table = {}
    identifier_id_counter = 0

    class TypeToken(Enum):
        IDENTIFIER = auto()
        INTEGER = auto()
        FLOAT = auto()
        OPERATOR = auto()
        FUNCTION = auto()
        KEYWORD = auto()
        ERROR = auto()
        STRING = auto()

    operators = ["+", "-", "*", "/", "==", "!=", ">=", "<=", "<", ">", "+=", "-=", ":"
                 "/=", "*=", "++", "--", "**", "(", ")", "{", "}", "[", "]", ";", "=", ","]
    functions = ['abs', 'all', 'any', 'ascii', 'bin', 'bool', 'range', 'bytearray', 'bytes', 'callable', 'chr',
                 'classmethod', 'compile', 'complex', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec',
                 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id',
                 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'list', 'locals', 'map', 'max',
                 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'range',
                 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum',
                 'super', 'tuple', 'type', 'vars', 'zip']

    keywords = ['and', 'than', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif',
                'else', 'except', 'False', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda',
                'None', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return', 'True', 'try', 'while', 'with', 'yield',
                "ПОБУДУВАТИ", "ПРОВЕСТИ", "СТВОРИТИ", "ПОЗНАЧИТИ", "ВИЗНАЧИТИ", "ПОКАЗАТИ", "ЗОБРАЗИТИ", "ДЕ", "ЧЕРЕЗ",
                "З", "ЗА", "ДО", "ПО"]

    identifier_pattern = re.compile("[А-Яа-яA-Za-zІіЇїҐґ_][А-Яа-яA-Za-zІіЇїҐґ0-9_]*")
    integer_pattern = re.compile("-?\\d+")
    float_pattern = re.compile("-?\\d+\\.\\d+")
    string_pattern = re.compile("\"[^\"]*\"")


    @staticmethod
    def analyze(input_str):
        input_str = input_str.strip()
        identifier_match = Lexer.identifier_pattern.match(input_str)
        integer_match = Lexer.integer_pattern.match(input_str)
        float_match = Lexer.float_pattern.match(input_str)
        string_match = Lexer.string_pattern.match(input_str)

        if identifier_match:
            token_value = identifier_match.group()
            if Lexer.is_keyword(token_value):
                return Token(Lexer.TypeToken.KEYWORD, token_value)
            elif Lexer.is_function(token_value):
                return Token(Lexer.TypeToken.FUNCTION, token_value)
            else:
                return Token(Lexer.TypeToken.IDENTIFIER, token_value)
        elif integer_match:
            return Token(Lexer.TypeToken.INTEGER, integer_match.group())
        elif float_match:
            return Token(Lexer.TypeToken.FLOAT, float_match.group())
        elif string_match:
            return Token(Lexer.TypeToken.STRING, input_str)
        elif Lexer.is_operator(input_str):
            return Token(Lexer.TypeToken.OPERATOR, input_str)
        else:
            return Token(Lexer.TypeToken.ERROR, input_str)

    @staticmethod
    def get_identifier_id(identifier):
        if identifier in Lexer.identifier_table:
            identifier_id = Lexer.identifier_table[identifier]
            return f"{identifier_id:04d}"
        else:
            Lexer.identifier_id_counter += 1
            Lexer.identifier_table[identifier] = Lexer.identifier_id_counter
            return f"{Lexer.identifier_id_counter:04d}"

    @staticmethod
    def is_operator(input_str):
        return input_str in Lexer.operators

    @staticmethod
    def is_function(input_str):
        return input_str in Lexer.functions

    @staticmethod
    def is_keyword(input_str):
        return input_str in Lexer.keywords
