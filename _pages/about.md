---
permalink: /
title: "Jean-Christophe Deneuville's Homepage"
excerpt: "About me"
author_profile: true
redirect_from: 
  - /about/
  - /about.html
---

Welcome to my homepage! I am Jean-Christophe Deneuville, post-doc in Computer Science at [INSA-CVL](http://www.insa-centrevaldeloire.fr/fr/) and [LIFO](https://www.univ-orleans.fr/lifo/), under the supervision of [Jérémy Briffaut](https://www.univ-orleans.fr/lifo/pageperso.php?lang=fr&id=63). I earned my Ph.D in 2016, under the supervision of [Philippe Gaborit](http://www.unilim.fr/pages_perso/philippe.gaborit/) and [Carlos Aguilar Melchor](http://www.irit.fr/spip.php?page=annuaire&code=8292). My research interests include Cryptography especially based on Error Correcting Codes and Lattices, as well as associated Algorithms for solving hard problems.

<br/>

Post-Quantum Cryptography
======
The rising threat of a large-scale quantum computer capable of vanishing classical number theory based cryptography has urged the need for alternative security solutions. Among the [quantum-safe candidates](https://en.wikipedia.org/wiki/Post-quantum_cryptography), three of them are of particular interest to me: Code-based cryptography, Lattice-based Cryptography and Rank-based Cryptography (using error correcting codes in rank metric).

Code-based Cryptography
------
The use of Coding Theory in Cryptography has been suggested by [McEliece](https://en.wikipedia.org/wiki/McEliece_cryptosystem) in 1978 (as old as number theoretic based [RSA](https://en.wikipedia.org/wiki/RSA_(cryptosystem))). Ever since then, many other cryptographic primitives were proposed. I am interested in designing provably secure and efficient protocols relying upon well-established Coding Theory problem. On an different --but related-- flavor, I am also interested in the cryptanalytic effort of such primitives.

Lattice-based Cryptography
------
Lattices are periodic sets of points in space (e.g. 3-dimensional ambient space although cryptography typically uses 256+ dimensions). Many difficult problems exist on lattices, all of them more or less related to the [Shortest Vector Problem (SVP)](https://en.wikipedia.org/wiki/Lattice_problem). These problems allow for the design of beautiful primitives such as worst-case to average-case reductions, or fully homomorphic encryption. I am interested in building efficient primitives using the aforementioned features. I am also interested in lattice reduction algorithms and their usage for cryptanalysis.

Rank-based Cryptography
------
Rank metric is an alternative to Hamming metric for codes in extension fields. The vector space notions are more involved. For instance, the support of a word corresponds to the vector space hosting the coordinates of the word. This results in exponentially many more possible supports for a word of given weight in rank metric than in Hamming metric, which in turn yields worse attacks hence better parameters. 
Although Rank metric has received less attention than the famous Hamming metric, it has inhenrently different properties that may enable features that are not reachable with usual code-based cryptography (such as Fully Homomorphic Encryption, Identity-based Encryption, etc...). 

NIST PQC standardization process 
======
In 2016, the [National Institute of Standards and Technology (a.k.a NIST)](https://www.nist.gov/) initiated a 5 to 7 years process for standardizing three kinds of cryptographic primitives: key-exchange, (public-key) encryption and digital signature. This event yielded 82 submissions (nov. 30, 2017) among which 69 were "complete and proper" and qualified for the 1st round. I actively participated in the design of 6 of them, all accepted to the 1st round:
* [BIKE](http://bikesuite.org/)
* [HQC](https://pqc-hqc.org/)
* [LAKE](http://nicolas-aragon.fr/lake/)
* [LOCKER](http://nicolas-aragon.fr/locker/)
* [Ouroboros-R](https://pqc-ouroborosr.org/)
* [RQC](https://pqc-rqc.org/)

You can find more information of NIST's related pages: [project main page](https://csrc.nist.gov/projects/post-quantum-cryptography), [submissions accepted for the 1st round](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Round-1-Submissions).

*11.30.18 UPDATE:* [LAKE](http://nicolas-aragon.fr/lake/), [LOCKER](http://nicolas-aragon.fr/locker/) and [Ouroboros-R](https://pqc-ouroborosr.org/) have been merged into a single submission [ROLLO](https://pqc-rollo.org/)

*01.30.19 UPDATE:* [BIKE](http://bikesuite.org/), [HQC](https://pqc-hqc.org/), [RQC](https://pqc-rqc.org/) and [ROLLO](https://pqc-rollo.org/) made it to the [second round](https://csrc.nist.gov/Projects/Post-Quantum-Cryptography/Round-2-Submissions) along with 22 other candidates.




