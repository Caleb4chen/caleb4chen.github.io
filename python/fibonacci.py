def fibonnaci(x):
  fib = [0]
  y = 1
  for i in range(x-1):
    fib.append(y)
    y = fib[len(fib) - 1] + fib[len(fib) - 2]

  return fib
  


print(fibonnaci(5))