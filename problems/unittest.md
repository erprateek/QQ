## Question

Use python ABC/Protocols library and list data structure to create a script Stack.py containing Stack class, interface that implements

- Stack pop
- Stack push
- whether Stack is empty or not
- Serializing Stack elements into a list
- Checking whether an element is in the stack or not
- Printing Stack
- Stack reverse

Create a test_stack.py script as well that tests individual components of the code. Examples:
```
import pytest
from Stack import Stack

# Test cases for Stack class
def test_stack_push():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.size == 3

def test_stack_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.pop() == 3
    assert stack.size == 2

def test_stack_is_empty():
    stack = Stack()
    assert stack.isEmpty() == True
    stack.push(1)
    assert stack.isEmpty() == False

def test_stack_is_in_stack():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    assert stack.isInStack(2) == True
    assert stack.isInStack(4) == False

def test_stack_reverse():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    reversed_stack = stack.reverse()
    assert reversed_stack.pop() == 1
    assert reversed_stack.pop() == 2
    assert reversed_stack.pop() == 3

```
Bonus:
- Use/extend these test cases to exhaustively test your stack implementation.
- Highlight any limitations/assumptions that your implementation has
- Add strict type checking for your variables
- Do you have a better idea about the limitations/assumptions now that you have added type checking?
