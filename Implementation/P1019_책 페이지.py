import sys
input = sys.stdin.readline

def count_pages(n):
    count = [0]*10
    start,end = 1, n
    digit = 1
    
    while start <= end:
        # end 를 9로 끝나는 수로 맞추기
        while end % 10 != 9 and start <= end:
            t = end
            while t > 0:
                count[t % 10] += digit
                t //= 10
            end -= 1
        
        # start 를 0으로 끝나는 수로 맞추기
        if start > end:
            break
        
        while start % 10 != 0 and start <= end:
            t = start
            while t > 0:
                count[t % 10] += digit
                t //= 10
            start += 1
        
        # 이제 start 는 0, end 는 9로 끝남 → 자릿수 전체 더하기
        if start > end:
            break
        
        cnt = (end//10 - start//10 + 1)
        for i in range(10):
            count[i] += cnt * digit
        
        digit *= 10
        start //= 10
        end //= 10
    
    return count

N = int(input())
ans = count_pages(N)
print(*ans)