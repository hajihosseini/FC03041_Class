void swap(int* a, int* b)
{
    if ( (0 == a) || (0 == b) )
        return;

    int tmp = *a;
    *a = *b;
    *b = tmp;
}