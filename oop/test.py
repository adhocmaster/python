from Dog import Dog
from Animal import Animal
from datetime import date

hound = Dog( "Hound", date.today() )

print( hound );

print( hound.speak() )

print( hound.getSalePrice() )
hound.setSalePrice( 400 )
print( hound.getSalePrice() )


shephard = Dog( "shephard", date.today() )
print( shephard.getSalePrice() )
print( Dog.baseSalePrice )
print( Animal.baseSalePrice )