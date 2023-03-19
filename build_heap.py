# python3 221RDB047 

def check_heap(heap):
    for index in range(len(heap)-1,0,-1):
        if heap[index]<heap[index//2]:
            return index
    return -1

def swap_with_parent(heap,index):
    heap[index],heap[index//2]=heap[index//2],heap[index]
    return heap

def build_heap(data):
    swaps = []
    
    heap=[0]
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    for index in range(len(data)):
        heap.append(data[index])
    index=check_heap(heap)
    while not check_heap(heap)==-1:
        current_index=index
        index=index-1
        while heap[current_index]<heap[current_index//2]:
            heap=swap_with_parent(heap,current_index)
            swaps.append((current_index//2-1,current_index-1))
            # print(current_index//2-1,"<->",current_index-1)
            current_index=current_index//2
    
    return swaps


def main():
    
    # TODO : add input and corresponding checks
    # add another input for I or F 5
    # 5 4 3 2 1
    # first two tests are from keyboard, third test is from a file
    type=input()
    lenght=int(input())

    # input from keyboard
    if not type.find("I")==-1:
        data = list(map(int, input().split()))
    # input from file
    else:
        data = list(map(int, open(input()).read().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == lenght

    # calls function to assess the data 
    # and give back all swaps
    
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()
