	local GameOutcome Position CheckVictoryVal CheckVictory GetRow GetCellVal GetValue in

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
		Position = [['x' 'x' 'x'] ['s' 's' 'x'] ['o' 'x' 'o']]
%		{Browse {GetValue Position 2 2 }}
		

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
%		{Browse {CheckVictoryVal Position 'o'}}

		fun {GameOutcome List}
		   if {CheckVictoryVal List 'o'} then "OWins"
		   elseif {CheckVictoryVal List 'x'} then "XWins"
			else
			   "MatchDraws"
			end
		end
		{Browse {GameOutcome Position}}
	end