#!/usr/bin/env python3

# It is currently impossible to get 'D' and 'E' type atmospheres

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
tab3 = ttk.Frame(tabControl)
tabControl.add(tab3, text='System Gen')
tab1 = ttk.Frame(tabControl)
tabControl.add(tab1, text='Desirability Calculator')
tabControl.pack(expand=1, fill='both')	# Pack to make visible

# Tab 2 ----------------------------
# Desirability Calculator

def calc():
	settl.delete('1.0', tk.END)
	st = star_t.get()
	ot = orbi_t.get()
	ob = obje_t.get()
	si = int(esiz.get())
	at = int(eatm.get()) 
	hy = int(ehyd.get())
	d = 0
	if ob == 'Belt':
		d = dice(1) - dice(1)
		if st == 'M-Ve':
			mod = dice(1,sides=3)
			d -= mod
		if ot == 'Inner':
			if st == 'M-V': d += 1
			elif st == 'K-III' or st == 'M-III' or st == 'M-Ve': d += 0
			else: d += 2
	else:
		d = 0
		if hy == 0: d -= 1
		
		if si >= 13 or at >= 13 or hy == 15: d -= 2
		
		if st == 'M-Ve':
			mod = dice(1,sides=3)
			d -= mod
		
		if si > 0 and si < 12:
			if at > 1 and at < 10:
				if hy < 12:
					if si > 4 and si < 11 and at > 3 and at < 10 and hy > 3 and hy < 9: d += 5
					elif hy == 10 or hy == 11: d += 3
					elif at > 1 and at < 7 and hy < 4: d += 2
					else: d += 4
		
		if si > 9 and at < 16: d -= 1
		
		if ot == 'Inner':
			if st == 'M-V': d += 1
			elif st == 'K-III' or st == 'M-III' or st == 'M-Ve': d += 0
			else: d += 2
		
		if si == 0: d -= 1
		
		if at == 6 or at == 8: d += 1
	desi.set(d)
	
	col_ch = dice(2,mod=-2)
	if col_ch <= d:
		tl = int(tech.get())
		pop = dice(1) + tl - 9
		if pop < 4: pop = 4
		gov = dice(2)-7+pop
		if gov < 0: gov = 0
		law = dice(2)-7+gov
		if law < 0: law = 0
		settle = 'Population: ' + str(pop) + '\nGovernment: ' + str(gov) + '\nLaw Level: ' + str(law)
		settl.insert(tk.INSERT, settle)
	else:
		out_ch = dice(1)
		if out_ch <= 2:
			pop = dice(1,sides=3) + d
			if pop > 0:
				gov = dice(2)-7+pop
				if gov < 0: gov = 0
				if gov > 6: gov = 6
				law = dice(2)-7+gov
				if law < 0: law = 0
				settle = 'Population: ' + str(pop) + '\nGovernment: ' + str(gov) + '\nLaw Level: ' + str(law)
				settl.insert(tk.INSERT, settle)

mighty = ttk.LabelFrame(tab1, text = ' Desirability Calculator ')
mighty.grid(column=0, row=0, padx=8, pady=4)

ttk.Label(mighty, width=12, text="Star Type:").grid(column=0, row=0, sticky='W')
ttk.Label(mighty, width=12, text="Orbit Region:").grid(column=2, row=0, sticky='W')

ttk.Label(mighty, width=12, text="Object Type:").grid(column=0, row=1, sticky='W')
ttk.Label(mighty, width=12, text="Size:").grid(column=2, row=1, sticky='W')

ttk.Label(mighty, width=12, text="Atmosphere:").grid(column=0, row=2, sticky='W')
ttk.Label(mighty, width=12, text="Hydrographics:").grid(column=2, row=2, sticky='W')

ttk.Label(mighty, width=12, text="Desirability:").grid(column=0, row=3, sticky='W')
ttk.Label(mighty, width=12, text="Tech Level:").grid(column=2, row=3, sticky='W')

descalc = ttk.Button(tab1, width=12, text="Calculate", command=calc).grid(column=0, row=1)

star = tk.StringVar()
orbi = tk.StringVar()
obje = tk.StringVar()

star_t = ttk.Combobox(mighty, width=10, textvariable=star, state='readonly')
star_t['values'] = ('A-V', 'F-V', 'G-V', 'K-V', 'M-V', 'M-Ve', 'F-IV', 'G-IV', 'K-IV', 'K-III', 'M-III', 'D', 'L')
star_t.grid(column=1,row=0, sticky=tk.W)
star_t.current(0)

orbi_t = ttk.Combobox(mighty, width=10, textvariable=orbi, state='readonly')
orbi_t['values'] = ('Epistellar', 'Inner', 'Outer')
orbi_t.grid(column=3,row=0, sticky=tk.W)
orbi_t.current(0)

obje_t = ttk.Combobox(mighty, width=10, textvariable=obje, state='readonly')
obje_t['values'] = ('Belt', 'Planet')
obje_t.grid(column=1,row=1, sticky=tk.W)
obje_t.current(0)
	
# Text Box
esiz = tk.StringVar()
eatm = tk.StringVar()
ehyd = tk.StringVar()
desi = tk.StringVar()
tech = tk.StringVar()

size_n = ttk.Entry(mighty, width=12, textvariable=esiz).grid(column=3, row=1, sticky=tk.W)
atmo_n = ttk.Entry(mighty, width=12, textvariable=eatm).grid(column=1, row=2, sticky=tk.W)
hydr_n = ttk.Entry(mighty, width=12, textvariable=ehyd).grid(column=3, row=2, sticky=tk.W)
desi_n = ttk.Entry(mighty, width=12, textvariable=desi, state='readonly').grid(column=1, row=3, sticky=tk.W)
hydr_n = ttk.Entry(mighty, width=12, textvariable=tech).grid(column=3, row=3, sticky=tk.W)

esiz.set(0)
eatm.set(0)
ehyd.set(0)
tech.set(10)

settl_w = 60
settl_h = 5
settl = scrolledtext.ScrolledText(mighty, width=settl_w, height=settl_h, wrap=tk.WORD)
settl.grid(column=0, sticky='WE', columnspan=4)


# TAB 3 ----------------------------
mighty3 = ttk.LabelFrame(tab3, text = ' System Generator ')
mighty3.grid(column=0, row=0, padx=8, pady=4)

def create_asteroid(orbit,reg=0):
	otype = 'Small Body'
	siz = 'Y'
	atm = hyd = bio = 0
	syssc.insert(tk.INSERT, str(orbit) + ': ' + otype + '-' + str(siz) + str(atm) + str(hyd) + str(bio) + '\n')
	roll = dice(1)
	if roll > 4:
		orb = str(orbit)+'-1'
		create_dwarf(orb,typ=1,reg=reg)

def create_moon(o,c='Dwarf',r=0,t=4):	
	# (c)lass, (o)rbit, (r)egion, (t)ype
	if c=='Dwarf':
		create_dwarf(o,typ=t,reg=r)
	elif c=='Terrestrial':
		create_terrestrial(o,typ=t,reg=r)

def create_dwarf(orbit,typ=0,reg=0):		# Type 4 is a normal moon
	chem = ''
	roll = dice(1)
	if typ == 1 and reg < 2: roll -= 2		# Asteroid Belt Member Epistellar/Inner
	elif typ == 1 and reg == 2: roll -= 1	# Asteroid Belt Member Outer	
	elif typ == 2: roll += 1				# Helian Satellite
	elif typ == 3: roll += 2				# Jovian Satellite
	if roll < 4:
		otype = 'Rockball'
		siz = dice(1,mod=-1)
		atm = 0
		hyd = dice(2) + siz - 13
		if hyd < 0: hyd = 0
		if p_star_type == 'L': hyd += 1
		bio = 0
	elif roll == 6:
		roll = dice(1)
		if roll < 5:
			otype = 'Hebean'
			siz = dice(1,mod=-1)
			atm = dice(1) + siz - 6
			if atm < 0: atm = 0
			if atm > 1: atm = 'A'
			hyd = dice(2) + siz - 11
			if hyd < 0: hyd = 0
			bio = 0
		else:
			otype = 'Promethean'
			siz = dice(1,mod=-1)
			chem = dice(1)
			if p_star_type == 'L':
				chem += 2
			if chem < 5: 
				chem = 'Water'
				amod = 0
			elif chem > 6:
				chem = 'Methane'
				amod = 3
			else:
				chem = 'Ammonia'
				amod = 1
			abmod = dice(1, sides=3)
			if system_age >= abmod + amod: 
				if system_age >= 4 + amod: 
					bio = dice(2)
					if p_star_type == 'D':
						bio -= 3
				else: bio = dice(1, sides=3)
			else: bio = 0
			if bio >= 3 and chem == 'Water':
				atm = dice(2)-7+siz
				if atm < 2: atm = 2
				if atm > 9: atm = 9
			else: atm = 'A'
			hyd = dice(2, mod=-2)
	else: 
		otype = 'Meltball'
		siz = dice(1,mod=-1)
		atm = 1
		hyd = 'F'
		bio = 0
	
	if bio == 10: bio = 'A'
	elif bio == 11: bio = 'B'
	elif bio >= 12: bio = 'C'
	
	syssc.insert(tk.INSERT, str(orbit) + ': ' + otype + '-' + str(siz) + str(atm) + str(hyd) + str(bio))
	if chem == '':
		syssc.insert(tk.INSERT, '\n')
	else:
		syssc.insert(tk.INSERT, ' ' + chem + '\n')
	
	if typ == 0:
		roll = dice(1)
		if roll == 6:
			orb = str(orbit) + '-1'
			create_moon(orb,r=reg)
		
def create_terrestrial(orbit,typ=0,reg=0):
	chem = ''
	if reg==0:
		roll = dice(1)
		if roll < 5:
			otype = 'JaniLithic'
			siz = dice(1,mod=4)
			roll = dice(1)
			if roll < 4: atm = 1
			else: atm = 'A'
			hyd = 0
			bio = 0
		elif roll == 5:
			otype = 'Vesperian'
			siz = dice(1,mod=4)
			chem = dice(2)
			if chem < 12: chem = 'Water'
			else: chem = 'Chlorine'
			abmod = dice(1,sides=3)
			if system_age >= abmod: 
				if system_age >= 4: bio = dice(2)
				else: bio = dice(1,sides=3)
			else: bio = 0		
			if bio >= 3 and chem == 'Water':
				atm = dice(2) + siz - 7
				if atm < 2: atm = 2
				if atm > 9: atm = 9
			elif bio >= 3 and chem == 'Chlorine':atm = 'B'
			else: atm = 'A'
			hyd = dice(2,mod=-2)
		else: otype = 'Telluric'
	elif reg==1:
		roll = dice(2)
		if roll < 4 or roll > 10: otype = 'Telluric'
		elif roll == 7 or roll == 10: otype = 'Tectonic'
		elif roll == 5 or roll == 6: otype = 'Arid'
		else: otype = 'Oceanic'
	elif reg==2:
		roll = dice(1)
		if roll < 5: otype = 'Arid'
		elif roll > 6: otype = 'Oceanic'
		else: otype = 'Tectonic'
	
	if otype == 'Telluric':
		siz = dice(1,mod=4)
		atm = 'C'
		roll = dice(1)
		if roll < 5: hyd = 0
		else: hyd = 'F'
		bio = 0
	elif otype == 'Tectonic':
		siz = dice(1,mod=4)
		chem = dice(1)
		if p_star_type == 'K-V': chem += 2
		elif p_star_type == 'M-V': chem += 4
		elif p_star_type == 'L': chem += 5
		if chem < 7:
			chem = dice(2)
			if chem < 9:
				amod = 0
				chem = 'Water'
			elif chem > 11:
				amod = 0
				chem = 'Chlorine'
			else:
				amod = 0
				chem = 'Sulphur'
		elif chem > 8:
			amod = 3
			chem = 'Methane'
		else:
			amod = 1
			chem = 'Ammonia'
		roll = dice(1,sides=3)
		if system_age >= roll + amod:
			if system_age >= 4 + amod:
				bio = dice(2)
				if p_star_type == 'D': bio -= 3
				if bio < 0: bio = 0
			else: bio = dice(1, sides=3)
		else: bio = 0
		if bio >= 3 and chem == 'Water':
			atm = dice(2)+siz-7
			if atm < 2: atm = 2
			if atm > 9: atm = 9
		elif bio >= 3 and chem == 'Sulphur': atm = 'B'
		elif bio >= 3 and chem == 'Chlorine': atm = 'B'
		else: atm = 'A'
		hyd = dice(2,mod=-2)
	elif otype == 'Arid':
		siz = dice(1,mod=4)
		chem = dice(1)
		if p_star_type == 'K-V': chem += 2
		elif p_star_type == 'M-V': chem += 4
		elif p_star_type == 'L': chem += 5
		if chem < 7: 
			amod = 0
			chem = 'Water'
		elif chem > 8: 
			amod = 3
			chem = 'Methane'
		else: 
			amod = 1
			chem = 'Ammonia'
		roll = dice(1,sides=3)
		if system_age >= roll + amod:
			if system_age >= 4 + amod:
				bio = dice(2)
				if p_star_type == 'D': bio -= 3
				if bio < 0: bio = 0
			else: bio = dice(1,sides=3)
		else: bio = 0
		if bio >= 3 and chem == 'Water': 
			atm = dice(2)-7+siz
			if atm < 2: atm = 2
			if atm > 9: atm = 9
		else: atm = 'A'
		hyd = dice(1,sides=3)
	elif otype == 'Oceanic':
		siz = dice(1,mod=4)
		chem = dice(1)
		if p_star_type == 'K-V': chem += 2
		elif p_star_type == 'M-V': chem += 4
		elif p_star_type == 'L': chem += 5
		if chem < 7:
			amod = 0
			chem = 'Water'
		elif chem > 8:
			amod = 3
			chem = 'Methane'
		else:
			amod = 1
			chem = 'Ammonia'
		roll = dice(1,sides=3)
		if system_age >= roll + amod:
			if system_age >= 4 + amod:
				bio = dice(2)
				if p_star_type == 'D': bio -= 3
				if bio < 0: bio = 0
			else: bio = dice(1,sides=3)
		else: bio = 0
		if chem == 'Water':
			atm = dice(2)+siz-6
			if p_star_type == 'K-V' or p_star_type == 'L': atm -= 1
			elif p_star_type == 'M-V': atm -= 2
			elif p_star_type == 'F-IV' or p_star_type == 'G-IV' or p_star_type == 'K-IV': atm -= 1
			if atm < 1: atm = 1
			if atm > 12: atm = 12
		else:
			roll = dice(1)
			if roll == 1: atm = 1
			elif roll > 4: atm = 'C'
			else: atm = 'A'
		hyd = 'B'
	
	if atm == 10: atm = 'A'
	elif atm == 11: atm = 'B'
	elif atm == 12: atm = 'C'
	
	if siz == 10: siz = 'A'
	
	if bio == 10: bio = 'A'
	elif bio == 11: bio = 'B'
	elif bio >= 12: bio = 'C'
	
	syssc.insert(tk.INSERT, str(orbit) + ': ' + otype + '-' + str(siz) + str(atm) + str(hyd) + str(bio))
	if chem == '':
		syssc.insert(tk.INSERT, '\n')
	else:
		syssc.insert(tk.INSERT, ' ' + chem + '\n')
	
	roll = dice(1)
	if typ==0:
		if roll > 4:
			orb = str(orbit)+'-1'
			create_dwarf(orb,typ=1,reg=reg)
	
def create_helian(orbit,typ=0,reg=0):
	chem = ''
	roll = dice(1)
	if reg == 0:
		if roll < 6: otype = 'Helian'
		else: otype = 'Asphodelian'
	elif reg == 1:
		if roll < 6: otype = 'Helian'
		else: otype = 'Panthalassic'
	else: otype = 'Helian'
	
	if otype == 'Helian':
		siz = dice(1,mod=9)
		atm = 'D'
		roll = dice(1)
		if roll < 3: hyd = 0
		elif roll > 4: hyd = 'F'
		else: hyd = dice(2,mod=-1)
		bio = 0
	elif otype == 'Asphodelian':
		siz = dice(1,mod=9)
		atm = 1
		hyd = 0
		bio = 0
	elif otype == 'Panthalassic':
		siz = dice(1,mod=9)
		atm = dice(1,mod=8)
		if atm == 10: atm = 'A'
		elif atm == 11: atm = 'B'
		elif atm == 12: atm = 'C'
		elif atm == 13 or atm == 14: atm = 'D'
		hyd = 'B'
		chem = dice(1)
		if p_star_type == 'K-V': chem += 2
		if p_star_type == 'M-V': chem += 4
		if p_star_type == 'L': chem += 5
		if chem < 7:
			chem = dice(2)
			amod = 0
			if chem < 9: chem = 'Water'
			elif chem > 11: chem = 'Chlorine'
			else: chem = 'Sulphur'
		elif chem > 8:
			amod = 3
			chem = 'Methane'
		else:
			amod = 1
			chem = 'Methane'
		roll = dice(1,sides=3)
		if system_age >= roll + amod:
			if system_age >= 4 + amod:
				bio = dice(2)
			else: bio = dice(1,sides=3)
		else: bio = 0
	if siz == 10: siz = 'A'
	elif siz == 11: siz = 'B'
	elif siz == 12: siz = 'C'
	elif siz == 13: siz = 'D'
	elif siz == 14: siz = 'E'
	elif siz == 15: siz = 'F'
	
	syssc.insert(tk.INSERT, str(orbit) + ': ' + otype + '-' + str(siz) + str(atm) + str(hyd) + str(bio))
	if chem == '':
		syssc.insert(tk.INSERT, '\n')
	else:
		syssc.insert(tk.INSERT, ' ' + chem + '\n')
	
	if typ == 0:
		satellites = dice(1,mod=-3)
		if satellites < 0: satellites = 0
		count = 0
		roll = dice(1)
		if roll == 6:
			count += 1
			orb = str(orbit)+'-1'
			create_moon(orb,c='Terrestrial')
		while count < satellites:
			count += 1
			orb = str(orbit) + '-' + str(count)
			create_moon(orb)

def create_jovian(orbit,reg=0):
	chem = ''
	if reg == 0:
		roll = dice(1)
		if roll == 6: otype = 'Chthonian'
		else: otype = 'Jovian'
	else: otype = 'Jovian'
	
	if otype == 'Jovian':
		siz = 'G'
		atm = 'G'
		hyd = 'G'
		roll = dice(1)
		if roll < 6:
			bio = 0
		else:
			abmod = dice(1)
			if system_age >= abmod: bio = dice(1,sides=3)
			elif system_age >= 7:
				bio = dice(2)
				if p_star_type == 'D': bio -= 3
			else: bio = 0
			if bio > 0:
				chem = dice(1,mod=-2)
				if p_star_type == 'L': chem += 1
				if chem < 4: chem = 'Water'
				else: chem = 'Ammonia'
	elif otype == 'Chthonian':
		siz = 'G'
		atm = 1
		hyd = 0
		bio = 0
	syssc.insert(tk.INSERT, str(orbit) + ': ' + otype + '-' + str(siz) + str(atm) + str(hyd) + str(bio))
	if chem == '':
		syssc.insert(tk.INSERT, '\n')
	else:
		syssc.insert(tk.INSERT, ' ' + chem + '\n')
	
	satellites = dice(1)
	roll = dice(1)
	count = 0
	if roll == 6:
		count += 1
		orb = str(orbit) + '-1'
		roll = dice(1)
		if roll == 6: create_moon(orb,c='Helian')
		else: create_moon(orb,c='Terrestrial')
	while count < satellites:
		count += 1
		orb = str(orbit) + '-' + str(count)
		create_moon(orb,c='Dwarf')
	
def sysgen():
	global p_star_type, system_age
	syssc.delete('1.0', tk.END)
	system_age = dice (3, mod=-3)
	syssc.insert(tk.INSERT, 'System Age: ' + str(system_age) + ' billion years\n')
	stno = dice(3)
	if stno < 11: systype = 'Primary'
	elif stno > 15: systype = 'Trinary'
	else: systype = 'Binary'
	
	syssc.insert(tk.INSERT, 'System Type: ' + systype + '\n')
	
	primary_roll = dice(2)
	if primary_roll == 2:
		if system_age <= 2: p_star_type = 'A-V'
		elif system_age >= 4: p_star_type = 'D'
		else:
			roll = dice(1)
			if roll == 3: p_star_type = 'K-III'
			elif roll > 3: p_star_type = 'D'
			else: star_type = 'F-IV'
	elif primary_roll == 3:
		if system_age <= 5: p_star_type = 'F-V'
		elif system_age >= 7: p_star_type = 'D'
		else:
			roll = dice(1)
			if roll < 5: p_star_type = 'G-IV'
			else: p_star_type = 'M-III'
	elif primary_roll == 4:
		if system_age <= 11: p_star_type = 'G-V'
		elif system_age >= 14: p_star_type = 'D'
		else:
			roll = dice(1)
			if roll < 4: p_star_type = 'K-IV'
			else: p_star_type = 'M-III'
	elif primary_roll == 5: p_star_type = 'K-V'
	elif primary_roll > 13: p_star_type = 'L'
	else:
		roll = dice(2)
		if roll < 10: p_star_type = 'M-V'
		elif roll >12: p_star_type = 'L'
		else: p_star_type = 'M-Ve'
	syssc.insert(tk.INSERT, 'Primary Star: ' + p_star_type + '\n')
	
	s_orbit = t_orbit = ''
	
	if systype == 'Binary' or systype == 'Trinary':
		roll = dice(1, mod=-1)
		roll = roll + primary_roll
		if roll == 2: 
			if system_age <= 2: star_type = 'A-V'
			elif system_age >= 4: star_type = 'D'
			else:
				roll = dice(1)
				if roll == 3: star_type = 'K-III'
				elif roll > 3: star_type = 'D'
				else: star_type = 'F-IV'
		elif roll == 3:
			if system_age <= 5: star_type = 'F-V'
			elif system_age >= 7: star_type = 'D'
			else:
				roll = dice(1)
				if roll < 5: star_type = 'G-IV'
				else: star_type = 'M-III'
		elif roll == 4:
			if system_age <= 11: star_type = 'G-V'
			elif system_age >= 14: star_type = 'D'
			else:
				roll = dice(1)
				if roll < 4: star_type = 'K-IV'
				else: star_type = 'M-III'
		elif roll == 5: star_type = 'K-V'
		elif roll > 13: star_type = 'L'
		else:
			roll = dice(2)
			if roll < 10: star_type = 'M-V'
			elif roll >12: star_type = 'L'
			else: star_type = 'M-Ve'
		orbit = dice(1)
		if orbit < 3: orbit = 'Tight Orbit'
		elif orbit == 5: s_orbit = 'Moderate Orbit'
		elif orbit == 6: s_orbit = 'Distant Orbit'
		else: s_orbit = 'Close Orbit'
		syssc.insert(tk.INSERT, 'Secondary Star: ' + star_type + ' ' + s_orbit + '\n')
	if systype == 'Trinary':
		roll = dice(1, mod=-1)
		roll = roll + primary_roll
		if roll == 2: 
			if system_age <= 2: star_type = 'A-V'
			elif system_age >= 4: star_type = 'D'
			else:
				roll = dice(1)
				if roll == 3: star_type = 'K-III'
				elif roll > 3: star_type = 'D'
				else: star_type = 'F-IV'
		elif roll == 3:
			if system_age <= 5: star_type = 'F-V'
			elif system_age >= 7: star_type = 'D'
			else:
				roll = dice(1)
				if roll < 5: star_type = 'G-IV'
				else: star_type = 'M-III'
		elif roll == 4:
			if system_age <= 11: star_type = 'G-V'
			elif system_age >= 14: star_type = 'D'
			else:
				roll = dice(1)
				if roll < 4: star_type = 'K-IV'
				else: star_type = 'M-III'
		elif roll == 5: star_type = 'K-V'
		elif roll > 13: star_type = 'L'
		else:
			roll = dice(2)
			if roll < 10: star_type = 'M-V'
			elif roll >12: star_type = 'L'
			else: star_type = 'M-Ve'
		orbit = dice(1)
		if orbit < 3: orbit = 'Tight Orbit'
		elif orbit == 5: t_orbit = 'Moderate Orbit'
		elif orbit == 6: t_orbit = 'Distant Orbit'
		else: t_orbit = 'Close Orbit'
		syssc.insert(tk.INSERT, 'Tertiary Star: ' + star_type + ' ' + t_orbit + '\n')
		
	epi = dice(1,mod=-3)
	if p_star_type == 'M-V': epi -= 1
	elif p_star_type == 'K-III' or p_star_type == 'M-III' or p_star_type == 'D' or p_star_type == 'L': epi = 0
	if epi < 0: epi = 0
	syssc.insert(tk.INSERT, 'Epistellar Orbits: ' + str(epi) + '\n')
	
	inn = dice(1,mod=-1)
	if p_star_type == 'M-V': inn -= 1
	elif p_star_type == 'L': inn = dice(1, mod=-1, sides=3)
	if s_orbit == 'Close Orbit' or t_orbit == 'Close Orbit': inn = 0
	if inn < 0: inn = 0
	syssc.insert(tk.INSERT, 'Inner Orbits: ' + str(inn) + '\n')
	
	out = dice(1,mod=-1)
	if p_star_type == 'M-V' or p_star_type == 'L': out -= 1
	if s_orbit == 'Moderate Orbit' or t_orbit == 'Moderate Orbit': out = 0
	if out < 0: out = 0
	syssc.insert(tk.INSERT, 'Outer Orbits: ' + str(out) + '\n\n')
	
	count = 0
	total = epi + inn + out
	while count < total:
		count += 1
		
		otype = dice(1)
		if p_star_type == 'L': otype -= 1
		if otype < 2: otype = 'Asteroid'
		elif otype == 2: otype = 'Dwarf'
		elif otype == 3: otype = 'Terrestrial'
		elif otype == 4: otype = 'Helian'
		else: otype = 'Jovian'
			
		if count < epi:
			if p_star_type == 'K-III' or p_star_type == 'M-III' or p_star_type == 'D':
				if otype == 'Dwarf':
					otype = 'Stygian'
					siz = dice(1,mod=-1)
					atm = 0
					hyd = 0
					bio = 0
				elif otype == 'Terrestrial':
					otype = 'Acheronian'
					siz = dice(1,mod=4)
					atm = 1
					hyd = 0
					bio = 0
				elif otype == 'Helian':
					otype = 'Asphodelian'
					siz = dice(1,mod=9)
					atm = 1
					hyd = 0
					bio = 0
				elif otype == 'Jovian': 
					otype = 'Chthonian'
					siz = 'G'
					atm = 1
					hyd = 0
					bio = 0
				syssc.insert(tk.INSERT, str(count) + ': ' + otype + '-' + str(siz) + str(atm) + str(hyd) + str(bio))
			else:
				if otype == 'Dwarf': create_dwarf(count,reg=0)
				elif otype == 'Terrestrial': create_terrestrial(count)
				elif otype == 'Helian': create_helian(count)
				elif otype == 'Jovian': create_jovian(count)
				else: create_asteroid(count)
		else:
			inner = epi + inn
			if count < inner: r = 1
			else: r = 2
			if otype == 'Dwarf': create_dwarf(count,reg=r)
			elif otype == 'Terrestrial': create_terrestrial(count,reg=r)
			elif otype == 'Helian': create_helian(count,reg=r)
			elif otype == 'Jovian': create_jovian(count,reg=r)
			else: create_asteroid(count,reg=r)

syssc_w = 60
syssc_h = 40
syssc = scrolledtext.ScrolledText(mighty3, width=syssc_w, height=syssc_h, wrap=tk.WORD)
syssc.grid(column=0, sticky='WE', columnspan=3)
sys_gen = ttk.Button(tab3, width=12, text="Generate", command=sysgen).grid(column=0, row=1)

#===================
# Start GUI
#===================

win.mainloop()
