# https://www.acmicpc.net/problem/2845

# wrong

l, p = map(int, input().split())

news_predict = map(int, input().split())

answer = l*p

for predict_num in news_predict:
    error = answer - predict_num
    
    print(error, end=' ')
    
# answer
    
l, p = map(int, input().split())

news_predict = map(int, input().split())

answer = l*p

for predict_num in news_predict:
    error = predict_num - answer
    
    print(error, end=' ')