import pandas as pd
import matplotlib.pyplot as plt

print("********** ENTER THE OPTION **********")
print("1.For flight search analysis\n")
print("2.For Google Trending Searches\n")
opt=int(input("\nEnter"))
if opt==1:
    def dateselect(x):
    
        if x=='2018-12-16':
            df=pd.read_csv('flights_tickets_serp2018-12-16.csv')
        elif x=='2019-07-15':
            df=pd.read_csv('flights_tickets_serp2019-07-15.csv')
        elif x=='2019-08-01':
            df=pd.read_csv('flights_tickets_serp2019-08-01.csv')
        elif x=='2020-02-15':
            df=pd.read_csv('flights_tickets_serp2020-02-15.csv')
        else:
            print("\n********************No Data Available for This Date********************")
    
    
        user=str(input("The flight was for : "))
        n="flights to " + user

       
        num=df.loc[df["searchTerms"]==n,"title"]
        print("The number of flight tickets booked to "+ user +" was: "+str(len(num)))



    def details(x):
    
        if x=='2018-12-16':
            df=pd.read_csv('flights_tickets_serp2018-12-16.csv')
        elif x=='2019-07-15':
            df=pd.read_csv('flights_tickets_serp2019-07-15.csv')
        elif x=='2019-08-01':
            df=pd.read_csv('flights_tickets_serp2019-08-01.csv')
        elif x=='2020-02-15':
            df=pd.read_csv('flights_tickets_serp2020-02-15.csv')
        else:
            print("\n******************** No Data Available for This Date ********************")
    
    
        user=str(input("Enter the flight : "))
        n="flights to " + user
        
       
        num=df.loc[df["searchTerms"]==n,"title"]
        print("**********Tiket details**********")
        print(num)

    def time(x):
    
        if x=='2018-12-16':
           df=pd.read_csv('flights_tickets_serp2018-12-16.csv')
        elif x=='2019-07-15':
           df=pd.read_csv('flights_tickets_serp2019-07-15.csv')
        elif x=='2019-08-01':
           df=pd.read_csv('flights_tickets_serp2019-08-01.csv')
        elif x=='2020-02-15':
           df=pd.read_csv('flights_tickets_serp2020-02-15.csv')
        else:
            print("\n********************No Data Available for This Date********************")
    
    
        user=str(input("The flight was for : "))
        n="flights to " + user
        #get the value
       
        t=df.loc[df["searchTerms"]==n,"queryTime"]
        print(t)




    print("******************** PLEASE SELECT THE OPTION ********************")
    print("\n1.For getting the number of tickets booked on a particular date\n")
    print("2.For getting the ticket details\n")
    print("3.For getting the time\n")

    op=int(input("Enter the Option number: "))
    dateentry=str(input("\nEnter the date: "))
    
    if op==1:
        dateselect(dateentry) #number of flight tickets booked 
    
    elif op==2:
        print(details(dateentry))#flight ticket details

    elif op==3:
        time(dateentry)#for getting time details
    else:
        print("********** ENTER THE CORRECT OPTION **********")


elif opt==2:
    
    import sys
    from pytrends.request import TrendReq
    
    Trending_topics = TrendReq()

    ch=1
    while ch in (1, 2, 3, 4):

        print("\n1.Most searched topic in any year\n")
        print("2.Most related search about any topic\n")
        print("3.Exploration about any topic\n")
        print("4.Latest trending searches\n")
        print("5.Topic searched over time\n")
        print("6.exit\n")

        op=int(input("Enter the option: "))

        if op==1:
            year=int(input("Enter the year: "))
            df = Trending_topics.top_charts(year, hl='en-US',
		  						    tz=300, geo='GLOBAL')
            print(df.head(20))

        elif op==2:
            top=str(input("Enter the topic: "))
            Trending_topics.build_payload(kw_list=[top])
            related_queries = Trending_topics.related_queries()
            print(related_queries.values())

        elif op==3:
            word=str(input("Enter the topic: "))
            keywords = Trending_topics.suggestions(keyword=word)
            df = pd.DataFrame(keywords)
            print(df.drop(columns= 'mid'))
        elif op==4:
            pytrend= TrendReq()
            df= pytrend.trending_searches(pn='india')
            print(df.head(10))
        elif op==5:
            kw_list = [str(input("Enter the topic : "))]

            Trending_topics.build_payload(kw_list, cat=0, timeframe='today 12-m') 
            data = Trending_topics.interest_over_time() 
            data = data.reset_index() 
        
            import plotly.express as px
            fig = px.line(data, x="date", y=kw_list, title='Keyword Web Search Interest Over Time')
            fig.show() 
        elif op==6:
            sys.exit()
        else:
            print("\n**********Enter the correct option.**********")




else:
    print("********** ENTER THE CORRECT OPTION **********")
