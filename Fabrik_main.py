class Chocolate:
 def __init__(self, name):
 self.name = name
 
 def __str__(self):
 return self._name

class Candies:
 def __init__(self, name):
 self.name = name

 def __str__(self):
 return self._name

class WhiteChocolate(Chocolate):
 def method_1(self):
 print(f"White Chocolate ({self.name})")

class WhiteCandies(Candies):
 def method_1(self):
 print(f"White Candies ({self.name})")

class BitterChocolate(Chocolate):
 def method_1(self):
 print(f"Bitter Chocolate ({self.name})")

class BitterCandies(Candies):
 def method_1(self):
 print(f"Bitter Candies ({self.name})")

class ChocolateFactory:
 
 def create_Chocolate(self):
 pass

 def create_Candies(self):
 pass

class BitterChocolateFactory(ChocolateFactory):
 
 def create_Chocolate(self, name):
 return BitterChocolate(name)

 def create_Candies(self, name):
 return BitterCandies(name)

class WhiteChocolateFactory(ChocolateFactory):
 
 def create_Chocolate(self, name):
 return WhiteChocolate(name)

 def create_Candies(self, name):
 return WhiteCandies(name)


Bitter_factory =BitterChocolateFactory()
Bitter_Chocolate = Bitter_factory.create_Chocolate("Chocolate 'HUG'-k")
Bitter_Candies = Bitter_factory.create_Candies("Bitter Candies ")
Bitter_Chocolate.method_1() 
Bitter_Candies.method_1()

White_factory = WhiteChocolateFactory()
White_Chocolate = White_factory.create_Chocolate("Chocolate 'HUG'-g")
White_Candies = White_factory.create_Candies("White Candies")
White_Chocolate.method_1() 
White_Candies.method_1()