# Tracking my refresher course content in Python

## Goal

Refresh general Python fundamentals to sharpen skills already built through BudgetWise and other data projects. Confirm strengths, catch any gaps before moving to advanced automation work.

## Folder Structure

Note: mini-projects built before Aug 16, 2026 sit inside their related concept 
folder. From Aug 17, 2026 onward, new mini-projects go into 06-mini-projects.

```
python-practice/
├── README.md
├── 01-basics/
│   ├── numbers.py
│   ├── strings.py
│   ├── variables.py
│   ├── user_input.py
│   ├── typecasting.py
│   ├── arithmetic_math.py
│   ├── string_indexes.py
│   ├── string_method.py
│   ├── format_specifiers.py
│   ├── random_numbers.py
├── 02-data-structures/
│   ├── lists.py
│   ├── tuples.py
│   ├── sets.py
│   ├── dictionaries.py
│   ├──2D_collection.py
├── 03-control-flow/
│   ├── if_statements.py
│   ├── match.py
│   ├── loops.py
│   ├── loop_clauses.py
│   ├── calculator.py
│   ├── temperature_conversion.py
│   ├── weight_converter.py
│   ├── conditional_expression.py
│   ├── logical_operators.py
│   ├── while_loops.py
│   ├── compound_interest_calculator.py 
│   ├── for_loops.py
│   ├── countdown_timer_program.py
│   ├── nested_loop.py
│   ├── shopping_cart_program.py
│   ├── quiz_game.py
├── 04-modules-and-errors/
│   ├── modules.py
│   └── errors_exceptions.py
├── 05-oop/
│   └── classes.py
└── 06-mini-projects/
│   ├── concession_stand_program.py
│   ├── number_guessing_game.py
│   ├── rock_paper_scissors_game.py
│   ├── dice_roller_program.py
```

## Progress Log

### Aug 5, 2026 - numbers

Refreshed arithmetic operators, floor division, modulus, and exponentiation. Confirmed solid.

### Aug 5, 2026 - lists

Covered indexing, slicing, concatenation, list comprehension, and built-in methods like append and nesting. Confirmed solid.

### Aug 5, 2026 - strings

Reviewed string indexing, slicing, immutability, and format(). Confirmed solid.

### Aug 6, 2026 - tuples

Covered tuple packing, unpacking, immutability, and nesting. Confirmed solid.

### Aug 6, 2026 - sets

Reviewed set uniqueness, membership testing, and set operations like union, intersection, and difference using pipe, ampersand, and caret symbols. Confirmed solid.

### Aug 6, 2026 - dictionaries

Reviewed key:value pairs, indexing by key, dict comprehension, and built-in methods like keys, values, and copy. Confirmed solid.

### Aug 6, 2026 - if_statements

Covered if, elif, else with a simple function example. Confirmed solid, straightforward.

### Aug 6, 2026 - match

New syntax from Python 3.10, not something covered in earlier data project work. Reviewed match with literal patterns, OR patterns using pipe, tuple unpacking patterns, and class pattern matching with dataclass. This one needs more repetition to stick.

### Aug 7, 2026 - loops

Covered for loops over lists and dictionaries, safe dictionary iteration using copy, building a new collection through filtering, and the range function with start, stop, and step. Confirmed solid.

### Aug 7, 2026 - loop_clauses

Covered break, continue, else on loops, and pass as a placeholder for classes and functions. The else on loops was new territory, easy to confuse with if-else at first glance since it only runs when no break occurs. Rest confirmed solid.

### Aug 7, 2026 - modules

Covered importing functions across files to avoid repeating code, the DRY principle, and calling imported functions inside a new script. Confirmed solid.

### Aug 7, 2026 - errors

Covered the difference between syntax errors and exceptions, Python's built-in exception types, handling exceptions with try/except, catching multiple exception types in a tuple, and the else and finally clauses in try statements. Confirmed solid.

### Aug 7, 2026 - classes

Covered class basics, instance creation, init for passing arguments, instance attributes versus class variables, adding and deleting attributes, and inheritance with method overriding using a subclass. Confirmed solid, this is where general programming depth mattered most compared to project work so far.

### Aug 10, 2026 - variables, Bro Code

Reviewed variable containers for strings, integers, floats, and booleans, with f-string formatting and boolean conditionals. Already confirmed solid from earlier fundamentals, no new gaps.

### Aug 10, 2026 - typecasting, Bro Code

Reviewed converting between str, int, float, and bool, including how a non-empty string converts to True and an empty string converts to False, and the TypeError that comes from adding an int directly to a string. Confirmed solid.

### Aug 10, 2026 - user_input, Bro Code

Reviewed input() and its string return type, converting input with int() and float() before doing math, plus two small practice programs, a rectangle area calculator and a shopping cart total. Confirmed solid.

### Aug 10, 2026 - arithmetic_math, Bro Code

Covered augmented assignment operators, built-in functions round, abs, pow, max, min, and the math module including pi, e, sqrt, ceil, and floor. Applied to three practice programs: circle circumference, circle area, and the Pythagorean theorem. New ground beyond Bobby Stearman's numbers.py, which did not cover the math module. Confirmed solid.

### Aug 11, 2026 - if_statements, case fix

Fixed the case sensitivity issue flagged earlier: prompt now reads "yes/no" lowercase to match the comparison. Confirmed solid.

### Aug 11, 2026 - calculator, Bro Code

Built a calculator program using if-elif-else with operator input as a string, handling addition, subtraction, multiplication, and division, plus an else branch to catch invalid operators. Confirmed solid.

### Aug 11, 2026 - temperature_conversion, Bro Code

Built a Celsius to Fahrenheit and Fahrenheit to Celsius converter using if-elif-else based on unit input. Confirmed solid.

### Aug 11, 2026 - weight_converter, Bro Code

Built a kilograms to pounds and pounds to kilograms converter using if-elif-else based on unit input. Confirmed solid.

### Aug 12, 2026 - logical_operators, Bro Code

Covered or, and, and not for combining multiple conditions, including a nested example combining temperature and weather state across six branches. Confirmed solid.

### Aug 12, 2026 - conditional_expression, Bro Code

Covered the ternary operator, a one-line shortcut for if-else, applied across six examples including finding max and min, checking even or odd, and role-based access checks. Confirmed solid.

### Aug 12, 2026 - string_method, Bro Code

Covered string methods find, rfind, capitalize, upper, lower, isdigit, isalpha, count, and replace, applied to a username validation exercise checking length, spaces, and digits. Confirmed solid.

### Aug 12, 2026- string_indexes, Bro Code

Covered string slicing with start, end, and step, including negative indexing, step slicing to skip characters, extracting the last four digits of a credit number, and reversing a string using [::-1]. Confirmed solid.

### Aug 13, 2026 - format_specifiers, Bro Code

Covered format specifier flags inside f-strings: decimal places, thousand separators, right and left alignment, zero padding, centering, and forcing a positive sign, including combining multiple flags together. Confirmed solid.


### Aug 13, 2026 - while_loops, Bro Code

Covered while loop validation patterns, repeating a prompt until valid input is given, applied across four examples, name entry, non-negative age, quit-on-command food list, and range validation. Confirmed solid.

### Aug 14, 2026 - compound_interest_calculator, Bro Code

Built a compound interest calculator combining three while loop validation blocks with the compound interest formula. Ties while loop validation and arithmetic together in one program. Confirmed solid.

### Aug 14, 2026 - for_loops, Bro Code

Covered for loops over a range, reversed range for countdown, stepping by 2, iterating over string characters, and continue versus break inside a loop. Confirmed solid.

### Aug 14, 2026 - countdown_timer_program, Bro Code

Built a countdown timer using a for loop counting down, converting seconds into hours, minutes, and seconds with modulus and division, and the time module to pause execution each second. Confirmed solid.

### Aug 14, 2026 - nested_loop, Bro Code

Covered a loop inside another loop, building a grid pattern from rows, columns, and a symbol input. This was new ground, first time combining two loops together, took a moment to see how the inner loop completes fully before the outer loop moves forward.

### Aug 14, 2026 - shopping_cart_program, Bro Code

Built a shopping cart program using two parallel lists for items and prices, a while loop for repeated entry, and a running total. Confirmed solid.

### Aug 15, 2026 - 2D_collection, Bro Code

Covered nested lists and tuples, indexing into a 2D structure, and looping through a nested collection with a nested for loop, applied to grocery categories, a skillset list, and a dial pad layout. Confirmed solid, ties directly into nested_loop concept covered earlier.

### Aug 16, 2026 - quiz_game, Bro Code

Built a quiz game using parallel tuples for questions, options, and answers, a for loop with a manual counter to track question number, and score calculated as a percentage. Confirmed solid.

### Aug 17, 2026 - concession_stand_program, Bro Code, first mini-project in new folder

Built a menu ordering system using a dictionary for menu items and prices, a while loop for repeated input, and dictionary lookups with get() to validate selections. Confirmed solid.

### Aug 17, 2026 - random_numbers, Bro Code

Covered the random module: randint for whole numbers in a range, random for a decimal between 0 and 1, choice for picking from a sequence, and shuffle for reordering a list in place. Confirmed solid, ties directly into random use already seen in dice_roller_program and number_guessing_game.

### Aug 17, 2026 - number_guessing_game, Bro Code

Built a number guessing game using random.randint, a while loop tied to a running flag, and isdigit() to validate input before converting to int. Confirmed solid.

### Aug 17, 2026 - rock_paper_scissors_game, Bro Code

Built a rock paper scissors game using random.choice, nested while loops for input validation and replay, and if-elif-else to determine the winner. Confirmed solid.

### Aug 17, 2026 - dice_roller_program, Bro Code

Built a dice roller using random.randint, a dictionary mapping numbers to ASCII dice art, and nested loops to print multiple dice side by side. New ground combining random, dictionaries, and formatted text output together.








