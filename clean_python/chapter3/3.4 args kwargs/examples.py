def foo(required_argument1, required_argument2, *args, **kwargs):
    print(f"required: {required_argument1}, {required_argument2}")
    print(f"args: {args}")
    print(f"kwargs: {kwargs}")


foo("A", "B", "C", "D", e="e", f="f")