functor
import
    Browser(browse:Browse)
    System(showInfo:Print)

define
%	Tic Tac Toe 1st part
	local GameOutcome Position CheckVictory GetRow GetCellVal GetValue in
		fun {GetCellVal List Yindex}
			if Yindex == 0 then List.1
			else
				case List
				of nil then nil
				[] H|T then {GetCellVal T Yindex-1}
				end
			end
		end
		fun {GetRow List Xindex}
			if Xindex == 0 then List.1
			else
				case List
				of nil then nil
				[] H|T then {GetRow T  Xindex-1}
				end
			end
		end
		fun {GetValue List Xindex Yindex}
			{GetCellVal {GetRow List Xindex} Yindex}
		end
		fun {CheckVictory List Val Xindex Yindex DeltaX DeltaY}
			if Val == 's' then false
			elseif Xindex > 2 then true
			elseif Yindex > 2 then true
			elseif Xindex < 0 then true
			elseif Yindex < 0 then true 
			elseif {GetValue List Xindex Yindex} == Val  then {CheckVictory List Val Xindex+DeltaX Yindex+DeltaY DeltaX DeltaY}
			else
				false
			end
		end
		fun {CheckVictoryVal List Val}
			if {CheckVictory List Val 0 0 0 1} then true
			elseif {CheckVictory List Val 0 0 1 0} then true
			elseif {CheckVictory List Val 0 0 1 1} then true
			elseif {CheckVictory List Val 0 1 1 0} then true
			elseif {CheckVictory List Val 1 0 0 1} then true
			elseif {CheckVictory List Val 0 2 1 0} then true
			elseif {CheckVictory List Val 2 0 0 1} then true
			elseif {CheckVictory List Val 2 0 ~1 1} then true
			else 
				false
			end
		end
		fun {GameOutcome List}
			if {CheckVictoryVal List 'o'} then "O"
			elseif {CheckVictoryVal List 'x'} then "X"
			else
				"Draws"
			end
		end
		Position = [['x' 'x' 'o'] ['s' 's' 'x'] ['o' 'x' 'o']]		
%		{Browse {GameOutcome Position}}
	end

	local GetCellVal GetRow GetValue ListAtIndex PossibleLists in
		fun {GetCellVal List Yindex}
			if Yindex == 0 then List.1
			else
				case List
				of nil then nil
				[] H|T then {GetCellVal T Yindex-1}
				end
			end
		end
		fun {GetRow List Xindex}
			if Xindex == 0 then List.1
			else
				case List
				of nil then nil
				[] H|T then {GetRow T  Xindex-1}
				end
			end
		end
		fun {GetValue List Xindex Yindex}
			{GetCellVal {GetRow List Xindex} Yindex}
		end

		fun {PossibleLists List Val N RetList}
			if N > 8 then RetList
			else
				local Xindex Yindex in
					Xindex = {Int.'div' N 3}
					Yindex = {Int.'mod' N 3}
					if {GetValue List Xindex Yindex} == 's' then {PossibleLists List Val N+1 {ListAtIndex List Xindex Yindex Val}|RetList }
					else {PossibleLists List Val N+1 RetList }
					end
				end
			end
		end

		fun {ListAtIndex List Xindex Yindex Val}
			case List
			of nil then nil
			[] H|T then 
				if Xindex == 0 then
					{ ChangeList H Val Yindex } | T 
				else H | {ListAtIndex T Xindex-1 Yindex Val}
				end
			end
		end

		fun {ChangeList List Val Yindex}
			case List
			of nil then nil
			[] H|T then 
				if Yindex == 0 then Val| T
				else H | {ChangeList T Val Yindex-1}
				end
			end
		end
		{Browse {PossibleLists [['s' 'o' 'o' ] ['o' 's' 'x'] ['x' 's' 'x']] 'x' 0 nil}}
	end
end