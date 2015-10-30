declare
Params = [ident(foo)]
Args = [ident(x1)]
Env = environment()
fun {Test Env Params Args}
   %Env#Params#Args
   case Params of nil then
      case Args of nil then Env end
   [] HP|TP then case Args of HA|TA then
		    %HA#TA#HP#TP
		    local EnvTemp in
		       EnvTemp = {Adjoin Env environment(a:1)}
		       {Test EnvTemp TP TA}
		    end
		 end
   end
end
{Browse {Test Env Params Args}}


