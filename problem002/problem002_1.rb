MAX = 400_0000 - 1

def fib(max)
  before_n = 1
  n = 1
  yield n
  while n < max do
    tmp = n
    n += before_n
    before_n = tmp
    yield n
  end
end

even_total = 0
fib(MAX) do |n|
  even_total += n if n % 2 == 0
end

p even_total
