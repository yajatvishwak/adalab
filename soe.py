def soe(n):
    #assume that all numbers till n are primes
    prime = [True for _ in range(n+1)]
    #now we know 0 and 1 arent primes comeon, duhhhhh
    prime[0] = False
    prime[1] = False
    #so we start from 2 all the way till N, cross off all the multiples on the way
    # oh i mean all multiples of current number are no longer primes, so make them FALSE in the prime list
    for i in range(2,n):
        # here we compare 2 things, 1st thing if the number is already marked as a non prime, if it is, we can skip that number
        # second thing is i*i <= n, what this does is skips the previous multiples eg 1x5, 2x5,3x5,4x5 are alredy marked, skip it and start from 5x5
            if prime[i] and i*i<=n: 
                    for j in range(i*i, n+1, i):
                            prime[j]=False
    return prime



# driver code - absolutely not required. can hardcode
n = int(input("enter number"))
k = 0
for i in soe(n):
    if i:
        print(str(k),"prime")
    else:
        print(str(k),"not prime")
    k+=1
