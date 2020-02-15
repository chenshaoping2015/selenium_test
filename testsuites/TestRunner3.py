#coding=utf-8
import unittest
import os

test_dir = os.path.abspath(os.path.dirname(os.getcwd()))+'/testsuites/'
print(test_dir)

suite = unittest.defaultTestLoader.discover(test_dir,pattern='test*.py')

if __name__=='__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite)

