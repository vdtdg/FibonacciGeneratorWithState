# Fibonacci Generator with state
Why not ?

Use this generator if you want to have a generator that saves the state it is in.

Give it the number of fibonacci number you want to generate, get them, and then you can ask for more !

## Usage
Import the FibonacciGenerator class as such
```
from FibonacciGenerator import FibonacciGenerator
```
Then start generating number using the `generate()` method
```
print(*[i for i in fibonacci_generator.generate(6)])
```

## Examples
```
fibonacci_generator = FibonacciGenerator()
for i in fibonacci_generator.generate(6):
    print(i, end=', ')
```
Will give you 0 1 1 2 3 5

```
fibonacci_generator = FibonacciGenerator()
for i in fibonacci_generator.generate(4):
    print(i, end=' ')
for i in fibonacci_generator.generate(5):
    print(i, end=' ')
```
Will give you 0 1 1 2 3 5 8 13 21