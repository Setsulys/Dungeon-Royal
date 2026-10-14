from dungeon.generator.dungeon_elements.entities import Monster,Skill


#Skills
bump = Skill("Bump", damage=8)
dague = Skill("Coup de Dague", damage=8)
flee = Skill("Jet de pierre et fuite", damage=3)
claw = Skill("claw", damage=15)

#Healing effects
life_drain = Skill("Life drain", damage=8)

#With effects
breath = Skill("Fire Breath", damage=40)
fire_ball = Skill("Fire ball", damage=20)
ice_spear = Skill("ice spear", damage=12)
thunderbolt = Skill("Thunderbolt",damage=25)

# Status effects





# Slime
slime = Monster("Slime",level=1, health=50, speed=14, atk=5)
slime.learn_monster_skill(bump,chance=100)


# Gobelin
goblin = Monster("Gobelin",level=5, health=50, speed=14, atk=5)
goblin.learn_monster_skill(dague, chance=20)
goblin.learn_monster_skill(flee, chance=80)


# Lich
lich = Monster("lich",level=45, health=50, speed=14, atk=5)
lich.learn_monster_skill(life_drain, chance=20)
lich.learn_monster_skill(fire_ball, chance=80)

# Dragon
dragon = Monster("Arch Dragon",level=100, health=200, speed=8, atk=15)
dragon.learn_monster_skill(claw, chance=70)
dragon.learn_monster_skill(breath, chance=30)






