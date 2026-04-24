import copy


class XExpansion:
    def __init__(self):
        self.soluzioni = []

    def calcola_list(self,input):
        self.soluzioni=[]
        self._ricorsione_list("",input)
    def _ricorsione_list(self,parziale: list, rimanenti: str):
        if len(rimanenti)==0:
            self.soluzioni.append(copy.deepcopy(parziale))
        else:
            if rimanenti[0]=="X":
                for c in["0","1"]:
                    parziale.append(c)
                    self._ricorsione_list(parziale, rimanenti[1:])
                    parziale.pop

            else:
                parziale.append(rimanenti[0])
                self._ricorsione_list(parziale, rimanenti[1:])
                

    def calcola(self, input):
        self.soluzioni=[]
        self._ricorsione("",input)



    #parziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare

    def _ricorsione(self,parziale: str, rimanenti: str):
        if len(rimanenti)==0:
            self.soluzioni.append(parziale)

        else:
            if rimanenti[0]=="X":
                self._ricorsione(parziale+"0", rimanenti[1:])
                self._ricorsione(parziale+"1", rimanenti[1:])
            else:
                self._ricorsione(parziale+rimanenti[0], rimanenti[1:])

    def x_expansion2(self, input):
        soluzioni=[]
    #parziale è la soluzione parziale
    #rimanenti sono il resto dei caratteri da esaminare

        def ricorsione(self,parziale: str, rimanenti: str):
            if len(rimanenti)==0:
                self.soluzioni.append(parziale)

            else:
                if rimanenti[0]=="X":
                    _ricorsione(parziale+"0", rimanenti[1:])
                    _ricorsione(parziale+"1", rimanenti[1:])
                else:
                    _ricorsione(parziale+rimanenti[0], rimanenti[1:])
            _ricorsione("",input)
            return soluzioni

if __name__ == '__main__':
    sequenza = "01X0X"
    xexp = XExpansion()
    xexp.calcola(sequenza)
    print(xexp.soluzioni)
    print(xexp.x_expansion2(sequenza))
    xexp.calcola_list(sequenza)
    print(xexp.soluzioni_list)