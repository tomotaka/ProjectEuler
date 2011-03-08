total = 0
(1...1000).each do |n|
  total += n if n % 3 == 0 || n % 5 == 0
end
p total
