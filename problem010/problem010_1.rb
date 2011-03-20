require File.expand_path("../lib/project-euler-mylib.rb", File.dirname(__FILE__))
total = 0
(1..2000000).each do |i|
  total += i if is_prime?(i)
end
p total
