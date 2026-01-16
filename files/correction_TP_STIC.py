from random import randint

f = [0x9, 0xb, 0xc,0x4, 0xa, 0x1, 0x2, 0x6, 0xd, 0x7, 0x3, 0x8, 0xf, 0xe, 0x0, 0x5]
finv = [0 for i in range(len(f))]

for i in range(len(f)):
	finv[f[i]]=i

def sbox(x):
	return f[x]

def invsbox(x):
	return finv[x]

def split(key):
	return ((key>>4)&0x0f, key&0x0f)

def round(state, roundkey):
	return sbox(state^roundkey)

def inverseround(state, roundkey):
	return invsbox(state)^roundkey

def encrypt(plaintext, key):
	(k0,k1) = split(key)
	state = plaintext
	state = round(state, k0)
	state = round(state, k1)
	return state

def decrypt(ciphertext, key):
	(k0,k1) = split(key)
	state = ciphertext
	state = inverseround(state, k1)
	state = inverseround(state, k0)
	return state

def bruteforce(plaintext, ciphertext):
	possibleKeys=[]
	for key in range(256):
		if encrypt(plaintext, key)==ciphertext:
			possibleKeys.append(key)
	return possibleKeys

def known_pairs_gen(key, n):
	couples=[]
	for i in range(n):
		plaintext=randint(0,15)
		ciphertext=encrypt(plaintext,key)
		couples.append((plaintext,ciphertext))
	return couples

def parity(x):
	return (bin(x)[2:].count('1'))%2

def nb_parity(a, b):
	cpt=0
	for x in range(16):
		if parity(x&a)==parity(sbox(x)&b):
			cpt+=1
	return cpt

def seekMax():
	MAX=0
	for a in range(16):
		for b in range(16):
			if a==0 and b==0: continue
			cpt=nb_parity(a,b)
			if cpt > MAX:
				MAX = cpt
				MAXa = a
				MAXb = b
	return (MAXa, MAXb, MAX)

def derivek1(x2, x1):
	return invsbox(x2)^x1

def derivek1fromknownPairs(known_pair, guessed_k0): #known_pair=(x0, x2)
	x1 = round(known_pair[0], guessed_k0)
	return derivek1(known_pair[1], x1)

def find_candidate_subkeys(mask, pairs):
	a, b = mask
	score = [0 for k in range(0, 16)]
	for k0 in range(0, 16):
		for p in pairs:
			x1 = round(p[0], k0)
			if parity(x1 & a) == parity(p[1] & b):
				score[k0] += 1
			else:
				score[k0] -= 1
		score[k0] = abs(score[k0])
	candidates = [k for k in range(0, 16) if score[k] == max(score)]
	return candidates





k = randint(0,255)
couples = known_pairs_gen(k, 16)


