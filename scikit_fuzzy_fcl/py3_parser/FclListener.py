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


    # Enter a parse tree produced by FclParser#fuzzify_block.
    def enterFuzzify_block(self, ctx:FclParser.Fuzzify_blockContext):
        pass

    # Exit a parse tree produced by FclParser#fuzzify_block.
    def exitFuzzify_block(self, ctx:FclParser.Fuzzify_blockContext):
        pass


    # Enter a parse tree produced by FclParser#linguistic_term.
    def enterLinguistic_term(self, ctx:FclParser.Linguistic_termContext):
        pass

    # Exit a parse tree produced by FclParser#linguistic_term.
    def exitLinguistic_term(self, ctx:FclParser.Linguistic_termContext):
        pass


    # Enter a parse tree produced by FclParser#membership_function.
    def enterMembership_function(self, ctx:FclParser.Membership_functionContext):
        pass

    # Exit a parse tree produced by FclParser#membership_function.
    def exitMembership_function(self, ctx:FclParser.Membership_functionContext):
        pass


    # Enter a parse tree produced by FclParser#piece_wise_linear.
    def enterPiece_wise_linear(self, ctx:FclParser.Piece_wise_linearContext):
        pass

    # Exit a parse tree produced by FclParser#piece_wise_linear.
    def exitPiece_wise_linear(self, ctx:FclParser.Piece_wise_linearContext):
        pass


    # Enter a parse tree produced by FclParser#singleton.
    def enterSingleton(self, ctx:FclParser.SingletonContext):
        pass

    # Exit a parse tree produced by FclParser#singleton.
    def exitSingleton(self, ctx:FclParser.SingletonContext):
        pass


    # Enter a parse tree produced by FclParser#singletons.
    def enterSingletons(self, ctx:FclParser.SingletonsContext):
        pass

    # Exit a parse tree produced by FclParser#singletons.
    def exitSingletons(self, ctx:FclParser.SingletonsContext):
        pass


    # Enter a parse tree produced by FclParser#points.
    def enterPoints(self, ctx:FclParser.PointsContext):
        pass

    # Exit a parse tree produced by FclParser#points.
    def exitPoints(self, ctx:FclParser.PointsContext):
        pass


    # Enter a parse tree produced by FclParser#atom.
    def enterAtom(self, ctx:FclParser.AtomContext):
        pass

    # Exit a parse tree produced by FclParser#atom.
    def exitAtom(self, ctx:FclParser.AtomContext):
        pass


    # Enter a parse tree produced by FclParser#defuzzify_block.
    def enterDefuzzify_block(self, ctx:FclParser.Defuzzify_blockContext):
        pass

    # Exit a parse tree produced by FclParser#defuzzify_block.
    def exitDefuzzify_block(self, ctx:FclParser.Defuzzify_blockContext):
        pass


    # Enter a parse tree produced by FclParser#defuzzify_item.
    def enterDefuzzify_item(self, ctx:FclParser.Defuzzify_itemContext):
        pass

    # Exit a parse tree produced by FclParser#defuzzify_item.
    def exitDefuzzify_item(self, ctx:FclParser.Defuzzify_itemContext):
        pass


    # Enter a parse tree produced by FclParser#vrange.
    def enterVrange(self, ctx:FclParser.VrangeContext):
        pass

    # Exit a parse tree produced by FclParser#vrange.
    def exitVrange(self, ctx:FclParser.VrangeContext):
        pass


    # Enter a parse tree produced by FclParser#default_value.
    def enterDefault_value(self, ctx:FclParser.Default_valueContext):
        pass

    # Exit a parse tree produced by FclParser#default_value.
    def exitDefault_value(self, ctx:FclParser.Default_valueContext):
        pass


    # Enter a parse tree produced by FclParser#data_type.
    def enterData_type(self, ctx:FclParser.Data_typeContext):
        pass

    # Exit a parse tree produced by FclParser#data_type.
    def exitData_type(self, ctx:FclParser.Data_typeContext):
        pass


