from fractions import Fraction

## 2/3の方が大きいのでTrueになる
print(Fraction(2, 3) > Fraction(1, 2))

## 1/3の方が大きいのでFalseになる
print(Fraction(1, 3) < Fraction(1, 5))

## 約分した結果で比較するのでTrueになる
print(Fraction(2, 4) == Fraction(1, 2))
