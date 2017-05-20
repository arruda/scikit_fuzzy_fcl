# Generated from tools/antlr/Fcl.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3_")
        buf.write("U\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\3\2\7\2\26\n\2\f\2\16\2\31\13\2\3")
        buf.write("\2\3\2\3\3\6\3\36\n\3\r\3\16\3\37\3\4\3\4\5\4$\n\4\3\4")
        buf.write("\7\4\'\n\4\f\4\16\4*\13\4\3\4\3\4\3\5\3\5\5\5\60\n\5\3")
        buf.write("\6\3\6\7\6\64\n\6\f\6\16\6\67\13\6\3\6\3\6\3\7\3\7\3\7")
        buf.write("\3\7\3\7\5\7@\n\7\3\b\3\b\6\bD\n\b\r\b\16\bE\3\b\3\b\3")
        buf.write("\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\n\3\n\3\n\2\2\13")
        buf.write("\2\4\6\b\n\f\16\20\22\2\2S\2\27\3\2\2\2\4\35\3\2\2\2\6")
        buf.write("!\3\2\2\2\b/\3\2\2\2\n\61\3\2\2\2\f:\3\2\2\2\16A\3\2\2")
        buf.write("\2\20I\3\2\2\2\22R\3\2\2\2\24\26\5\4\3\2\25\24\3\2\2\2")
        buf.write("\26\31\3\2\2\2\27\25\3\2\2\2\27\30\3\2\2\2\30\32\3\2\2")
        buf.write("\2\31\27\3\2\2\2\32\33\7\2\2\3\33\3\3\2\2\2\34\36\5\6")
        buf.write("\4\2\35\34\3\2\2\2\36\37\3\2\2\2\37\35\3\2\2\2\37 \3\2")
        buf.write("\2\2 \5\3\2\2\2!#\7!\2\2\"$\7[\2\2#\"\3\2\2\2#$\3\2\2")
        buf.write("\2$(\3\2\2\2%\'\5\b\5\2&%\3\2\2\2\'*\3\2\2\2(&\3\2\2\2")
        buf.write("()\3\2\2\2)+\3\2\2\2*(\3\2\2\2+,\7\27\2\2,\7\3\2\2\2-")
        buf.write("\60\5\n\6\2.\60\5\16\b\2/-\3\2\2\2/.\3\2\2\2\60\t\3\2")
        buf.write("\2\2\61\65\7B\2\2\62\64\5\f\7\2\63\62\3\2\2\2\64\67\3")
        buf.write("\2\2\2\65\63\3\2\2\2\65\66\3\2\2\2\668\3\2\2\2\67\65\3")
        buf.write("\2\2\289\7\32\2\29\13\3\2\2\2:;\7[\2\2;<\7H\2\2<=\5\22")
        buf.write("\n\2=?\7T\2\2>@\5\20\t\2?>\3\2\2\2?@\3\2\2\2@\r\3\2\2")
        buf.write("\2AC\7C\2\2BD\5\f\7\2CB\3\2\2\2DE\3\2\2\2EC\3\2\2\2EF")
        buf.write("\3\2\2\2FG\3\2\2\2GH\7\32\2\2H\17\3\2\2\2IJ\7\64\2\2J")
        buf.write("K\7G\2\2KL\7N\2\2LM\7W\2\2MN\7K\2\2NO\7W\2\2OP\7S\2\2")
        buf.write("PQ\7T\2\2Q\21\3\2\2\2RS\7A\2\2S\23\3\2\2\2\n\27\37#(/")
        buf.write("\65?E")
        return buf.getvalue()


class FclParser ( Parser ):

    grammarFileName = "Fcl.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "':'", "','", "'.'", "'..'", 
                     "'^'", "'{'", "'('", "'-'", "'%'", "'+'", "'}'", "')'", 
                     "';'", "'/'", "'*'" ]

    symbolicNames = [ "<INVALID>", "ABS", "ACCU", "ACT", "AND", "ASUM", 
                      "BDIF", "BSUM", "COA", "COSINE", "COG", "COGS", "COGF", 
                      "COS", "DEFAULT", "DEFUZZIFY", "DMAX", "DMIN", "DSIGM", 
                      "EINSTEIN", "END_DEFUZZIFY", "END_FUNCTION_BLOCK", 
                      "END_FUZZIFY", "END_RULEBLOCK", "END_VAR", "EXP", 
                      "HAMACHER", "FUNCTION", "GAUSS", "GAUSS2", "GBELL", 
                      "FUNCTION_BLOCK", "FUZZIFY", "IF", "IS", "LM", "LN", 
                      "LOG", "MAX", "METHOD", "MIN", "NIPMIN", "NIPMAX", 
                      "MM", "NC", "NOT", "NSUM", "OR", "PROBOR", "PROD", 
                      "RANGE", "RM", "RULE", "RULEBLOCK", "SIGM", "SIN", 
                      "SINGLETONS", "SUM", "TAN", "TERM", "THEN", "TRAPE", 
                      "TRIAN", "TYPE_REAL", "VAR_INPUT", "VAR_OUTPUT", "WITH", 
                      "WS", "NEWLINE", "ASSIGN_OPERATOR", "COLON", "COMMA", 
                      "DOT", "DOTS", "HAT", "LEFT_CURLY", "LEFT_PARENTHESIS", 
                      "MINUS", "PERCENT", "PLUS", "RIGHT_CURLY", "RIGHT_PARENTHESIS", 
                      "SEMICOLON", "SLASH", "STAR", "REAL", "COMMENT", "COMMENT_C", 
                      "COMMENT_SL", "ID", "POINT", "FCL", "VALUE_REAL", 
                      "VALUE_ID" ]

    RULE_main = 0
    RULE_fcl = 1
    RULE_function_block = 2
    RULE_declaration = 3
    RULE_var_input = 4
    RULE_var_def = 5
    RULE_var_output = 6
    RULE_vrange = 7
    RULE_data_type = 8

    ruleNames =  [ "main", "fcl", "function_block", "declaration", "var_input", 
                   "var_def", "var_output", "vrange", "data_type" ]

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

    def __init__(self, input:TokenStream):
        super().__init__(input)
        self.checkVersion("4.5.3")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None



    class MainContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(FclParser.EOF, 0)

        def fcl(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.FclContext)
            else:
                return self.getTypedRuleContext(FclParser.FclContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_main

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMain" ):
                listener.enterMain(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMain" ):
                listener.exitMain(self)




    def main(self):

        localctx = FclParser.MainContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_main)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 21
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.FUNCTION_BLOCK:
                self.state = 18
                self.fcl()
                self.state = 23
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 24
            self.match(FclParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class FclContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Function_blockContext)
            else:
                return self.getTypedRuleContext(FclParser.Function_blockContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_fcl

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFcl" ):
                listener.enterFcl(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFcl" ):
                listener.exitFcl(self)




    def fcl(self):

        localctx = FclParser.FclContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_fcl)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 27 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 26
                    self.function_block()

                else:
                    raise NoViableAltException(self)
                self.state = 29 
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

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION_BLOCK(self):
            return self.getToken(FclParser.FUNCTION_BLOCK, 0)

        def END_FUNCTION_BLOCK(self):
            return self.getToken(FclParser.END_FUNCTION_BLOCK, 0)

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def declaration(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(FclParser.DeclarationContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_function_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_block" ):
                listener.enterFunction_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_block" ):
                listener.exitFunction_block(self)




    def function_block(self):

        localctx = FclParser.Function_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_function_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 31
            self.match(FclParser.FUNCTION_BLOCK)
            self.state = 33
            _la = self._input.LA(1)
            if _la==FclParser.ID:
                self.state = 32
                self.match(FclParser.ID)


            self.state = 38
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.VAR_INPUT or _la==FclParser.VAR_OUTPUT:
                self.state = 35
                self.declaration()
                self.state = 40
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 41
            self.match(FclParser.END_FUNCTION_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def var_input(self):
            return self.getTypedRuleContext(FclParser.Var_inputContext,0)


        def var_output(self):
            return self.getTypedRuleContext(FclParser.Var_outputContext,0)


        def getRuleIndex(self):
            return FclParser.RULE_declaration

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDeclaration" ):
                listener.enterDeclaration(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDeclaration" ):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = FclParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 45
            token = self._input.LA(1)
            if token in [FclParser.VAR_INPUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 43
                self.var_input()

            elif token in [FclParser.VAR_OUTPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 44
                self.var_output()

            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_inputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_INPUT(self):
            return self.getToken(FclParser.VAR_INPUT, 0)

        def END_VAR(self):
            return self.getToken(FclParser.END_VAR, 0)

        def var_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Var_defContext)
            else:
                return self.getTypedRuleContext(FclParser.Var_defContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_var_input

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_input" ):
                listener.enterVar_input(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_input" ):
                listener.exitVar_input(self)




    def var_input(self):

        localctx = FclParser.Var_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 47
            self.match(FclParser.VAR_INPUT)
            self.state = 51
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.ID:
                self.state = 48
                self.var_def()
                self.state = 53
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 54
            self.match(FclParser.END_VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_defContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def COLON(self):
            return self.getToken(FclParser.COLON, 0)

        def data_type(self):
            return self.getTypedRuleContext(FclParser.Data_typeContext,0)


        def SEMICOLON(self):
            return self.getToken(FclParser.SEMICOLON, 0)

        def vrange(self):
            return self.getTypedRuleContext(FclParser.VrangeContext,0)


        def getRuleIndex(self):
            return FclParser.RULE_var_def

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_def" ):
                listener.enterVar_def(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_def" ):
                listener.exitVar_def(self)




    def var_def(self):

        localctx = FclParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 56
            self.match(FclParser.ID)
            self.state = 57
            self.match(FclParser.COLON)
            self.state = 58
            self.data_type()
            self.state = 59
            self.match(FclParser.SEMICOLON)
            self.state = 61
            _la = self._input.LA(1)
            if _la==FclParser.RANGE:
                self.state = 60
                self.vrange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_outputContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def VAR_OUTPUT(self):
            return self.getToken(FclParser.VAR_OUTPUT, 0)

        def END_VAR(self):
            return self.getToken(FclParser.END_VAR, 0)

        def var_def(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Var_defContext)
            else:
                return self.getTypedRuleContext(FclParser.Var_defContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_var_output

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVar_output" ):
                listener.enterVar_output(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVar_output" ):
                listener.exitVar_output(self)




    def var_output(self):

        localctx = FclParser.Var_outputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.match(FclParser.VAR_OUTPUT)
            self.state = 65 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 64
                self.var_def()
                self.state = 67 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FclParser.ID):
                    break

            self.state = 69
            self.match(FclParser.END_VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VrangeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(FclParser.RANGE, 0)

        def ASSIGN_OPERATOR(self):
            return self.getToken(FclParser.ASSIGN_OPERATOR, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(FclParser.LEFT_PARENTHESIS, 0)

        def REAL(self, i:int=None):
            if i is None:
                return self.getTokens(FclParser.REAL)
            else:
                return self.getToken(FclParser.REAL, i)

        def DOTS(self):
            return self.getToken(FclParser.DOTS, 0)

        def RIGHT_PARENTHESIS(self):
            return self.getToken(FclParser.RIGHT_PARENTHESIS, 0)

        def SEMICOLON(self):
            return self.getToken(FclParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return FclParser.RULE_vrange

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterVrange" ):
                listener.enterVrange(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitVrange" ):
                listener.exitVrange(self)




    def vrange(self):

        localctx = FclParser.VrangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_vrange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 71
            self.match(FclParser.RANGE)
            self.state = 72
            self.match(FclParser.ASSIGN_OPERATOR)
            self.state = 73
            self.match(FclParser.LEFT_PARENTHESIS)
            self.state = 74
            self.match(FclParser.REAL)
            self.state = 75
            self.match(FclParser.DOTS)
            self.state = 76
            self.match(FclParser.REAL)
            self.state = 77
            self.match(FclParser.RIGHT_PARENTHESIS)
            self.state = 78
            self.match(FclParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TYPE_REAL(self):
            return self.getToken(FclParser.TYPE_REAL, 0)

        def getRuleIndex(self):
            return FclParser.RULE_data_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterData_type" ):
                listener.enterData_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitData_type" ):
                listener.exitData_type(self)




    def data_type(self):

        localctx = FclParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_data_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 80
            self.match(FclParser.TYPE_REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





