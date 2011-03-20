# load other files
here = File.dirname(__FILE__)
require File.expand_path("./set.rb", here)

# create prime factor list of 'n'
def factors(n)
  return [n] if n == 1
  ret = []
  x = n
  while 1 < x
    sqrt = Math.sqrt(x).floor
    no_devide = true
    2.upto(sqrt) do |i|
      if x % i == 0 then
        ret << i
        x /= i
        no_devide = false
        break
      end
    end
    if no_devide then
      ret << x
      break
    end
  end
  return ret
end


# greatest common divisor
def gcd(a, b)
  gcd = 1

  no_update = false
  while not no_update
    no_update = true
    2.upto([a,b].max) do |i|
      if a % i == 0 && b % i == 0 then
        a = a / i
        b = b / i
        no_update = false
        gcd = gcd * i
        break
      end
    end
  end

  return gcd
end

# least common multiple
def lcm(a, b)
  return (a*b) / gcd(a, b)
end

# check if the given number is prime number
def is_prime?(n)
  return false if n == 1
  return true if n == 2
  return false if n % 2 == 0

  3.step(Math.sqrt(n).ceil, 2) do |i|
    return false if n % i == 0
  end
  
  return true
end


