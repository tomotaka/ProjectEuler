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

  def test_gcd
    assert_equal 1, gcd(1, 1)
    assert_equal 1, gcd(1, 2)
    assert_equal 2, gcd(4, 6)
    assert_equal 4, gcd(4, 8)
    assert_equal 6, gcd(6, 6)
    assert_equal 6, gcd(12, 18)
    assert_equal 3, gcd(6, 9)
    assert_equal 1, gcd(4, 9)
  end

  def test_lcm
    assert_equal 1, lcm(1, 1)
    assert_equal 6, lcm(2, 3)
    assert_equal 4, lcm(2, 4)
    assert_equal 12, lcm(3, 4)
    assert_equal 24, lcm(6, 8)
  end

  def test_is_prime?
    assert_equal false, is_prime?(1)
    assert_equal true, is_prime?(2)
    assert_equal true, is_prime?(3)
    assert_equal false, is_prime?(4)
    assert_equal true, is_prime?(5)
    assert_equal false, is_prime?(6)
    assert_equal true, is_prime?(7)
    assert_equal false, is_prime?(8)
    assert_equal false, is_prime?(9)
    assert_equal false, is_prime?(10)
    assert_equal false, is_prime?(100)
    assert_equal false, is_prime?(1000)
    assert_equal true, is_prime?(11)
    assert_equal true, is_prime?(13)
    assert_equal true, is_prime?(17)
    assert_equal true, is_prime?(19)
    assert_equal true, is_prime?(149)
    assert_equal true, is_prime?(163)
    assert_equal true, is_prime?(193)
    assert_equal true, is_prime?(211)
    assert_equal true, is_prime?(251)
    assert_equal true, is_prime?(271)
    assert_equal true, is_prime?(331)
    assert_equal true, is_prime?(373)
    assert_equal true, is_prime?(397)
    assert_equal true, is_prime?(439)
    assert_equal true, is_prime?(479)
    assert_equal true, is_prime?(491)
    assert_equal true, is_prime?(617)
    assert_equal true, is_prime?(631)
    assert_equal true, is_prime?(683)
    assert_equal true, is_prime?(709)
    assert_equal true, is_prime?(757)
    assert_equal true, is_prime?(787)
    assert_equal true, is_prime?(811)
    assert_equal true, is_prime?(829)
    assert_equal true, is_prime?(839)
    assert_equal true, is_prime?(937)
    assert_equal true, is_prime?(953)
    assert_equal true, is_prime?(919)
  end

end
