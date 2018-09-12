# -*- coding: utf-8 -*-
"""
Created on Wed Sep  5 18:08:37 2018

@author: Bryon Mosier
"""

import glob
import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET

###############################################################################

# def for looping through xml files
    # path need to be set to whatever folder ends up being the
    # this function will not collect text between oprning and closing element tags - only values tied to attributes inside the elements
def xmlCC(path='H:/Performance Analytics/CC*.xml'):
    # read in files into a list
    xmlList = [open(filename).read() for filename in glob.glob(path)] 
    # create empty list to house roots of each xml file
    roots = []
    for i in xmlList:
        roots += [ET.XML(i)]
    
    concatData = []
    for aroot in roots:
    
        pairs = []
        for child in aroot.iter():
            pairs += [child.tag, child.attrib]
    
        # loop to convert dicts in lists
        cleaned = []
        for i in pairs:
            if type(i)==str:
                cleaned.append([i])
    
            elif type(i)==dict:
                for k,v in i.items():
                    
                    cleaned.append([k,v])
                    #print('dictionary!!')
            else:
                print('Something bad happened')
            
            # convert list to DataFrame
            cleaned_DF = pd.DataFrame.from_records(cleaned)
            # transpose DF
            cleaned_DF_T = cleaned_DF.T
            # set row 0 as column headers
            cleaned_DF_T.columns = cleaned_DF_T.iloc[0]
        
        # append cleaned_DF_T to concatData while removing row 0
        concatData += [cleaned_DF_T.reindex(cleaned_DF_T.index.drop(0))]       
    
    # concatenate rows from 
    woohoo = pd.concat(concatData, axis=0)
    return woohoo

###############################################################################
test5 =xmlCC()

# =============================================================================
# # experimentation required to get to the final product
# path = 'H:/Performance Analytics/CC_8164_OK.xml'
# xml_data = open(path).read()
# root = ET.XML(xml_data)
# type(tree)
# root = tree.getroot()
# 
# 
# for child in root:
#     print(child.tag, child.attrib)
#     
# 
# [elem.tag for elem in root.iter()]
# 
# for elem in root.iter():
#     print(elem.tag)
#     
# # single line loop - gives list of all     
# [elem.tag for elem in root]
# 
# 
# # Loop for iterating through child and sub-child elements - shows promise - needs to iterate through sub-child elements    
# for elem.tag in root.iter():
#     for attrib in elem.tag:
#         print(attrib.attrib)
# 
# 
# # Loop for iterating through child and sub-child elements - not working        
# elemList = []
# for elem in root.iter():
#     temp = elem.find
#     for i in temp.iter():
#         print(i)
#     #print(type(temp))
# 
#     
# # Testing xpath - not working
# root.findall('./{http://www.meridianlink.com/CLF}APPLICANTS/{http://www.meridianlink.com/CLF}APPLICANT/')
# 
# 
# applicants = root.findall('./{http://www.meridianlink.com/CLF}APPLICANTS/')
# fname = root.findall('./{http://www.meridianlink.com/CLF}APPLICANTS/{http://www.meridianlink.com/CLF}APPLICANT/')
# print(applicants)
# 
# 
# print(ET.tostring(root, encoding='utf8').decode('utf8'))
# 
# # showing promise - need to find how to convert to list/df/etc
# for item in root.iter('{http://www.meridianlink.com/CLF}APPLICANT'):
#     print(item.attrib)
# 
# applicantList = []
# for item in root.iter('{http://www.meridianlink.com/CLF}APPLICANT'):
#     applicantList = [item.attrib]
# 
# # practice stuff    
# print(root)
# 
# childTest = root[0]
# childTest
# 
# for child in root:
#     print(child.tag)
# 
# # IT WORKS!!!!!!!!!!!!!!! - small victories
# root[0][0].get('first_name')
# 
# # this doesn't work - indices need to be integers
# root['{http://www.meridianlink.com/CLF}APPLICANTS']['{http://www.meridianlink.com/CLF}APPLICANT'].get('first_name')
# 
# 
# root[0].attrib
# 
# 
# for i in root[0][0]:
#     print(i.attrib)
#     
#     
# for name, value in root[0][0].items():
#     print('%s=%r' % (name, value))
#     
# for i in root[0][0].items():
#     print(i)
# 
# testtest = []
# for i in root[0][0].items():
#     testtest += [i]
#     
# for i in testtest:
#     for x in i:
#         print(x.split())
# 
# # NOT NEEDED MUAHAHAHAAHAHAHAH!!!!
# # starting test build for manually pulling data
# # applicants
# #   applicant
# fname = root[0][0].get('first_name')
# lname = root[0][0].get('last_name')
# mname = root[0][0].get('middle_name')
# cis = root[0][0].get('member_number')
# ssn = root[0][0].get('ssn')
# dob = root[0][0].get('dob')
# creditscore = root[0][0].get('credit_score')
# 
# #       financial info
# #           income
# income = root[0][0][6][1].get('monthly_income_base_salary')
# 
# #           liabilities
# liability = root[0][0][6][2].get('monthly_liability')
# 
# # loan info
# card_name = root[1].get('card_name')
# apr = root[1].get('apr')
# credit_limit = root[1].get('credit_limit')
# 
# 
# # price adjustment
# #   price adjustment
# ###############################################################################
# 
# what=root[0][0].items()
# 
# path = 'H:/Performance Analytics/CC_8164_OK.xml'
# xml_data = open(path).read()
# root = ET.XML(xml_data)
# type(tree)
# root = tree.getroot()
# 
# path = 'H:/Performance Analytics/CC*.xml'
# xmllist = [open(filename).read() for filename in glob.glob(path)]
# 
# 
# 
# 
# 
# # def for looping through xml files
# def xmlCC(path='H:/Performance Analytics/CC*.xml'):
#     xmlList = [open(filename).read() for filename in glob.glob(path)]
#     roots = []
#     for i in xmlList:
#         roots += [ET.XML(i)]
#     
#     testList = []
#     for i in roots:
#         applicant = pd.DataFrame.from_records(i[0][0].items())
#         applicantT = applicant.T
#         applicantT.columns = applicantT.iloc[0]
#         testList += [applicantT.reindex(applicantT.index.drop(0))]
# 
#     woohoo = pd.concat(testList, axis=0)
#     return woohoo
# 
# cc_data = xmlCC()
# 
# # testing loop without def
# roots = []
# for i in xmllist:
#     roots += [ET.XML(i)]
# 
# 
# 
# testList = []
# for i in roots:
#     applicant = pd.DataFrame.from_records(i[0][0].items())
#     applicantT = applicant.T
#     applicantT.columns = applicantT.iloc[0]
#     testList += [applicantT.reindex(applicantT.index.drop(0))]
#     
# woohoo = pd.concat(testList, axis=0)
# 
# # HEll YEAH!!!!!!!!
# 
# woohoo.to_csv('H:/Performance Analytics/qatest.csv')    
# 
# 
# 
# xmlCC1.readFiles()
# xmlCC.rootList(xmlList)
# xmlCC.struc_stack(roots)
# xmlCC.concatList(testList)
# xmlCC.createCSV(woohoo)
# 
# allData = []
# for child in root.iter():
#     allData += [child.tag, child.attrib]
# 
# 
# temp = []
# allDataForReal = []
# for i in allData:
#     if type(i)==str:
#         allDataForReal.append([i])
#     
#     elif type(i)==dict:
#         for k,v in i.items():
#             temp = [k, v]
#             #print(type(temp))
#             allDataForReal.append(temp)
#             #print('dictionary!!')
#     else:
#         #allDataForReal.append(i)
#         print(type(i))
#         print('what the hell is going on?')
# 
# 
# 
# test1 = pd.DataFrame.from_records(allDataForReal)
# test1T = test1.T
# test1T.columns = test1T.iloc[0]
# test1TList = test1T.reindex(test1T.index.drop(0))
# test1TList.to_csv('H:/Performance Analytics/woohoo.csv')
# 
# allData.count(type)
# 
# dictionary1 = {1:2,
#                3:4}
# 
# type(dictionary1)        
# 
# type(allData[1])
# 
# temp = []
# dictList = []
# for k,v in dictionary1.items():
#     print(k,v)
#     temp = [k,v]
#     dictList.append([k,v])
# 
# 
# applicant = pd.DataFrame.from_records(root[0][0].items())
# test = applicant.T
# test.columns = test.iloc[0]
# test = test.reindex(test.index.drop(0))
# test.to_csv('H:/Performance Analytics/qatest.csv')
# root
# 
# 
# 
# 
# 
# # def for looping through xml files
# def xmlCC(path='H:/Performance Analytics/CC*.xml'):
#     xmlList = [open(filename).read() for filename in glob.glob(path)]
#     roots = []
#     for i in xmlList:
#         roots += [ET.XML(i)]
#     
#     testList = []
#     for i in roots:
#         applicant = pd.DataFrame.from_records(i[0][0].items())
#         applicantT = applicant.T
#         applicantT.columns = applicantT.iloc[0]
#         testList += [applicantT.reindex(applicantT.index.drop(0))]
# 
#     woohoo = pd.concat(testList, axis=0)
#     return woohoo
# ###############################################################################
# 
# # def for looping through xml files
#     # path need to be set to whatever folder ends up being the
#     # this function will not collect text between 
# def xmlCC(path='H:/Performance Analytics/CC*.xml'):
#     # read in files into a list
#     xmlList = [open(filename).read() for filename in glob.glob(path)] 
#     # create empty list to house roots of each xml file
#     roots = []
#     for i in xmlList:
#         roots += [ET.XML(i)]
#     
#     concatData = []
#     for aroot in roots:
#     
#         pairs = []
#         for child in root.iter():
#             pairs += [child.tag, child.attrib]
#     
#         # loop to convert dicts in lists
#         cleaned = []
#         for i in allData:
#             if type(i)==str:
#                 cleaned.append([i])
#     
#             elif type(i)==dict:
#                 for k,v in i.items():
#                     
#                     cleaned.append([k,v])
#                     #print('dictionary!!')
#             else:
#                 print('Something bad happened')
#             
#             # convert list to DataFrame
#             cleaned_DF = pd.DataFrame.from_records(cleaned)
#             # transpose DF
#             cleaned_DF_T = cleaned_DF.T
#             # set row 0 as column headers
#             cleaned_DF_T.columns = cleaned_DF_T.iloc[0]
#         
#         # append cleaned_DF_T to concatData while removing row 0
#         concatData += [cleaned_DF_T.reindex(cleaned_DF_T.index.drop(0))]       
#     
#     # concatenate rows from 
#     woohoo = pd.concat(concatData, axis=0)
#     return woohoo
# 
# ###############################################################################
# test5 =xmlCC()
# 
# allData = []
# for child in root.iter():
#     allData += [child.tag, child.attrib]
# 
# 
# temp = []
# allDataForReal = []
# for i in allData:
#     if type(i)==str:
#         allDataForReal.append([i])
#     
#     elif type(i)==dict:
#         for k,v in i.items():
#             temp = [k, v]
#             #print(type(temp))
#             allDataForReal.append(temp)
#             #print('dictionary!!')
#     else:
#         #allDataForReal.append(i)
#         print(type(i))
#         print('what the hell is going on?')
# =============================================================================
