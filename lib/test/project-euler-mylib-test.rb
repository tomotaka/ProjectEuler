here = File.dirname(__FILE__)
lib = File.expand_path("../project-euler-mylib.rb", here)
require(lib)
require "test/unit"

class Test_ProjectEulerMyLib < Test::Unit::TestCase

  def setup
  end

  def teardown
  end

  def test_factors
    assert_equal [1], factors(1)
    assert_equal [2], factors(2)
    assert_equal [3], factors(3)
    assert_equal [2, 2], factors(4)
    assert_equal [5], factors(5)
    assert_equal [2, 3], factors(6)
    assert_equal [7], factors(7)
    assert_equal [2, 2, 2], factors(8)
    assert_equal [3, 3], factors(9)
    assert_equal [2, 5], factors(10)
  end

end
