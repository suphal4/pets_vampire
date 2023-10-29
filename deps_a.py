#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

options = {
  'updr': 'off',
  'fde': 'none',
  'nm': 0,
  'av': 'off',
  'fsr': 'off',
  's': 1,
  'awr': '1:1',
  'sa': 'discount',
  'ep': 'RSTC' }

tree = [
    57,[51,[46,[45,[29,[18,[14]],[15,[10,[2]],[14]]],[22,[9,[8,[1]]],[12,[4]]]],[9,[8,[1]]]],[30,[18,[14]],[16,[11,[3]],[14]]]],[13,[7,[6,[5]]]]
]

nodes = {
    1: '! [X0] : (require(X0) => require(depend(X0)))',
    2: 'depend(clang) = llvm ',
    3: 'depend(llvm) = libc ',
    4: 'require(clang) ',
    5: 'require(libc) ',
    6: '~require(libc) ',
    7: '~require(libc) ',
    8: '! [X0] : (require(depend(X0)) | ~require(X0))',
    9: '~require(X0) | require(depend(X0)) ',
    10: 'depend(clang) = llvm ',
    11: 'depend(llvm) = libc ',
    12: 'require(clang) ',
    13: '~require(libc) ',
    14: '! [X0,X1] : (sQ0_eqProxy(X0,X1) <=> X0 = X1) ',
    15: 'sQ0_eqProxy(depend(clang),llvm) ',
    16: 'sQ0_eqProxy(depend(llvm),libc) ',
    18: '~sQ0_eqProxy(X0,X1) | ~require(X0) | require(X1) ',
    22: 'require(depend(clang))',
    29: '~require(depend(clang)) | require(llvm) ',
    30: '~require(depend(llvm)) | require(libc)',
    45: 'require(llvm) ',
    46: 'require(depend(llvm)) ',
    51: 'require(libc) ',
    57: '$false'
}

resolution = {
  'active': [18,25,20,22,9,16,15,19,12,13],
  'passive': [21,17,23,24,26,27],
  'unprocessed': [29,28],
  'premises': [18,15],
  'conclusion': 29,
  'mgu': {'X0':'depend(clang)','X1':'llvm'} }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=2 ts=2:
