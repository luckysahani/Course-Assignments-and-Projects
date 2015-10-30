\insert 'Unify.oz'
\insert 'ProcessRecords.oz'
declare
SemStack = {NewCell nil}
Program = [localvar ident(x)
	   [bind ident(x)
	    [record literal(a) [[literal(feature1) literal(1)] [literal(feature2) ident(x)]]]
	   ]
	  ]


Environment = environment()
SemStack := {Append [semStmt(Program environment)] @SemStack}

fun {SortRecord Record}
   case Record of [record Label Flist] then
      [record  Label {Map {Canonize {Map Flist fun{$ X} X.1#X.2 end}} fun{$ X} [X.1 X.2] end}
      ]
   else
      raise recordStructureErr(Record) end
   end
end

fun {CreateProcEnv Env Params Args}
   case Params of nil then
      case Args of nil then Env end
   [] HP|TP then case Args of HA|TA then
		    %HA#TA#HP#TP
		    local EnvTemp in
		       case HA of ident(X) then
			  EnvTemp = {Adjoin Env environment(X:{AddKeyToSAS})}
		       end
		       {Browse HP#HA}
		       {Unify HP HA EnvTemp}
		       {CreateProcEnv EnvTemp TP TA}
		    end
		 end
   end
end

fun {FindInList Xs Y}
   case Xs
   of nil then false
   [] H|T then
      if H == Y then true
      else {FindInList T Y}
      end
   end
end

fun {FindClosure Env EnvTemp Args FuncStmt}
   case FuncStmt
   of nil then EnvTemp
   [] ident(H)|T then
      if {FindInList Args ident(H)} == false then
	 if {Value.hasFeature Env H} == true then
	    {FindClosure Env {Adjoin EnvTemp environment(H:Env.H)} Args T}
	 else {FindClosure Env EnvTemp Args T}
	 end
      else {FindClosure Env EnvTemp Args T}
      end
   []H|T then {FindClosure Env EnvTemp Args T}
   end
end


fun {CreatePEnv Env  FList PFList}
   %{Browse 'Entered CreatePEnv'}
   %{Browse FList}
   %{Browse PFList}
   case FList of nil then
      case PFList of nil then Env end
   [] HFList|TFList then case PFList of HPFList|TPFList then
			    if (HFList.1 == HPFList.1) then
			       local EnvTemp in
				  %{Browse HPFList.2.1#Env}
				  case HPFList.2.1 of [ident(X)] then
				     EnvTemp = {Adjoin Env environment(X:{AddKeyToSAS})}
				     %{Browse EnvTemp}
				  else
				     skip
				  end
				  %{Browse 'Unifying'#HFList.2.1.1#HPFList.2.1.1}
				  {Unify HFList.2.1.1 HPFList.2.1.1 EnvTemp} 
				  {CreatePEnv EnvTemp TFList TPFList}
			       end
			    else
			       featureUnmatch
			    end
			 end
   end
end

fun {Interpretor}
   % ==========================================
   % Print the execution state
   % Execution State = <semantic stack>,<SAS>
   % ==========================================
   
%   {Browse [@SemStack {Dictionary.entries SAS}]}
   
   local Stmt Env in
      % =======================================
      % Pop top of the semantic stack
      % =======================================
      
      case @SemStack of nil then
	 Stmt = nil
	 Env = nil
      else
	 Stmt = @SemStack.1.1
	 Env = @SemStack.1.2
	 SemStack := @SemStack.2
      end
      {Browse [Stmt  Env {Dictionary.entries SAS}]}
      % ======================================
      % Check the popped statement
      % ======================================
      case Stmt of nil then done

         % ======================================
	 % If top is [nop] then do nothing and
	 % call the Interpretor again
	 % ======================================
	 
      [] nop|nil then
	 % {Browse nop}
	 {Interpretor}

	 % ======================================
	 % If top of stack is variable scope introduction
	 % ======================================

      [] [localvar ident(X) S] then
	 % ======================================
	 % Create new variable X in the store
	 % Push S with new environment and
	 % Increment SASKey
	 % ======================================
	 % {Browse S}
	 SemStack := {Append [semStmt(S {Adjoin Env environment(X:{AddKeyToSAS})})] @SemStack}
	 
	 % ======================================
	 % Continue with interpretor
	 % ======================================
	 
	 {Interpretor}

	 % ======================================
	 % If top of the stack is bind expression
	 % ======================================
	 
      [] [bind Expression1 Expression2] then
	 %{Browse Expression1#Expression2}
	 % ======================================
	 % Unify given expression, trusting
	 % Unify.oz
	 % ======================================
	 case Expression2 of [record Label FList] then
	    {Unify Expression1 {SortRecord Expression2} Env}
	 [] [procedure Arguments ProcStmt] then
	    {Browse 'myclosure'}
	    {Browse {FindClosure Env environment() Arguments {List.flatten ProcStmt}}}
	    {Unify Expression1 procedure(Arguments ProcStmt {FindClosure Env environment() Arguments {List.flatten ProcStmt}}) Env}
	 else
	    {Unify Expression1 Expression2 Env}
	 end
	 {Interpretor}

	 % ======================================
	 % If top of stack is a conditional
	 % ======================================
	 
      [] [conditional ident(X) S1 S2] then
	 local CondVarVal in
	    % ===================================
	    % Retrieve value from store
	    % ===================================
	    CondVarVal = {RetrieveFromSAS Env.X}
	    %{Browse CondVarVal}
	    
	    % ===================================
	    % If value of variable is equivalence(_)
	    % it means that it is unbound.
	    % ===================================
	    case CondVarVal of equivalence(_) then
	       raise unboundCondVar(X) end
	    [] literal(t) then
	       SemStack := {Append [semStmt(S1 Env)] @SemStack}
	    [] literal(f) then
	       SemStack := {Append [semStmt(S2 Env)] @SemStack}
	    else
	       raise illegalCondVar(X) end
	    end
	    {Interpretor}
	 end

	 % ======================================
	 % If top of stack is case stmt
	 % ======================================
	 
      [] [match ident(X) P S1 S2] then
	 local MatchVar in
	    MatchVar = {RetrieveFromSAS Env.X}
	    
	    case MatchVar of equivalence(_) then
	       raise unboundMatch(X) end
	       
	    [] [record Label FeatureList] then
	       case P of [record PLabel PFeatureList] then
		  if {And Label==PLabel {Length FeatureList}=={Length PFeatureList}} then
		     local PEnv in
			PEnv = {CreatePEnv Env FeatureList {Nth {SortRecord [record PLabel PFeatureList]} 3}}
			if PEnv \= featureUnmatch then
			   SemStack := {Append [semStmt(S1 PEnv)] @SemStack}
			else
			   SemStack := {Append [semStmt(S2 Env)] @SemStack}
			end
		     end
		  else
		     SemStack := {Append [semStmt(S2 Env)] @SemStack}
		  end
	       else
		  SemStack := {Append [semStmt(S2 Env)] @SemStack}
	       end
	    else
	       raise recordStuctureErr(MatchVar) end 
	    end
	 end
	 {Interpretor}

      [] apply|ident(ProcName)|Params then
	 local ProcVal in
	    ProcVal = {RetrieveFromSAS Env.ProcName}
	    case ProcVal
	    of procedure(Arguments ProcStmt ProcEnv) then
	       if {Length Params} == {Length Arguments} then
		  local TempEnv in
		     {Browse 'iniEnv'#ProcEnv}
		     TempEnv = {CreateProcEnv ProcEnv Params Arguments}
		     {Browse 'tempEnv'#TempEnv}
		     SemStack:= {Append [semStmt(ProcStmt TempEnv)] @SemStack}
		  end
	       else raise procArityMismatch(ProcName Params) end
	       end
	    else raise unknownProcedure(ProcName)
		 end
	    end
	 end
	 {Interpretor}
	 
	 % ======================================
	 % If stack is of the form <S1> <S2> then
	 % ======================================
	 
      [] S1|S2 then
	 % ======================================
	 % Push S2 on stack
	 % ======================================
	 
	 case S2 of nil then skip
	 else
	    SemStack := {Append [semStmt(S2 Env)] @SemStack}
	 end

	 % ======================================
	 % Push S1 on stack
	 % ======================================
	 SemStack := {Append [semStmt(S1 Env)] @SemStack}

	 % ======================================
	 % Call the interpretor again
	 % ======================================
	 {Interpretor}
      else
	 Stmt
	 
      end
   end
end

{Browse 'Starting Interpretor'}
try
   {Browse {Interpretor}}
catch Err then
   case Err of unboundCondVar(X) then {Browse X}{Browse 'Unbound variable in conditional statement.'}
   [] illegalCondVar(X) then {Browse X}{Browse 'Illegal conditional variable.'}
   [] unboundMatch(X) then {Browse X}{Browse 'Unbound variable in case statement.'}
   [] recordStructureErr(X) then {Browse X}{Browse 'Unexpected record structure.'}
   [] recordFeatureMismatch(X Y) then {Browse X#Y}{Browse 'Feature of given records do not match.'}
   [] procArityMismatch(X Y) then {Browse X#Y}{Browse 'The arity of given procedure and arguments does not match.'}
   [] unknownProcedure(X) then {Browse X}{Browse 'Unknown procedure call.'}
      
   else {Browse 'Unknown exception.'}
   end{Browse 'Quitting program due to error.'}
end
{Browse 'Program succesfully terminated'}
