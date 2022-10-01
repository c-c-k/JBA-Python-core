## Honest Calculator

###### This is the "Honest Calculator" project from Jet Brains Academies "Python Core" track.

### The project consists of 5 stages:  
#### Stage 1 - Data Collection:  
  * [Copy of stage assignment from Jet Brains Academy.](source_copy/stage_1.html)
  * assignment key steps:  
    * (1) Print welcome message.
      * The welcome message is:  
        _"Enter an equation"_
    * (1) Read a string from input that should represent a simple arithmetic operation.  
       * String should be in the format "x operation y".
       * Operands "x" and "y" should be integers or floats.
       * Operator "operation" should be a single character string that is one of the arithmetic symbols "+,-,*,/".
    * (2) Handle input validation.
      * If either of the "x" and "y" operands is not an integer or a float,  
        print the error message:  
        _"Do you even know what numbers are? Stay focused!"_
      * If the operator is not valid,  
        print the error message:  
        _"Yes ... an interesting math operation. You've slept through all classes, haven't you?"_
      * In either of the above two cases of invalid input, return to step (1) after printing the error message.
    * (3) Finish stage.
      * No need to print anything here.
