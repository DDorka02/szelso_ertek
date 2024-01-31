def minimum_ertek():
    vege = 0
    db = 0
    mini = 214748
    while szam := int(input("Szám: ")) != vege:
        if szam < mini:
            mini = szam
            db += 1
    print(f"{db} számból a legkisebb: {mini}")


minimum_ertek()
