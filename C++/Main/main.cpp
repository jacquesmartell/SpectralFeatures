#include <iostream>
#include <vector>
#include "SpectralFeatures.h"

int main(int argc, const char * argv[])
{
    // DATA
    float data[] = {0.5, 0.3, 0.2, 0.6, -0.2, -0.7, 0.20, 0.47, -0.21, 0.99};
    
    // STD VECTOR
    std::vector<float> samples;
    for(int i=0; i < 10; i++)
    {
        samples.push_back(data[i]);
    }
    
    SpectralFeatures spectralFeatures;
    
    // RMS
    spectralFeatures.getRMS(samples, "dB");
    spectralFeatures.getRMS(samples, "linear");
    
    return 0;
}
