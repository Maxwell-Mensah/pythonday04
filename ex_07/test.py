from team import Team
from astronaut import Astronaut
from mars import Mars
import planet
mutta = Astronaut("Mutta")
hibito = Astronaut("Hibito")
serika = Astronaut("Serika")
spaceBro = Team("SpaceBrothers")
spaceBro.add(mutta)
spaceBro.add(hibito)
spaceBro.add(serika)
spaceBro.add(3)
print(spaceBro.count_members())
titi = planet.Mars()
mutta.do_actions(titi)
spaceBro.show_members()
spaceBro.remove(hibito)
print(spaceBro.count_members())
spaceBro.do_actions(titi)
