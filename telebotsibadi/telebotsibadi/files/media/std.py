
def lab_pk(pk):
    #/lab/52/?next=/group/10/
    lab_pk = ''
    change_pk = pk[5:-7]
    for i in change_pk:
        if i.isdigit():
            lab_pk += i
    return lab_pk
    

