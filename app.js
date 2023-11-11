#!/usr/bin/env node
//Coolscript by willmil11
// DO NOT EDIT
//

var app = async function () {
    var easynodes;
    var end = false;
    try {
        easynodes = require("easynodes");
        end = true;
    }
    catch (error) {
        console.log("[Coolscript] [Dependencies] Unable to find dependencie \"easynodes\", trying to install...");
        var installer = require("child_process").spawn("npm", ["install", "-g", "easynodes@1.0.1"]);
        //On exit
        installer.on("exit", function (code) {
            if (code === 0) {
                console.log("[Coolscript] [Dependencies] \"easynodes\" installed successfully!");
                try {
                    easynodes = require("easynodes");
                    end = true;
                }
                catch (error) {
                    console.log("[Coolscript] [Dependencies] \"easynodes\" is corrupted.");
                    process.exit(1);
                }
            }
            else {
                console.log("[Coolscript] [Dependencies] \"easynodes\" installation failed!");
                process.exit(1);
            }
        });
    }
    while (end === false) {
        await new Promise(function (resolve) { setTimeout(resolve, 25) });
    }
    var dynamicprocessor;
    try {
        dynamicprocessor = require("./dynamicprocessor");
    }
    catch (error) {
        console.log("[Coolscript] [Dependencies] Unable to find dependencie \"dynamicprocessor\", coolscript installation is corrupted.");
        process.exit(1);
    }
    easynodes.init();

    //Get args
    var args = process.argv.slice(2);
    var verbose = false;
    var pathtofile = args[0];
    if (pathtofile === "-v") {
        pathtofile = args[1];
        verbose = true;
    }
    else {
        if (pathtofile === "--verbose") {
            pathtofile = args[1];
            verbose = true;
        }
        else {
            if (args[1] === "-v") {
                verbose = true;
            }
            else {
                if (args[1] === "--verbose") {
                    verbose = true;
                }
            }
        }
    }
    var verboselog = function (operation, message) {
        if (verbose === true) {
            console.log("[Coolscript] [" + operation + "] " + message);
        }
    }
    var path = require("path");

    //Try to resolve path
    try {
        pathtofile = path.resolve(pathtofile);
        verboselog("Path", "Path resolved to \"" + pathtofile + "\"");
    }
    catch (error) {
        console.log("[Coolscript] [Path] Bad path, unable to resolve.");
        process.exit(1);
    }

    //Check if path exists
    if (!(easynodes.files.exists.sync(pathtofile))) {
        console.log("[Coolscript] [Path] Path doesn't exists.");
        process.exit(1);
    }
    else {
        verboselog("Path", "Path exists.");
    }

    //Check if path is a file
    if (!(easynodes.files.getTypeOf.sync(pathtofile) === "File")) {
        console.log("[Coolscript] [Path] Path is not a directory instead of a file.");
        process.exit(1);
    }
    else {
        verboselog("Path", "Path is a file.");
    }

    //Try to read file
    var file;
    try {
        file = `${easynodes.files.read.sync(pathtofile)}`;
        verboselog("File", "File read successfully.");
    }
    catch (error) {
        console.log("[Coolscript] [File] Unable to read file.");
        process.exit(1);
    }

    file = file.split("\n");

    verboselog("Interpreter", "Creating new instance of coolscript interpreter");

    var interpreter = {
        "interpretLine": function (data, scope) {
            //Check if line is empty
            if (data.trim() === "") {
                return;
            }

            //Check if line is a comment
            if (data.trim().startsWith("//")) {
                return;
            }

            var keywords = ["var", "if", "else", "while", "for", "function", "return", "break", "continue"];
            if (!(keywords.includes(data.trim().split(" ")[0]))) {
                interpreter.dynamicprocessor(data, scope);
                return;
            }
            else{
                //If is var
                if (data.trim().startsWith("var ")) {
                    //Variable could be defined as var name = value or var name=value or var name =value or var name= value
                    //Get name and value
                    var name = data.trim().split(" ")[1].split("=")[0];
                    var value = data.trim().split("=")[1].trim();
                    //dynamicprocessor value
                    value = interpreter.dynamicprocessor(value, scope);
                    //Add variable to scope
                    scope.vars.names.push(name);
                    scope.vars.values.push({
                        "type": "string",
                        "data": value
                    });
                    return;
                }
            }
        },
        "dynamicprocessor": function (data, scope) {
            // Get variables of current and parents scopes
            var global = this.scopes.global;
            var currentscope = this.scopes.global;
            var variables = {
                "names": [],
                "values": []
            }

            var analyzescope = function (scope) {
                var variables = {
                    "names": [],
                    "values": []
                }

                var gatherVariablesFromScope = function (scope) {
                    variables.names = variables.names.concat(scope.vars.names);
                    variables.values = variables.values.concat(scope.vars.values);

                    if (scope.conditional) {
                        // Gather variables from conditional scope
                        variables.names = variables.names.concat(analyzescope(scope).names);
                        variables.values = variables.values.concat(analyzescope(scope).values);
                    }

                    // Gather variables from subscopes
                    var i = 0;
                    while (i < scope.subscopes.length) {
                        gatherVariablesFromScope(scope.subscopes[i]);
                        i += 1;
                    }
                }

                gatherVariablesFromScope(scope);

                return variables;
            }

            variables.names = variables.names.concat(analyzescope(scope).names);
            variables.values = variables.values.concat(analyzescope(scope).values);

            // Now, 'variables' contains the names and values of variables from the current scope and its parent scopes.

            //Replace variables names that are not in double quotes by their values
            var ok = false;
            var index = 0;
            while (index < variables.names.length) {
                var indextmp = index
                var regex = new RegExp('\\b' + variables.names[index] + '\\b', 'g');
                data = data.replace(regex, function (match, offset, str, index=indextmp) {
                    var prevChar = str.charAt(offset - 1);
                    var nextChar = str.charAt(offset + match.length);
                    if ((prevChar !== "\"" && nextChar !== "\"") && (prevChar !== "'" && nextChar !== "'")) {
                        var value = variables.values[index].data;
                        if (variables.values[index].type === "string") {
                            return "\"" + value + "\"";
                        }
                        else {
                            if (variables.values[index].type === "number") {
                                return value;
                            }
                            else {
                                if (variables.values[index].type === "boolean") {
                                    return value ? "true" : "false";
                                }
                                else {
                                    if (variables.values[index].type === "function") {
                                        var nextChar = str.charAt(offset + match.length);
                                    
                                        // Check if there is a space after function or a "("
                                        while (nextChar === " ") {
                                            offset += 1;
                                            nextChar = str.charAt(offset + match.length);
                                        }
                                    
                                        // Check if next char is not a "("
                                        if (nextChar !== "(") {
                                            return "\"[Function]\"";
                                        } 
                                        else {
                                            ok = true;
                                            // Remove the "("
										    //ofset doesn't include the "("
										    str = str.slice(0, offset + match.length) + str.slice(offset + match.length + 1);
										    offset -= 1;
										    nextChar = str.charAt(offset);
								            
                                            // Loop until the next , or ")"
                                            var args = [];
                                            var index = 0;
                                            var inQuotes = false; // flag to check if we are inside quotes

                                            while (nextChar !== ")") {
                                                var arg = "";

                                                // Loop until the next , or ")"
                                                while ((nextChar !== "," && nextChar !== ")") || inQuotes) {
                                                    arg += nextChar;
                                                    offset += 1;
                                                    nextChar = str.charAt(offset + match.length);

                                                    // check if we are inside quotes
                                                    if (nextChar === "\"") {
                                                        inQuotes = !inQuotes;
                                                    }

                                                    //If we did all chars function isn't closed throw an error
                                                    if (nextChar === "") {
                                                        console.log("[Coolscript] [Interpreter] Unable to process dynamic data.");
                                                        console.log("[Coolscript] [Interpreter] Error in dynamic data: Function not closed.");
                                                        process.exit(1)
                                                    }
                                                }

                                                args[index] = arg;
                                                index += 1;

                                                // If the next char is a ",", skip it
                                                if (nextChar === "," && !inQuotes) {
                                                    offset += 1;
                                                    nextChar = str.charAt(offset + match.length);
                                                }
                                            }
                                    
                                            // At this point, 'args' array contains the arguments passed to the function
                                    
                                            // Now, you can use 'args' to process the function call
                                    
                                            // For example, you can use dynamicprocessor on each argument, and then execute the function with the processed arguments
										    //If there are no arguments
										    if (args.length === 1 && args[0] === "") {
												var processedArgs = [];
										    }
										    else{
												var processedArgs = args.map(function(arg) {
												    arg = arg.trim();
                                                    return interpreter.dynamicprocessor(arg, scope);
                                                });
										    
										        var processedArgsTmp = [];
										        var index = 0;
								                while (index < processedArgs.length) {
										            processedArgsTmp.push(processedArgs[index]);
				    								index += 1;
					    					    }
						    				    processedArgs = processedArgsTmp;
							    	            processedArgsTmp = null;
											}
                                            
                                            //Run the function
                                            var result = interpreter.runfunction(variables.values[indextmp].data, scope, variables.values[indextmp].functype, processedArgs);
                                            return "\"" + result + "\"";
                                        }
                                    }                                    
                                    else{
                                        return "\"[" + variables.values[index].type + "]\"";
                                    }
                                }
                            }
                        }
                    }
                    else {
                        return match; // Variable name is within quotes, so no replacement
                    }
                });
                index += 1;
            }
            if (ok){
                return;
            }
            var result;
            try {
                result = dynamicprocessor.parse(data);
            }
            catch (error) {
                console.log("[Coolscript] [Interpreter] Unable to process dynamic data.");
                console.log("[Coolscript] [Interpreter] Error in dynamic data: " + error);
                process.exit(1)
            }
            if (!(result === result)) {
                //NaN because NaN is the only value that is not equal to itself
                console.log("[Coolscript] [Interpreter] Unable to process dynamic data.");
                console.log("[Coolscript] [Interpreter] Error in dynamic data: Unauthorized operation.");
                process.exit(1)
            }
            return result;
        },
        "runfunction": function (data, scope, functype, processedArgs) {
            //Create a scope in the scope for the function and set scope to that new scope
            var randomFuncId = Math.random().toString(36).substring(2, 15) + Math.random().toString(36).substring(2, 15);
            var newScope = {
                "id": "function_" + randomFuncId,
                "conditional": false,
                "vars": {
                    "names": [],
                    "values": []
                },
                "subscopes": []
            }
            scope.subscopes.push(newScope);
            scope = newScope;
            var lines = data.split("\n");
            var args = lines[0].slice(0, -1).slice("function(".length).slice(0, -1).split(",");
            var argstmp = [];
            var index = 0;
            while (index < args.length) {
                argstmp.push(args[index].trim());
                index += 1;
            }
            args = argstmp;
            argstmp = null;
            var body = lines.slice(1, -1)
            if (functype === "native") {
                var code = "";
                //Define all arguments as variables
                var index = 0;
                while (index < args.length) {
                    code += "var " + args[index] + " = \"" + processedArgs[index] + "\";\n";
                    index += 1;
                }
                //Add body
                var index = 0;
                while (index < body.length) {
                    code += body[index] + "\n";
                    index += 1;
                }
                eval(code);
                return;
            }
            var result;
            var index = 0;
            while (index < body.length) {
                result = this.interpretLine(body[index], scope);
                if (result){
                    //Hit a return statement
                    return result;
                }
                index += 1;
            }
            if (result == null){
                return {
                    "type": "null",
                    "data": "null"
                }
            }
        },
        "scopes": {
            "global": {
                "id": "global",
                "conditional": false,
                "vars": {
                    "names": ["log"],
                    "values": [{
                        "type": "function",
                        "functype": "native",
                        "data": `function(tolog){
                            console.log(tolog)
                        }`
                    }]
                },
                "subscopes": []
            }
        },
        "current-scope": null
    }
    interpreter["current-scope"] = interpreter.scopes.global;

    var index = 0;
    while (index < file.length) {
        //Interpret line
        var line = file[index];
        interpreter.interpretLine(line, interpreter["current-scope"]);
        index += 1;
    }
}
app()
