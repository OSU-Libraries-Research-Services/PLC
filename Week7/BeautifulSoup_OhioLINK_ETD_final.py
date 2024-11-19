# -*- coding: utf-8 -*-
"""
Created on Thu Nov 14 09:39:36 2024

@author: murphy.465

Helpful references for Week7 lesson

https://regex101.com/
Regular Expressions Cheat Sheet https://www.datacamp.com/cheat-sheet/regular-expresso

"""

# Import modules
import os
from pathlib import Path
from bs4 import BeautifulSoup as bs
import re
import pandas as pd

#####Store Search Results
results=pd.DataFrame(columns=['title','author','degree','degre_year','department','advisors','subjects'])


###### START BY LOOKING AT ONE FILE ONLY!!!!!

filepath = "C:/Users/murphy.465/OneDrive - The Ohio State University/Desktop/Week7/2023_dissertations/2023_etd_phd_1.html"
contents=open(filepath, encoding="utf-8").read()
soup = bs(contents, 'lxml')
count=0
etd_contents=soup.find_all(attrs={"class":'t-SearchResults-content'})
etd_authors=soup.find_all(attrs={"class":'t-SearchResults-author'})
etd_titles=soup.find_all(attrs={'t-SearchResults-title','a'})


committee_members=[]
for each_record in etd_contents:
    author=each_record.span.text
    title=each_record.a.text
    degree_paragraph=each_record.p.text
    degree_paragraph_parsed=degree_paragraph.split(',')
    degree=degree_paragraph_parsed[0].strip()
    degree_year=degree_paragraph_parsed[2].strip()
    search_for_department_in=".*[0-9]{4}, (.*)"
    department=re.findall(search_for_department_in,degree_paragraph)
    department=department[0]
    dissertation_committee_members=each_record.find_all(attrs={"class":'t-SearchResults-misc'})
    for members in dissertation_committee_members[0]:
        dissertation_committee=members.text
        advisors=[]
        list_of_committee_members=dissertation_committee.split(';')
        for each_committee_member in list_of_committee_members:
            if "Advisor" in each_committee_member:
                advisor=each_committee_member.split('(')
                advisor=advisor[0]
                advisor=advisor.strip()
                advisors.append(advisor)
                
    advisors=', '.join(advisors)
    assigned_subjects=dissertation_committee_members[1]
    for subject in assigned_subjects:
        subjects=subject.text

    
    print("*********************")
    print(title)
    print(author)
    print(degree)
    print(degree_year)
    print(department)
    print(f"advisor(s) = {advisors}")
    print(f"subject(s) = {subjects}")
    
    
###### THEN ITERATE THROUGH DIRECTORY!!!!! 

# Assign directory
filepath = r"C:/Users/murphy.465/OneDrive - The Ohio State University/Desktop/Week7/2023_dissertations"

# # Find all files from directory
files = Path(filepath).glob("*")
# Iterate over files in directory
for filename in files:
    # Open file


    with open(os.path.join(filepath, filename), encoding="utf8") as f:

        print(f"Content of '{filename}'")
        # Read content of file
        # print(f.read())

    # print()

        contents=open(filename, encoding="utf-8").read()
        soup = bs(contents, 'lxml')
        count=1
        etd_contents=soup.find_all(attrs={"class":'t-SearchResults-content'})
        etd_authors=soup.find_all(attrs={"class":'t-SearchResults-author'})
        etd_titles=soup.find_all(attrs={'t-SearchResults-title','a'})
        
        
        committee_members=[]
        for each_record in etd_contents:
            count += 1

            author=each_record.span.text
            title=each_record.a.text
            degree_paragraph=each_record.p.text
            degree_paragraph_parsed=degree_paragraph.split(',')
            degree=degree_paragraph_parsed[0].strip()
            degree_year=degree_paragraph_parsed[2].strip()
            search_for_department_in=".*[0-9]{4}, (.*)"
            department=re.findall(search_for_department_in,degree_paragraph)
            department=department[0]
            dissertation_committee_members=each_record.find_all(attrs={"class":'t-SearchResults-misc'})
            for members in dissertation_committee_members[0]:
                dissertation_committee=members.text
                advisors=[]
                list_of_committee_members=dissertation_committee.split(';')
                for each_committee_member in list_of_committee_members:
                    if "Advisor" in each_committee_member:
                        advisor=each_committee_member.split('(')
                        advisor=advisor[0]
                        advisor=advisor.strip()
                        advisors.append(advisor)
                        
            advisors=', '.join(advisors)
            assigned_subjects=dissertation_committee_members[1]
            for subject in assigned_subjects:
                subjects=subject.text
                
                
        
            
            print("*********************")
            print(count)
            # print(count100)
            print(title)
            print(author)
            print(degree)
            print(degree_year)
            print(department)
            print(f"advisor(s) = {advisors}")
            print(f"subject(s) = {subjects}")
            
            entry={
                'title':title,
                'author':author,
                'degree':degree,
                'degree_year':degree_year,
                'department':department,
                'advisors':advisors,
                'subjects':subjects
                }
            
            record_results=pd.DataFrame(entry, index=[0])
            results=pd.concat([record_results, results], axis=0)
            


            

            

            

    
    
    
    
