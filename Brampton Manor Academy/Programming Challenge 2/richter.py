richter = [["1",1], ["5",5], ["indonesia_04",9.1], ["alaksa_64",9.2], ["chile_60",9.5]]

print("Richter " + " "*15 + "Joules " + " "*15 + "TNT" )
for i in range(len(richter)):
    exponent = 1.5 * (richter[i][1]) + 4.8
    energy = 10**(exponent)
    TNT = energy / (4.184 * 10**9)
    print(str(richter[i][1]) + " "*15 + str(energy) + " "*10 + str(TNT))

def calc_user_richt():
    user_Richter = float(input("Please enter a Richter scale value: "))
    print("Richter value: " + str(user_Richter))
    user_exponent = 1.5 * user_Richter + 4.8
    energy_user = 10**user_exponent
    tnt_user = energy_user / (4.184 * 10**9)
    print(f"Equivalence in joules: {energy_user}")
    print(f"Equivalence in tons of TNT: {tnt_user}")
