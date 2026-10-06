# Functions in Python

## Overview

A **function** is a named, reusable block of code that performs one specific task. It takes inputs (**parameters**), processes them, and hands back an output (**return value**). Functions are the building block of *modular programming*: a large program is split into modules (files), each module groups related functions, and each function solves one small sub‑problem.

This reference covers:

- What functions are and why we use them
- Writing and calling a function (`def`, header/signature, `return`)
- Formal vs actual parameters and how Python passes arguments
- Positional and keyword arguments, and the rules for mixing them
- Default arguments, including the mutable‑default pitfall and `__defaults__`
- Positional‑only (`/`) and keyword‑only (`*`) parameters, and combining them
- Worked practice programs

---

## 1. What Are Functions?

### Built‑in functions

Python ships with many ready‑made, tested functions. You call them with round brackets.

| Function | Purpose | Example |
|----------|---------|---------|
| `print()` | Display output | `print("Hello")` |
| `input()` | Read user input (as `str`) | `name = input("Name: ")` |
| `range(start, stop, step)` | Generate a sequence of integers | `range(1, 5)` → 1, 2, 3, 4 |
| `len()` | Length of an iterable | `len([1, 2, 3])` → `3` |
| `int()`, `str()` | Type conversion | `int("10")` → `10` |
| `max()` | Largest element | `max(4, 9, 2)` → `9` |

```python
print("Hello, World!")
name = input("Enter your name: ")
print("Welcome,", name)

for i in range(1, 5):
    print(i)        # 1 2 3 4
```

### User‑defined functions

```python
def greet(name):
    return "Hello, " + name + "!"

message = greet("Alice")
print(message)      # Hello, Alice!
```

### Characteristics of a function

| Characteristic | Meaning |
|----------------|---------|
| Performs a specific task | One function = one job |
| Takes parameters | Inputs the task needs |
| Returns a result | Output sent back to the caller |
| Reusable | Write once, call many times |
| Modular | Lets teams work on separate pieces independently |

### Modular programming

Large applications are divided into **modules**, and each module contains related **functions**. A university management system, for example, might have `admissions`, `fees`, `exams`, and `library` modules.

```python
# module_admissions.py
def add_student(student_name):
    return "Student added: " + student_name

# module_fees.py
def calculate_fee(student_id):
    return 5000  # example fixed fee

# main_program.py
import module_admissions
import module_fees

print(module_admissions.add_student("Bob"))
print("Fee due:", module_fees.calculate_fee(123))
```

**Advantages:** less repetition, easier debugging and maintenance, better readability, team collaboration, and easier extension.

---

## 2. How to Write a Function

```python
def function_name(parameter_list):   # header / signature
    # function body (indented)
    return result
```

| Part | Description |
|------|-------------|
| `def` | Keyword that starts a function definition |
| `function_name` | Follows variable naming rules. Must be unique and should **not** reuse a built‑in name (`max`, `list`, `sum`, ...) |
| `(parameter_list)` | Formal parameters: the inputs the function expects |
| `:` | Marks the start of the body |
| Body | Consistently indented statements |
| `return` | Sends a value back to the caller. Without it the function returns `None` |

The first line (`def volume(length, breadth, height):`) is called the **header** or **signature**. Other languages call it a *prototype*.

### Example: volume of a cuboid

```python
def volume(length, breadth, height):
    vol = length * breadth * height
    return vol

v = volume(10, 5, 3)
print(v)            # 150
```

### Formal vs actual parameters

| Term | Where it appears | Example |
|------|------------------|---------|
| **Formal parameters** | In the function definition | `length`, `breadth`, `height` |
| **Actual parameters (arguments)** | In the function call | `10`, `5`, `3` in `volume(10, 5, 3)` |

```python
def add_numbers(a, b):      # a, b -> formal parameters
    return a + b

result = add_numbers(5, 3)  # 5, 3 -> actual parameters
print(result)               # 8
```

### Flow of control during a call

1. Control jumps from the call to the function body.
2. Actual parameters are bound to the formal parameters.
3. The body runs and reaches `return`.
4. Control (and the returned value) goes back to the caller.

> **Tip:** In PyCharm, set a breakpoint on the call and use *Step Into* to watch this flow.

### How Python passes arguments

Python has one parameter‑passing mechanism. The formal parameter becomes a new name for the **same object** the caller passed. What happens next depends on the type:

- **Immutable** objects (`int`, `float`, `str`, `tuple`): rebinding the parameter inside the function never affects the caller's variable.
- **Mutable** objects (`list`, `dict`, `set`): in‑place changes (`append`, `update`, ...) **are** visible to the caller.

### The `if __name__ == "__main__":` guard

```python
if __name__ == "__main__":
    v = volume(10, 5, 3)
    print(v)
```

Code inside this block runs only when the file is executed directly, not when it is imported as a module.

---

## 3. Ways to Supply Arguments

1. **Positional arguments**: matched by order
2. **Keyword arguments**: matched by name
3. **Default arguments**: used when the caller omits a value
4. **Variable‑length arguments**: `*args` / `**kwargs` (covered in a later section)

### 3.1 Positional arguments

Values are assigned to parameters by position. Changing the order changes the assignment.

```python
def volume(length, breadth, height):
    print(length, breadth, height)
    return length * breadth * height

volume(10, 5, 3)    # 10 5 3  -> 150
volume(5, 10, 3)    # 5 10 3  -> 150 (length and breadth swapped)
```

### 3.2 Keyword arguments

Each value is tagged with its parameter name, so order does not matter.

```python
volume(length=10, breadth=5, height=3)   # 10 5 3
volume(height=3, length=10, breadth=5)   # 10 5 3
```

### 3.3 Mixing positional and keyword arguments

```python
volume(10, 5, height=3)                  # ✅ valid
```

| Rule | Invalid call | Error |
|------|--------------|-------|
| Positional arguments must come **before** keyword arguments | `volume(length=5, 3, height=2)` | `SyntaxError: positional argument follows keyword argument` |
| A parameter can receive only **one** value | `volume(5, length=3, height=2)` | `TypeError: volume() got multiple values for argument 'length'` |
| Keyword names must **exactly match** the parameter names | `volume(length=5, width=3, height=2)` | `TypeError: volume() got an unexpected keyword argument 'width'` |
| Every required parameter must be supplied | `volume(5)` | `TypeError: volume() missing 2 required positional arguments: 'breadth' and 'height'` |

> ⚠️ **Warning:** "Positional after keyword" is caught when the code is *compiled*, so it is a `SyntaxError` and the line never runs. The other three are `TypeError`s raised at call time.

---

## 4. Default Arguments

A parameter can declare a default value, which is used when the caller does not provide one.

```python
def greet(name, greeting="Hello"):
    return f"{greeting}, {name}!"

greet("John")          # 'Hello, John!'
greet("John", "Hi")    # 'Hi, John!'
```

### Defaults in built‑in methods

```python
l1 = [10, 20, 30, 10, 20, 20, 30]

l1.index(20)          # 1  -> searches the whole list
l1.index(20, 2)       # 4  -> starts searching at index 2
l1.index(20, 2, 4)    # ValueError: 20 is not in l1[2:4]

l2 = [1, 2, 3, 4]
l2.pop()              # 4  -> default index is the last element
l2.pop(1)             # 2
```

`list.index(value, start=0, stop=...)` needs only one argument. `start` and `stop` are optional.

### Writing your own

```python
def volume(l=1, b=1, h=1):
    return l * b * h

volume(10, 5, 3)   # 150
volume(10, 5)      # 50  (h = 1)
volume()           # 1   (all defaults)
```

Defaults can be any type, and a value passed in the call replaces the default:

```python
def fun(a=12.5, b=25, c="hello"):
    print(a, b, c)

fun()                  # 12.5 25 hello
fun(5, 10, 15)         # 5 10 15
fun(5, 10, [10, 11])   # 5 10 [10, 11]
```

### Rule: defaults go on the right

Once a parameter has a default, every parameter after it must also have one.

```python
def volume(length, breadth, height=1): ...    # ✅
def volume(length=1, breadth, height): ...    # ❌ SyntaxError: parameter without a default follows parameter with a default
```

### ⚠️ Pitfall: mutable default arguments

Default values are evaluated **once, when the function is defined**, not on every call. A mutable default such as a list or dict is therefore **shared across calls**.

```python
def func(l=[1, 2, 3]):
    l.append(len(l))
    print(l)

func()           # [1, 2, 3, 3]
func()           # [1, 2, 3, 3, 4]        <- same list reused
func([10, 11])   # [10, 11, 2]            <- caller's own list
func()           # [1, 2, 3, 3, 4, 5]     <- the shared default keeps growing
```

```python
def add_item_to_list(item, my_list=[]):
    my_list.append(item)
    return my_list

add_item_to_list(1)       # [1]
add_item_to_list(2)       # [1, 2]
add_item_to_list(3, [4])  # [4, 3]
add_item_to_list(5)       # [1, 2, 5]
```

**Fix:** use `None` as a sentinel and create a new object inside the function.

```python
def add_item_to_list(item, my_list=None):
    if my_list is None:
        my_list = []
    my_list.append(item)
    return my_list

add_item_to_list(1)       # [1]
add_item_to_list(2)       # [2]
add_item_to_list(3, [4])  # [4, 3]
add_item_to_list(5)       # [5]
```

### Inspecting defaults: `__defaults__`, `__kwdefaults__`, `inspect`

Defaults are stored on the **function object**, not in its local scope.

```python
def volume(length, breadth, height=1): ...
volume.__defaults__          # (1,)

def kw(a, *, c=10, d=20): ...
kw.__defaults__              # None
kw.__kwdefaults__            # {'c': 10, 'd': 20}   <- keyword-only defaults live here
```

Built‑in methods are written in C, so they have no `__defaults__`. Use `inspect.signature()` instead:

```python
import inspect

print(inspect.signature(list.index))
# (self, value, start=0, stop=9223372036854775807, /)

sig = inspect.signature([10, 20, 30].index)
for name, param in sig.parameters.items():
    if param.default is not inspect.Parameter.empty:
        print(f"{name} = {param.default}")
# start = 0
# stop = 9223372036854775807
```

> **Note:** Why `9223372036854775807` and not `len(list)`? The signature is defined once for the whole `list` class, before any list exists, so it cannot store a per‑instance length. CPython uses `sys.maxsize` as the upper bound and at runtime stops at `min(stop, len(list))`. The trailing `/` also shows that `list.index` is positional‑only.

> ⚠️ **Watch out:** writing `max = func_max_finder(...)` (or `volume = 150`) rebinds a function name to a plain value. After that, `volume.__defaults__` raises `AttributeError: 'int' object has no attribute '__defaults__'`. Avoid reusing function names and built‑ins as variable names.

---

## 5. Positional‑Only Parameters (`/`), Python 3.8+

Every parameter **before** `/` is positional‑only and **cannot** be passed by keyword. Parameters after `/` can be passed either way.

```python
def func(a, b, /, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")
    return a + b + c + d
```

| Call | Result |
|------|--------|
| `func(1, 2, 3, 4)` | ✅ all positional |
| `func(1, 2, c=3, d=4)` | ✅ |
| `func(1, 2, 3, d=4)` | ✅ |
| `func(a=1, b=2, c=3, d=4)` | ❌ `TypeError: func() got some positional-only arguments passed as keyword arguments: 'a, b'` |
| `func(1, 2, c=3, 4)` | ❌ `SyntaxError: positional argument follows keyword argument` |
| `func(1, b=2, 3, 4)` | ❌ `SyntaxError`. The positional‑after‑keyword check fires first, before the positional‑only rule is even considered |

### Placement of `/`

| Signature | Meaning |
|-----------|---------|
| `def fun(a, b, /, c, d)` | `a`, `b` positional‑only; `c`, `d` either |
| `def fun(a, b, c, d, /)` | **All** positional‑only |
| `def fun(/, a, b, c, d)` | ❌ `SyntaxError: at least one argument must precede /` |

### Rules for `/`

1. Parameters before `/` are positional‑only.
2. Parameters after `/` are positional‑or‑keyword.
3. `/` is a marker, not a parameter.
4. `/` cannot be the first item. It *can* be the last item, which makes all parameters positional‑only.
5. Use it for API clarity, when parameter names are meaningless to callers or may change later.

---

## 6. Keyword‑Only Parameters (`*`)

Every parameter **after** a bare `*` is keyword‑only and **must** be passed by name.

```python
def func(a, b, *, c, d):
    print(f"a={a}, b={b}, c={c}, d={d}")
    return a + b + c + d
```

| Call | Result |
|------|--------|
| `func(1, 2, c=3, d=4)` | ✅ |
| `func(a=1, b=2, c=3, d=4)` | ✅ |
| `func(1, 2, 3, 4)` | ❌ `TypeError: func() takes 2 positional arguments but 4 were given` |
| `func(1, 2, c=3, 4)` | ❌ `SyntaxError: positional argument follows keyword argument` |

### Placement of `*`

| Signature | Meaning |
|-----------|---------|
| `def fun(a, b, *, c, d)` | `a`, `b` either; `c`, `d` keyword‑only |
| `def fun(a, b, c, *, d)` | only `d` keyword‑only |
| `def fun(*, a, b, c, d)` | **All** keyword‑only |
| `def fun(a, b, c, d, *)` | ❌ `SyntaxError: named arguments must follow bare *` |
| `def fun(a, *, b, *, c)` | ❌ `SyntaxError`. Only one `*` is allowed |

### Keyword‑only with defaults

Unlike ordinary parameters, keyword‑only parameters may have defaults in any order, because they are never matched by position.

```python
def func_keyword_default(a, b, *, c=10, d=20):
    print(f"a={a}, b={b}, c={c}, d={d}")
    return a + b + c + d

func_keyword_default(1, 2)              # a=1, b=2, c=10, d=20
func_keyword_default(1, 2, c=30)        # a=1, b=2, c=30, d=20
func_keyword_default(1, 2, d=40)        # a=1, b=2, c=10, d=40
func_keyword_default(1, 2, c=30, d=40)  # a=1, b=2, c=30, d=40
```

---

## 7. Mixing `/` and `*`

```python
def fun(a, b, /, c, d, *, e, f):
    print(a, b, c, d, e, f)
```

```
def fun(a, b, /, c, d, *, e, f)
        └─┬─┘    └─┬─┘    └─┬─┘
   positional‑  positional  keyword‑
      only      or keyword    only
```

| Call | Result |
|------|--------|
| `fun(15, 20, 30, 40, e=2, f=3)` | ✅ |
| `fun(15, 20, c=30, d=40, e=2, f=3)` | ✅ |
| `fun(a=15, b=20, c=30, d=40, e=2, f=3)` | ❌ `TypeError`: `a`, `b` are positional‑only |
| `fun(15, b=20, c=30, d=40, e=2, f=3)` | ❌ `TypeError`: `b` is positional‑only |
| `fun(15, 20, 30, 40, 2, 3)` | ❌ `TypeError: fun() takes 4 positional arguments but 6 were given` |

A minimal example:

```python
def fun(a, /, b, *, c):
    print(a, b, c)

fun(5, b=10, c=15)     # ✅ 5 10 15
fun(5, 10, c=15)       # ✅
fun(a=5, b=10, c=15)   # ❌ a is positional-only
fun(5, 10, 15)         # ❌ c is keyword-only
```

Both markers can sit next to each other, with no parameters between them:

```python
def func_positional_keyword(a, b, /, *, c, d):
    return a + b + c + d

func_positional_keyword(1, 2, c=3, d=4)   # 10
```

> ⚠️ **Order matters:** `/` must come **before** `*`. Writing `def f(a, *, b, /, c)` raises `SyntaxError: / must be ahead of *`.

### Quick reference: parameter kinds

| Kind | Declared | Pass by position | Pass by keyword |
|------|----------|:---:|:---:|
| Positional‑only | before `/` | ✅ | ❌ |
| Positional‑or‑keyword | between `/` and `*` (or no markers) | ✅ | ✅ |
| Keyword‑only | after `*` | ❌ | ✅ |

Full ordering of a signature:

```python
def f(pos_only, /, pos_or_kw, *, kw_only):
```

---

## 8. Practice Programs

### 8.1 Maximum of three numbers (positional‑only)

*Task:* find the maximum of 3 numbers. All three values must be passed positionally.

```python
def func_max_finder(a, b, c, /):
    if a > b:
        if a > c:
            return a
        else:
            return c
    else:
        if b > c:
            return b
        else:
            return c

result = func_max_finder(5, 20, 15)
print(result)        # 20
```

- The trailing `/` makes `a`, `b`, and `c` positional‑only, so `func_max_finder(a=5, b=20, c=15)` raises `TypeError`.
- Nested `if/else` compares pairs. The built‑in equivalent is `max(a, b, c)`.
- Store the result in a name like `result` rather than `max`, so the built‑in `max()` is not shadowed.

### 8.2 Simple interest (keyword‑only)

*Task:* SI = (P × R × T) / 100, and every parameter must be passed by keyword.

```python
def func_simple_interest(*, P, R, T):
    return (P * R * T) / 100

SI = func_simple_interest(P=1000, R=5, T=2)
print(SI)            # 100.0
```

- A leading `*` makes **all** parameters keyword‑only. This prevents mix‑ups between principal, rate, and time.
- `func_simple_interest(1000, 5, 2)` raises `TypeError: func_simple_interest() takes 0 positional arguments but 3 were given`.
- `/` always returns a `float`, which is why the output is `100.0`.

### 8.3 Pangram checker

*Task:* check whether a phrase uses every letter of the English alphabet at least once.

```python
def fun_anagram(pharse):
    unique_chars = set()

    for char in pharse:
        if char.isalpha():
            unique_chars.add(char.lower())

    if len(unique_chars) == 26:
        return True
    else:
        return False

print(fun_anagram("P1ack my box witph five dozen liquor jugs@1"))   # True
```

- A `set` collects each letter only once. Digits and symbols are skipped by `isalpha()`.
- Despite its name, this checks for a **pangram**, not an anagram.
- `isalpha()` also accepts non‑English letters (`é`, `ß`), which could push the count to 26 without covering a–z. A stricter, shorter version:

```python
import string

def is_pangram(phrase):
    return set(string.ascii_lowercase) <= set(phrase.lower())
```

- Return the comparison directly (`return len(unique_chars) == 26`) instead of wrapping it in `if/else`.

---

## 9. Common Errors at a Glance

| Mistake | Error |
|---------|-------|
| Positional argument after a keyword argument | `SyntaxError: positional argument follows keyword argument` |
| Same parameter given twice | `TypeError: ... got multiple values for argument 'x'` |
| Misspelled keyword | `TypeError: ... got an unexpected keyword argument 'x'` |
| Missing required argument | `TypeError: ... missing N required positional argument(s)` |
| Non‑default parameter after a default one | `SyntaxError: parameter without a default follows parameter with a default` |
| Positional‑only passed by keyword | `TypeError: ... got some positional-only arguments passed as keyword arguments` |
| Keyword‑only passed by position | `TypeError: ... takes N positional arguments but M were given` |
| `/` as the first item | `SyntaxError: at least one argument must precede /` |
| Bare `*` as the last item | `SyntaxError: named arguments must follow bare *` |
| `*` placed before `/` | `SyntaxError: / must be ahead of *` |

---

## Key Takeaways

1. A function is a reusable block, defined with `def`, that takes parameters and returns a result (or `None` without `return`).
2. Functions enable modular programming: programs are split into modules, and modules into functions.
3. **Formal** parameters appear in the definition. **Actual** parameters (arguments) appear in the call.
4. Python passes references to objects. Mutating a mutable argument is visible to the caller, while rebinding a parameter is not.
5. Positional arguments match by order and keyword arguments match by name. In a call, positional arguments must come first.
6. Default parameters must come after non‑default ones, and they are evaluated **once** at definition time.
7. Never use a mutable default (`[]`, `{}`). Use `None` and create the object inside the function.
8. `/` makes the preceding parameters positional‑only. A bare `*` makes the following parameters keyword‑only.
9. When both are used, the order is always `pos_only, /, pos_or_kw, *, kw_only`.
10. Inspect defaults with `func.__defaults__` / `func.__kwdefaults__`, or with `inspect.signature()` for built‑ins.
