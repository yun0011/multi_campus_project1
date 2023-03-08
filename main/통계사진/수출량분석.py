import pandas as pd
import matplotlib.pyplot as plt	
import seaborn as sns  
import matplotlib.image as img

ex = pd.read_excel(f'./Exports_calendar_year.xlsx', engine = "openpyxl")  #데이터 불러오기
#'C:/Users/master/Desktop/커피사이트_프로젝트/Exports_calendar_year.xlsx'
#필요없는 열 삭제
df = ex.drop(ex.columns[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]], axis = 1, inplace = False)

#필요없는 행 삭제
df = df.drop([0,1,2,58,59,60], axis=0, inplace=False)
df = df.rename(columns = {'Exports of all forms of coffee\nby all exporting countries':'국가', 'Unnamed: 21':'2010', 'Unnamed: 22':'2011', 'Unnamed: 23':'2012',
                          'Unnamed: 24':'2013','Unnamed: 25':'2014', 'Unnamed: 26':'2015','Unnamed: 27':'2016','Unnamed: 28':'2017','Unnamed: 29':'2018','Unnamed: 30':'2019'})  #열 이름 변경

#인덱스 초기화
df = df.reset_index(drop=True)                         

#결측치 0으로 채우기
df = df.fillna(0)

#국가를 인덱스로 설정
df = df.set_index('국가')

#국가별 수출량 합계
df['합계'] = df.sum(axis=1)

#국가별 평균 수출량
df['평균'] = df.mean(axis=1)

#국가별 평균 수출량 내림차순 정렬
df = df.sort_values(by='평균', ascending=False)

df_top5 = df.head(5)  #상위 5개 국가

############################################################
################seaborn#####################################
############################################################
ratio = [34, 32, 16, 18]
colors = sns.color_palette('copper',5, desat=0.5)
explode = [0, 0.10, 0, 0.10, 0]

plt.pie( df_top5['평균'], labels=df_top5.index, autopct='%.1f%%', startangle=90,
         counterclock=False, explode=explode, shadow = True, colors = colors)
plt.title('Average percentage of exports of coffee beans from the top five countries')
#plt.savefig(f'./line_plot.jpg', dpi = 300)
plt.show()

#막대그래프 만들기
plt.figure(figsize=(10,5))
plt.bar(df.index, df['평균'], color = colors)
plt.title('Average exports of coffee beans by country')
plt.xticks(rotation=90)
plt.show()