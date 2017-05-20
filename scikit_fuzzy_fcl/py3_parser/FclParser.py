# Generated from tools/antlr/Fcl.g4 by ANTLR 4.5.3
# encoding: utf-8
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3_")
        buf.write("v\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16\t")
        buf.write("\16\4\17\t\17\3\2\7\2 \n\2\f\2\16\2#\13\2\3\2\3\2\3\3")
        buf.write("\6\3(\n\3\r\3\16\3)\3\4\3\4\5\4.\n\4\3\4\7\4\61\n\4\f")
        buf.write("\4\16\4\64\13\4\3\4\3\4\3\5\3\5\3\5\5\5;\n\5\3\6\3\6\7")
        buf.write("\6?\n\6\f\6\16\6B\13\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7")
        buf.write("K\n\7\3\b\3\b\6\bO\n\b\r\b\16\bP\3\b\3\b\3\t\3\t\3\t\7")
        buf.write("\tX\n\t\f\t\16\t[\13\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\13\3\13\3\f\3\f\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\16\3\16\3\16\3\16\3\17\3\17\3\17\2\2\20\2\4\6\b\n\f\16")
        buf.write("\20\22\24\26\30\32\34\2\3\4\2WW[[q\2!\3\2\2\2\4\'\3\2")
        buf.write("\2\2\6+\3\2\2\2\b:\3\2\2\2\n<\3\2\2\2\fE\3\2\2\2\16L\3")
        buf.write("\2\2\2\20T\3\2\2\2\22^\3\2\2\2\24d\3\2\2\2\26f\3\2\2\2")
        buf.write("\30h\3\2\2\2\32j\3\2\2\2\34s\3\2\2\2\36 \5\4\3\2\37\36")
        buf.write("\3\2\2\2 #\3\2\2\2!\37\3\2\2\2!\"\3\2\2\2\"$\3\2\2\2#")
        buf.write("!\3\2\2\2$%\7\2\2\3%\3\3\2\2\2&(\5\6\4\2\'&\3\2\2\2()")
        buf.write("\3\2\2\2)\'\3\2\2\2)*\3\2\2\2*\5\3\2\2\2+-\7!\2\2,.\7")
        buf.write("[\2\2-,\3\2\2\2-.\3\2\2\2.\62\3\2\2\2/\61\5\b\5\2\60/")
        buf.write("\3\2\2\2\61\64\3\2\2\2\62\60\3\2\2\2\62\63\3\2\2\2\63")
        buf.write("\65\3\2\2\2\64\62\3\2\2\2\65\66\7\27\2\2\66\7\3\2\2\2")
        buf.write("\67;\5\n\6\28;\5\16\b\29;\5\20\t\2:\67\3\2\2\2:8\3\2\2")
        buf.write("\2:9\3\2\2\2;\t\3\2\2\2<@\7B\2\2=?\5\f\7\2>=\3\2\2\2?")
        buf.write("B\3\2\2\2@>\3\2\2\2@A\3\2\2\2AC\3\2\2\2B@\3\2\2\2CD\7")
        buf.write("\32\2\2D\13\3\2\2\2EF\7[\2\2FG\7H\2\2GH\5\34\17\2HJ\7")
        buf.write("T\2\2IK\5\32\16\2JI\3\2\2\2JK\3\2\2\2K\r\3\2\2\2LN\7C")
        buf.write("\2\2MO\5\f\7\2NM\3\2\2\2OP\3\2\2\2PN\3\2\2\2PQ\3\2\2\2")
        buf.write("QR\3\2\2\2RS\7\32\2\2S\17\3\2\2\2TU\7\"\2\2UY\7[\2\2V")
        buf.write("X\5\22\n\2WV\3\2\2\2X[\3\2\2\2YW\3\2\2\2YZ\3\2\2\2Z\\")
        buf.write("\3\2\2\2[Y\3\2\2\2\\]\7\30\2\2]\21\3\2\2\2^_\7=\2\2_`")
        buf.write("\7[\2\2`a\7G\2\2ab\5\24\13\2bc\7T\2\2c\23\3\2\2\2de\5")
        buf.write("\26\f\2e\25\3\2\2\2fg\5\30\r\2g\27\3\2\2\2hi\t\2\2\2i")
        buf.write("\31\3\2\2\2jk\7\64\2\2kl\7G\2\2lm\7N\2\2mn\7W\2\2no\7")
        buf.write("K\2\2op\7W\2\2pq\7S\2\2qr\7T\2\2r\33\3\2\2\2st\7A\2\2")
        buf.write("t\35\3\2\2\2\13!)-\62:@JPY")
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
    RULE_fuzzify_block = 7
    RULE_linguistic_term = 8
    RULE_membership_function = 9
    RULE_singleton = 10
    RULE_atom = 11
    RULE_vrange = 12
    RULE_data_type = 13

    ruleNames =  [ "main", "fcl", "function_block", "declaration", "var_input", 
                   "var_def", "var_output", "fuzzify_block", "linguistic_term", 
                   "membership_function", "singleton", "atom", "vrange", 
                   "data_type" ]

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
            self.state = 31
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.FUNCTION_BLOCK:
                self.state = 28
                self.fcl()
                self.state = 33
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 34
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
            self.state = 37 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 36
                    self.function_block()

                else:
                    raise NoViableAltException(self)
                self.state = 39 
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
            self.state = 41
            self.match(FclParser.FUNCTION_BLOCK)
            self.state = 43
            _la = self._input.LA(1)
            if _la==FclParser.ID:
                self.state = 42
                self.match(FclParser.ID)


            self.state = 48
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & ((1 << (FclParser.FUZZIFY - 32)) | (1 << (FclParser.VAR_INPUT - 32)) | (1 << (FclParser.VAR_OUTPUT - 32)))) != 0):
                self.state = 45
                self.declaration()
                self.state = 50
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 51
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


        def fuzzify_block(self):
            return self.getTypedRuleContext(FclParser.Fuzzify_blockContext,0)


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
            self.state = 56
            token = self._input.LA(1)
            if token in [FclParser.VAR_INPUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.var_input()

            elif token in [FclParser.VAR_OUTPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.var_output()

            elif token in [FclParser.FUZZIFY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.fuzzify_block()

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
            self.state = 58
            self.match(FclParser.VAR_INPUT)
            self.state = 62
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.ID:
                self.state = 59
                self.var_def()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 65
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
            self.state = 67
            self.match(FclParser.ID)
            self.state = 68
            self.match(FclParser.COLON)
            self.state = 69
            self.data_type()
            self.state = 70
            self.match(FclParser.SEMICOLON)
            self.state = 72
            _la = self._input.LA(1)
            if _la==FclParser.RANGE:
                self.state = 71
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
            self.state = 74
            self.match(FclParser.VAR_OUTPUT)
            self.state = 76 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 75
                self.var_def()
                self.state = 78 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FclParser.ID):
                    break

            self.state = 80
            self.match(FclParser.END_VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fuzzify_blockContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUZZIFY(self):
            return self.getToken(FclParser.FUZZIFY, 0)

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def END_FUZZIFY(self):
            return self.getToken(FclParser.END_FUZZIFY, 0)

        def linguistic_term(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Linguistic_termContext)
            else:
                return self.getTypedRuleContext(FclParser.Linguistic_termContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_fuzzify_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFuzzify_block" ):
                listener.enterFuzzify_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFuzzify_block" ):
                listener.exitFuzzify_block(self)




    def fuzzify_block(self):

        localctx = FclParser.Fuzzify_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fuzzify_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 82
            self.match(FclParser.FUZZIFY)
            self.state = 83
            self.match(FclParser.ID)
            self.state = 87
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.TERM:
                self.state = 84
                self.linguistic_term()
                self.state = 89
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 90
            self.match(FclParser.END_FUZZIFY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Linguistic_termContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def TERM(self):
            return self.getToken(FclParser.TERM, 0)

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def ASSIGN_OPERATOR(self):
            return self.getToken(FclParser.ASSIGN_OPERATOR, 0)

        def membership_function(self):
            return self.getTypedRuleContext(FclParser.Membership_functionContext,0)


        def SEMICOLON(self):
            return self.getToken(FclParser.SEMICOLON, 0)

        def getRuleIndex(self):
            return FclParser.RULE_linguistic_term

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLinguistic_term" ):
                listener.enterLinguistic_term(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLinguistic_term" ):
                listener.exitLinguistic_term(self)




    def linguistic_term(self):

        localctx = FclParser.Linguistic_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_linguistic_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 92
            self.match(FclParser.TERM)
            self.state = 93
            self.match(FclParser.ID)
            self.state = 94
            self.match(FclParser.ASSIGN_OPERATOR)
            self.state = 95
            self.membership_function()
            self.state = 96
            self.match(FclParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Membership_functionContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def singleton(self):
            return self.getTypedRuleContext(FclParser.SingletonContext,0)


        def getRuleIndex(self):
            return FclParser.RULE_membership_function

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMembership_function" ):
                listener.enterMembership_function(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMembership_function" ):
                listener.exitMembership_function(self)




    def membership_function(self):

        localctx = FclParser.Membership_functionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_membership_function)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 98
            self.singleton()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class SingletonContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def atom(self):
            return self.getTypedRuleContext(FclParser.AtomContext,0)


        def getRuleIndex(self):
            return FclParser.RULE_singleton

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingleton" ):
                listener.enterSingleton(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingleton" ):
                listener.exitSingleton(self)




    def singleton(self):

        localctx = FclParser.SingletonContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_singleton)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 100
            self.atom()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class AtomContext(ParserRuleContext):

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def REAL(self):
            return self.getToken(FclParser.REAL, 0)

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def getRuleIndex(self):
            return FclParser.RULE_atom

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtom" ):
                listener.enterAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtom" ):
                listener.exitAtom(self)




    def atom(self):

        localctx = FclParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            _la = self._input.LA(1)
            if not(_la==FclParser.REAL or _la==FclParser.ID):
                self._errHandler.recoverInline(self)
            else:
                self.consume()
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
        self.enterRule(localctx, 24, self.RULE_vrange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 104
            self.match(FclParser.RANGE)
            self.state = 105
            self.match(FclParser.ASSIGN_OPERATOR)
            self.state = 106
            self.match(FclParser.LEFT_PARENTHESIS)
            self.state = 107
            self.match(FclParser.REAL)
            self.state = 108
            self.match(FclParser.DOTS)
            self.state = 109
            self.match(FclParser.REAL)
            self.state = 110
            self.match(FclParser.RIGHT_PARENTHESIS)
            self.state = 111
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
        self.enterRule(localctx, 26, self.RULE_data_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(FclParser.TYPE_REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





