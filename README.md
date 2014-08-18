#after collision detect with everything done, do 
smooth collision detection, to slowly push entities away from eachother

todo
perfect collision detection

Make collision detection have a predicted position to move entities to, then take average of all entities and move

bounciness for entities

transfer momentum based on weight and bounciness (almost done -bounciness)

include bounciness in coll detec

calculate collision detection based on size, inertia, and position instead of just inertia and position

eventually include friction 

make collision detection check for if the entity exists, if no, pass

when entities are deleted use entity_table.remove[NUMBER] for easy dynamic deletion and additions
