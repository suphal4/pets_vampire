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
  444,[431,[417,[414,[410,[408,[334,[255,[251,[248,[246,[243,[115,[67,[47,[27,[7],[2]],[11]],[1]],[38,[37,[33,[32,[17],[4]]],[4]]]],[10]]],[3]]],[43,[24,[9],[2]],[1]]],[12]],[22,[8],[2]]]],[3]]],[16]],[251,[248,[246,[243,[115,[67,[47,[27,[7],[2]],[11]],[1]],[38,[37,[33,[32,[17],[4]]],[4]]]],[10]]],[3]]]
]

nodes = {
  1: '~member(X0,X2) | ~subset(X2,X1) | member(X0,X1) ',
  2: 'member(member_of_1_not_of_2(X2,X1),X2) | subset(X2,X1)', 
  3: '~member(member_of_1_not_of_2(X2,X1),X1) | subset(X2,X1) ',
  4: '~equal_sets(X2,X1) | subset(X2,X1) ',
  7: '~member(X1,X2) | ~role(X1,X0) | member(X0,dirimg(X2))',
  8: '~member(X0,dirimg(X2)) | role(sK0(X0,X2),X0) ',
  9: '~member(X0,dirimg(X2)) | member(sK0(X0,X2),X2) ',
  10:'~member(sK1(X0,X2),X2) | member(X0,valres(X2)) ',
  11: 'role(X0,sK1(X0,X2)) | member(X0,valres(X2)) ',
  12: '~member(X0,valres(X2)) | ~role(X0,X4) | member(X4,X2)', 
  16: '~subset(dirimg(sK2),sK3) | ~subset(sK2,valres(sK3)) ',
  17: 'equal_sets(dirimg(sK2),sK3) | subset(dirimg(sK2),sK3) | subset(sK2,valres(sK3)) | equal_sets(sK2,valres(sK3))', 
  22: 'role(sK0(member_of_1_not_of_2(dirimg(X0),X1),X0),member_of_1_not_of_2(dirimg(X0),X1)) | subset(dirimg(X0),X1) ',
  24: 'member(sK0(member_of_1_not_of_2(dirimg(X0),X1),X0),X0) | subset(dirimg(X0),X1) ',
  27: '~role(member_of_1_not_of_2(X0,X1),X2) | member(X2,dirimg(X0)) | subset(X0,X1) ',
  32: 'subset(dirimg(sK2),sK3) | subset(sK2,valres(sK3)) | equal_sets(sK2,valres(sK3)) | subset(dirimg(sK2),sK3)', 
  33: 'equal_sets(sK2,valres(sK3)) | subset(sK2,valres(sK3)) | subset(dirimg(sK2),sK3) ',
  37: 'subset(sK2,valres(sK3)) | subset(dirimg(sK2),sK3) | subset(sK2,valres(sK3)) ',
  38: 'subset(dirimg(sK2),sK3) | subset(sK2,valres(sK3)) ',
  43: '~subset(X3,X5) | subset(dirimg(X3),X4) | member(sK0(member_of_1_not_of_2(dirimg(X3),X4),X3),X5)', 
  47: 'member(sK1(member_of_1_not_of_2(X0,X1),X2),dirimg(X0)) | subset(X0,X1) | member(member_of_1_not_of_2(X0,X1),valres(X2))', 
  67: '~subset(dirimg(X12),X15) | member(member_of_1_not_of_2(X12,X13),valres(X14)) | subset(X12,X13) | member(sK1(member_of_1_not_of_2(X12,X13),X14),X15) ',
  115: 'member(sK1(member_of_1_not_of_2(sK2,X0),X1),sK3) | subset(sK2,X0) | member(member_of_1_not_of_2(sK2,X0),valres(X1)) | subset(sK2,valres(sK3)) ',
  243: 'subset(sK2,X0) | member(member_of_1_not_of_2(sK2,X0),valres(sK3)) | subset(sK2,valres(sK3)) | member(member_of_1_not_of_2(sK2,X0),valres(sK3))',
  246: 'member(member_of_1_not_of_2(sK2,X0),valres(sK3)) | subset(sK2,X0) | subset(sK2,valres(sK3)) ',
  248: 'subset(sK2,valres(sK3)) | subset(sK2,valres(sK3)) | subset(sK2,valres(sK3)) ',
  251: 'subset(sK2,valres(sK3)) ',
  255: 'member(sK0(member_of_1_not_of_2(dirimg(sK2),X4),sK2),valres(sK3)) | subset(dirimg(sK2),X4)', 
  334: '~role(sK0(member_of_1_not_of_2(dirimg(sK2),X0),sK2),X1) | subset(dirimg(sK2),X0) | member(X1,sK3)', 
  408: 'subset(dirimg(sK2),X0) | member(member_of_1_not_of_2(dirimg(sK2),X0),sK3) | subset(dirimg(sK2),X0) ',
  410: 'member(member_of_1_not_of_2(dirimg(sK2),X0),sK3) | subset(dirimg(sK2),X0) ',
  414: 'subset(dirimg(sK2),sK3) | subset(dirimg(sK2),sK3) ',
  417: 'subset(dirimg(sK2),sK3) ',
  431: '~subset(sK2,valres(sK3))', 
  444: '$false' 
}

resolution = {
  'active': [1,2,3,4,5,6,8,13,14,15,16,19,9,21],
  'passive': [7,10,11,12,17,18,20,22,23],
  'unprocessed': [24],
  'premises': [9,2],
  'conclusion': 24,
  'mgu': {'X0':'member_of_1_not_of_2(X1,X3)','X2':'dirimg(X4)'} }

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# vim:set et sw=2 ts=2:
