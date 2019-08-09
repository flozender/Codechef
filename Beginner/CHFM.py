for _t in range(int(input())):
    _ = int(input())
    coins = list(map(int, input().split()))
    origMean = sum(coins)/len(coins)
    for i in range(len(coins)):
        if coins[i] == origMean:
            print(i+1)
            break
    else:
        print("Impossible")