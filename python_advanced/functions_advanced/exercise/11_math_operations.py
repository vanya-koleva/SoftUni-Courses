def math_operations(*numbers, **kwargs):
    mapper = {
        "a": lambda x: kwargs["a"] + x,
        "s": lambda x: kwargs["s"] - x,
        "d": lambda x: kwargs["d"] / x if x != 0 else kwargs["d"],
        "m": lambda x: kwargs["m"] * x,
    }

    keys = list(kwargs.keys())
    for i in range(len(numbers)):
        key = keys[i % 4]
        kwargs[key] = mapper[key](numbers[i])

    result = []
    kwargs = sorted(kwargs.items(), key=lambda x: (-x[1], x[0]))
    for key, value in kwargs:
        result.append(f"{key}: {value:.1f}")

    return "\n".join(result)


print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=(-2.3), d=0, m=0))
print(math_operations(6.0, a=0, s=0, d=5, m=0))
