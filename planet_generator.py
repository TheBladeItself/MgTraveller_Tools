#!/usr/bin/env python3

# TO DO --------------------------------------------
# * Make the System gen generate satellites using the rules from:
# https://wiki.rpg.net/index.php/RTT_Worldgen#Telluric

#===================
# Imports
#===================

import tkinter as tk
from tkinter import ttk
from random import randint
from tkinter import scrolledtext

def dice(number_of_dice, mod=0, sides=6):
	x = 0
	for i in range(0,number_of_dice):
		t = randint(1,sides)
		x += t
	x += mod
	return x
	
# Create Instance
win = tk.Tk()

# Add a title
win.title("System Generator GUI")

tabControl = ttk.Notebook(win)			# Create tab control
tab1 = ttk.Frame(tabControl)			# Create a tab
tabControl.add(tab1, text='World Gen')		# Add to the tab
tab2 = ttk.Frame(tabControl)			# Create a tab
tabControl.add(tab2, text='Alien Gen')		# Add to the tab
tabControl.pack(expand=1, fill='both')	# Pack to make visible

# Button Click Event Function
def system_gen_click():
	s = dice(2, mod=-2)
	size.set(s)
	s_mod = int(size.get())
	
	a = dice(2, mod=-7)
	a += int(s_mod)
	if a < 0: a = 0	
	atmo.set(a)
	a_mod = int(atmo.get())
	
	t = dice(2)
	if a_mod == 2 or a_mod == 3: t -= 2
	elif a_mod == 4 or a_mod == 5 or a_mod == 14: t -= 1
	elif a_mod == 8 or a_mod == 9: t += 1
	elif a_mod == 10 or a_mod == 13 or a_mod == 15: t += 2
	elif a_mod == 11 or a_mod == 12: t += 6
	temp.set(t)
	t_mod = int(temp.get())
	
	h = dice(2)
	if s_mod < 2: h == 0
	if a_mod < 2 or a_mod == 10 or a_mod == 11 or a_mod == 12: h -= 4
	if t_mod == 10 or t_mod == 11: h -= 2
	elif t_mod > 11: h -= 6
	if h < 0: h = 0
	hydr.set(h)
	h_mod = int(hydr.get())
	
	p = dice(2, mod=-2)
	popu.set(p)
	p_mod = int(popu.get())
	
	g = dice(2, mod=-7)
	g += p_mod
	if g < 0: g = 0
	if p_mod == 0: g = 0
	gove.set(g)
	g_mod = int(gove.get())
	
	l = dice(2, mod=-7)
	l += g_mod
	if l < 0: l = 0
	if g_mod == 0: l = 0
	lawl.set(l)
	l_mod = int(lawl.get())
	
	sp = dice(2)
	if sp < 3: sp = 'X'
	elif sp == 3 or sp == 4: sp = 'E'
	elif sp == 5 or sp == 6: sp = 'D'
	elif sp == 7 or sp == 8: sp = 'C'
	elif sp == 9 or sp == 10: sp = 'B'
	elif sp >= 11: sp = 'A'
	sppt.set(sp)
	sp_mod = sppt.get()
	
	t = dice(1)
	if sp_mod == 'X': t -= 4
	elif sp_mod == 'C': t += 2
	elif sp_mod == 'B': t += 4
	elif sp_mod == 'A': t += 6
	if s_mod <= 1: t += 2
	elif s_mod >= 2 and s_mod <= 4: t += 1
	if a_mod <= 3: t += 1
	elif a_mod >= 10: t += 1
	if h_mod == 0 or h_mod == 9: t += 1
	elif h_mod == 10: t += 2
	if h_mod > 0 and h_mod < 6: t += 1
	elif h_mod == 9: t += 1
	elif h_mod == 10: t += 2
	elif h_mod == 11: t += 3
	elif h_mod == 12: t += 4
	if g_mod == 0 or g_mod == 5: t += 1
	elif g_mod == 7: t += 2
	elif g_mod == 13 or g_mod == 14: t -= 2
	tech.set(t)
	tc_mod = int(tech.get())
	
	if s_mod == 10: code_size = 'A'
	else: code_size = s_mod
	
	if a_mod == 10: code_atmo = 'A'
	elif a_mod == 11: code_atmo = 'B'
	elif a_mod == 12: code_atmo = 'C'
	elif a_mod == 13: code_atmo = 'D'
	elif a_mod == 14: code_atmo = 'E'
	elif a_mod == 15: code_atmo = 'F'
	else: code_atmo = a_mod
	
	if t_mod == 10: code_temp = 'A'
	elif t_mod == 11: code_temp = 'B'
	elif t_mod == 12: code_temp = 'C'
	else: code_temp = t_mod
	
	if h_mod == 10: code_hydr = 'A'
	elif h_mod == 11: code_hydr = 'B'
	elif h_mod >= 12: code_hydr = 'C'
	else: code_hydr=h_mod
	
	if p_mod == 10: code_popu = 'A'
	elif p_mod == 11: code_popu = 'B'
	elif p_mod >= 12: code_popu = 'C'
	else: code_popu = p_mod
	
	if g_mod == 10: code_gove = 'A'
	elif g_mod == 11: code_gove = 'B'
	elif g_mod == 12: code_gove = 'C'
	elif g_mod == 13: code_gove = 'D'
	elif g_mod == 14: code_gove = 'E'
	elif g_mod == 15: code_gove = 'F' 
	else: code_gove = g_mod
	
	if l_mod == 10: code_gove = 'A'
	elif l_mod == 11: code_lawl = 'B'
	elif l_mod == 12: code_lawl = 'C'
	elif l_mod == 13: code_lawl = 'D'
	elif l_mod == 14: code_lawl = 'E'
	elif l_mod == 15: code_lawl = 'F' 
	else: code_lawl = l_mod
	
	c = sppt.get() + str(code_size) + str(code_atmo) + str(code_temp) + str(code_hydr) + str(code_popu) + str(code_gove) + str(code_lawl) + "-" + str(tech.get())
	code.set(c)
	
	h = dice(3)
	if h >= 17: h = 'Yes'
	else: h = 'No'
	home.set(h)
	
	bn = dice(2)
	bs = dice(2)
	br = dice(2)
	bt = dice(2)
	bc = dice(2)
	bp = dice(2)
	b = ''
	po = sppt.get()
	if po == 'A':
		if bn >= 8:	b = b + 'N'
		if bs >= 10:b = b + 'S'
		if br >= 8:	b = b + 'R'
		if bt >= 4:	b = b + 'T'
		if bc >= 6:	b = b + 'C'
	elif po == 'B':
		if bn >= 8:	b = b + 'N'
		if bs >= 8:	b = b + 'S'
		if br >= 10:b = b + 'R'
		if bt >= 6:	b = b + 'T'
		if bc >= 8:	b = b + 'C'
		if bp >= 12:b = b + 'P'
	elif po == 'C':
		if bs >= 8:	b = b + 'S'
		if br >= 10:b = b + 'R'
		if bt >= 10:b = b + 'T'
		if bc >= 10:b = b + 'C'
		if bp >= 10:b = b + 'P'
	elif po == 'D':
		if bs >= 7:	b = b + 'S'
		if bp >= 12:b = b + 'P'
	elif po == 'E':
		if bp >= 12:b = b + 'P'
	base.set(b)
	
	aw = 'No'
	if g_mod == 0 or g_mod == 7 or g_mod == 'A': aw = 'Yes'
	if l_mod == 0 or l_mod == 9: aw = 'Yes'
	ambe.set(aw)
	
	tgs = ""
	if a_mod >= 4 and a_mod <= 9 and h_mod >= 4 and h_mod <= 8 and p_mod >= 5 and p_mod <= 7: tgs = tgs + "Ag "
	if s_mod == 0 and a_mod == 0 and h_mod == 0: tgs = tgs + "As "
	if p_mod == 0 and g_mod and l_mod == 0: tgs = tgs + "Ba "
	if a_mod >= 2 and h_mod == 0: tgs = tgs + "De "
	if a_mod >= 10 and h_mod >= 1: tgs = tgs + "Fl "
	if s_mod >= 5 and a_mod >= 4 and a_mod <= 9 and h_mod >= 4 and h_mod <= 8: tgs = tgs + "Ga "
	if p_mod >= 9: tgs = tgs + "Hi "
	if tc_mod >= 12: tgs = tgs + "Ht "
	if a_mod <= 1 and p_mod >= 1: tgs = tgs + "IC "
	if a_mod <= 2 and p_mod >= 9: tgs = tgs + "In "
	if a_mod == 4 and p_mod >= 9: tgs = tgs + "In "
	if a_mod == 7 and p_mod >= 9: tgs = tgs + "In "
	if a_mod == 9 and p_mod >= 9: tgs = tgs + "In "
	if p_mod <= 3 and p_mod >= 1: tgs = tgs + "Lo "
	if tc_mod <= 5: tgs = tgs + "Lt "
	if a_mod <= 3 and h_mod <= 3 and p_mod >= 6: tgs = tgs + "Na "
	if p_mod <= 6 and p_mod >= 4: tgs = tgs + "NI "
	if a_mod >= 2 and a_mod <= 5 and h_mod <= 3: tgs = tgs + "Po "
	if a_mod == 6 and p_mod <= 8 and p_mod >= 6: tgs = tgs + "Ri "
	if a_mod == 8 and p_mod <= 8 and p_mod >= 6: tgs = tgs + "Ri "
	if a_mod == 0: tgs = tgs + "Va "
	if h_mod == 10: tgs = tgs + "Wa "
	tags.set(tgs)

# Labelframe using tab1 as parent
mighty = ttk.LabelFrame(tab1, text = ' System Generator ')
mighty.grid(column=0, row=0, padx=8, pady=4)

# Labels
ttk.Label(mighty, width=12, text="System Name:").grid(column=0, row=0, sticky='W')
ttk.Label(mighty, width=12, text="Co-ordinates:").grid(column=2, row=0, sticky='W')

ttk.Label(mighty, width=12, text="Size:").grid(column=0, row=1, sticky='W')
ttk.Label(mighty, width=12, text="Atmosphere:").grid(column=2, row=1, sticky='W')

ttk.Label(mighty, width=12, text="Temperature:").grid(column=0, row=2, sticky='W')
ttk.Label(mighty, width=12, text="Hydrography:").grid(column=2, row=2, sticky='W')

ttk.Label(mighty, width=12, text="Population:").grid(column=0, row=3, sticky='W')
ttk.Label(mighty, width=12, text="Government:").grid(column=2, row=3, sticky='W')

ttk.Label(mighty, width=12, text="Law level:").grid(column=0, row=4, sticky='W')
ttk.Label(mighty, width=12, text="Space Port:").grid(column=2, row=4, sticky='W')

ttk.Label(mighty, width=12, text="Tech Level:").grid(column=0, row=5, sticky='W')
ttk.Label(mighty, width=12, text="UWP Code:").grid(column=2, row=5, sticky='W')

ttk.Label(mighty, width=12, text="Potential Homeworld:").grid(column=0, row=6, sticky='W')
ttk.Label(mighty, width=12, text="Bases:").grid(column=2, row=6, sticky='W')

ttk.Label(mighty, width=12, text="Amber World:").grid(column=0, row=7, sticky='W')
ttk.Label(mighty, width=12, text="Tags:").grid(column=2, row=7, sticky='W')

# Adding a button
action = ttk.Button(mighty, text="Generate", command=system_gen_click).grid(column=5, row=0)
	
# Text Box
name = tk.StringVar()
coord = tk.StringVar()
size = tk.StringVar()
atmo = tk.StringVar()
temp = tk.StringVar()
hydr = tk.StringVar()
popu = tk.StringVar()
gove = tk.StringVar()
lawl = tk.StringVar()
sppt = tk.StringVar()
tech = tk.StringVar()
code = tk.StringVar()
home = tk.StringVar()
base = tk.StringVar()
ambe = tk.StringVar()
tags = tk.StringVar()

name_entered = ttk.Entry(mighty, width=12, textvariable=name).grid(column=1, row=0, sticky=tk.W)
coord_entered = ttk.Entry(mighty, width=12, textvariable=coord).grid(column=3, row=0, sticky=tk.W)

size_gen = ttk.Entry(mighty, width=12, textvariable=size, state='readonly')
size_gen.grid(column=1, row=1, sticky=tk.W)
atmo_gen = ttk.Entry(mighty, width=12, textvariable=atmo, state='readonly')
atmo_gen.grid(column=3, row=1, sticky=tk.W)

temp_gen = ttk.Entry(mighty, width=12, textvariable=temp, state='readonly')
temp_gen.grid(column=1, row=2, sticky=tk.W)
hydr_gen = ttk.Entry(mighty, width=12, textvariable=hydr, state='readonly')
hydr_gen.grid(column=3, row=2, sticky=tk.W)

popu_gen = ttk.Entry(mighty, width=12, textvariable=popu, state='readonly')
popu_gen.grid(column=1, row=3, sticky=tk.W)
gove_gen = ttk.Entry(mighty, width=12, textvariable=gove, state='readonly')
gove_gen.grid(column=3, row=3, sticky=tk.W)

lawl_gen = ttk.Entry(mighty, width=12, textvariable=lawl, state='readonly')
lawl_gen.grid(column=1, row=4, sticky=tk.W)
sppt_gen = ttk.Entry(mighty, width=12, textvariable=sppt, state='readonly')
sppt_gen.grid(column=3, row=4, sticky=tk.W)

tech_gen = ttk.Entry(mighty, width=12, textvariable=tech, state='readonly')
tech_gen.grid(column=1, row=5, sticky=tk.W)
code_gen = ttk.Entry(mighty, width=12, textvariable=code, state='readonly')
code_gen.grid(column=3, row=5, sticky=tk.W)

home_gen = ttk.Entry(mighty, width=12, textvariable=home, state='readonly')
home_gen.grid(column=1, row=6, sticky=tk.W)
base_gen = ttk.Entry(mighty, width=12, textvariable=base, state='readonly')
base_gen.grid(column=3, row=6, sticky=tk.W)

ambe_gen = ttk.Entry(mighty, width=12, textvariable=ambe, state='readonly')
ambe_gen.grid(column=1, row=7, sticky=tk.W)
tags_gen = ttk.Entry(mighty, width=12, textvariable=tags, state='readonly')
tags_gen.grid(column=3, row=7, sticky=tk.W)

# Tab 2 -----------------------------------------------------------------
mighty2 = ttk.LabelFrame(tab2, text = ' Alien Generator ')
mighty2.grid(column=0, row=0, padx=8, pady=4, columnspan=2)

def transfer_val():
	size_c.set(int(size.get()))
	atmo_c.set(int(atmo.get()))
	hydr_c.set(int(hydr.get()))
	temp_c.set(int(temp.get()))
	

def creature_gen():
	scrol.delete('1.0', tk.END)
	trait_qty = 0
	
	wsiz = int(size_c.get())
	if wsiz == 0: 
		c_s = "Zero-Gravity Adaptation & Gravity Intolerance"
		trait_qty += 2
	elif wsiz >= 1 and wsiz <= 3: 
		c_s = "Low Gravity Adaptation & Gravity Intolerance"
		trait_qty += 2
	elif wsiz >= 4 and wsiz <= 6: 
		c_s = "Low Gravity Adaptation"
		trait_qty += 1
	elif wsiz >= 10: 
		c_s = "Heavy Gravity Adaptation"
		trait_qty += 1
	else: c_s = ""
	if c_s is not "": scrol.insert(tk.INSERT, c_s + '\n')
	
	watm = int(atmo_c.get())
	if watm == 0: c_a = "Vacuum Survival"
	elif watm == 1:
		c = dice(2)
		if c > 11: 
			c_a = "Trace Breather & Vacuum Survival, Limited"
			trait_qty += 2
		else: 
			c_a = "Trace Breather"
			trait_qty += 1
	elif watm == 2:
		c = dice(2)
		d = dice(2)
		if d >= 9:
			if c > 11: 
				c_a = "Trace Breather & Taint Immunity & Vacuum Survival, Limited"
				trait_qty += 3
			else: 
				c_a = "Trace Breather, Limited & Taint Immunity"
				trait_qty += 2
		else:
			if c > 11: 
				c_a = "Trace Breather & Tainted Breather & Vacuum Survival, Limited"
				trait_qty += 3
			else: 
				c_a = "Trace Breather, Limited & Tainted Breather"
				trait_qty += 2
	elif watm == 3:
		c = dice(2)
		if c > 11: 
			c_a = "Trace Breather & Vacuum Survival, Limited"
			trait_qty += 2
		else: 
			c_a = "Trace Breather, Limited"
			trait_qty += 1
	elif watm == 10 or watm == 'A': 
		c_a = "Atmospheric Requirements"
		trait_qty += 1
	elif watm == 11 or watm == 'B': 
		c_a = "Atmospheric Requirements"
		trait_qty += 1
	elif watm == 12 or watm == 'C': 
		c_a = "Atmospheric Requirements"
		trait_qty += 1
	elif watm == 4 or watm == 7 or watm == 9:
		c = dice(2)
		if c >= 9: 
			c_a = "Taint Immunity"
			trait_qty += 1
		else: 
			c_a = "Tainted Breather"
			trait_qty += 1
	else: c_a = ""
	if c_a is not "": scrol.insert(tk.INSERT, c_a + '\n')
	
	whyd = int(hydr_c.get())
	if whyd == 0: 
		c_h = "Desert Adaptation"
		trait_qty += 1
	elif whyd == 10 or whyd == 'A':
		c = dice(2)
		if c < 10: 
			c_h = "Aquatic & Natural Swimmer"
			trait_qty += 2
		else:
			d = dice(2)
			if d < 6: 
				c_h = "Aquatic & Natural Swimmer & Amphibious"
				trait_qty += 3
			else: 
				c_h = "Aquatic & Natural Swimmer & Amphibious & Water Dependent"
				trait_qty += 4
	else: c_h = ""
	if c_h is not "": scrol.insert(tk.INSERT, c_h + '\n')
	
	wcli = int(temp_c.get())
	if wcli <= 3: 
		c_t = "Cold Endurance & Cold Resistance & Fire Vulnerability"
		trait_qty += 3
	elif wcli == 4 or wcli == 5: 
		c_t = "Cold Endurance"
		trait_qty += 1
	elif wcli == 9 or wcli == 10: 
		c_t = " Heat Endurance"
		trait_qty += 1
	elif wcli >= 11: 
		c_t = "Heat Endurance & Fire Resistance & Cold Vulnerability"
		trait_qty += 3
	else: c_t = ""
	if c_t is not "": scrol.insert(tk.INSERT, c_t + '\n')
	
	pr = dice(2)
	st = dice(2)
	if pr <= 3:
		if st == 2: et = "Scavenger/Reducer"
		elif st == 3 or st == 4: et = "Scavenger/Hijacker"
		elif st >= 3 and st <= 9: et = "Scavenger/Intimidator"
		else: et = "Scavenger/Carrion-eater"
	elif pr == 4 or pr == 5 or pr == 10:
		if st <= 3: et = "Herbivore/Filter"
		elif st >= 4 and st <= 7: et = "Herbivore/Intermittent"
		elif st >= 8: et = "Herbivore/Grazer"
	elif pr >= 11:
		if st <= 4: et = "Carnivore/Pouncer"
		elif st == 5: et = "Carnivore/Trapper"
		elif st >= 6 and st <= 9: et = "Carnivore/Chaser"
		elif st == 10: et = "Carnivore/Siren"
		elif st >= 11: et = "Carnivore/Killer"
	else:
		if st <= 4: et = "Omnivore/Gatherer"
		if st >= 5 and st <= 9: et = "Omnivore/Hunter"
		if st >= 10: et = "Omnivore/Eater"
	ecty.set(et)
	
	metabolism = dice(2)
	if metabolism >= 11: metabolism = 'Cold-Blooded'
	else: metabolism = 'Warm-Blooded'
	meta.set(metabolism)
	
	gender = dice(2)
	if gender == 2: gender = 'Asexual'
	elif gender == 3 or gender == 4: gender = 'Hermaphroditic'
	elif gender == 12:
		g_num = dice(1, mod=1)
		gm = dice(2)
		if gm == 12: gender = str(g_num) + " genders (gendermorphic)"
		else: gender = str(g_num) + " genders"
	else: 
		gm = dice(2)
		if gm == 12: gender = "2 genders (gendermorphic)"
		else: gender = "2 genders"
	gend.set(gender)
	
	reproduction = dice(2)
	if gender == 'Asexual': reproduction -= 3
	if metabolism == 'Cold-Blooded': reproduction += 3
	if reproduction <= 2: reproduction = 'External Budding'
	elif reproduction >= 9: reproduction = 'Egg-laying'
	else: reproduction = 'Live-bearing'
	rprd.set(reproduction)
	
	respiration = dice(2, mod=2)
	resp_mod = 0
	if int(hydr_c.get()) >= 8 and int(hydr_c.get()) is not 10:
		if respiration >= 12:
			am = dice(2)
			resp_mod = 1
			if am < 6: respiration = 'Aquatic, Amphibious & Natural Swimmer'
			else: respiration = 'Aquatic, Amphibious & Natural Swimmer & Water Dependent'
		else: respiration = 'Normal'
	else: respiration = 'Normal'
	if respiration is "Normal": resp.set(respiration)
	else:
		scrol.insert(tk.INSERT, c_s + '\n')
		resp.set("Aquatic")
	
	size_cat = dice(2)
	if int(size_c.get()) >= 8: size_cat -= 1
	elif int(size_c.get()) <= 4: size_cat += 1
	if resp_mod == 1: size_cat += 2
	
	if size_cat <= 2: size_cat = 'Tiny'
	elif size_cat == 3 or size_cat == 4: size_cat = 'Small'
	elif size_cat >= 11 and size_cat <= 13: size_cat = 'Large'
	elif size_cat >= 14: size_cat = 'Huge'
	else: size_cat = 'Medium'
	alsz.set(size_cat)
	
	height = dice(2)	
	if int(size_c.get()) == 0: height += 3
	elif int(size_c.get()) >= 1 and int(size_c.get()) <= 3: height += 2
	elif int(size_c.get()) >= 4 and int(size_c.get()) <= 6: height += 1
	elif int(size_c.get()) >= 10: height -= 3
	else: height = height
	if height < 2: height = 2
	elif height > 12: height = 12
	htm = ""
	if size_cat == 'Tiny':
		if height < 5:	height = 2*height + 24
		elif height > 9: height = 2*height+28
		else: height = 2*height + 26
		htm = "+1d6 cm"
	elif size_cat == 'Small':
		if height < 10: height = 5 * height + 45
		else: height = 5* height +50
		htm = "+(2d6x2) cm"
	elif size_cat == 'Medium':
		if height == 2: height = 5 * height + 100
		elif height >= 3 and height <= 5 : height = 5 * height + 105
		elif height >= 6 and height <= 8 : height = 5 * height + 110
		elif height >= 9 and height <= 11 : height = 5 * height + 115
		else: height = 5 * height + 120
		htm = "+(2d6x5) cm"
	elif size_cat == 'Large':
		if height == 2: height = 15 * height + 190
		elif height == 12: height = 15 * height + 180
		else: height = 15 * height + 185
		htm = "+(4d6x5) cm"
	elif size_cat == 'Huge':
		if height == 2: height = 30 * height + 380
		elif height == 12: height = 30 * height + 360
		else: height = 30 * height + 370
		htm = "+(4d6x10) cm"
	alht.set(str(height)+htm)
	
	weigh1 = dice(2)
	weigh2 = dice(2)
	if size_cat == 'Tiny':
		if weigh1 < 5: weigh1 = 0
		elif weigh1 > 9: weigh1 = 2
		else: weigh1 = 1
		weigh2 = '+1d6 kg'
	elif size_cat == 'Small':
		if weigh1 < 4: weigh1 = 2 * weigh1 + 2
		elif weigh1 == 4 or weigh1 == 5: weigh1 = 10
		elif weigh1 == 6 or weigh1 == 7: weigh1 = 12
		elif weigh1 == 8 or weigh1 == 9: weigh1 = 14
		else: weigh1 = 2 * weigh1 - 4
		if weigh2 > 10: weigh2 = '+2d6 kg'
		else: weigh2 = '+(2d6x2) kg'
	elif size_cat == 'Medium':
		weigh1 = 5 * weigh1 + 20
		if weigh2 < 5: weigh2 = '+(2d6x4) kg'
		elif weigh2 > 9: weigh2 = '+(2d6x6) kg'
		else: weigh2 = '+(2d6x5) kg'
	elif size_cat == 'Large':
		weigh1 = 20 * weigh1 + 80
		if weigh2 < 5: weigh2 = '+(4d6x4) kg'
		elif weigh2 > 9: weigh2 = '+(4d6x6) kg'
		else: weigh2 = '+(4d6x5) kg'
	elif size_cat == 'Huge':
		weigh1 = 100 * weigh1 + 350
		if weigh2 < 5: weigh2 = '+(4d6x8) kg'
		elif weigh2 > 9: weigh2 = '+(4d6x15) kg'
		else: weigh2 = '+(4d6x10) kg'
	alwt.set(str(weigh1)+str(weigh2))
	
	symmetry = dice(2)
	if symmetry == 2: 
		syme = 'Trilateral'
		lnum = (dice(1, sides=3)+1)*3
		print(lnum)
	elif symmetry == 12:
		syme = 'Radial'
		lnum = dice(2, sides=3)+1
	elif symmetry == 11:
		syme = 'Bilateral'
		lnum = 2*dice(2)
	elif symmetry == 10:
		syme = 'Bilateral'
		lnum = 8
	elif symmetry == 9:
		syme = 'Bilateral'
		lnum = 6
	else:
		syme = 'Bilateral'
		lnum = 4
	bsym.set(syme)
	limb.set(lnum)
	
	legs = arms = dual = 0
	if syme == 'Bilateral':
		count = 0
		while count < lnum/2:
			x = dice(2)
			if x <= 7: legs += 1
			elif x == 12: dual += 1
			else: arms += 1
			count = count +1
	elif syme == 'Trilateral':
		count = 0
		while count < lnum/3:
			x = dice(2)
			if x <= 7: legs += 1
			elif x == 12: dual += 1
			else: arms += 1
			count = count +1
	else:
		count = 0
		while count < lnum:
			x = dice(2)
			if x <= 7: legs += 1
			elif x == 12: dual += 1
			else: arms += 1
			count = count +1
	ltyp.set(str(arms) + ' arms, ' + str(legs) + ' legs, ' + str(dual) + ' dual.' )
	
	
# Labels
ttk.Label(mighty2, width=12, text="System Name:").grid(column=0, row=0, sticky='W')
ttk.Label(mighty2, width=12, text="Co-ordinates:").grid(column=2, row=0, sticky='W')

ttk.Label(mighty2, width=12, text="Size:").grid(column=0, row=1, sticky='W')
ttk.Label(mighty2, width=12, text="Atmosphere:").grid(column=0, row=2, sticky='W')
ttk.Label(mighty2, width=12, text="Climate:").grid(column=0, row=3, sticky='W')
ttk.Label(mighty2, width=12, text="Hydrography:").grid(column=0, row=4, sticky='W')

ttk.Label(mighty2, width=12, text="Ecol. Type:").grid(column=0, row=5, sticky='W')
ttk.Label(mighty2, width=12, text="Metabolism:").grid(column=0, row=6, sticky='W')

ttk.Label(mighty2, width=12, text="Gender:").grid(column=0, row=7, sticky='W')
ttk.Label(mighty2, width=12, text='Reproduction:').grid(column=0, row=8, sticky='W')

ttk.Label(mighty2, width=12, text='Respiration:').grid(column=0, row=9, sticky='W')
ttk.Label(mighty2, width=12, text='Alien Size:').grid(column=0, row=10, sticky='W')

ttk.Label(mighty2, width=12, text='Alien Height:').grid(column=0, row=11, sticky='W')
ttk.Label(mighty2, width=12, text='Alien Weight:').grid(column=0, row=12, sticky='W')

ttk.Label(mighty2, width=12, text='Symmetry:').grid(column=0, row=13, sticky='W')
ttk.Label(mighty2, width=12, text='No. Limbs:').grid(column=0, row=14, sticky='W')

ttk.Label(mighty2, width=12, text='Limb Types:').grid(column=0, row=15, sticky='W')

# Adding a button
action = ttk.Button(tab2, width=12, text="Transfer Values", command=transfer_val).grid(column=0, row=1)
action = ttk.Button(tab2, width=12, text="Generate", command=creature_gen).grid(column=1, row=1)
	
# Text Box
name_c = tk.StringVar()
coord_c = tk.StringVar()
size_c = tk.StringVar()
atmo_c = tk.StringVar()
temp_c = tk.StringVar()
hydr_c = tk.StringVar()

ecty = tk.StringVar()
meta = tk.StringVar()
gend = tk.StringVar()
rprd = tk.StringVar()
resp = tk.StringVar()
alsz = tk.StringVar()
alht = tk.StringVar()
alwt = tk.StringVar()

bsym = tk.StringVar()
limb = tk.StringVar()

ltyp = tk.StringVar()

name_entered = ttk.Entry(mighty2, width=12, textvariable=name_c).grid(column=1, row=0, sticky=tk.W)
coord_entered = ttk.Entry(mighty2, width=12, textvariable=coord_c).grid(column=3, row=0, sticky=tk.W)
size_genc = ttk.Entry(mighty2, width=12, textvariable=size_c).grid(column=1, row=1, sticky=tk.W)
atmo_genc = ttk.Entry(mighty2, width=12, textvariable=atmo_c).grid(column=1, row=2, sticky=tk.W)
temp_genc = ttk.Entry(mighty2, width=12, textvariable=temp_c).grid(column=1, row=3, sticky=tk.W)
hydr_genc = ttk.Entry(mighty2, width=12, textvariable=hydr_c).grid(column=1, row=4, sticky=tk.W)

ecty_gen = ttk.Entry(mighty2, width=24, textvariable=ecty, state='readonly')
ecty_gen.grid(column=1, row=5, columnspan=2, sticky=tk.W)
meta_gen = ttk.Entry(mighty2, width=24, textvariable=meta, state='readonly')
meta_gen.grid(column=1, row=6, columnspan=2, sticky=tk.W)
gend_gen = ttk.Entry(mighty2, width=24, textvariable=gend, state='readonly')
gend_gen.grid(column=1, row=7, columnspan=2, sticky=tk.W)
rprd_gen = ttk.Entry(mighty2, width=24, textvariable=rprd, state='readonly')
rprd_gen.grid(column=1, row=8, columnspan=2, sticky=tk.W)
resp_gen = ttk.Entry(mighty2, width=62, textvariable=resp, state='readonly')
resp_gen.grid(column=1, row=9, columnspan=4, sticky=tk.W)
alsz_gen = ttk.Entry(mighty2, width=24, textvariable=alsz, state='readonly')
alsz_gen.grid(column=1, row=10, columnspan=4, sticky=tk.W)
alht_gen = ttk.Entry(mighty2, width=24, textvariable=alht, state='readonly')
alht_gen.grid(column=1, row=11, columnspan=4, sticky=tk.W)
alwt_gen = ttk.Entry(mighty2, width=24, textvariable=alwt, state='readonly')
alwt_gen.grid(column=1, row=12, columnspan=4, sticky=tk.W)

bsym_gen = ttk.Entry(mighty2, width=24, textvariable=bsym, state='readonly')
bsym_gen.grid(column=1, row=13, columnspan=4, sticky=tk.W)
limb_gen = ttk.Entry(mighty2, width=24, textvariable=limb, state='readonly')
limb_gen.grid(column=1, row=14, columnspan=4, sticky=tk.W)

ltyp_gen = ttk.Entry(mighty2, width=24, textvariable=ltyp, state='readonly')
ltyp_gen.grid(column=1, row=15, columnspan=4, sticky=tk.W)

# Using a scrolled Text control
scrol_w = 30
scrol_h = 3
scrol = scrolledtext.ScrolledText(mighty2, width=scrol_w, height=scrol_h, wrap=tk.WORD)
scrol.grid(column=0, sticky='WE', columnspan=3)

#===================
# Start GUI
#===================

win.mainloop()
