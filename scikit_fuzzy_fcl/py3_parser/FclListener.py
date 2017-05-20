# Generated from tools/antlr/Fcl.g4 by ANTLR 4.5.3
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .FclParser import FclParser
else:
    from FclParser import FclParser

# This class defines a complete listener for a parse tree produced by FclParser.
class FclListener(ParseTreeListener):

    # Enter a parse tree produced by FclParser#main.
    def enterMain(self, ctx:FclParser.MainContext):
        pass

    # Exit a parse tree produced by FclParser#main.
    def exitMain(self, ctx:FclParser.MainContext):
        pass


    # Enter a parse tree produced by FclParser#fcl.
    def enterFcl(self, ctx:FclParser.FclContext):
        pass

    # Exit a parse tree produced by FclParser#fcl.
    def exitFcl(self, ctx:FclParser.FclContext):
        pass


    # Enter a parse tree produced by FclParser#function_block.
    def enterFunction_block(self, ctx:FclParser.Function_blockContext):
        pass

    # Exit a parse tree produced by FclParser#function_block.
    def exitFunction_block(self, ctx:FclParser.Function_blockContext):
        pass


    # Enter a parse tree produced by FclParser#declaration.
    def enterDeclaration(self, ctx:FclParser.DeclarationContext):
        pass

    # Exit a parse tree produced by FclParser#declaration.
    def exitDeclaration(self, ctx:FclParser.DeclarationContext):
        pass


    # Enter a parse tree produced by FclParser#var_input.
    def enterVar_input(self, ctx:FclParser.Var_inputContext):
        pass

    # Exit a parse tree produced by FclParser#var_input.
    def exitVar_input(self, ctx:FclParser.Var_inputContext):
        pass


    # Enter a parse tree produced by FclParser#var_def.
    def enterVar_def(self, ctx:FclParser.Var_defContext):
        pass

    # Exit a parse tree produced by FclParser#var_def.
    def exitVar_def(self, ctx:FclParser.Var_defContext):
        pass


    # Enter a parse tree produced by FclParser#var_output.
    def enterVar_output(self, ctx:FclParser.Var_outputContext):
        pass

    # Exit a parse tree produced by FclParser#var_output.
    def exitVar_output(self, ctx:FclParser.Var_outputContext):
        pass


    # Enter a parse tree produced by FclParser#vrange.
    def enterVrange(self, ctx:FclParser.VrangeContext):
        pass

    # Exit a parse tree produced by FclParser#vrange.
    def exitVrange(self, ctx:FclParser.VrangeContext):
        pass


    # Enter a parse tree produced by FclParser#data_type.
    def enterData_type(self, ctx:FclParser.Data_typeContext):
        pass

    # Exit a parse tree produced by FclParser#data_type.
    def exitData_type(self, ctx:FclParser.Data_typeContext):
        pass


