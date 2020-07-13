def lower(str1):
    result=""
    # str1="Vikash Kumar Gupta"
    new=list(str1.split(" "))
    new.reverse()
    for i in new:
        for j in i:
            if j.isupper():
                j=j.lower()
            else:
                j=j.upper()
            result+=""+j
        result+=" "
    return result
if __name__ == "__main__":
    str1=input()
    print(lower(str1))
