include('SET001-0.ax').
fof(l,axiom,![Y,A]:(member(Y,dirimg(A)) <=> ?[X]:(member(X,A) & role(X,Y)))).
fof(m,axiom,![X,B]:(member(X,valres(B)) <=> ![Y]:(role(X,Y) => member(Y,B)))).
fof(n,conjecture, ![A,B]:( (subset(dirimg(A),B) | equal_sets(dirimg(A),B)) <=> (subset(A,valres(B)) | equal_sets(A,valres(B))))).