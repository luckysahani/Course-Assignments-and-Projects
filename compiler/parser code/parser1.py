#!/usr/bin/env python
<<<<<<< HEAD
=======

import ply.yacc as yacc

from lexer import tokens

>>>>>>> 67777347d7e4bf79e42b481a0f548b4f0a258c75

import ply.yacc as yacc

from lexer import tokens
# TypeSpecifier
# 	: TypeName
# 	| TypeName Dims
# 	;

def p_TypeSpecifier(p):
	''' TypeSpecifier : TypeName
						| TypeName Dims '''


# TypeName
# 	: PrimitiveType
# 	| QualifiedName
# 	;

def p_TypeName(p):
	''' TypeName : PrimitiveType
	| TypeName Dims '''


# ClassNameList
#         : QualifiedName
#         | ClassNameList ',' QualifiedName
# 	;

def p_ClassNameList(p):
	''' ClassNameList : QualifiedName
	| ClassNameList 'COMMA' QualifiedName '''

# PrimitiveType
# 	: BOOLEAN
# 	| CHAR
# 	| BYTE
# 	| SHORT
# 	| INT
# 	| LONG
# 	| FLOAT
# 	| DOUBLE
# 	| VOID
# 	;

def p_PrimitiveType(p):
	''' PrimitiveType : BOOLEAN_CONST
	| CHAR_CONST
	| BYTE
	| SHORT
	| INT_CONST
	| LONG
	| FLOAT_CONST
	| DOUBLE
	| VOID '''

# SemiColons
# 	: ';'
#         | SemiColons ';'
#         ;

# CompilationUnit
# 	: ProgramFile
#         ;

# ProgramFile
# 	: PackageStatement ImportStatements TypeDeclarations
# 	| PackageStatement ImportStatements
# 	| PackageStatement                  TypeDeclarations
# 	|                  ImportStatements TypeDeclarations
# 	| PackageStatement
# 	|                  ImportStatements
# 	|                                   TypeDeclarations
# 	;

# PackageStatement
# 	: PACKAGE QualifiedName SemiColons
# 	;

# TypeDeclarations
# 	: TypeDeclarationOptSemi
# 	| TypeDeclarations TypeDeclarationOptSemi
# 	;

# TypeDeclarationOptSemi
#         : TypeDeclaration
#         | TypeDeclaration SemiColons
#         ;

# ImportStatements
# 	: ImportStatement
# 	| ImportStatements ImportStatement
# 	;

# ImportStatement
# 	: IMPORT QualifiedName SemiColons
# 	| IMPORT QualifiedName '.' '*' SemiColons
# 	;

# QualifiedName
# 	: IDENTIFIER
# 	| QualifiedName '.' IDENTIFIER
# 	;

# TypeDeclaration
# 	: ClassHeader '{' FieldDeclarations '}'
# 	| ClassHeader '{' '}'
# 	;

# ClassHeader
# 	: Modifiers ClassWord IDENTIFIER Extends Interfaces
# 	| Modifiers ClassWord IDENTIFIER Extends
# 	| Modifiers ClassWord IDENTIFIER       Interfaces
# 	|           ClassWord IDENTIFIER Extends Interfaces
# 	| Modifiers ClassWord IDENTIFIER
# 	|           ClassWord IDENTIFIER Extends
# 	|           ClassWord IDENTIFIER       Interfaces
# 	|           ClassWord IDENTIFIER
# 	;

# Modifiers
# 	: Modifier
# 	| Modifiers Modifier
# 	;

def p_Modifiers(p):
	''' Modifiers : Modifier
					| Modifiers Modifier '''
# Modifier
# 	: ABSTRACT
# 	| FINAL
# 	| PUBLIC
# 	| PROTECTED
	# | PRIVATE
	# | STATIC
	# | TRANSIENT
	# | VOLATILE
	# | NATIVE
	# | SYNCHRONIZED
# 	;

def p_Modifier(p):
	''' Modifier : ABSTRACT
					| FINAL
					| PUBLIC
					|PROTECTED
					| PRIVATE
					| STATIC
					| TRANSIENT
					| VOLATILE
					| NATIVE
					| SYNCHRONIZED '''







# ClassWord
# 	: CLASS
# 	| INTERFACE
# 	;

def p_ClassWord(p):
	''' ClassWord : CLASS
					| INTERFACE '''

# Interfaces
# 	: IMPLEMENTS ClassNameList
# 	;

def p_Interfaces(p):
	''' Interfaces : IMPLEMENTS ClassNameList '''

# FieldDeclarations
# 	: FieldDeclarationOptSemi
#         | FieldDeclarations FieldDeclarationOptSemi

def p_FieldDeclarations(p) :
	'''FieldDeclarations : FieldDeclarationOptSemi
        | FieldDeclarations FieldDeclarationOptSemi'''

# FieldDeclarationOptSemi
#         : FieldDeclaration
#         | FieldDeclaration SemiColons

def p_FieldDeclarationOptSemi(p):
	''' FieldDeclarationOptSemi : FieldDeclaration
        | FieldDeclaration SemiColons '''


# FieldDeclaration
# 	: FieldVariableDeclaration ';'
# 	| MethodDeclaration
# 	| ConstructorDeclaration
# 	| StaticInitializer
#         | NonStaticInitializer
#         | TypeDeclaration

def p_FieldDeclaration(p):
	''' FieldDeclaration : FieldVariableDeclaration ';'
						| MethodDeclaration
						| ConstructorDeclaration
						| StaticInitializer
					    | NonStaticInitializer
					    | TypeDeclaration '''

# FieldVariableDeclaration
# 	: Modifiers TypeSpecifier VariableDeclarators
# 	|           TypeSpecifier VariableDeclarators
def p_FieldVariableDeclaration(p):
	''' FieldVariableDeclaration : Modifiers TypeSpecifier VariableDeclarators
	|           TypeSpecifier VariableDeclarators '''

VariableDeclarators
	: VariableDeclarator
	| VariableDeclarators ',' VariableDeclarator
	;

VariableDeclarator
	: DeclaratorName
	| DeclaratorName '=' VariableInitializer
	;

VariableInitializer
	: Expression
	| '{' '}'
        | '{' ArrayInitializers '}'
        ;

ArrayInitializers
	: VariableInitializer
	| ArrayInitializers ',' VariableInitializer
	| ArrayInitializers ','
	;

MethodDeclaration
	: Modifiers TypeSpecifier MethodDeclarator Throws MethodBody
	| Modifiers TypeSpecifier MethodDeclarator        MethodBody
	|           TypeSpecifier MethodDeclarator Throws MethodBody
	|           TypeSpecifier MethodDeclarator        MethodBody
	;

MethodDeclarator
	: DeclaratorName '(' ParameterList ')'
	| DeclaratorName '(' ')'
	| MethodDeclarator OP_DIM
	;

ParameterList
	: Parameter
	| ParameterList ',' Parameter
	;

Parameter
	: TypeSpecifier DeclaratorName
        | FINAL TypeSpecifier DeclaratorName
	;

DeclaratorName
	: IDENTIFIER
        | DeclaratorName OP_DIM
        ;

Throws
	: THROWS ClassNameList
	;

MethodBody
	: Block
	| ';'
	;

ConstructorDeclaration
	: Modifiers ConstructorDeclarator Throws Block
	| Modifiers ConstructorDeclarator        Block
	|           ConstructorDeclarator Throws Block
	|           ConstructorDeclarator        Block
	;

ConstructorDeclarator
	: IDENTIFIER '(' ParameterList ')'
	| IDENTIFIER '(' ')'
	;

StaticInitializer
	: STATIC Block
	;

NonStaticInitializer
        : Block
        ;

Extends
	: EXTENDS TypeName
	| Extends ',' TypeName
	;

Block
	: '{' LocalVariableDeclarationsAndStatements '}'
	| '{' '}'
        ;

LocalVariableDeclarationsAndStatements
	: LocalVariableDeclarationOrStatement
	| LocalVariableDeclarationsAndStatements LocalVariableDeclarationOrStatement
	;

LocalVariableDeclarationOrStatement
	: LocalVariableDeclarationStatement
	| Statement
	;

LocalVariableDeclarationStatement
	: TypeSpecifier VariableDeclarators ';'
        | FINAL TypeSpecifier VariableDeclarators ';'
	;

Statement
	: EmptyStatement
	| LabelStatement
	| ExpressionStatement ';'
        | SelectionStatement
        | IterationStatement
	| JumpStatement
	| GuardingStatement
	| Block
	;

EmptyStatement
	: ';'
        ;

LabelStatement
	: IDENTIFIER ':'
        | CASE ConstantExpression ':'
	| DEFAULT ':'
        ;

ExpressionStatement
	: Expression
	;

SelectionStatement
	: IF '(' Expression ')' Statement
        | IF '(' Expression ')' Statement ELSE Statement
        | SWITCH '(' Expression ')' Block
        ;

IterationStatement
	: WHILE '(' Expression ')' Statement
	| DO Statement WHILE '(' Expression ')' ';'
	| FOR '(' ForInit ForExpr ForIncr ')' Statement
	| FOR '(' ForInit ForExpr         ')' Statement
	;

ForInit
	: ExpressionStatements ';'
	| LocalVariableDeclarationStatement
	| ';'
	;

ForExpr
	: Expression ';'
	| ';'
	;

ForIncr
	: ExpressionStatements
	;

ExpressionStatements
	: ExpressionStatement
	| ExpressionStatements ',' ExpressionStatement
	;

JumpStatement
	: BREAK IDENTIFIER ';'
	| BREAK            ';'
        | CONTINUE IDENTIFIER ';'
	| CONTINUE            ';'
	| RETURN Expression ';'
	| RETURN            ';'
	| THROW Expression ';'
	;

GuardingStatement
	: SYNCHRONIZED '(' Expression ')' Statement
	| TRY Block Finally
	| TRY Block Catches
	| TRY Block Catches Finally
	;

Catches
	: Catch
	| Catches Catch
	;

Catch
	: CatchHeader Block
	;

CatchHeader
	: CATCH '(' TypeSpecifier IDENTIFIER ')'
	| CATCH '(' TypeSpecifier ')'
	;

Finally
	: FINALLY Block
	;

PrimaryExpression
	: QualifiedName
	| NotJustName
	;

NotJustName
	: SpecialName
	| NewAllocationExpression
	| ComplexPrimary
	;

ComplexPrimary
	: '(' Expression ')'
	| ComplexPrimaryNoParenthesis
	;

ComplexPrimaryNoParenthesis
	: LITERAL
	| BOOLLIT
	| ArrayAccess
	| FieldAccess
	| MethodCall
	;

ArrayAccess
	: QualifiedName '[' Expression ']'
	| ComplexPrimary '[' Expression ']'
	;

FieldAccess
	: NotJustName '.' IDENTIFIER
	| RealPostfixExpression '.' IDENTIFIER
        | QualifiedName '.' THIS
        | QualifiedName '.' CLASS
        | PrimitiveType '.' CLASS
	;

MethodCall
	: MethodAccess '(' ArgumentList ')'
	| MethodAccess '(' ')'
	;

MethodAccess
	: ComplexPrimaryNoParenthesis
	| SpecialName
	| QualifiedName
	;

SpecialName
	: THIS
	| SUPER
	| JNULL
	;

ArgumentList
	: Expression
	| ArgumentList ',' Expression
	;

NewAllocationExpression
        : PlainNewAllocationExpression
        | QualifiedName '.' PlainNewAllocationExpression
        ;

PlainNewAllocationExpression
    	: ArrayAllocationExpression
    	| ClassAllocationExpression
    	| ArrayAllocationExpression '{' '}'
    	| ClassAllocationExpression '{' '}'
    	| ArrayAllocationExpression '{' ArrayInitializers '}'
    	| ClassAllocationExpression '{' FieldDeclarations '}'
    	;

ClassAllocationExpression
	: NEW TypeName '(' ArgumentList ')'
	| NEW TypeName '('              ')'
        ;

ArrayAllocationExpression
	: NEW TypeName DimExprs Dims
	| NEW TypeName DimExprs
        | NEW TypeName Dims
	;

DimExprs
	: DimExpr
	| DimExprs DimExpr
	;

DimExpr
	: '[' Expression ']'
	;

Dims
	: OP_DIM
	| Dims OP_DIM
	;

PostfixExpression
	: PrimaryExpression
	| RealPostfixExpression
	;

RealPostfixExpression
	: PostfixExpression OP_INC
	| PostfixExpression OP_DEC
	;

UnaryExpression
	: OP_INC UnaryExpression
	| OP_DEC UnaryExpression
	| ArithmeticUnaryOperator CastExpression
	| LogicalUnaryExpression
	;

LogicalUnaryExpression
	: PostfixExpression
	| LogicalUnaryOperator UnaryExpression
	;

LogicalUnaryOperator
	: '~'
	| '!'
	;

ArithmeticUnaryOperator
	: '+'
	| '-'
	;

CastExpression
	: UnaryExpression
	| '(' PrimitiveTypeExpression ')' CastExpression
	| '(' ClassTypeExpression ')' CastExpression
	| '(' Expression ')' LogicalUnaryExpression
	;

PrimitiveTypeExpression
	: PrimitiveType
        | PrimitiveType Dims
        ;

ClassTypeExpression
	: QualifiedName Dims
        ;

MultiplicativeExpression
	: CastExpression
	| MultiplicativeExpression '*' CastExpression
	| MultiplicativeExpression '/' CastExpression
	| MultiplicativeExpression '%' CastExpression
	;

AdditiveExpression
	: MultiplicativeExpression
        | AdditiveExpression '+' MultiplicativeExpression
	| AdditiveExpression '-' MultiplicativeExpression
        ;

ShiftExpression
	: AdditiveExpression
        | ShiftExpression OP_SHL AdditiveExpression
        | ShiftExpression OP_SHR AdditiveExpression
        | ShiftExpression OP_SHRR AdditiveExpression
	;

RelationalExpression
	: ShiftExpression
        | RelationalExpression '<' ShiftExpression
	| RelationalExpression '>' ShiftExpression
	| RelationalExpression OP_LE ShiftExpression
	| RelationalExpression OP_GE ShiftExpression
	| RelationalExpression INSTANCEOF TypeSpecifier
	;

EqualityExpression
	: RelationalExpression
        | EqualityExpression OP_EQ RelationalExpression
        | EqualityExpression OP_NE RelationalExpression
        ;

AndExpression
	: EqualityExpression
        | AndExpression '&' EqualityExpression
        ;

ExclusiveOrExpression
	: AndExpression
	| ExclusiveOrExpression '^' AndExpression
	;

InclusiveOrExpression
	: ExclusiveOrExpression
	| InclusiveOrExpression '|' ExclusiveOrExpression
	;

ConditionalAndExpression
	: InclusiveOrExpression
	| ConditionalAndExpression OP_LAND InclusiveOrExpression
	;

ConditionalOrExpression
	: ConditionalAndExpression
	| ConditionalOrExpression OP_LOR ConditionalAndExpression
	;

ConditionalExpression
	: ConditionalOrExpression
	| ConditionalOrExpression '?' Expression ':' ConditionalExpression
	;

AssignmentExpression
	: ConditionalExpression
	| UnaryExpression AssignmentOperator AssignmentExpression
	;

AssignmentOperator
	: '='
	| ASS_MUL
	| ASS_DIV
	| ASS_MOD
	| ASS_ADD
	| ASS_SUB
	| ASS_SHL
	| ASS_SHR
	| ASS_SHRR
	| ASS_AND
	| ASS_XOR
	| ASS_OR
	;

Expression
	: AssignmentExpression
        ;

ConstantExpression
	: ConditionalExpression
	;

	
#---------------------------------------------------------------------------------------------------------
#Parser
parser = yacc.yacc()

while True:
   try:
       s = raw_input('Input:')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print result
