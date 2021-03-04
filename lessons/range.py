"""Range example."""

start: int = 0
stop: int = 100
step: int = 10

a_range = range = range(start, stop, step)
print(a_range[0])
print(a_range[1])
print(a_range[2])
print(len(a_range))
print(f"Max value in range: {a_range}")

a_range = range(10,100) # Default step value is 1
a_range = range(10) # Stop is 10, start is 1 by default, step is 1 by default
