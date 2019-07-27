import os
import re
import nltk
from nltk.corpus import stopwords

class GetInformation:
   
    """Logic for reading all files inside given directory path"""
    def get_filepaths(self,directory):
        file_paths = []  # List which will store all of the full filepaths.
        # Walk the tree.
        for root, directories, files in os.walk(directory):
            for filename in files:
                # Join the two strings in order to form the full filepath.
                filepath = os.path.join(root, filename)
                file_paths.append(filepath)  # Add it to the list.

            return file_paths  # Self-explanatory.

#This below function is implementing the NLTK
#Removing stop words after tokenize
    def Apply_NLTK(self,fileData):
        #nltk.download('stopwords')
        text = fileData
        words_token = nltk.word_tokenize(text)
        #sr = stopwords.words('english')
        for token in words_token:
            if token in stopwords.words('english'):
                words_token.remove(token)
        freq = nltk.FreqDist(words_token)
        return freq

        
    def fetch_email(self,resume_text):
        email = r"[A-Z0-9._%+-]+@[A-Z0-9.-]+\.[A-Z]{2,4}"
        regular_expression = re.compile(email, re.IGNORECASE)
        emails = ""
        result = re.search(regular_expression, resume_text)
        while result:
            emails = result.group()
            resume_text = resume_text[result.end():]
            result = re.search(regular_expression, resume_text)
        return emails

    '''Getting Phone Details'''
    def get_phone(self,i,j,n):
        return r"\(?(\+)?(\d{1,3})?\)?[\s-]{0,1}?(\d{"+str(i)+"})[\s\.-]{0,1}(\d{"+str(j)+"})[\s\.-]{0,1}(\d{"+str(n-i-j)+"})"

    def fetch_phone(self,resume_text):
        regular_expression = re.compile(self.get_phone(3, 3, 10), re.IGNORECASE)
        result = re.search(regular_expression, resume_text)
        phone = ''
        if result:
            result = result.group()
            for part in result:
                if part:
                    phone += part
        if phone is '':
            for i in range(1, 10):
                for j in range(1, 10-i):
                    regular_expression =re.compile(self.get_phone(i, j, 10), re.IGNORECASE)
                    result = re.search(regular_expression, resume_text)
                    if result:
                        result = result.groups()
                        for part in result:
                            if part:
                                phone += part
        if phone is not '':
            return phone
        return phone

    
    def fetch_skills(self,cleaned_resume,skills):
        skill_set = []
        for skill in skills.split(','):
            if skill.lower() in cleaned_resume:
                skill_set.append(skill)
        return skill_set
