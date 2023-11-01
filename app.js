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
            //Interpret data with scope variables and parents scopes variables and only if scope is reached
            //if ...: <-- Scope global
            //   ... <-- Sub-scope (executed if the if is true)
            //If scope is a conditional scope it's variables are not local to itself

            console.log(this.dynamicprocessor(data, scope));
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

                function gatherVariablesFromScope(scope) {
                    variables.names = variables.names.concat(scope.vars.names);
                    variables.values = variables.values.concat(scope.vars.values);

                    if (scope.conditional) {
                        // Gather variables from conditional scope
                        variables.names = variables.names.concat(analyzescope(scope).names);
                        variables.values = variables.values.concat(analyzescope(scope).values);
                    }

                    // Gather variables from subscopes
                    for (var i = 0; i < scope.subscopes.length; i++) {
                        gatherVariablesFromScope(scope.subscopes[i]);
                    }
                }

                gatherVariablesFromScope(scope);

                return variables;
            }

            variables.names = variables.names.concat(analyzescope(scope).names);
            variables.values = variables.values.concat(analyzescope(scope).values);

            // Now, 'variables' contains the names and values of variables from the current scope and its parent scopes.

            //Replace variables names that are not in double quotes by their values
            var index = 0;
            while (index < variables.names.length) {
                var regex = new RegExp('\\b' + variables.names[index] + '\\b', 'g');
                data = data.replace(regex, function (match, offset, str) {
                    var prevChar = str.charAt(offset - 1);
                    var nextChar = str.charAt(offset + match.length);
                    if ((prevChar !== '"' && nextChar !== '"') && (prevChar !== "'" && nextChar !== "'")) {
                        var value = variables.values[index].data;
                        if (variables.values[index].type === 'string') {
                            return '"' + value + '"';
                        } else if (variables.values[index].type === 'number') {
                            return value;
                        } else if (variables.values[index].type === 'boolean') {
                            return value ? 'true' : 'false';
                        } else {
                            // Handle other types as needed
                            return '[' + variables.values[index].type + ']';
                        }
                    } else {
                        return match; // Variable name is within quotes, so no replacement
                    }
                });
                index += 1;
            }
            var result;
            try{
                result = dynamicprocessor.parse(data);
            }
            catch (error){
                console.log("[Coolscript] [Interpreter] Unable to process dynamic data.");
                console.log("[Coolscript] [Interpreter] Error in dynamic data: " + error);
                process.exit(1)
            }
            if (!(result === result)){
                //NaN because NaN is the only value that is not equal to itself
                console.log("[Coolscript] [Interpreter] Unable to process dynamic data.");
                console.log("[Coolscript] [Interpreter] Error in dynamic data: Unauthorized operation.");
                process.exit(1)
            }
            return result;
        },
        "scopes": {
            "global": {
                "id": "global",
                "conditional": false,
                "vars": {
                    "names": ["stuff"],
                    "values": [{
                        "type": "string",
                        "data": "Hello world!"
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