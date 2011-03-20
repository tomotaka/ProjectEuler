require File.expand_path("../lib/project-euler-mylib.rb", File.dirname(__FILE__))
N = 10001
count = 0
last_prime_number = nil
i = 1
while count < N
  if is_prime?(i) then
    last_prime_number = i
    count += 1
  end
  i += 1
end
puts "##{N} => #{last_prime_number}"
