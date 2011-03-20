require File.expand_path("../lib/project-euler-mylib.rb", File.dirname(__FILE__))

ans = 1
(1..20).each do |n|
  ans = lcm(ans, n)
end

p ans
