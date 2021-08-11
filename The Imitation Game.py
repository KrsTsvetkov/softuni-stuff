
duma = input()
duma_list = [bukvi for bukvi in duma]
command = input().split("|")
while not command[0] == "Decode":


    if command[0] == "Move":
        num_cut = int(command[1])
        cut_bukvi = duma_list[0:num_cut]
        ost_bukvi = duma_list[num_cut:]
        new_duma = ost_bukvi + cut_bukvi
        duma_list = new_duma


    elif command[0] == "Insert":
        index_insrt = int(command[1])
        kur = [bukvi for bukvi in command[2]]
        bukva_insrt = command[2]
        duma_list.insert(index_insrt,kur)
        final_list = [j for i in duma_list for j in i ]
        duma_list = final_list
    elif command[0] == "ChangeAll":

        for n,i in enumerate(duma_list):
            if i == command[1]:
                duma_list[n] = command[2]
    command = input().split("|")
final_duma = "".join(duma_list)
print(f"The decrypted message is: {final_duma}")