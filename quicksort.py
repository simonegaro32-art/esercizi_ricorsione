def quicksort(sequenza):
#caso terminale
    if len(sequenza) <= 1:
        return sequenza
    #caso ricorsivo
    else:
        #scelta pivot
        pivot = sequenza[0]
        #dividere sequenza secondo pivot
        sequenza_smaller=[]
        sequenza_pivot=[]
        sequenza_larger=[]
        for i in sequenza:
            #il numero è minore del pivot
            if i < pivot:
                sequenza_smaller.append(i)
            elif i == pivot:
                sequenza_pivot.append(i)
            else:
                sequenza_larger.append(i)
        return quicksort(sequenza_smaller) + sequenza_pivot + quicksort(sequenza_larger)
    #FORMA COMPATTA PER RIEMPIRE LE LISTE
    sequenza_smaller=[n for n in sequenza if n<pivot]

if __name__ == '__main__':
    sequenza = [9, 3, 2, 6, 8, 5, 199]
    print(quicksort(sequenza))