max_reversible = 0
(100..999).each do |a|
  (100..999).each do |b|
    n = a * b
    max_reversible = n if max_reversible < n && n.to_s == n.to_s.reverse
  end
end

p max_reversible
