# Generated from tools/antlr/Fcl.g4 by ANTLR 4.5.3
# encoding: utf-8
from __future__ import print_function
from antlr4 import *
from io import StringIO

def serializedATN():
    with StringIO() as buf:
        buf.write(u"\3\u0430\ud6d1\u8206\uad2d\u4417\uaef1\u8d80\uaadd\3")
        buf.write(u"_f\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4")
        buf.write(u"\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\3\2\7\2\32\n")
        buf.write(u"\2\f\2\16\2\35\13\2\3\2\3\2\3\3\6\3\"\n\3\r\3\16\3#\3")
        buf.write(u"\4\3\4\5\4(\n\4\3\4\7\4+\n\4\f\4\16\4.\13\4\3\4\3\4\3")
        buf.write(u"\5\3\5\3\5\5\5\65\n\5\3\6\3\6\7\69\n\6\f\6\16\6<\13\6")
        buf.write(u"\3\6\3\6\3\7\3\7\3\7\3\7\3\7\5\7E\n\7\3\b\3\b\6\bI\n")
        buf.write(u"\b\r\b\16\bJ\3\b\3\b\3\t\3\t\3\t\7\tR\n\t\f\t\16\tU\13")
        buf.write(u"\t\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3\13")
        buf.write(u"\3\13\3\13\3\f\3\f\3\f\2\2\r\2\4\6\b\n\f\16\20\22\24")
        buf.write(u"\26\2\2d\2\33\3\2\2\2\4!\3\2\2\2\6%\3\2\2\2\b\64\3\2")
        buf.write(u"\2\2\n\66\3\2\2\2\f?\3\2\2\2\16F\3\2\2\2\20N\3\2\2\2")
        buf.write(u"\22X\3\2\2\2\24Z\3\2\2\2\26c\3\2\2\2\30\32\5\4\3\2\31")
        buf.write(u"\30\3\2\2\2\32\35\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2")
        buf.write(u"\34\36\3\2\2\2\35\33\3\2\2\2\36\37\7\2\2\3\37\3\3\2\2")
        buf.write(u"\2 \"\5\6\4\2! \3\2\2\2\"#\3\2\2\2#!\3\2\2\2#$\3\2\2")
        buf.write(u"\2$\5\3\2\2\2%\'\7!\2\2&(\7[\2\2\'&\3\2\2\2\'(\3\2\2")
        buf.write(u"\2(,\3\2\2\2)+\5\b\5\2*)\3\2\2\2+.\3\2\2\2,*\3\2\2\2")
        buf.write(u",-\3\2\2\2-/\3\2\2\2.,\3\2\2\2/\60\7\27\2\2\60\7\3\2")
        buf.write(u"\2\2\61\65\5\n\6\2\62\65\5\16\b\2\63\65\5\20\t\2\64\61")
        buf.write(u"\3\2\2\2\64\62\3\2\2\2\64\63\3\2\2\2\65\t\3\2\2\2\66")
        buf.write(u":\7B\2\2\679\5\f\7\28\67\3\2\2\29<\3\2\2\2:8\3\2\2\2")
        buf.write(u":;\3\2\2\2;=\3\2\2\2<:\3\2\2\2=>\7\32\2\2>\13\3\2\2\2")
        buf.write(u"?@\7[\2\2@A\7H\2\2AB\5\26\f\2BD\7T\2\2CE\5\24\13\2DC")
        buf.write(u"\3\2\2\2DE\3\2\2\2E\r\3\2\2\2FH\7C\2\2GI\5\f\7\2HG\3")
        buf.write(u"\2\2\2IJ\3\2\2\2JH\3\2\2\2JK\3\2\2\2KL\3\2\2\2LM\7\32")
        buf.write(u"\2\2M\17\3\2\2\2NO\7\"\2\2OS\7[\2\2PR\5\22\n\2QP\3\2")
        buf.write(u"\2\2RU\3\2\2\2SQ\3\2\2\2ST\3\2\2\2TV\3\2\2\2US\3\2\2")
        buf.write(u"\2VW\7\30\2\2W\21\3\2\2\2XY\7W\2\2Y\23\3\2\2\2Z[\7\64")
        buf.write(u"\2\2[\\\7G\2\2\\]\7N\2\2]^\7W\2\2^_\7K\2\2_`\7W\2\2`")
        buf.write(u"a\7S\2\2ab\7T\2\2b\25\3\2\2\2cd\7A\2\2d\27\3\2\2\2\13")
        buf.write(u"\33#\',\64:DJS")
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
                      u"VALUE_REAL", u"VALUE_ID" ]

    RULE_main = 0
    RULE_fcl = 1
    RULE_function_block = 2
    RULE_declaration = 3
    RULE_var_input = 4
    RULE_var_def = 5
    RULE_var_output = 6
    RULE_fuzzify_block = 7
    RULE_linguistic_term = 8
    RULE_vrange = 9
    RULE_data_type = 10

    ruleNames =  [ u"main", u"fcl", u"function_block", u"declaration", u"var_input", 
                   u"var_def", u"var_output", u"fuzzify_block", u"linguistic_term", 
                   u"vrange", u"data_type" ]

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
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.FUNCTION_BLOCK:
                self.state = 22
                self.fcl()
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 28
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
            self.state = 31 
            self._errHandler.sync(self)
            _alt = 1
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt == 1:
                    self.state = 30
                    self.function_block()

                else:
                    raise NoViableAltException(self)
                self.state = 33 
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

        def declaration(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.DeclarationContext)
            else:
                return self.getTypedRuleContext(FclParser.DeclarationContext,i)


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
            self.state = 35
            self.match(FclParser.FUNCTION_BLOCK)
            self.state = 37
            _la = self._input.LA(1)
            if _la==FclParser.ID:
                self.state = 36
                self.match(FclParser.ID)


            self.state = 42
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while ((((_la - 32)) & ~0x3f) == 0 and ((1 << (_la - 32)) & ((1 << (FclParser.FUZZIFY - 32)) | (1 << (FclParser.VAR_INPUT - 32)) | (1 << (FclParser.VAR_OUTPUT - 32)))) != 0):
                self.state = 39
                self.declaration()
                self.state = 44
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 45
            self.match(FclParser.END_FUNCTION_BLOCK)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class DeclarationContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.DeclarationContext, self).__init__(parent, invokingState)
            self.parser = parser

        def var_input(self):
            return self.getTypedRuleContext(FclParser.Var_inputContext,0)


        def var_output(self):
            return self.getTypedRuleContext(FclParser.Var_outputContext,0)


        def fuzzify_block(self):
            return self.getTypedRuleContext(FclParser.Fuzzify_blockContext,0)


        def getRuleIndex(self):
            return FclParser.RULE_declaration

        def enterRule(self, listener):
            if hasattr(listener, "enterDeclaration"):
                listener.enterDeclaration(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitDeclaration"):
                listener.exitDeclaration(self)




    def declaration(self):

        localctx = FclParser.DeclarationContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_declaration)
        try:
            self.state = 50
            token = self._input.LA(1)
            if token in [FclParser.VAR_INPUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 47
                self.var_input()

            elif token in [FclParser.VAR_OUTPUT]:
                self.enterOuterAlt(localctx, 2)
                self.state = 48
                self.var_output()

            elif token in [FclParser.FUZZIFY]:
                self.enterOuterAlt(localctx, 3)
                self.state = 49
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

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Var_inputContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR_INPUT(self):
            return self.getToken(FclParser.VAR_INPUT, 0)

        def END_VAR(self):
            return self.getToken(FclParser.END_VAR, 0)

        def var_def(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Var_defContext)
            else:
                return self.getTypedRuleContext(FclParser.Var_defContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_var_input

        def enterRule(self, listener):
            if hasattr(listener, "enterVar_input"):
                listener.enterVar_input(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar_input"):
                listener.exitVar_input(self)




    def var_input(self):

        localctx = FclParser.Var_inputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_var_input)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 52
            self.match(FclParser.VAR_INPUT)
            self.state = 56
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.ID:
                self.state = 53
                self.var_def()
                self.state = 58
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 59
            self.match(FclParser.END_VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_defContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Var_defContext, self).__init__(parent, invokingState)
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

        def enterRule(self, listener):
            if hasattr(listener, "enterVar_def"):
                listener.enterVar_def(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar_def"):
                listener.exitVar_def(self)




    def var_def(self):

        localctx = FclParser.Var_defContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_var_def)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 61
            self.match(FclParser.ID)
            self.state = 62
            self.match(FclParser.COLON)
            self.state = 63
            self.data_type()
            self.state = 64
            self.match(FclParser.SEMICOLON)
            self.state = 66
            _la = self._input.LA(1)
            if _la==FclParser.RANGE:
                self.state = 65
                self.vrange()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Var_outputContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Var_outputContext, self).__init__(parent, invokingState)
            self.parser = parser

        def VAR_OUTPUT(self):
            return self.getToken(FclParser.VAR_OUTPUT, 0)

        def END_VAR(self):
            return self.getToken(FclParser.END_VAR, 0)

        def var_def(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Var_defContext)
            else:
                return self.getTypedRuleContext(FclParser.Var_defContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_var_output

        def enterRule(self, listener):
            if hasattr(listener, "enterVar_output"):
                listener.enterVar_output(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVar_output"):
                listener.exitVar_output(self)




    def var_output(self):

        localctx = FclParser.Var_outputContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_var_output)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 68
            self.match(FclParser.VAR_OUTPUT)
            self.state = 70 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 69
                self.var_def()
                self.state = 72 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==FclParser.ID):
                    break

            self.state = 74
            self.match(FclParser.END_VAR)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Fuzzify_blockContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Fuzzify_blockContext, self).__init__(parent, invokingState)
            self.parser = parser

        def FUZZIFY(self):
            return self.getToken(FclParser.FUZZIFY, 0)

        def ID(self):
            return self.getToken(FclParser.ID, 0)

        def END_FUZZIFY(self):
            return self.getToken(FclParser.END_FUZZIFY, 0)

        def linguistic_term(self, i=None):
            if i is None:
                return self.getTypedRuleContexts(FclParser.Linguistic_termContext)
            else:
                return self.getTypedRuleContext(FclParser.Linguistic_termContext,i)


        def getRuleIndex(self):
            return FclParser.RULE_fuzzify_block

        def enterRule(self, listener):
            if hasattr(listener, "enterFuzzify_block"):
                listener.enterFuzzify_block(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitFuzzify_block"):
                listener.exitFuzzify_block(self)




    def fuzzify_block(self):

        localctx = FclParser.Fuzzify_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_fuzzify_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 76
            self.match(FclParser.FUZZIFY)
            self.state = 77
            self.match(FclParser.ID)
            self.state = 81
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==FclParser.REAL:
                self.state = 78
                self.linguistic_term()
                self.state = 83
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 84
            self.match(FclParser.END_FUZZIFY)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Linguistic_termContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Linguistic_termContext, self).__init__(parent, invokingState)
            self.parser = parser

        def REAL(self):
            return self.getToken(FclParser.REAL, 0)

        def getRuleIndex(self):
            return FclParser.RULE_linguistic_term

        def enterRule(self, listener):
            if hasattr(listener, "enterLinguistic_term"):
                listener.enterLinguistic_term(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitLinguistic_term"):
                listener.exitLinguistic_term(self)




    def linguistic_term(self):

        localctx = FclParser.Linguistic_termContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_linguistic_term)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(FclParser.REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class VrangeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.VrangeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def RANGE(self):
            return self.getToken(FclParser.RANGE, 0)

        def ASSIGN_OPERATOR(self):
            return self.getToken(FclParser.ASSIGN_OPERATOR, 0)

        def LEFT_PARENTHESIS(self):
            return self.getToken(FclParser.LEFT_PARENTHESIS, 0)

        def REAL(self, i=None):
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

        def enterRule(self, listener):
            if hasattr(listener, "enterVrange"):
                listener.enterVrange(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitVrange"):
                listener.exitVrange(self)




    def vrange(self):

        localctx = FclParser.VrangeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_vrange)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 88
            self.match(FclParser.RANGE)
            self.state = 89
            self.match(FclParser.ASSIGN_OPERATOR)
            self.state = 90
            self.match(FclParser.LEFT_PARENTHESIS)
            self.state = 91
            self.match(FclParser.REAL)
            self.state = 92
            self.match(FclParser.DOTS)
            self.state = 93
            self.match(FclParser.REAL)
            self.state = 94
            self.match(FclParser.RIGHT_PARENTHESIS)
            self.state = 95
            self.match(FclParser.SEMICOLON)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx

    class Data_typeContext(ParserRuleContext):

        def __init__(self, parser, parent=None, invokingState=-1):
            super(FclParser.Data_typeContext, self).__init__(parent, invokingState)
            self.parser = parser

        def TYPE_REAL(self):
            return self.getToken(FclParser.TYPE_REAL, 0)

        def getRuleIndex(self):
            return FclParser.RULE_data_type

        def enterRule(self, listener):
            if hasattr(listener, "enterData_type"):
                listener.enterData_type(self)

        def exitRule(self, listener):
            if hasattr(listener, "exitData_type"):
                listener.exitData_type(self)




    def data_type(self):

        localctx = FclParser.Data_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_data_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 97
            self.match(FclParser.TYPE_REAL)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx





