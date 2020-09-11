def story1():
  adjetive = input("Enter an adjetive: ")
  place = input("Enter a place: ")
  color = input("Enter a color: ")
  substance = input("Enter a substance: ")
  food = input("Enter a food: ")
  print("It's been a " + adjetive + " quarintine here in " +place+ ". The sky has been " +color+ ". The ground has been covered in " +substance+ ". We have all been survining on a steady diet of " +food+ ".")

def story2():
  name = input("Enter a name: ")
  event = input("Enter a event: ")
  Time = input("Enter a time: ")
  emotion = input("Enter a emotion: ")
  outcome = input("Enter a outcome: ")
  print("Hello my name is "+name+ ". I am preparing for the " +event+ ". I will be preparing for " +Time+ ". I'm very " +emotion+ " but I know I will " +outcome+ ".")

def randomstory():
  print(story1() , story2())    


def storypicker(sc):
  if sc=="1":
    story1()
  elif sc=="2":
    story2()
  elif (sc == "R")or(sc == "r"):
    randomstory()

def main():
  print("Choose your story:")
  storyChoice = input("Enter 1, 2, or (R)andom: ")
  storypicker(storyChoice)

if __name__=="__main__":
  main()
