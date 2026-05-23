#!/usr/bin/env python3
import ast
import operator
import sys

_OPS = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.Pow: operator.pow,
    ast.Mod: operator.mod,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}


def _eval(node):
    if isinstance(node, ast.Expression):
        return _eval(node.body)
    if isinstance(node, ast.BinOp):
        left = _eval(node.left)
        right = _eval(node.right)
        op_type = type(node.op)
        if op_type in _OPS:
            return _OPS[op_type](left, right)
        raise ValueError(f"Unsupported operator: {op_type}")
    if isinstance(node, ast.UnaryOp):
        operand = _eval(node.operand)
        op_type = type(node.op)
        if op_type in _OPS:
            return _OPS[op_type](operand)
        raise ValueError(f"Unsupported unary operator: {op_type}")
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise ValueError("Only int/float constants are supported")
    if isinstance(node, ast.Num):  # Python <3.8
        return node.n
    raise ValueError(f"Unsupported expression: {type(node)}")


def evaluate(expr: str):
    """Safely evaluate a simple arithmetic expression.

    Supports +, -, *, /, %, ** and parentheses.
    """
    try:
        parsed = ast.parse(expr, mode="eval")
        return _eval(parsed)
    except Exception as e:
        raise ValueError(f"Invalid expression: {e}")


def repl():
    print("Simple Calculator REPL. Type 'quit' or 'exit' to leave.")
    while True:
        try:
            s = input('> ').strip()
        except (EOFError, KeyboardInterrupt):
            print()
            break
        if not s:
            continue
        if s.lower() in ("quit", "exit"):
            break
        try:
            print(evaluate(s))
        except Exception as e:
            print('Error:', e)


def main():
    if len(sys.argv) > 1:
        expr = " ".join(sys.argv[1:])
        try:
            print(evaluate(expr))
        except Exception as e:
            print('Error:', e)
            sys.exit(2)
    else:
        repl()


if __name__ == '__main__':
    main()
