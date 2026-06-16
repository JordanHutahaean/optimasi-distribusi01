def branch_and_bound(sisa, kapA, kapB, kapC):
    best_total = 999999
    best_kelebihan = 999999

    best_a = best_b = best_c = 0

    for a in range(0, 6):
        for b in range(0, 6):
            for c in range(0, 6):

                total = (a * kapA) + (b * kapB) + (c * kapC)

                if total >= sisa:
                    kelebihan = total - sisa

                    if kelebihan < best_kelebihan:
                        best_kelebihan = kelebihan
                        best_total = total

                        best_a = a
                        best_b = b
                        best_c = c

    return {
        "kombinasi": [f"A={best_a}", f"B={best_b}", f"C={best_c}"],
        "total": best_total,
        "kelebihan": best_kelebihan
    }