
import os
import shutil
import docx2txt
from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.template import loader

from .businessLayer import GetInformation 

# Create your views here.
def index(request):
    #return render(request,'home.html')
    template = loader.get_template('cv.html')
    data = {'scancv'}
    value ={
            'data':data
        }
    return HttpResponse(template.render(value,request))
def search(request):
    getInfo = GetInformation()
    trainedData = request.GET.get('searchKey', None)
    '''Provide your folder locations'''
    print(trainedData)
    #Below path is for out put directory
    outputFileDirectoryPath = os.path.abspath("ScanedCVs")
    
    #Below path is for input put directory
    inputFileDirectoryPath = os.path.abspath("Resume_data")
    '''Setp 1:- Getting the set of search keys, and convert 
                to a list for further uses'''
    #Below path is for train data, Only directory path.
    fileData = open(os.path.abspath("Trained_Data") +"\\" +trainedData ,'r')
    content = fileData.readlines()
    fileData =[]
    for value in content:
         fileData=value
    '''End of Setp 1''' 
       
    memberData = []
    '''Setp 2:- Logic for reading all resumes from dir '''
    filesDir= getInfo.get_filepaths(inputFileDirectoryPath)
    #print(filesDir)
    for filePath in filesDir:
        print(filePath)
        itemList=[]
        member_phoneNumber=""
        member_email=""
        fileName = os.path.basename(filePath).split('.')[0]
        text = docx2txt.process(filePath)
        '''Calling NLTK function after removing the stop words '''
        freq = getInfo.Apply_NLTK(text) #nltk.FreqDist(words_token)

        """Logic for words frequenct count----"""
        #searchKeyList = searchKey.split(',')
        for key,val in freq.items():
            for value in fileData.split(","):
                if value.strip().lower() == str(key).strip().lower():
                    if val >= 2:
                        member_email = getInfo.fetch_email(text)
                        member_phoneNumber = getInfo.fetch_phone(text)
                        #memer_skills=fetch_skills(text,fileData)
                        if fileName not in itemList:
                            itemList.append(fileName)
                            itemList.append(member_email)
                            itemList.append(member_phoneNumber)
                            itemList.append(key)
                            itemList.append(outputFileDirectoryPath)
                        shutil.copy(filePath , outputFileDirectoryPath)
        memberData.append(itemList)

    '''filesDir= get_filepaths(outputFileDirectoryPath)
    for filePath in filesDir:
        fileName = os.path.basename(filePath).split('.')[0]
        resultSet.append([fileName,filePath])
    print("Member data: ",memberData)'''

    if len(memberData) < 1:
        memberData.append(["No data"])  
    return render(request, 'CV_List.html', {'CV_List':memberData})

