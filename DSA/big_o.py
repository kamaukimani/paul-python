#Big O notation

# Problem
# given a number calutate the total of sum
# 5-> 5+4+3+2+1
# 10-> 
import time

def calculate_sum(n):

    sum =0
    for numb in range (1,n+1):
        print(f"sum ={sum} , numb={numb}")
        sum=sum+numb
    print(f"For {n} The sum is {sum}")
    return sum


start_time=time.time()
calculate_sum(5000)
end_time=time.time()
diff=end_time-start_time
print(f"Speed {diff}")