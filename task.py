import re
PATTERN = re.compile(r'^([a-z]+?)\1*$')
def f(s):
    seg = PATTERN.findall(s)[0]
    return seg, len(s) / len(seg)

def solve(c,s):
        s1=list(s.replace(" " , ""))
        c1=list(c.replace(" " ,""))
        if s1==c1 :
            return True
        if c1[:] == ["*"]:
            return True
        if len(c1)>len(s1):
            if "*" in c1 :
                c1.remove("*")
                if len(c1)==len(s1) and c1==s1:
                     return True
                elif len(c1)>len(s1):
                    return False
        if len(c1)==len(s1) and c1==s1:
            return True
        elif len(c1)==len(s1) and c1!=s1:
             return  False 
        if len(c1)<len(s1) :
            if len(c1)==1 and "* " in c1 :
                    return True 
            elif len(c1)>1 :
                k= c.find("*")
                x=len(s1)- len(c1) +k+1
                for i in range(k,x) :
                    c1.insert(i , s1[i])
                c1.remove("*")
        if c1==s1:
            return True

def is_palindrome(s):
        a=s.lower()
        b=s[::-1].lower()
        try:
            if a==b:
                return  True
            else:
                return False
        except:
            print("error") 
              
def find_nth_occurrence(substring, string, occurrence=1):             
                place = string.find("example", 0 , len(string))
                if occurance ==1:
                    return  place
                while occurance > 1 :
                    place= string.find("example",place+1,len(string))
                    occurance-=1
                return place
            
            
def find_nth_occurrence(substring, string, occurrence=1):             
                ind= string.find(substring, 0 , len(string))
                if occurrence ==1:
                    return  ind
                while occurrence > 1 :
                    ind = string.find(substring ,ind+1,len(string))
                    occurrence-=1
                return ind                
                 