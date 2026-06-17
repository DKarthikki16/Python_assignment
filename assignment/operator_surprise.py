"""

Q4. OPERATOR SURPRISE
    Predict the output of each line, then verify your understanding:

        print(0.1 + 0.2 == 0.3)                    # ___
        print(round(0.1 + 0.2, 10) == 0.3)         # ___
        print(True + True + False + True)           # ___
        print(2 ** 3 ** 2)                          # ___ (careful!)
        print(10 % 3 + 10 // 3)                     # ___
        print("5" + str(5))                         # ___
        print(int("10") + float("10"))              # ___
        print(bool("False"))                        # ___ (careful!)
        print(1_000 + 2_000_000)                    # ___
        print(not (True and False) == (not True) or (not False))  # ___

    For any answer that surprised you: write one sentence explaining WHY.


"""

print(0.1 + 0.2 == 0.3)                    # ___F
print(round(0.1 + 0.2, 10) == 0.3)        # ___T
print(True + True + False + True)           # ___3
print(2 ** 3 ** 2)                          # ___ 512
print(10 % 3 + 10 // 3)                     # ___4
print("5" + str(5))                         # ___"55"
print(int("10") + float("10"))              # ___20.00
print(bool("False"))                        # ___ (careful!)T
print(1_000 + 2_000_000)                    # ___2_001_000
print(not (True and False) == (not True) or (not False))  # ___T==T  so T