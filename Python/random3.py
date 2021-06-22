import datetime

def dateandtime(val,tup):
    # Write your code here
    empty_list = []
    date = list(tup)    
    if val == 1:
        input_date = datetime.date(date[0],date[1],date[2])
        format_date = input_date.strftime('%d/%m/%Y')        
        empty_list.append(input_date)
        empty_list.append(format_date)
    elif val == 2:
        date2 = datetime.datetime.fromtimestamp(date[0])
        proper_date = date2.strftime('%Y %m %d')
        split_str = proper_date.split(' ')
        val2 = datetime.date(int(split_str[0]),int(split_str[1]),int(split_str[2]))
        empty_list.append(val2)
    elif val == 3:
        time = datetime.time(date[0],date[1],date[2])
        empty_list.append(time)
        time_str = str(time)
        h1 = ord(time_str[0]) - ord('0')
        h2 = ord(time_str[1]) - ord('0')
        hh = h1 * 10 + h2
        h3 = str(hh % 12)
        empty_list.append(h3)
    elif val == 4:

    elif val == 5:
        


    
if __name__ == '__main__':
    val = int(input().strip())
    
    if val ==1 or val==4 or val ==3:
        qw1_count=3
    if val==2:
        qw1_count=1
    if val ==5:
        qw1_count=6
    qw1 = []

    for _ in range(qw1_count):
        qw1_item = int(input().strip())
        qw1.append(qw1_item)
        
    tup=tuple(qw1)
    
    ans = dateandtime(val,tup)
    
    print(ans)




        

