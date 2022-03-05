class PartyCounter:

    limit = 50
    partyCounter = 0

    def __init__(self, limit=None, partyCounter=None):
        self.limit = limit if limit is not None else self.limit
        self.partyCounter = (
            partyCounter if partyCounter is not None else self.partyCounter
        )

    def party(self, partySize=1):
        if self.limit - partySize < 0:
            print("not available space")
            return None
        self.partyCounter += partySize
        self.limit -= partySize
        print("So far", self.partyCounter)
        print("So near", self.limit)


pc = PartyCounter(100)
pc.party()
pc.party()
pc.party()


class FuncionsParty(PartyCounter):
    def party_out(self, partySize=1):
        self.limit += partySize
        print("The available space is:", self.limit)


fp = FuncionsParty(10)
fp.party()
fp.party_out()
fp.party(5)
fp.party(6)
