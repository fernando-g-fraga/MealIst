import datetime

def get_WeekArray(n_Receitas:int)-> list[str]:
    week_Days = []
    
    start_date = datetime.datetime.now()
    end =  n_Receitas + start_date.day

    for i in range(start_date.day,end):
            x = datetime.date(start_date.year,start_date.month,i)    
            week_Days.append(x.strftime("%A"))
            
    return week_Days
