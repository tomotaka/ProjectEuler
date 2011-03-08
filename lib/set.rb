
# Collection which do not allow duplication of element. (Each element must be unique in a set)
class Set

  include Enumerable

  def initialize
    @internal = {}
  end

  def add(x)
    return false if @internal.has_key?(x)
    @internal[x] = true
  end

  alias << add

  def each(&proc)
    to_a.each(&proc)
  end

  def to_a
    return @internal.keys
  end

  def size
    return @internal.size
  end

end
