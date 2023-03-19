# python3 221RDB047 
swaps=[]

def parent(index):
    return index//2

def fix_branch(heap,index):
    index=index+1
    if index==1:
        return heap
    if heap[parent(index)-1]>heap[index-1]:
        heap[parent(index)-1],heap[index-1]=heap[index-1],heap[parent(index)-1]
        swaps.append((parent(index)-1,index-1))
        heap=fix_branch(heap,parent(index)-1)
    return heap

def rebuild_heap(heap):
    
    for i in range(len(heap)-1,0,-1):
        heap=fix_branch(heap,i)
    
    # print(heap)


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 5
    # 5 4 3 2 1
    # first two tests are from keyboard, third test is from a file
    type=input()
    

    # input from keyboard
    if not type.upper().find("I")==-1:
        lenght=int(input())
        data = list(map(int, input().split()))
    # input from file
    else:
        filename = "tests/"+input()
        file=open(filename)
        lenght=int(file.readline())
        data = list(map(int, file.readline().split()))

    # checks if lenght of data is the same as the said lenght

    assert len(data) == lenght

    # calls function to assess the data 
    # and give back all swaps
    
    rebuild_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
