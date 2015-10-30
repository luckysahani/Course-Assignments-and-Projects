%% Unify two expressions.
%% See KLInterpreter for the language used here ("Loz").
%%
%% An expression can be one of:
%%
%% 1. An integer, boolean or atom literal -- literal(42),
%%    literal(t)/literal(f) or literal(foo).
%%
%% 2. A record -- [record label [[feature expression]
%%                               [feature expression] ...]]
%%
%% 3. An identifier -- in this case we look at the encosing
%%    environment and the SAS.

\insert 'SingleAssignmentStore.oz'

declare

%% Replaces every identifier with its key in the SAS store, or with
%% its value, as needed. Remember that the SAS should never know about
%% identifiers, only about other keys.
fun {SubstituteIdentifiers Expression Environment}
  case Expression
  of Head|Tail then
    %% It's a list, so recurse
    {SubstituteIdentifiers Head Environment} |
    {SubstituteIdentifiers Tail Environment}
  [] ident(X) then
    {RetrieveFromSAS Environment.X}
  else
    Expression
  end
end

%% As a first pass, we substitute SAS values for identifiers.
proc {Unify Expression1 Expression2 Environment}
  Expression1S = {SubstituteIdentifiers Expression1 Environment}
  Expression2S = {SubstituteIdentifiers Expression2 Environment}
in
  {UnifySubstituted Expression1S Expression2S nil}
end

%% To make things easier, we guarantee here that if Expression2 is an
%% identifier, then so is Expression1.
proc {UnifySubstituted Expression1 Expression2 UnificationsDone}
  %% A very very simple way to do this is to check if Expression2 is
  %% an identifier. If it is, then reverse the order, otherwise
  %% don't. This is obviously going to work in all cases.
  case Expression2
  of equivalence(_) then
    {UnifyInternal Expression2 Expression1 UnificationsDone}
  else
    {UnifyInternal Expression1 Expression2 UnificationsDone}
  end
end

proc {UnifyInternal Expression1 Expression2 UnificationsDone}
  %% Check if we've already performed this particular unification
  if {List.member [Expression1 Expression2] UnificationsDone} orelse
    {List.member [Expression2 Expression1] UnificationsDone} then
    skip
  else
    UnificationsDoneNow = {List.append UnificationsDone [[Expression1 Expression2]]}
  in
    %% First check if Expression1 is an identifier
    case Expression1
    of equivalence(EqKey1) then
      %% Expression1 is unbound. Don't think, just bind.
      case Expression2
      of equivalence(Y) then
        {BindRefToKeyInSAS EqKey1 Y}
      else
        {BindValueToKeyInSAS EqKey1 Expression2}
      end
    [] literal(X) then
      %% We *know* from Unify that Expression2 is not an identifier. It
      %% is either a literal or a record.
      case Expression2
      of literal(!X) then
        %% !X means that the value of X will be matched. This is fine,
        %% as 2 = 2 is a valid Oz kernel statement.
        skip
      else
        {Raise incompatibleTypes(Expression1 Expression2)}
      end
    [] record|Record1Label|Record1FeaturePairs then
      %% Again, Expression2 is not an identifier. It has to be a literal
      %% or a record.
      case Expression2
      of record|Record2Label|Record2FeaturePairs then
        %% The record labels have to be the same, and so do the feature
        %% pairs.
        if Record1Label == Record2Label andthen {IsAritySame Record1FeaturePairs
                                                 Record2FeaturePairs} then
          %% Unify all the values within
          {List.zip Record1FeaturePairs Record2FeaturePairs
           fun {$ FeaturePair1 FeaturePair2}
             %% In case we've added a few things to the SAS in between...
             Val1 = FeaturePair1.2.1
             Val2 = FeaturePair2.2.1
             RealVal1 RealVal2
           in
             case Val1 of equivalence(X) then
               RealVal1 = {RetrieveFromSAS X}
             else
               RealVal1 = Val1
             end

             case Val2 of equivalence(X) then
               RealVal2 = {RetrieveFromSAS X}
             else
               RealVal2 = Val2
             end

             {UnifySubstituted RealVal1 RealVal2 UnificationsDoneNow}
             unit
           end _}
        else
          {Raise incompatibleTypes(Expression1 Expression2)}
        end
      else
        {Raise incompatibleTypes(Expression1 Expression2)}
      end
    end
  end
end

%% Checks whether the elements of two lists are the same
fun {IsEquivalentList List1 List2}
  {List.all List1 fun {$ X} {List.member X List2} end} andthen
  {List.all List2 fun {$ X} {List.member X List1} end}
end

%% Checks whether the arities are the same
fun {IsAritySame FeaturePairs1 FeaturePairs2}
  FeatureList1 = {List.map FeaturePairs1 fun {$ Pair} Pair.1 end}
  FeatureList2 = {List.map FeaturePairs2 fun {$ Pair} Pair.1 end}
in
  {IsEquivalentList FeatureList1 FeatureList2}
end
