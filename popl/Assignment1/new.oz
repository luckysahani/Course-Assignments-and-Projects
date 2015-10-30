functor
import
    Browser(browse:Browse)
    System(showInfo:Print)

define
    local Take in
    	fun {Take Xs N}
    		if N < 1 then nil
    		else 
    			case Xs
    			of nil then nil
    			[] H|T then H|{Take T N-1}
    			end
    		end
    	end
%    	{Browse {Take [1 2 3] ~2}}
    end

    local Drop Length in
    	fun {Length Xs}
    		case Xs
    		of nil then 0
    		[] H|T then 1+ {Length T}
    		end
    	end

    	fun {Drop Xs N}
    		if N < 1 then Xs
    		elseif N > {Length Xs} then nil
    		elseif N == {Length Xs} then Xs
    		else {Drop Xs.2 N}
    		end
    	end
%    	{Browse {Drop [1 2 3] 0 }}
    end

    local Merge Length in
    	fun {Merge Xs Ys}
    		if Xs == nil then Ys
    		elseif Ys == nil then Xs
    		else
    			if Xs.1 < Ys.1 then Xs.1 | {Merge Xs.2 Ys}
    			else Ys.1 | {Merge Xs Ys.2}
    			end
    		end
    	end
%    	{Browse {Merge [4 8] [2 3 8 10 11]}}
    end

    local ZipWith BinOp in
    	fun {BinOp A B}
    		A * B
    	end

    	fun {ZipWith BinOp Xs Ys}
    		if Xs == nil then Ys
    		elseif Ys == nil then Xs
    		else
    			{BinOp Xs.1 Ys.1} | {ZipWith BinOp Xs.2 Ys.2}
    		end
    	end

%    	{Browse {ZipWith BinOp [1 2 3 4] [2 3 4 5 6 ]}}
    end

    local F in
        fun {F X}
            2 * X
        end
    	fun {FoldR Listify Xs Identity}
            case Xs
            of nil then Identity
            [] H|T then {Listify H {FoldR Listify T Identity}}
            end
        end
%       to find {Map F Xs}
        {Browse {FoldR fun{$ X Y} {F X} | Y end [1 2 3 4] nil}}        
    end

    local FoldL Subtract in
        fun { Subtract X Y}
            X - Y
        end
        
        fun {FoldL Function X Y}
           case X
           of nil then Y
           [] H|T then {FoldL Function T {Function Y H} }
           end 
        end

%        {Browse {FoldL Subtract [1 2 3] 0}}
    end

    local Sine LazySine H in

        fun {Sine Xi}
            {LazySine Xi Xi 1.0 Xi}
        end

        fun lazy{LazySine Value Prev N X}
            local Curprev = ((Prev*X*X*~1.0)/((2.0*N+1.0)*2.0*N))  in
                Value|{LazySine Value+Curprev Curprev N+1.0 X}
            end
        end

        H = {Sine 0.5}
        {Browse H.2.2.2.2.1}
    end

end
 %           Value|{Sine (Value+ (Prev*X*X*~1)/((2*N+1)*2*(N+1))) (Prev*X*X*~1)/((2*N+1)*2*(N+1)) N+1 X}