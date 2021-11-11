# Anatomy of a compiler

[Compilation Diagram](./static/Anatomy_of_a_compiler/2021-06-06T13:21:22.png)

## Front-End analysis

1.  **Lexical analysis:** Lexical analysis is the process of taking the source code as a stream of characters and splitting it into `tokens` (Tokens are sequences of characters that have a collective meaning.).

2.  **Syntax analysis & Parsing:** Syntax analysis is the process of parsing a sequence of tokens generated in lexical analysis and outputting a `parse-tree` or a `derivation`.

3.  **Semantic Analysis:** In semantic analysis we check the code for non-syntactic but semantic errors. These errors include improper arguments, access violations and undeclared variables. An example of a semantic error is:

    ``` python
    foo = [1,2,3]
    foo + 2 # You can't add an int to a list
    ```

4.  **Intermediate Code Generation:** In this step we create the `intermediate representation` of the source code. Intermediate representation should be easy to generate and translate to the target program. A very common form is the `three-address code(TAC)` which is a sequence of simple instructions with at most three operands.

```
      real code            TAC
      -------------------- ---------------
      a = ( c + b ) \* 2   ~t1~ = c + b
                           a = ~t1~ \* 2
```

## Back-End analysis (Synthesis)

1.  **Intermediate Code Optimisation:** This stage accepts the `intermediate representation` generated in **Intermediate Code Generation** and applies several optimisation techniques to it including but not limited to:
    -   suppressing code generation of unreachable code segments,
    -   ridding of unused variables,
    -   eliminating multiplication by 1 and addition by 0,
    -   loop optimisation (e.g., remove statements that are not modified in the loop),
    -   common sub-expression elimination,
2.  **Object Code Generation:** In this step, the target program gets generated. This step usually outputs either machine code or assembly.
3.  **Object Code Optimisation:** This is a non-mandatory step that processes the machine code generated and applies hardware-specific optimisations such as special instructions, pipelining and branch prediction).

# Lexical Analysis

[Lexical Analysis Diagram](./static/Lexical_Analysis/2021-06-06T13:38:04.png)

A lexical analyser takes a stream of characters and generates tokens as its output. It can recognise particular instances of tokens which are called `lexemes`. A lexeme is the actual sequence forming a token. The scanner's task is to determine the tokens from an input stream but it has no idea where the tokens belong to. Therefore it can only detect errors caused by invalid tokens, it can't detect out of place tokens, mismatched parentheses etc. The lexical analyser is a convenient tool to strip out comments and unnecessary white spaces

## How rules are implemented

When scanning a stream of characters, an analyser might encounter situations where multiple rules match the same string or some rules might match a substring of another rule that matches a longer string. In order to prevent undefined behaviour in those cases, the scanner uses these two principles:

-   If the same string is matched by two or more rules, the rule that was defined first is used.
-   If two strings are matched by the same rule, the longer string is considered to be a lexeme and turned into a token.

## Scanner Implementation with Regular Expressions and Finite Automata

### Important terminology

-   `symbol` an abstract entity that we shall not define formally (such as \"point\" in geometry). Letters, digits and punctuation are examples of symbols.
-   `alphabet` a finite set of symbols out of which we build larger structures, typically denoted by Σ.
-   `formal language Σ*` the set of all possible strings that can be generated from a given alphabet

### From RegEx to Automata

A finite automata can be used to implement scanners in the following manner:

-   The scanner reads the source program one character at a time, changing its state accordingly.
-   The automaton starts from an initial state and makes moves according to the the next character in the stream, changing its state along the way.
-   When the automaton ends up in one of the final states, it makes a move associated with that state, after that, the procedure restarts from the point in the stream that we left off.
-   If an unexpected symbol(a symbol which does not have an action associated with it in our current state) occurs, an error condition is formed.

1.  Nondeterministic Finite Automata

    What sets an NFA different from a Deterministic Finite Automata(DFA) is that a state can have ε moves(moves that don\'t shift the input stream) and multiple moves from the same state that are associated with the same character. These features allow us to more easily generate NFAs from regular expressions.

    An NFA that accepts the RegEx `(0|1)*(000|111)(0|1)*` [RegToNFA](./static/Lexical_Analysis/2021-06-06T19:46:57_RegToNFA.png)

    When generating an NFA from a regular expression, one can follow the following rules:

    -   `Rule 1` An NFA that accepts any symbol from the alphabet

        [NFAR1](./static/Lexical_Analysis/2021-06-06T19:47:14_NFAR1.png)

    -   `Rule 2` An NFA that accepts only ϵ

        [NFAR2](./static/Lexical_Analysis/2021-06-06T19:49:15_NFAR2.png)

    -   `Rule 3` An ϵ NFA that accepts `r1|r2`

        [NFAR3](./static/Lexical_Analysis/2021-06-06T19:51:28_NFAR3.png)

    -   `Rule 4` An ϵ NFA that accepts `r1r2`

        [NFAR4](./static/Lexical_Analysis/2021-06-06T19:53:04_NFAR4.png)

    -   `Rule 5` An ϵ NFA that accepts `r1*`

        [NFAR5](./static/Lexical_Analysis/2021-06-06T19:53:50_NFAR5.png)

2.  Converting from NFA to Deterministic Finite Automata

    In the process of conversion from NFA to DFA we use a technique called `subset construction`. Each state in the resulting DFA is made up of a set of states from the original NFA and it has the same start state and the same alphabets. This means that given a state from the original NFA, an input symbol `x` takes us from our current state to all the possible states we can reach using the x move and ϵ moves. The combined set of all those states form a new state in our DFA. Therefore, each state in our DFA is a subset of S(the set of states in our NFA) so it can have at most $2^n$ states, n being the size of the set S.

# flex Overview

**flex** allows you to specify the scanner you want using patterns to match and actions to apply. It then uses the language you specified to generate and NFA, then converts it into an equivalent DFA and generates C code that implements that automaton. You can learn more about flex [here](http://flex.sourceforge.net/manual/) or by running `info flex`.

## A flex Input File

``` bison
%{
Declarations
%}
Definitions
%%
Rules
%%
User subroutines
```

The optional fields **Declarations** and **User subroutines** sections are copied directly to the generated C. In the **Definitions** field you specify options for the scanner and setup definitions to give names to regular expressions. The only required field, **Rules** allows you to specify patterns that identify your tokens and the actions performed upon recognising. Rules in flex are simply RegEx rules.

## flex Global variables

The **yylex** function is a function that takes no argument and returns an integer, it is the token-grabbing function. Since it returns nothing, it sets global variables that be read by the caller. Here are the global variables it uses:

-   `yytext` is a null-terminated string containing the text of the lexeme just recognised.
-   `yyleng` is an integer holding the length of the lexeme stored in `yytext`
-   `yylval` is the global variable used to store attributes about the token, it is of type YYSTYPE.
-   `yylloc` is the global variable used to store the location of the lexeme
