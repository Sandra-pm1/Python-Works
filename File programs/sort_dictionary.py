
placements={"python":50,"asp":23,"testing":70}

def get_value(key):
    return placements.get(key)

srt=sorted(placements,key=get_value,reverse=True)
print(srt)