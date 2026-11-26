def formula(s,K,zv):
    c=(-1)**((K-1)//2)*2**(K-1)*s[K-1]
    for i in range(K-1):
        c*=s[i]**3
        for j in range(i+1,K-1): c*=(s[i]**2-s[j]**2)**4
        c*=(s[i]**2-s[K-1]**2)**2
    return c*zv**((2*K-1)*(K-1))
