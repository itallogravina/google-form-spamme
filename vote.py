'''
Form Link

https://docs.google.com/forms/d/e/1FAIpQLScEm6OKcAEuso9P955IlaohxmjrcN8dFXTgwRrhU20GXiTlZw/viewform

POST Link

https://docs.google.com/forms/d/e/1FAIpQLScEm6OKcAEuso9P955IlaohxmjrcN8dFXTgwRrhU20GXiTlZw/formResponse

Logical Conclusion after scanning the source code of the form

Question : What if I say you spam this question ??

entry.481806567
I can
entry.481806567
I can't

What's your CodeChef rank ?

entry.1631013625

Rate Python

entry.736567249

What is needed to hack the form

entry.2012950491
entry.2109148023
entry.797761672

Select the best day of your life till now 

entry.2115250323_year
entry.2115250323_month
entry.2115250323_day

INSTRUCTIONS

Save the file with .py extension and execute it to see the result.

'''
import requests
import time
i=0;
a=0;
a1=0;
a2=0;
a3=0;
url = 'https://docs.google.com/forms/u/0/d/e/1FAIpQLScfWI6FvjOnPsytNERbZhBV1h1haRtPOwiMiLMSuDg1UCPs9g/formResponse'

form_data = {
		'entry.918888786'	:	'Alice',
		}
form_data2 = {
		'entry.918888786'	:	'Gabriela',
		}
	
form_data3 = {
		'entry.918888786'	:	'Samuel',
		}

user_agent ={
		'Referer':'https://docs.google.com/forms/d/e/1FAIpQLScfWI6FvjOnPsytNERbZhBV1h1haRtPOwiMiLMSuDg1UCPs9g/viewform',
		'User-Agent':"Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/28.0.1500.52 Safari/537.36"
		}

while(1):

	a=a+1
	i=i+1
 
	if(a>=6):
		a=0;
	
 	if(i%1==0):
		# if(a>=0 and a<=2):
		print('Alice')
		r = requests.post(url, data=form_data, headers=user_agent)
		print(r)
		a1=a1+1
		print("total",a1)
		# # if(a>=3 and a<5):
		# 	print('Samuel ')
		# 	r = requests.post(url, data=form_data3, headers=user_agent)
		# 	print(r)
		# 	a2=a2+1
		# 	print('total',a2)
		# # if(a==5):
		# # 	print('Gabriela')
		# # 	r = requests.post(url, data=form_data2, headers=user_agent)  
		# # 	print(r)
		# # 	a3=a3+1
		# # 	print("total",a3)
	
		print(i)
		if(i==50):
			break
 
		time.sleep(2)
		

  
  
  
