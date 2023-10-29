fof(a1,axiom,$distinct(r1,r2,r3,r4,r5,r6)).
fof(a2,axiom,(next(r1,r2) & ~(next(r1,r1) | next(r1,r3) | next(r1,r4) | next(r1,r5) | next(r1,r6)))).
fof(a3,axiom,(next(r2,r3) & ~(next(r2,r1) | next(r2,r2) | next(r2,r4) | next(r2,r5) | next(r2,r6)))).
fof(a4,axiom,(next(r3,r4) & ~(next(r3,r1) | next(r3,r3) | next(r3,r2) | next(r3,r5) | next(r3,r6)))).
fof(a5,axiom,(next(r4,r5) & ~(next(r4,r1) | next(r4,r3) | next(r4,r4) | next(r4,r2) | next(r4,r6)))).
fof(a6,axiom,(next(r5,r6) & ~(next(r5,r1) | next(r5,r3) | next(r5,r4) | next(r5,r5) | next(r5,r2)))).
fof(a7,axiom,~(next(r6,r1) | next(r6,r3) | next(r6,r4) | next(r6,r5) | next(r6,r6) | next(r6,r2))).
fof(a8,axiom,![X]:(cat(X)|dog(X)|hamster(X)) & (~cat(X)|~dog(X)) & (~cat(X)|~hamster(X))& (~hamster(X)|~dog(X))).
fof(a9,axiom,(~hamster(r1) & ~hamster(r2) & ~hamster(r3) & ~hamster(r4) & ~hamster(r5) & hamster(r6))).
fof(a10,axiom,![X]:(hamster(X)=>~lit(X))).
fof(a11,axiom,![X,Y,Z]:(dog(X) & dog (Y) & dog (Z) & next(X,Y) & next(Y,Z) => lit(Y))).
fof(a12,axiom,![X,Y]:(cat(X) & cat(Y) & (next(X,Y) | next(Y,X)) => lit(X) & lit(Y))).
fof(a13,axiom,(lit(r1) | lit(r2) | lit(r3) | lit(r4) | lit(r5)) & (~lit(r1) | ~lit(r2)) & (~lit(r1) | ~lit(r3)) & (~lit(r1) | ~lit(r4)) & (~lit(r1) | ~lit(r5)) & (~lit(r2) | ~lit(r3)) &(~lit(r2) | ~lit(r4)) & (~lit(r5) | ~lit(r2)) & (~lit(r3) | ~lit(r4)) & (~lit(r3) | ~lit(r5)) & (~lit(r4) | ~lit(r5))).
fof(a14,axiom,dog(r1)=>~(lit(r1))).
fof(a15,axiom,dog(r5)=>~(lit(r5))).
fof(a16,axiom,![X,Y]:(dog(X) & (~dog(Y)) & (next(X,Y)| next(Y,X)) => ~lit(X))).
fof(a17,axiom,![X,Y,Z]:(~cat(X) & cat(Y) & ~cat(Z) & next(X,Y) & next(Y,Z) => ~lit(Y))).
fof(a18,axiom,cat(r1) & ~cat(r2)=>~(lit(r1))).
fof(a19,axiom,![X,Y]:~(cat(X) & cat(Y) & (next(X,Y)|next(Y,X)))).