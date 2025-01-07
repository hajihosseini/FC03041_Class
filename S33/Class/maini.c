#include"image_utils.h"

void main()
{
    BitMapFile  myImage;
    InitImage(&myImage, 300, 300);
    myImage.bmHeader.colorIdx[0].g = 255;
    myImage.bmHeader.colorIdx[1].r = 255;

    for(int i=0; i<290; i+=25)
        for(int j=0; j<300; j++)
        {
            for(int k=0; k<3; k++)
                myImage.bmData[(i+k)*300 + j] = 1;
        }
    
    WriteBitmapFile("simple_test.bmp", &myImage);
}