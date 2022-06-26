class evComp():
    def compEv (base, iv, ev, level, mod, stats):
        M=(((2*base) + iv (ev/4)) *(level/100))
        statMods = stats/mod
        return(((((statMods - M) * 400)) / level) / 4) * 4