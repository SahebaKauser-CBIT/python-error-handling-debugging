
# Python Error Handling and Debugging

## Introduction

Error handling is an important part of Python programming.
It helps programs handle unexpected situations without
terminating suddenly.

Debugging is the process of identifying and correcting
errors in a program.

## Types of Errors

### 1. Syntax Errors
These occur when Python rules are violated.

Example:
```python
if x > 5
    print(x)
```

The colon is missing.

### 2. Runtime Errors
These occur while a program is running.

Examples:
- ZeroDivisionError
- ValueError
- FileNotFoundError
- TypeError

### 3. Logical Errors
The program executes but produces an incorrect result.

Example:
Using the wrong comparison operator.

## Exception Handling

The try block contains code that may cause an exception.

The except block handles the exception.

The else block executes when no exception occurs.

The finally block executes regardless of whether
an exception occurs.

## Debugging Techniques

1. Read the error message carefully.
2. Identify the line number.
3. Check variable values.
4. Use print statements.
5. Use breakpoints in VS Code.
6. Use Python's pdb debugger.

## Conclusion

Exception handling and debugging improve program
reliability and make programs easier to maintain.
