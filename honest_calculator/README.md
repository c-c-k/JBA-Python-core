## Honest Calculator

###### This is the "Honest Calculator" project from Jet Brains Academies "Python Core" track.

### The project consists of 5 stages:  

#### Stage 1 - Data Collection:  
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_1.html)
  * Stage assignment key steps:  
    * __(1) Print welcome message.__
      * __The welcome message is:__  
        _"Enter an equation"_
    * __(2) Read a string from input that should represent a simple arithmetic operation.__  
       * __String should be in the format "x operation y".__
       * __Operands "x" and "y" should be integers or floats.__
       * __Operator "operation" should be a single character string that is one of the arithmetic symbols "+,-,*,/".__
    * __(3) Handle input validation.__
      * __If either of the "x" and "y" operands is not an integer or a float:__  
        *  __print the error message:__  
          _"Do you even know what numbers are? Stay focused!"_
      * __If the operator is not valid:__  
        * __print the error message:__  
          _"Yes ... an interesting math operation. You've slept through all classes, haven't you?"_
      * __In either of the above two cases of invalid input, return to step (1) after printing the error message.__
    * (4) Finish stage 1.
      * No need to print anything here.

#### Stage 2 - First calculations:
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_2.html)
  * Stage assignment key steps:
      * (1) Print welcome message.
          * The welcome message is:  
            _"Enter an equation"_
      * (2) Read a string from input that should represent a simple arithmetic operation.
          * String should be in the format "x operation y".
          * Operands "x" and "y" should be integers or floats.
          * Operator "operation" should be a single character string that is one of the arithmetic symbols "+,-,*,/".
      * (3) Handle input validation.
          * If either of the "x" and "y" operands is not an integer or a float,
              *  print the error message:  
                 _"Do you even know what numbers are? Stay focused!"_
          * If the operator is not valid,
              * print the error message:  
                _"Yes ... an interesting math operation. You've slept through all classes, haven't you?"_
          * In either of the above two cases of invalid input:
            * return to step (1) after printing the error message.
    * __(4) Calculate the expression "x operation y" and store the result, also, handle division by zero if relevant.__
      * __Do not use builtin function's (e.g. eval) to calculate the input string directly.__
      * __The result should be stored as a float.__
      * __In case of division by zero:__
        * __print the error message:__  
          _"Yeah... division by zero. Smart move..."_
        * __Return to step (1) after printing the error message.__
    * __(5) Print the result.__
    * (6) Finish stage 2.

#### Stage 3 - Total recall:
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_3.html)
  * Stage assignment key steps:
      * __(1) Initialize memory variable.__
      * (2) Print welcome message.
          * The welcome message is:  
            _"Enter an equation"_
      * (2) Read a string from input that should represent a simple arithmetic operation.
          * String should be in the format "x operation y".
          * Operands "x" and "y" should be integers, floats or the one character string "M".
          * Operator "operation" should be a single character string that is one of the arithmetic symbols "+,-,*,/".
      * __(3) Assign value from memory variable to operands if required.__
        * __If the input for operand "x" is "M", assign the value of the memory variable to operand "x".__
        * __If the input for operand "y" is "M", assign the value of the memory variable to operand "y".__
        * __The above options are not exclusive, both operands can be assigned to simultaneously.__
      * (4) Handle input validation.
          * If either of the "x" and "y" operands is not an integer or a float,
              *  print the error message:  
                 _"Do you even know what numbers are? Stay focused!"_
          * If the operator is not valid:
              * print the error message:  
                _"Yes ... an interesting math operation. You've slept through all classes, haven't you?"_
          * In either of the above two cases of invalid input, return to step (2) after printing the error message.
      * (5) Calculate the expression "x operation y" and store the result, also, handle division by zero if relevant.
        * Do not use builtin function's (e.g. eval) to calculate the input string directly.
        * The result should be stored as a float.
        * In case of division by zero:
          * print the error message:  
            _"Yeah... division by zero. Smart move..."_
          * Return to step (2) after printing the error message.
      * (6) Print the result.
      * __(7) Query the user if they want to store the result to memory.__
        * __The Query message is:__  
          _"Do you want to store the result? (y / n):"_
      * __(8) Read and process the users answer.__
        * __Valid answers are the single character strings "y" or "n".__
        * __If the answer is "y", assign the value of the result variable to the memory variable.__
        * __If the answer is invalid, return to step (7).__
      * __(9) Query the user if they want to do more calculations.__
        * __The Query message is:__  
          _"Do you want to continue calculations? (y / n):"_
      * __(10) Read and process the users answer.__
        * __Valid answers are the single character strings "y" or "n".__
        * __If the answer is "y", return to step (2).__
        * __If the answer is invalid, return to step (9).__
    * (11) Finish stage 3.

#### Stage 4 - The laziness test:
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_4.html)
  * Stage assignment key steps:
      * (1) Initialize memory variable.
      * (2) Print welcome message.
          * The welcome message is:  
            _"Enter an equation"_
      * (2) Read a string from input that should represent a simple arithmetic operation.
          * String should be in the format "x operation y".
          * Operands "x" and "y" should be integers, floats or the one character string "M".
          * Operator "operation" should be a single character string that is one of the arithmetic symbols "+,-,*,/".
      * (3) Assign value from memory variable to operands if required.
        * If the input for operand "x" is "M", assign the value of the memory variable to operand "x".
        * If the input for operand "y" is "M", assign the value of the memory variable to operand "y".
        * The above options are not exclusive, both operands can be assigned to simultaneously.
      * (4) Handle input validation.
          * If either of the "x" and "y" operands is not an integer or a float,
              *  print the error message:  
                 _"Do you even know what numbers are? Stay focused!"_
          * If the operator is not valid:
              * print the error message:  
                _"Yes ... an interesting math operation. You've slept through all classes, haven't you?"_
          * In either of the above two cases of invalid input, return to step (2) after printing the error message.
      * __(5) Perform "laziness" tests and build the appropriate "laziness" message (order is the messages construction is important).__
        * __Start with an empty message.__
        * __If both operands are single digit integers,__
          * __Append to the message the sub-message:__  
            _" ... lazy"_
        * __If either of the operands is "1" and the operator is "*",__
            * __Append to the message the sub-message:__  
              _" ... very lazy"_
        * __If either of the operands is "0" and the operator is one of "-+*",__
            * __Append to the message the sub-message:__  
              _" ... very, very lazy"_
        * __If the message is not empty at this point:__
          * __prefix the message with the sub-message:__
            _"You are"_
          * __print the message.__
      * (6) Calculate the expression "x operation y" and store the result, also, handle division by zero if relevant.
        * Do not use builtin function's (e.g. eval) to calculate the input string directly.
        * The result should be stored as a float.
        * In case of division by zero,
          * print the error message:  
            _"Yeah... division by zero. Smart move..."_
          * Return to step (2) after printing the error message.
      * (7) Print the result.
      * (8) Query the user if they want to store the result to memory.
        * The Query message is:  
          _"Do you want to store the result? (y / n):"_
      * (9) Read and process the users answer.
        * Valid answers are the single character strings "y" or "n".
        * If the answer is "y", assign the value of the result variable to the memory variable.
        * If the answer is invalid, return to step (8).
      * (10) Query the user if they want to do more calculations.
        * The Query message is:  
          _"Do you want to continue calculations? (y / n):"_
      * (11) Read and process the users answer.
        * Valid answers are the single character strings "y" or "n".
        * If the answer is "y", return to step (2).
        * If the answer is invalid, return to step (10).
      * (12) Finish stage 4.