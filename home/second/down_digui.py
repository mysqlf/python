#!/usr/bin/env python
# -*- coding: utf-8 -*-
import re
import collections
NUM = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
MINUS = r'(?P<MINUS>-)'
TIMES = r'(?P<TIMES>\*)'
DIVIDE = r'(?P<DIVIDE>/)'
LPAREN = r'(?P<LPAREN>\()'
RPAREN = r'(?P<RPAREN>\))'
WS = r'(?P<WS>\s+)'
master_pat = re.compile('|'.join([NUM, PLUS, MINUS, TIMES,
                                  DIVIDE, LPAREN, RPAREN, WS]))
Token = collections.namedtuple('Token', ['type', 'value'])


def generate_tokens(text):
    scanner = master_pat.scanner(text)
    for m in iter(scanner.match, None):
        tok = Token(m.lastgroup, m.group())
        if tok.type != 'WS':
            yield tok


class ExpressionEvaluator:

    def parse(self, text):
        # 初始化
        self.tokens = generate_tokens(text)
        self.tok = None
        self.nexttok = None
        self._advance()
        return self.expr()
    # 赋值

    def _advance(self):
        'Advance one token ahead'
        self.tok, self.nexttok = self.nexttok, next(self.tokens, None)

    # 判断

    def _accept(self, toktype):
        if self.nexttok and self.nexttok.type == toktype:
            self._advance()
            return True
        else:
            return False

    # 判断抛错
    # 判断下一个运算符是否是预定的运算符
    def _expect(self, toktype):
        if not self._accept(toktype):
            raise SyntaxError('Expected' + toktype)

    # 执行加减计算

    def expr(self):
        exprval = self.term()
        while self._accept('PLUS') or self._accept('MINUS'):
            op = self.tok.type
            # 加减优先级低于乘除,所以先执行右侧的乘除运算
            right = self.term()
            if op == 'PLUS':
                exprval += right
            elif op == 'MINUS':
                exprval -= right
        return exprval

    # 执行乘除计算

    def term(self):
        termval = self.factor()
        while self._accept('TIMES') or self._accept('DIVIDE'):
            op = self.tok.type
            # 乘除优先级低于括号,所以右侧先执行括号内的运算
            right = self.factor()
            if op == 'TIMES':
                termval *= right
            elif op == 'DIVIDE':
                termval /= right
        return termval

    # 括号对称判断

    def factor(self):
        if self._accept('NUM'):
            # 如果是数字返回int数值
            return int(self.tok.value)
        elif self._accept('LPAREN'):
            # 左括号则执行加减计算
            exprval = self.expr()
            # 判断是否有右括号
            self._expect('RPAREN')
            return exprval
        else:
            raise SyntaxError('Expected NUMBER or LPAREN')


def descent_parser():
    e = ExpressionEvaluator()
    print(e.parse('2'))
    print(e.parse('2*(2/3*3)'))
descent_parser()
