import random
from superheros import batman, ironman, superman, captain, thor, spidey



while True:
  def get_user_name():
    name = input('What is your name?\n')
    print('Hi, %s.' % name)
    return name
  def select_hero(name):
    vowels = ['A', 'E', 'I', 'O', 'U']
    if name[0].upper() in vowels:
      superheroes = [ "Thor","Batman", "Iron Man", "Superman", "Captain America", "Spiderman"]
    else:
      superheroes = [ "Spiderman", "Superman", "Iron Man", "Captain America", "Batman", "Thor"]
    return random.choice(superheroes)
  def main():
    name = get_user_name()
    random_hero = select_hero(name)
    num = random.randint(1,17)
    print("You have to design somthing to help " + random_hero + " solve real world problem number")
    print(num)
    if random_hero == "Spiderman":
      spidey.draw()
    if random_hero == "Captain America":
      captain.draw()
    if random_hero == "Batman":
      batman.draw()
    if random_hero == "Superman":
      superman.draw()
    if random_hero == "Iron Man":
      ironman.draw()
    if random_hero == "Thor":
      thor.draw()
  if __name__ == "__main__":
    main()