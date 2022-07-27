def check_collision(object1, object2):
    o1x = object1.x
    o1y = object1.y
    o2x = object2.x
    o2y = object2.y

    o1w = object1.width
    o1h = object1.height
    o2w = object2.width
    o2h = object2.height

    if o1x < o2x + o2w and o1x + o1w > o2x and o1y < o2y + o2h and o1h + o1y > o2y:
        return True
    else:
        return False