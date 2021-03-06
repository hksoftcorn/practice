import requests
from pprint import pprint

my_key = 'AiBUNmsM9K9sjzrEnMG%2FIxnDykPdCDksW5KZKqUQKb%2BntuYdERzd7Vtvm6axiB3py85Z9b3Tn4dLJZEluy0WKg%3D%3D'
return_type = 'json'
num_of_rows = '5'
page_no = '1'
sido_name = '서울'


url = f'http://apis.data.go.kr/B552584/ArpltnInforInqireSvc/getCtprvnRltmMesureDnsty?serviceKey={my_key}&returnType={return_type}&numOfRows={num_of_rows}&pageNo={page_no}&sidoName={sido_name}&ver=1.0'

response = requests.get(url).json()
pprint(response)

# ~구의 미세먼지 농도는 {pm10Value}입니다.
my_sido = response['response']['body']['items'][0]['stationName']
my_pm10Value = response['response']['body']['items'][0]['pm10Value']
print(f'{my_sido}의 미세먼지 농도는 {my_pm10Value}입니다.')