max_reversible = 0
(100..999).each do |a|
  (100..999).each do |b|
    n = a * b
    if max_reversible < n then
      k1 = n % 10
      k6 = (n / 100000) % 10
      next if k1 != k6

      k2 = (n / 10) % 10
      k5 = (n / 10000) % 10
      next if k2 != k5
      
      k3 = (n / 100) % 10
      k4 = (n / 1000) % 10
      next if k3 != k4

      max_reversible = n
    end
  end
end

p max_reversible
