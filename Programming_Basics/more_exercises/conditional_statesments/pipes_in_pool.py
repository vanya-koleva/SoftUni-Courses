volume = int(input())
pipe_one_yield = int(input())
pipe_two_yield = int(input())
hours = float(input())

total_pipe_one_yield = pipe_one_yield * hours
total_pipe_two_yield = pipe_two_yield * hours
total_yield = total_pipe_one_yield + total_pipe_two_yield

if total_yield <= volume:
    percentage = total_yield /volume * 100
    percentage_pipe_one = total_pipe_one_yield / total_yield * 100
    percentage_pipe_two = total_pipe_two_yield / total_yield * 100
    print(f"The pool is {percentage:.02f}% full. Pipe 1: {percentage_pipe_one:.02f}%."
          f" Pipe 2: {percentage_pipe_two:.02f}%.")
else:
    excess = abs(volume - total_yield)
    print(f"For {hours:.02f} hours the pool overflows with {excess:.02f} liters.")
