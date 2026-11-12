from dungeon.generator.dungeon_elements.entities import Monster,Skill


#Skills
BUMP = Skill("Bump", damage=8)
dague = Skill("Coup de Dague", damage=8)
ROCK_AND_FLEE = Skill("Jet de pierre et fuite", damage=3)
CLAW = Skill("claw", damage=15)
SWORD_SLASH = Skill("Sword_slash",damage=15)
AXE_SLASH =  Skill("Axe Slash",damage=25)

#Healing effects
LIFE_DRAIN = Skill("Life drain", damage=8)

#With effects
FIRE_BREATH = Skill("Fire Breath", damage=40)
FIRE_BALL = Skill("Fire ball", damage=20)
ICE_SPEAR = Skill("ice spear", damage=12)
THUNDERBOLT = Skill("Thunderbolt",damage=25)
REGEN = Skill("Regeneration",damage=0)
# Status effects


# Slime
SLIME = Monster("Slime",level=1, health=2, speed=14, atk=1)
SLIME.learn_monster_skill(BUMP,chance=100)


# Gobelin
GOBLIN = Monster("Gobelin",level=5, health=50, speed=14, atk=5)
GOBLIN.learn_monster_skill(dague, chance=20)
GOBLIN.learn_monster_skill(BUMP, chance=80)

#Skeleton
SKELETTON=Monster("Skeleton",level=10,health=12,speed=12,atk=25)
SKELETTON.learn_monster_skill(SWORD_SLASH,chance=100)

#Minautorus
MINAUTOR=Monster("Minautor",level=20,health=85,speed=12,atk=25)
MINAUTOR.learn_monster_skill(AXE_SLASH,chance=100)


# Lich
LICH = Monster("lich",level=45, health=50, speed=14, atk=5)
LICH.learn_monster_skill(LIFE_DRAIN, chance=20)
LICH.learn_monster_skill(FIRE_BALL, chance=80)

# Dragon
DRAGON = Monster("Arch Dragon",level=100, health=200, speed=8, atk=15)
DRAGON.learn_monster_skill(CLAW, chance=70)
DRAGON.learn_monster_skill(FIRE_BREATH, chance=30)






