# -*- coding: utf-8 -*-
"""
Created on Thu Mar 20 13:37:32 2014

@author: florian
"""
import numpy as np
import os

files_Mg3 = ['AlMg3_33kW_6_1.txt', 'AlMg3_33kW_6_2.txt', 'AlMg3_33kW_6_3.txt', 'AlMg3_33kW_6_4.txt',]


class DataReader:
    
    def read_pyro(self,file_list, cols_of_interest):
        """  returns dictionary: [filename1][column1],...[filename_n][column_n]  """
        AlMgSi1 = dict()
        for fi in file_list:  
            print 'read: ', fi 
            lines = []
            dictdata = dict()
            f = open(fi)
            line = f.readline()
            i = 0
            cols = list() # numbers of cols_of_interest
            while line !='':
                print line
                if i ==9:   #--------header in line 9
                    header = f.readline().strip('\n').split(' ')
                    headers = [h for h in header if h != '' and h in cols_of_interest]
                    all_headers = [h for h in header if h != '']
                    for j in range(len(all_headers)):
                        if all_headers[j] in headers:
                            cols.append(j)
                    print headers
                if i >9:
                    #print i
                    line = line.rstrip('\n').split(' ')   #-----columns seperated by ' '
                    line = [l for l in line if l != '']
                    #line.remove('')
                    lines.append(line)
                line = f.readline()
                i = i+1
            numdata = np.asanyarray(lines, dtype = 'float')
            for i,h in enumerate(headers):
                dictdata[h] = numdata[:,cols[i]]    
    #        norm_data(dictdata)# scale to max = 1
            AlMgSi1[os.path.basename(fi)] = dictdata     
        return AlMgSi1
        
    def get_labdict(self, labbook):
        """   """
        print 'get_labdict'
        lb = open(labbook, 'r')
        line = lb.readline()
        while not line.startswith('# lfd'):
            line = lb.readline()
        print line
        headers = line.rstrip('\n').split('\t')
        print headers
        l = lb.readline()
        file_dict = dict()
        while l !='':
            filename = l.split('\t')[0] + '.txt'
            print filename
            file_dict[filename] = dict()
            for i,col in enumerate(l.strip('\n').split('\t')):
                file_dict[filename][headers[i]] = col
            l = lb.readline()
        return file_dict
                
    
    def read_files(self,file_list, cols_of_interest):
        """  returns dictionary: [filename1][column1],...[filename_n][column_n]  """
        AlMgSi1 = dict()
        for fi in file_list:  
            print 'read: ', fi 
            lines = []
            dictdata = dict()
            f = open(fi)
            line = f.readline()
            i = 0
            cols = list() # numbers of cols_of_interest
            while line !='':
                #print line
                if i ==8:   #--------header in line 9
                    header = f.readline().strip('\n').split(' ')
                    headers = [h for h in header if h != '' and h in cols_of_interest]
                    all_headers = [h for h in header if h != '']
                    for j in range(len(all_headers)):
                        if all_headers[j] in headers:
                            cols.append(j)
                if i >8:
                    #print i
                    line = line.rstrip('\n').split(' ')   #-----columns seperated by ' '
                    line = [l for l in line if l != '']
                    #line.remove('')
                    lines.append(line)
                line = f.readline()
                i = i+1
            numdata = np.asanyarray(lines, dtype = 'float')
            for i,h in enumerate(headers):
                dictdata[h] = numdata[:,cols[i]]    
#            norm_data(dictdata)# scale to max = 1
            AlMgSi1[os.path.basename(fi)] = dictdata     
        return AlMgSi1
        
    def cutzeros_file_dict(self,file_dict):
        print 'cutzeros_file_dict'
        lenlist = list()
        for k in file_dict.keys():
            file_dict[k] = self.cutzeros_column(file_dict[k])
            lenlist.append(len(file_dict[k]))
        for k in file_dict.keys():
            c = np.zeros(np.max(lenlist))
            c[0:len(file_dict[k])] = file_dict[k]
            file_dict[k] = c            
        return file_dict
    
    def cutzeros_column(self, column):
        print 'cutzeros_column'
        print 'before ', len(column)
        for i in range(len(column)):
            if column[-i] != 0:
                break
        column = column[0:-i]
        print 'after ', len(column)
        return column
        
        
if __name__ == '__main__':
    d = DataReader()
    print 'read_files'
    print d.read_files(files_Mg3)