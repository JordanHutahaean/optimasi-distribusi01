def greedy(sisa, kapasitas):
    urut = sorted(kapasitas, reverse=True)

    total = 0
    pilihan = []

    while total < sisa:
        total += urut[0]
        pilihan.append(urut[0])

    kelebihan = total - sisa

    return {
        "pilihan": pilihan,
        "total": total,
        "kelebihan": kelebihan
    }