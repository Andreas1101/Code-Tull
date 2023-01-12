using System;
using System.Linq;

namespace ArgsProblem.Tests
{
    public class ValidateArguments
    {
        public int Validate(string[] args)
        {
            if (args == null){
                return 0;
            }

            for(int i = 0; i<args.Length; i = i+2){
                if(args[i].ToLower == "--name"){
                    if(args[i+1] != null && args[i+1].Length >= 3 && args[i+1].Length <= 10){
                        //All okay
                    } else{
                        return -1;
                    }
                }

                if(args[i].ToLower == "--count"){
                    if(args[i+1] != null && int.TryParse(args[i+1], out int x) && x <= 100 && x >= 10){
                        //All okay
                    } else {
                        return -1;
                    }
                }

                if(args[i].ToLower == "--help"){
                    return 1;
                }


            }
            // Console.WriteLine("Sample debug output");
        }
    }
}
