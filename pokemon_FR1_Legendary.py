tmp = '''
cheat0_address = "0"
cheat0_address_bit_position = "0"
cheat0_big_endian = "false"
cheat0_cheat_type = "1"
cheat0_code = "83007CEE 0000"
cheat0_desc = "NAME_HERE"
cheat0_enable = "false"
cheat0_handler = "0"
cheat0_memory_search_size = "3"
cheat0_repeat_add_to_address = "1"
cheat0_repeat_add_to_value = "0"
cheat0_repeat_count = "1"
cheat0_rumble_port = "0"
cheat0_rumble_primary_duration = "0"
cheat0_rumble_primary_strength = "0"
cheat0_rumble_secondary_duration = "0"
cheat0_rumble_secondary_strength = "0"
cheat0_rumble_type = "0"
cheat0_rumble_value = "0"
cheat0_value = "0"
'''

all_vals = '''
0090 = Articuno
0091 = Zapdos
0092 = Moltres
0093 = Dratini
0094 = Dragonair
0095 = Dragonite
0096 = Mewtwo
0199 = Jirachi
0191 = Regirock
0192 = Regice
0193 = Registeel
0195 = Groudon
0097 = Mew
019A = Deoxys
00F4 = Entei
00F9 = Lugia
00FA = Ho-oh
0196 = Rayquaza
'''

op_str = '''
cheat0_address = "0"
cheat0_address = "0"
cheat0_address_bit_position = "0"
cheat0_big_endian = "false"
cheat0_cheat_type = "1"
cheat0_code = "000014D1 000A+1003DAE6 0007"
cheat0_desc = "Pre - Legend"
cheat0_enable = "false"
cheat0_handler = "0"
cheat0_memory_search_size = "3"
cheat0_repeat_add_to_address = "1"
cheat0_repeat_add_to_value = "0"
cheat0_repeat_count = "1"
cheat0_rumble_port = "0"
cheat0_rumble_primary_duration = "0"
cheat0_rumble_primary_strength = "0"
cheat0_rumble_secondary_duration = "0"
cheat0_rumble_secondary_strength = "0"
cheat0_rumble_type = "0"
cheat0_rumble_value = "0"\n
'''

all_vals = all_vals.strip().split("\n")
cnt = 1

flag = "cheat0_"

for a in all_vals:
	new_flag = flag.replace("0",str(cnt))
	o = tmp.replace(flag,new_flag)
	a = a.strip()
	a = a.split(' = ')
	assert(len(a) == 2)
	o = o.replace('"83007CEE 0000"', '"83007CEE '+a[0]+'"')
	o = o.replace('NAME_HERE', a[1])
	op_str += o + "\n"
	cnt += 1


op_str = op_str.split("\n")
op_str = [i for i in op_str if i]
op_str = "\n".join(op_str)
op_str = op_str + '\ncheats = ' + '"' + str(cnt) +'"'

'''
opFL = open("PFR1_Pokemart.cht","w")
tmp = opFL.write(op_str)
opFL.close()
'''
print(op_str)