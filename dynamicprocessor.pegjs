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
  / num:Number { return num; }

String "string"
  = "\"" content:$(!"\"" .)* "\"" { return content; }

Number "number"
  = _ [0-9]+ ("." [0-9]+)? { return parseFloat(text()); }

_ "whitespace"
  = [ \t\n\r]*