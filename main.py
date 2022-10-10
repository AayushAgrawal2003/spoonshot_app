X = open('data.txt')
data = str(X.read())
data = data.strip().split()
from search import arr
# arr = ['hello my good' , "good","freind","g"]
# data = ["hello" ,"my", "good" ,"freind"]
#Brute Force Approach
def brute():
    for j in range(len(arr)):
        word_count = len(arr[j].strip().split())
        #print(arr[j], word_count)
        for i in range(len(data)):

            for k in range(word_count):
                print(arr[j].split()[k])
                if arr[j].split()[k] == data[i]:
                    print(arr[j].split()[k])
            #word_count = len(arr[j].strip().split())
            #print(len(data)-i)
            if (len(data) - i) >= word_count:
                #print(" ".join(data[i:i+word_count]) + "  " + arr[j])
                if (" ".join(data[i:i+word_count])) == arr[j]:
                    print(" ".join(data[i:i+word_count]))





if __name__ == '__main__':
    brute()