## Honest Calculator

###### This is the "Honest Calculator" project from Jet Brains Academies "Python Core" track.

### The project consists of 5 stages:  

#### Stage 1 - Data Collection:  
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_1.html)
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
      * In either of the above two cases of invalid input, return to step (1) after printing the error message.
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
          * In either of the above two cases of invalid input, return to step (1) after printing the error message.
    * (4) Calculate the expression "x operation y" and store the result, also, handle division by zero if relevant.
      * Do not use builtin function's (e.g. eval) to calculate the input string directly.
      * The result should be stored as a float.
      * In case of division by zero,
        * print the error message:  
          "Yeah... division by zero. Smart move..."
        * Return to step (1) after printing the error message.
    * (5) Print the result.
    * (6) Finish stage 2.

#### Stage 3 - Total recall:
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_3.html)
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
          * If the operator is not valid,
              * print the error message:  
                _"Yes ... an interesting math operation. You've slept through all classes, haven't you?"_
          * In either of the above two cases of invalid input, return to step (2) after printing the error message.
      * (5) Calculate the expression "x operation y" and store the result, also, handle division by zero if relevant.
        * Do not use builtin function's (e.g. eval) to calculate the input string directly.
        * The result should be stored as a float.
        * In case of division by zero,
          * print the error message:  
            "Yeah... division by zero. Smart move..."
          * Return to step (2) after printing the error message.
      * (6) Print the result.
      * (7) Query the user if they want to store the result to memory.
        * The Query message is:  
          "Do you want to store the result? (y / n):"
      * (8) Read and process the users answer.
        * Valid answers are the single character strings "y" or "n".
        * If the answer is "y", assign the value of the result variable to the memory variable.
        * If the answer is invalid, return to step (7).
      * (9) Query the user if they want to do more calculations.
        * The Query message is:  
          "Do you want to continue calculations? (y / n):"
      * (10) Read and process the users answer.
        * Valid answers are the single character strings "y" or "n".
        * If the answer is "y", return to step (2).
        * If the answer is invalid, return to step (9).
    * (11) Finish stage 3.
