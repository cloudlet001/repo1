# -*- coding:utf8 -*-
'''
Created on 2018年4月11日

@author: bhlin
'''
#Python函数 dict()
#https://www.cnblogs.com/guyuyuan/p/6952442.html

d1=dict()    # 创建空字典 {}

d2=dict(a='1', b='2', t='t')    # 传入关键字 {'a': '1', 'b': '2', 't': 't'}

d3 = dict(zip(['one', 'two', 'three'], [1, 2, 3]))   # 映射函数方式来构造字典 {'three': 3, 'two': 2, 'one': 1} 

d4 = dict([('one', 1), ('two', 2), ('three', 3)])    # 可迭代对象方式来构造字典  {'three': 3, 'two': 2, 'one': 1}


if __name__ == '__main__':
    #list all keys
    print "#list all keys"
    for k in d4 : print k
    
    #list of keys
    keys=[k for k in d4]
    print "keys = %s" % (keys)
    
    # check if key k existed
    print "# check if key k existed"
    k="one"
    if k in d4: print "Has key : %s" % (k)
    
    if d4.has_key(k): print "Has key : %s" % (k)
    else: print "Has no key : %s" % (k)
    
    #list all k, v pairs
    print "#list all k, v pairs"
    for k, v in d4.items(): print k, v