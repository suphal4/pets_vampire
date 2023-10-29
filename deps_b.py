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
  'ep': 'off' }

tree = [
  18,[17,[16,[15,[14,[9,[8,[1]]],[12,[4]]],[10,[2]]],[9,[8,[1]]]],[11,[3]]],[13,[7,[6,[5]]]]
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
  10:'depend(clang) = llvm ',
  11: 'depend(llvm) = libc ',
  12: 'require(clang) ',
  13: '~require(libc) ',
  14: 'require(depend(clang))', 
  15: 'require(llvm) ',
  16: 'require(depend(llvm))', 
  17: 'require(libc) ',
  18: '$false '
}
resolution = {
  'active': [9,10,11,12,13],
  'passive': [],
  'unprocessed': [14],
  'premises': [9,12],
  'conclusion': 14,
  'mgu': {'X0':'clang'} }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=2 ts=2:
