# Generated from tools/antlr/Fcl.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"`\"\4\2\t\2\4\3\t\3\4\4\t\4\3\2\7\2\n\n\2\f\2\16\2\r")
        buf.write(u"\13\2\3\2\3\2\3\3\6\3\22\n\3\r\3\16\3\23\3\4\3\4\5\4")
        buf.write(u"\30\n\4\3\4\7\4\33\n\4\f\4\16\4\36\13\4\3\4\3\4\3\4\2")
        buf.write(u"\2\5\2\4\6\2\2\"\2\13\3\2\2\2\4\21\3\2\2\2\6\25\3\2\2")
        buf.write(u"\2\b\n\5\4\3\2\t\b\3\2\2\2\n\r\3\2\2\2\13\t\3\2\2\2\13")
        buf.write(u"\f\3\2\2\2\f\16\3\2\2\2\r\13\3\2\2\2\16\17\7\2\2\3\17")
        buf.write(u"\3\3\2\2\2\20\22\5\6\4\2\21\20\3\2\2\2\22\23\3\2\2\2")
        buf.write(u"\23\21\3\2\2\2\23\24\3\2\2\2\24\5\3\2\2\2\25\27\7!\2")
        buf.write(u"\2\26\30\7[\2\2\27\26\3\2\2\2\27\30\3\2\2\2\30\34\3\2")
        buf.write(u"\2\2\31\33\7`\2\2\32\31\3\2\2\2\33\36\3\2\2\2\34\32\3")
        buf.write(u"\2\2\2\34\35\3\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2\37 ")
        buf.write(u"\7\27\2\2 \7\3\2\2\2\6\13\23\27\34")
        return buf.getvalue()


class FclParser ( Parser ):

    grammarFileName = "Fcl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"<INVALID>", u"<INVALID>", 
                     u"<INVALID>", u"<INVALID>", u"':'", u"','", u"'.'", 
                     u"'..'", u"'^'", u"'{'", u"'('", u"'-'", u"'%'", u"'+'", 
                     u"'}'", u"')'", u"';'", u"'/'", u"'*'" ]

    symbolicNames = [ u"<INVALID>", u"ABS", u"ACCU", u"ACT", u"AND", u"ASUM", 
                      u"BDIF", u"BSUM", u"COA", u"COSINE", u"COG", u"COGS", 
                      u"COGF", u"COS", u"DEFAULT", u"DEFUZZIFY", u"DMAX", 
                      u"DMIN", u"DSIGM", u"EINSTEIN", u"END_DEFUZZIFY", 
                      u"END_FUNCTION_BLOCK", u"END_FUZZIFY", u"END_RULEBLOCK", 
                      u"END_VAR", u"EXP", u"HAMACHER", u"FUNCTION", u"GAUSS", 
                      u"GAUSS2", u"GBELL", u"FUNCTION_BLOCK", u"FUZZIFY", 
                      u"IF", u"IS", u"LM", u"LN", u"LOG", u"MAX", u"METHOD", 
                      u"MIN", u"NIPMIN", u"NIPMAX", u"MM", u"NC", u"NOT", 
                      u"NSUM", u"OR", u"PROBOR", u"PROD", u"RANGE", u"RM", 
                      u"RULE", u"RULEBLOCK", u"SIGM", u"SIN", u"SINGLETONS", 
                      u"SUM", u"TAN", u"TERM", u"THEN", u"TRAPE", u"TRIAN", 
                      u"TYPE_REAL", u"VAR_INPUT", u"VAR_OUTPUT", u"WITH", 
                      u"WS", u"NEWLINE", u"ASSIGN_OPERATOR", u"COLON", u"COMMA", 
                      u"DOT", u"DOTS", u"HAT", u"LEFT_CURLY", u"LEFT_PARENTHESIS", 
                      u"MINUS", u"PERCENT", u"PLUS", u"RIGHT_CURLY", u"RIGHT_PARENTHESIS", 
                      u"SEMICOLON", u"SLASH", u"STAR", u"REAL", u"COMMENT", 
                      u"COMMENT_C", u"COMMENT_SL", u"ID", u"POINT", u"FCL", 
                      u"VALUE_REAL", u"VALUE_ID", u"ALPHANUM" ]

    RULE_main = 0
    RULE_fcl = 1
    RULE_function_block = 2

    ruleNames =  [ u"main", u"fcl", u"function_block" ]

    EOF = Token.EOF
    ABS=1
    ACCU=2
    ACT=3
    AND=4
    ASUM=5
    BDIF=6
    BSUM=7
    COA=8
    COSINE=9
    COG=10
    COGS=11
    COGF=12
    COS=13
    DEFAULT=14
    DEFUZZIFY=15
    DMAX=16
    DMIN=17
    DSIGM=18
    EINSTEIN=19
    END_DEFUZZIFY=20
    END_FUNCTION_BLOCK=21
    END_FUZZIFY=22
    END_RULEBLOCK=23
    END_VAR=24
    EXP=25
    HAMACHER=26
    FUNCTION=27
    GAUSS=28
    GAUSS2=29
    GBELL=30
    FUNCTION_BLOCK=31
    FUZZIFY=32
    IF=33
    IS=34
    LM=35
    LN=36
    LOG=37
    MAX=38
    METHOD=39
    MIN=40
    NIPMIN=41
    NIPMAX=42
    MM=43
    NC=44
    NOT=45
    NSUM=46
    OR=47
    PROBOR=48
    PROD=49
    RANGE=50
    RM=51
    RULE=52
    RULEBLOCK=53
    SIGM=54
    SIN=55
    SINGLETONS=56
    SUM=57
    TAN=58
    TERM=59
    THEN=60
    TRAPE=61
    TRIAN=62
    TYPE_REAL=63
    VAR_INPUT=64
    VAR_OUTPUT=65
    WITH=66
    WS=67
    NEWLINE=68
    ASSIGN_OPERATOR=69
    COLON=70
    COMMA=71
    DOT=72
    DOTS=73
    HAT=74
    LEFT_CURLY=75
    LEFT_PARENTHESIS=76
    MINUS=77
    PERCENT=78
    PLUS=79
    RIGHT_CURLY=80
    RIGHT_PARENTHESIS=81
    SEMICOLON=82
    SLASH=83
    STAR=84
    REAL=85
    COMMENT=86
    COMMENT_C=87
    COMMENT_SL=88
    ID=89
    POINT=90
    FCL=91
    VALUE_REAL=92
    VALUE_ID=93
    ALPHANUM=94

    def __init__(self, input):
        super(FclParser, self).__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.MainContext, self).__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FclParser.EOF, 0)

        def fcl(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.FclContext)
            else:
                return self.getTypedRuleContext(FclParser.FclContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_main

        def enterRule(self, listener):
            if hasattr(listener, "enterMain"):
                listener.enterMain(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitMain"):
                listener.exitMain(self)




    def main(self):

        localctx = FclParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 9
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.FUNCTION_BLOCK:
                self.state = 6
                self.fcl()
                self.state = 11
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 12
            self.match(FclParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FclContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.FclContext, self).__init__(parent, invokingState)
            self.parser = parser

        def function_block(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Function_blockContext)
            else:
                return self.getTypedRuleContext(FclParser.Function_blockContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_fcl

        def enterRule(self, listener):
            if hasattr(listener, "enterFcl"):
                listener.enterFcl(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFcl"):
                listener.exitFcl(self)




    def fcl(self):

        localctx = FclParser.FclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 15 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 14
                    self.function_block()

                else:
                    raise NoViableAltException(self)
                self.state = 17 
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,1,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Function_blockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Function_blockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_BLOCK(self):
            return self.getToken(FclParser.FUNCTION_BLOCK, 0)

        def END_FUNCTION_BLOCK(self):
            return self.getToken(FclParser.END_FUNCTION_BLOCK, 0)

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def ALPHANUM(self, i=None):
            if i is None:
                return self.getTokens(FclParser.ALPHANUM)
            else:
                return self.getToken(FclParser.ALPHANUM, i)

        def getRuleIndex(self):
            return FclParser.RULE_function_block

        def enterRule(self, listener):
            if hasattr(listener, "enterFunction_block"):
                listener.enterFunction_block(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFunction_block"):
                listener.exitFunction_block(self)




    def function_block(self):

        localctx = FclParser.Function_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 19
            self.match(FclParser.FUNCTION_BLOCK)
            self.state = 21
            _la = self._input.LA(1)
            if _la==FclParser.ID:
                self.state = 20
                self.match(FclParser.ID)


            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.ALPHANUM:
                self.state = 23
                self.match(FclParser.ALPHANUM)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(FclParser.END_FUNCTION_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





