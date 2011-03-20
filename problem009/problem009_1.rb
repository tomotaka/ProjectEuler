(1..(1000-2)).each do |a|
  (a..(1000-1)).each do |t_b|
    b = t_b - a
    c = 1000 - t_b
    next if c <= b || b <= a
    next if a*a + b*b != c*c

    puts "a=#{a}, b=#{b}, c=#{c}"
    exit
  end
end
