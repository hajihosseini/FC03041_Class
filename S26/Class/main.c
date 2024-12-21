
char set_bit(char c, int i, int v)
{
    char x = 1;
    if (v == 0)
        c = ~(x << i) & c;
    else
        c = (x << i) | c;
}

char get_bit(char c, int i)
{
    if ((1 << i) & c)
        return 1;
    return 0;
}

char swap_bits(char c, int i, int j)
{
    char biti = get_bit(c, i);
    char bitj = get_bit(c, j);

    c = set_bit(c, i, bitj);
    c = set_bit(c, j, biti);
}

char rev_bits(char c)
{
    for(int i=0; i<4; i++)
        c = swap_bits(c, i, 8-i-1);
}


void main()
{
    char x = 0x7b; // 0111 1011
                   // 0101 1110  0x5e
    char r = rev_bits(x);
}