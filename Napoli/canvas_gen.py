import sys
import pandas as pd




#These values will be character cutoff limits for text formatting
small_text = 10
medium_text = 50
large_text = 500

format_text = 50



#building_number_size = 10           #0 A
#apartment_number_size = 10          #1 B
#names_size = 50                     #2 C
#phone_number_size = 50              #3 D
#email_size = 50                     #4 E
#facebook_size = 10                  #5 F
#contact_size = 10                   #7 H
#interest_size = 10                  #9 J
#spanish_size = 10                   #12 M
#complaints_size = 500               #8  I
#apartment_acc_size = 10             #13 N
#pamphlet_size = 10                  #14 O
#last_visit_size = 50                #6  G
#knowledge_neighbor_size = 50        #11 L
#potential_leader_size = 50          #10 K
#comments_size = 500                 #15 P

class color:
   PURPLE = '\033[95m'
   CYAN = '\033[96m'
   DARKCYAN = '\033[36m'
   BLUE = '\033[94m'
   GREEN = '\033[92m'
   YELLOW = '\033[93m'
   RED = '\033[91m'
   BOLD = '\033[1m'
   UNDERLINE = '\033[4m'
   END = '\033[0m' 

#create list from dataframe   
def createList():
    
    df = pd.read_excel(sys.argv[1], 
                       dtype = str)
    df = df.fillna('')
    df_list = df.values.tolist()
    return df_list

#clean up the input and format it a bit
def sanitizeList(df_list):
    
    #format building numbers
    sep = '.'
    sep2 = ' '
    for i in df_list:
        i[0] = str(i[0]).split(sep, 1)[0]
        i[0] = (str(i[0])[0:small_text]).ljust(format_text)
    
        #format unit numbers    
        i[1] = str(i[1]).split(sep, 1)[0]
        i[1] = str(i[1])[0:small_text]
        
        #names
        i[2] = (str(i[2])[0:medium_text]).ljust(format_text)
        
        #phone
        if i[3] != '':
            i[3] = 'Yes'
        i[3] = (str(i[3])[0:medium_text].ljust(format_text)).upper()
        
        if i[4] != '':
            i[4] = 'Yes'
        i[4] = (str(i[4])[0:medium_text].ljust(format_text)).upper() #email
        
        i[5] = (str(i[5])[0:small_text].ljust(small_text)).upper()   #Facebook
        i[7] = (str(i[7])[0:small_text].ljust(format_text)).upper()  #contact
        i[9] = (str(i[9])[0:small_text].ljust(format_text)).upper()  #Interest
        i[12] = str(i[12])[0:small_text].ljust(format_text)  #spanish
        i[8] = (str(i[8])[0:large_text]).lower()                     #complaints
        i[13] = str(i[13])[0:small_text].ljust(format_text)#apartment accessible
        i[14] = str(i[14])[0:small_text].ljust(format_text)#pamphlet
        
        i[6] = str(i[6]).split(sep2, 1)[0]
        i[6] = str(i[6])[0:medium_text].ljust(small_text)#last visit
        
        i[11] = str(i[11])[0:medium_text].ljust(format_text)#knowledge of neighbors
        i[10] = str(i[10])[0:medium_text].ljust(format_text)#potential leader
        i[15] = str(i[15])[0:large_text].ljust(large_text)  #comments
        
    return df_list

#Write info to file    
def writeText(df_list):
    f = open("tenantinfo.txt", "a")
    bld_count = "-1"
    
    
    for i in df_list:
        #print(i[1])
        contactible = (i[8].find('do not contact') == -1) #are they not a do not contact? #yes
        contact_info = ((i[3] != '') or (i[4] != '') or (i[5] != '')) #DO WE HAVE ANY CONTACT INFO? #yes
        some_interest_level = ((i[9].find('MEDIUM') != -1) or (i[9].find('HIGH')) != -1) #Is there interest? #yes
        contacted = (i[7].find('YES') != -1) #Have we contacted them previously? #yes
        #print(contactible,contact_info,some_interest_level,contacted)
        if i[0] != bld_count and i[1] != '':
            f.write("\nBuilding Number: " + i[0] + '\n')
            f.write("_________________________" + '\n')
            bld_count = i[0]
        if i[1] != '':  
            #print((contactible and not(contacted)) or (not(contact_info) and some_interest_level))
            if((contactible and not(contacted)) or (not(contact_info))): #and some_interest_level)):
                f.write("_________________________" + '\n')
                f.write("Unit " + i[1] + "\n" + "Name: " + i[2] + "Phone: " + i[3] + "Facebook: " + i[5] + "Last visit: " + i[6] + '\n')
                f.write("Email: " + i[4] + '\n')
                f.write("\nNotes: " + i[8] + ' ' + i[15] + '\n')
           
            
    #f.write("Now the file has more content!")
    f.close()
    
    
df_list = createList()

df_list = sanitizeList(df_list)
writeText(df_list)


#{"Building number": str,
#                            "Apartment Number": str,
#                            "Name(s)": str,
#                            "Phone Number": str,
#                            "FaceBook group": str,
#                            "Able to contact": str
#                            "Price":float})
#"Park At Napoli Tenant Info.xlsx"