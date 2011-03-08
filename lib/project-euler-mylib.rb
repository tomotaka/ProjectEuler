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
