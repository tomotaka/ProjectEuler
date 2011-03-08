here = File.dirname(__FILE__)
require File.expand_path("../set.rb", here)
require "test/unit"

class Test_Set < Test::Unit::TestCase

  def setup
    @s1 = Set.new
  end
  
  def teardown
  end

  def test_add
    @s1.add("a")
    assert_equal ["a"], @s1.to_a

    @s1.add("b")
    assert_equal ["a", "b"], @s1.to_a

    @s1 << "c"
    assert_equal ["a", "b", "c"], @s1.to_a

    assert_equal false, @s1.add("a")
  end

  def test_each
    # 1
    @s1.add("a")
    e1 = ["a"]
    c = 0
    @s1.each do |x|
      assert_equal e1[c], x
      c += 1
    end
    assert_equal e1.size, c

    # 2
    @s1.add("b")
    e1 = ["a", "b"]
    c = 0
    @s1.each do |x|
      assert_equal e1[c], x
      c += 1
    end
    assert_equal e1.size, c

    # 3
    @s1.add("a") # duplication
    c = 0
    @s1.each do |x|
      assert_equal e1[c], x
      c += 1
    end
    assert_equal e1.size, c
  end

  def test_size
    @s1.add "a"
    assert_equal 1, @s1.size

    @s1.add "b"
    assert_equal 2, @s1.size

    @s1.add "a" # duplication
    assert_equal 2, @s1.size
  end

end
