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
│   └── random_numbers.py
├── 02-data-structures/
│   ├── lists.py
│   ├── tuples.py
│   ├── sets.py
│   ├── dictionaries.py
│   ├── 2D_collection.py
│   └── list_comprehension.py
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
│   └── membership_operators.py
├── 04-modules-and-errors/
│   ├── modules.py
│   ├── errors_exceptions.py
│   ├── function.py
│   ├── default_arguments.py
│   ├── keyword_argument.py
│   └── args_&_kwargs.py
├── 05-oop/
│   ├── classes.py
│   ├── python-object-oriented-programming-example/
│   |   ├── car.py
│   |   └── main.py
│   ├── class_variables.py
│   ├── inheritance.py
│   ├── multiple_inheritance.py
│   ├── super.py
│   ├── polymorphism.py
│   ├── duck_typing.py
│   ├── static_methods.py
│   ├── class_methods.py
│   ├── magic_methods.py
│   └── property.py
├── 06-mini-projects/
│   ├── concession_stand_program.py
│   ├── number_guessing_game.py
│   ├── rock_paper_scissors_game.py
│   ├── dice_roller_program.py
│   ├── bank_program.py
│   ├── slot_machine.py
│   ├── encryption_program.py
│   ├── hangman_art.py
│   └── alarm-clock-project/
│       ├── alarm_clock.py
│       └── my_music.mp3
├── 07-name-main-pattern/
│   ├── script1.py
│   └── script2.py
└── 09-advanced-topics/
│    ├── decorator.py
│    ├── exception_handling.py
│    ├── dates_and_times.py
│    ├── multithreading.py
│    ├── request_api_data.py
│    └── PyQt5-projects/
│       ├── PyQt5_GUI_intro.py
│       └── my_pic.png
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

### Aug 18, 2026 - function, Bro Code

Covered defining functions, calling them with different arguments, and return to send a value back to the caller, applied across birthday greetings, invoice display, basic math operations, and name formatting.

### Aug 18, 2026 - default_arguments, Bro Code

Covered setting default parameter values so arguments can be omitted, reducing how many values need to be passed in, applied to a pricing calculation and a countdown-style counter. 

### Aug 18, 2026 - keyword_argument, Bro Code

Covered passing arguments by name instead of position, so order does not matter, applied to a greeting function and a phone number builder. 

### Aug 18, 2026 - args_&_kwargs, Bro Code

Covered *args for multiple non-keyword arguments and **kwargs for multiple keyword arguments, including combining both together in one function, applied to a shipping label builder. This one took more repetition to fully click, first time seeing the unpacking operator used this way.

### Aug 19, 2026 - membership_operators, Bro Code

Covered in and not in for checking whether a value exists inside a string, set, or dictionary, applied to a letter guessing check, a student lookup, a grade lookup, and a basic email validation check combining membership with and.

### Aug 19, 2026 - list_comprehension, Bro Code

Covered building lists in one line instead of a full loop, including conditionals inside the comprehension to filter values, applied to doubling numbers, capitalizing strings, and filtering positive, negative, even, odd, and passing grades.

### Aug 19, 2026 - match, Bro Code addition

Added match-case as an alternative to long elif chains, applied to a day-of-week lookup and a weekend check using the pipe symbol to match multiple values in one case. Builds on the match fundamentals from Bobby Stearman's version, this addition reinforced it further with cleaner, more practical use cases.

### Aug 19, 2026 - script1 & script2, Bro Code

Covered if name == "main": for writing code that can be imported into another file without automatically running, keeping functions reusable and avoiding unintended execution. script1.py defines a function and its own main() guarded by the block; script2.py imports script1 with a wildcard import and reuses favourite_food inside its own separate main(). First real use of splitting logic across two files and controlling what runs where

### Aug 20, 2026 - banking_program, Bro Code

Built a banking program using separate functions for showing balance, depositing, and withdrawing, a while loop menu tied to a running flag, and if name == "main": to control execution. Ties together functions, return values, and the main pattern covered in script1 and script2.

### Aug 21, 2026 - slot_machine, Bro Code

Built a slot machine using random.choice with a list comprehension to spin three symbols, a payout function matching three identical symbols to different multipliers, and a while loop tied to balance and a play-again prompt. Combines functions, return values, random, list comprehension, and the main pattern into one program.

### Aug 22, 2026 - encryption_program, Bro Code

Built an encryption and decryption program using a substitution cipher, mapping every character to a shuffled version of itself with random.shuffle, then using index() to look up and swap characters between the two lists for encrypting and decrypting a message. Noted the key regenerates each run, so decrypt only works within the same session, matches how Bro Code built it.

### Aug 24, 2026 - hangman_art, Bro Code

Built a hangman game using a dictionary to store ASCII art for each wrong guess stage, a set to track guessed letters, and a hint list built with underscores that fills in as correct letters are guessed. Combines dictionaries, sets, lists, string joining, and the main pattern into one full game with win and lose conditions.

### Aug 24, 2026 - car-example, Bro Code

Covered defining a class in one file and importing it into another, applied to a Car class with model, year, colour, and for_sale attributes, plus drive, stop, and describe methods. Ties class basics together with the import pattern covered in script1 and script2.

### Aug 24, 2026 - class_variables, Bro Code

Covered class variables shared across all instances, defined outside the constructor, used to track a running count of students created from the class.

### Aug 24, 2026 - inheritance, Bro Code

Covered a child class inheriting attributes and methods from a parent class, with each child overriding a shared method differently, applied to an Animal base class and Dog, Cat, and Lion subclasses.

### Aug 24, 2026 - multiple_inheritance, Bro Code

Covered a class inheriting from more than one parent, and multilevel inheritance where a class inherits from a class that itself inherits from another, applied to Prey and Predator as parents of Rabbit, Hawk, and Fish.

### Aug 24, 2026 - super, Bro Code

Covered super() for calling a parent class's method from inside a child class, extending rather than replacing the parent's behaviour, applied to a Shape base class with Circle, Square, and Triangle subclasses each adding their own area calculation before calling the shared describe().

### Aug 24, 2026 - polymorphism, Bro Code

Covered polymorphism through inheritance, where different shape classes all implement their own version of the same area() method, called the same way regardless of which shape it is, using ABC and abstractclassmethod to enforce the pattern.

### Aug 24, 2026- duck_typing, Bro Code

Covered the second way to achieve polymorphism, no shared inheritance required, just matching method names across unrelated classes, demonstrated with Dog, Cat, and Car all responding to the same speak() call.

### Aug 25, 2026 - static_methods, Bro Code

Covered @staticmethod for utility functions that belong to a class but do not need access to instance or class data, applied to validating a job position string against a list of allowed roles.

### Aug 25, 2026 - class_methods, Bro Code

Covered @classmethod and cls as the first parameter, used to calculate a running total and average GPA across all student instances without needing a specific instance.

### Aug 25, 2026 - magic_methods, Bro Code

Covered dunder methods that customize built-in behaviour: str for print output, eq for equality comparison, lt and gt for comparison operators, add for combining objects, contains for the in keyword, and getitem for dictionary-style key access, all applied to a Book class.

### Aug 25, 2026 - property, Bro Code

Covered the @property decorator for getter, setter, and deleter behaviour, letting a method be accessed like a plain attribute while still validating input, applied to width and height on a Rectangle class.

### Aug 26, 2026 - decorator, Bro Code

Covered decorators, functions that wrap another function to extend its behaviour without modifying it, including stacking two decorators on top of the same function using @ syntax, applied to an ice cream order example.

### Aug 26, 2026 - exception_handling, Bro Code

Covered a deeper pass on try/except/finally, catching specific exceptions like ZeroDivisionError and ValueError separately before falling back to a general Exception catch, plus finally for cleanup that always runs. Builds on errors.py from Bobby Stearman's course with more targeted exception handling.

### Aug 27, 2026 - dates_and_times, Bro Code

Covered the datetime module: creating specific dates and times, getting the current date and time, formatting output with strftime, and comparing two datetime objects to check if a target date has passed.

### Aug 27, 2026 - multithreading, Bro Code

Covered running multiple functions concurrently using threading.Thread, starting each thread, then using join() to wait for all threads to finish before the program continues, applied to three chores running at the same time instead of one after another.

### Aug 27, 2026 - request_api_data, Bro Code

Covered connecting to a real external API using the requests library, sending a GET request, checking the response status code, and parsing JSON data back into usable values, applied to fetching Pokémon data from PokeAPI and also it requires an internet connection and a working requests install.

### Aug 28, 2026 - alarm-clock-project, Bro Code

Built an alarm clock using the pygame library to play a sound file once the current time matches the set alarm time, checked every second with a while loop, plus the datetime module for tracking current time and time.sleep for pausing between checks.

### Aug 28, 2026 - PyQt5_GUI_intro, Bro Code

Covered building a basic desktop GUI window using PyQt5, setting window title, size, and geometry, plus a custom window icon loaded from an image file. First GUI work outside the terminal-based programs done so far.