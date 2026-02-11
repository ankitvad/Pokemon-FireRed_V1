tmp = '''
cheat0_address = "0"
cheat0_address_bit_position = "0"
cheat0_big_endian = "false"
cheat0_cheat_type = "1"
cheat0_code = "82003884 0000"
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
0121 = TM01 (Focus Punch)
0122 = TM02 (Dragon Claw)
0123 = TM03 (Water Pulse)
0124 = TM04 (Calm Mind)
0125 = TM05 (Roar)
0126 = TM06 (Toxic)
0127 = TM07 (Hail)
0128 = TM08 (Bulk Up)
0129 = TM09 (Bullet Seed)
012A = TM10 (Hidden Power)
012B = TM11 (Sunny Day)
012C = TM12 (Taunt)
012D = TM13 (Ice Beam)
012E = TM14 (Blizzard)
012F = TM15 (Hyper Beam)
0130 = TM16 (Light Screen)
0131 = TM17 (Protect)
0132 = TM18 (Rain Dance)
0133 = TM19 (Giga Drain)
0134 = TM20 (Safeguard)
0135 = TM21 (Frustration)
0136 = TM22 (Solar Beam)
0137 = TM23 (Iron Tail)
0138 = TM24 (Thunderbolt)
0139 = TM25 (Thunder)
013A = TM26 (Earthquake)
013B = TM27 (Return)
013C = TM28 (Dig)
013D = TM29 (Psychic)
013E = TM30 (Shadow Ball)
013F = TM31 (Brick Break)
0140 = TM32 (Double Team)
0141 = TM33 (Reflect)
0142 = TM34 (Shock Wave)
0143 = TM35 (Flamethrower)
0144 = TM36 (Sludge Bomb)
0145 = TM37 (Sandstorm)
0146 = TM38 (Fire Blast)
0147 = TM39 (Rock Tomb)
0148 = TM40 (Aerial Ace)
0149 = TM41 (Torment)
014A = TM42 (Facade)
014B = TM43 (Secret Power)
014C = TM44 (Rest)
014D = TM45 (Attract)
014E = TM46 (Thief)
014F = TM47 (Steel Wing)
0150 = TM48 (Skill Swap)
0151 = TM49 (Snatch)
0152 = TM50 (Overheat)
0153 = HM01 (Cut)
0154 = HM02 (Fly)
0155 = HM03 (Surf)
0156 = HM04 (Strength)
0157 = HM05 (Flash)
0158 = HM06 (Rock Smash)
0159 = HM07 (Waterfall)
015A = HM08 (Dive)
015D = Oak’s Parcel
015E = Poke Flute
015F = Secret Key
0160 = Bike Voucher
0161 = Gold Teeth
0162 = Old Amber
0163 = Card Key
0164 = Elevator Key
0165 = Dome Fossil
0166 = Helix Fossil
0167 = Silph Scope
0168 = Bicycle
0169 = Town Map
016A = Battle Searcher
016B = Voice Checker
016C = TM Case
016D = Berry Bag
016E = Help TV
016F = Tri-Pass
0170 = Rainbow Pass
0171 = Tea
0172 = Mystery Ticket
0173 = Aurora Ticket
0174 = Konaire
0175 = Ruby Plate
0176 = Sapphire Plate
01F4 = Jail Key
01F5 = Elevator Key
01F6 = Small Tablet
01F7 = F-Disk
01F8 = R-Disk
01F9 = L-Disk
01FA = D-Disk
01FB = you-Disk
01FC = Subway Key
01FD = Maingate Key
01FE = Card Key
01FF = Down St Key
0200 = DNA Sample 1
0201 = Bayleef DNA
0202 = DNA Sample 2
0203 = Quilava DNA
0204 = DNA Sample 3
0205 = Croconaw DNA
0206 = DNA Sample 4
0207 = Sudowoodo DNA
0208 = DNA Sample 5
0209 = Misdreavus DNA
020A = DNA Sample 6
020B = Mightyena DNA
020C = DNA Sample 7
020D = Raikou DNA
020E = DNA Sample 8
020F = Entei DNA
0210 = DNA Sample 9
0211 = Suicune DNA
0212 = Data ROM
0213 = Steel Teeth
0214 = Gear
0215 = Red ID Badge
0216 = Green ID Badge
0217 = Blue ID Badge
0218 = Yellow ID Badge
0219 = Time Flute
021A = Ein File S
021B = Ein File H
021C = Ein File C
021D = Ein File P
021E = Cologne Case
021F = Joy Scent
0220 = Excite Scent
0221 = Vivid Scent
0222 = Powerup Part
0223 = Ein File F
'''

op_str = 'cheat0_address = "0"\n'

all_vals = all_vals.strip().split("\n")
cnt = 0

flag = "cheat0_"

for a in all_vals:
	new_flag = flag.replace("0",str(cnt))
	o = tmp.replace(flag,new_flag)
	a = a.strip()
	a = a.split(' = ')
	assert(len(a) == 2)
	o = o.replace('"82003884 0000"', '"82003884 '+a[0]+'"')
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