class Csincsilla:
    def __init__(self, sor:str):
        v:list[str] = sor.strip().split(';')
        self.nev:str = v[0]
        self.szul:str = v[1]
        self.suly:int = int(v[2])
        self.simi:bool = v[3] == 'I'
        self.kor:int = 2018 - int(self.szul[0:4])