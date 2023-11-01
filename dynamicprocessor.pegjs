Expression
  = head:Term tail:(_ ("+" / "-") _ Term)* {
      return tail.reduce(function(result, element) {
        if (element[1] === "+") { 
          return result + element[3];
        }
        if (element[1] === "-") { 
          return result - element[3];
        }
      }, head);
    }

Term
  = head:Factor tail:(_ ("*" / "/") _ Factor)* {
      return tail.reduce(function(result, element) {
        if (element[1] === "*") { return result * element[3]; }
        if (element[1] === "/") { return result / element[3]; }
      }, head);
    }

Factor
  = "(" _ expr:Expression _ ")" { return expr; }
  / str:String { return str; }
  / int:Integer { return int; }

String "string"
  = "\"" content:$(!"\"" .)* "\"" { return content; }

Integer "integer"
  = _ [0-9]+ { return parseInt(text(), 10); }

_ "whitespace"
  = [ \t\n\r]*
