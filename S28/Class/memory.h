void swap(int  *a, int* b)
{
    if ( (0 == a) || (0 == b) )
        return;

    int tmp = *a;
    *a = *b;
    *b = tmp;
}

unsigned char get_byte2(unsigned int n, int c)
{
    unsigned int w = n >> (8*c);
    return (unsigned char) (w & 0xff);
}

unsigned char get_byte(unsigned int n, int c)
{
    unsigned char* pch = (unsigned char*) &n;
    return pch[c]; //*(pch+c)
}

int array_as_int(char* pch)
{
    int* pn = (int*)pch;
    return pn[0];
}

char* address_plus(char* pch, int n)
{
    return &(pch[n]);
    // pch = pch + n;
    // return pch;
}