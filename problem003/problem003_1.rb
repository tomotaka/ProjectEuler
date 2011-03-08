N = 600851475143

def list_factor(n)
  return [n] if n == 1
  first_factor = lambda{|m|
    2.upto(m-1) do |i|
      return i if m % i == 0
    end
    return m
  }

  factors = []
  x = n
  while x != 1
    x_factor = first_factor.call(x)
    factors << x_factor
    x = x / x_factor
  end

  return factors
end

p list_factor(N).max
