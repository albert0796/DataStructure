def ans(srr,stt):
    if(len(stt) < len(srr)):
        for cc in srr:
            if not cc in stt:
                stt.append(cc)
                ans(srr, stt) 
                stt.remove(cc)
    else:
        print(stt)
sr= "ABCD"
st= list()
ans(sr, st) 
