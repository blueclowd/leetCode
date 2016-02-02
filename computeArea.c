#include "functionInterface.h"


/**
 Find the total area covered by two rectilinear rectangles in a 2D plane.

 Each rectangle is defined by its bottom left corner and top right corner as shown in the figure.
*/
int computeArea(int A, int B, int C, int D, int E, int F, int G, int H) {

    // (A,B) - (C,D)   (E,F) - (G-H)
    int minX, minY, maxX, maxY;

    minX = A < E ? E : A;
    maxX = C < G ? C : G;

    minY = B < F ? F : B;
    maxY = D < H ? D : H;

    printf("[%d,%d]-[%d,%d]", minX, minY, maxX, maxY);

    int overlap;

    if (minX >=maxX || minY >= maxY)
    {
        overlap = 0;
    }
    else
    {
        overlap = (maxX-minX)*(maxY-minY);
    }

    return (C-A)*(D-B) + (G-E)*(H-F) - overlap;

}

