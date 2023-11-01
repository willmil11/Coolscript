//Coolscript by willmil11
// DO NOT EDIT
//

(async function(){
    var easynodes;
    var end = false;
    try{
        easynodes = require("easynodes");
        end = true;
    }
    catch (error){
        console.log("[Coolscript] [Dependencies] Unable to find dependencie \"easynodes\", trying to install...");
        var installer = require("child_process").spawn("npm", ["install", "-g", "easynodes@1.0.1"]);
        //On exit
        installer.on("exit", function(code){
            if(code === 0){
                console.log("[Coolscript] [Dependencies] \"easynodes\" installed successfully!");
                try{
                    easynodes = require("easynodes");
                    end = true;
                }
                catch (error){
                    console.log("[Coolscript] [Dependencies] \"easynodes\" is corrupted.");
                    process.exit(1);
                }
            }
            else{
                console.log("[Coolscript] [Dependencies] \"easynodes\" installation failed!");
                process.exit(1);
            }
        });
    }
    while (end === false){
        await new Promise(function(resolve){setTimeout(resolve, 25)});
    }
    
    //Get args
    var args = process.argv.slice(2);
    var pathtofile = args[0];
    var path = require("path");
    
    //Try to resolve path
    try{
        pathtofile = path.resolve(pathtofile);
    }
    catch (error){
        console.log("[Coolscript] [Path] Bad path, unable to resolve.");
        process.exit(1);
    }
    
    //Check if path exists
    if (!(easynodes.files.exists.sync(pathtofile))){
        console.log("[Coolscript] [Path] Path doesn't exists.");
        process.exit(1);
    }

    //Check if path is a file
    
})();