---
title: "Sealing the leak on classical NTRU signatures"
collection: publications
permalink: /publication/2014-07-21
excerpt: 'with C. Aguilar Melchor, X. Boyen, and P. Gaborit'
date: 2014-07-21
venue: 'Post-Quantum Cryptography 2014'
paperurl: 'https://deneuville.github.io/files/PQC14.pdf'
citation: 'Aguilar Melchor, C., Boyen, X., Deneuville, J.-C., and Gaborit, P. (2014, October). Sealing the leak on classical NTRU signatures. In International Workshop on Post-Quantum Cryptography (pp. 1-21). Springer, Cham.
'
---

Abstract
======
Initial attempts to obtain lattice based signatures were closely related to reducing
a vector modulo the fundamental parallelepiped of a secret basis (like GGH, or NTRUSign). 
This approach leaked some information on the secret, namely the shape of the parallelepiped,
which has been exploited on practical attacks. NTRUSign was an extremely
efficient scheme, and thus there has been a noticeable interest on developing countermeasures
to the attacks, but with little success.

Gentry, Peikert and Vaikuntanathan proposed a randomized version of Babai’s nearest
plane algorithm such that the distribution of a reduced vector modulo a secret parallelepiped
only depended on the size of the base used. Using this algorithm and generating large, close to
uniform, public keys they managed to get provably secure GGH-like lattice-based signatures.
Recently, Stehl´e and Steinfeld obtained a provably secure scheme very close to NTRUSign
(from a theoretical point of view).

In this paper we present an alternative approach to seal the leak of NTRUSign. Instead of
modifying the lattices and algorithms used, we do a classic leaky NTRUSign signature and
hide it with gaussian noise using techniques present in Lyubashevky’s signatures. Our main
contributions are thus a set of strong NTRUSign parameters, obtained by taking into account
latest known attacks against the scheme, a statistical way to hide the leaky NTRU signature
so that this particular instantiation of CVP-based signature scheme becomes zero-knowledge
and secure against forgeries, based on the worst-case hardness of the $\tilde{O}(N^{
1.5})$-Shortest Independent
Vector Problem over NTRU lattices. Finally, we give a set of concrete parameters to
gauge the efficiency of the obtained signature scheme.

[Download paper here](https://deneuville.github.io/files/PQC14.pdf)

Bibtex:
<pre>
@inproceedings{PQC:ABDG14,
  title="Sealing the leak on classical {NTRU} signatures",
  author="{Aguilar Melchor}, Carlos and Boyen, Xavier and Deneuville, {Jean-Christophe} and Gaborit, Philippe",
  booktitle="International Workshop on Post-Quantum Cryptography",
  pages="1--21",
  year="2014",
  organization="Springer"
}
</pre>

