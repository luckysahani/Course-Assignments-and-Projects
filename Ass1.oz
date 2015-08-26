functor
import
	Browser(browse:Browse)
	System(showInfo:Print)

define
	%% 1.1 %%
	local Take in   
		fun {Take Xs N}
			if N<1 then nil
			else
				case Xs
				of nil then nil
				[] H|T then H|{Take
					     T N-1}
				end
			end
		end
	%{Browse {Take [1 2 3 4] 2}}
	end

	%% 1.2 %%
	local Drop ListLength Length in
		fun{Length Xs}
			case Xs
			of nil then 0
			[] H|T then 1+{Length T}
			end
		end
		fun {Drop Xs N}
			if N<1 then Xs
			elseif N>{Length Xs} then nil
			elseif N=={Length Xs} then Xs
			else {Drop Xs.2 N}
			end
		end
		%{Browse {Drop [1 2 3 4] 3}}
	end

	%% 1.3 %%
	local Merge in
		fun {Merge Xs Xr}
			if Xs == nil then Xr
			elseif Xr == nil then Xs
			elseif Xs.1 < Xr.1 then Xs.1|{Merge Xs.2 Xr}
			else Xr.1|{Merge Xs Xr.2}
			end
		end
		%{Browse {Merge [1 2 5 9] [3 4 6 10]}}
	end

	%% 2.1 %%
	local ZipWith Add in
		fun {ZipWith BinOp Xs Ys}
			if (Xs == nil) then nil
			elseif (Ys == nil) then nil
			else
				{BinOp Xs.1 Ys.1}|{ZipWith BinOp Xs.2 Ys.2}
			end
		end
		% fun {Add A B}
		% 	A+B
		% end
		% {Browse {ZipWith Add [1 2 5 9] [3 4 6 10]}}
	end

	%% 2.2 %%
	local Map FoldR Add2 in
		fun {FoldR BinOp Xs Identity}
			case Xs
			of nil then Identity
			[] H|T then {BinOp H {FoldR BinOp T Identity }}
			end
		end
		% fun {Map FoldR F Xs Identity}
		% 	case Xs
		% 	of nil then nil
		% 	[] H|T then {{FoldR fun{$ A B}{F A}end H Identity} | {Map FoldR F T Identity}}
		% 	end
		% end
		fun {Add2 A}
			A+2
		end
		%{Browse {Map FoldR Add2 [1 2 5 9] 0}}
	end

	%% 2.3 %%
	local Map FoldL Add in
		fun {FoldL BinOp Xs Identity}
			case Xs
			of nil then Identity
			[] H|T then {FoldL BinOp T {BinOp Identity H }}
			end
		end
		% fun {Add A B}
		% 	A+B
		% end
		% {Browse {FoldL Add [1 2 5 9] 0}}
	end

end
