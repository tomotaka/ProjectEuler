N = 100

p (1..N).to_a.inject{|r,n| r+n }**2 - (1..N).to_a.inject{|r,n| r+n*n}
