#include <iostream>
#include <vector>
#include "SpectralFeatures.h"

int main(int argc, const char * argv[])
{
    // DATA
    float data[] = {0.5, 0.3, 0.2, 0.6, -0.2, -0.7, 0.20, 0.47, -0.21, 0.99};
    float sampleRate = 48000;
    
    // STD VECTOR
    std::vector<float> samples;
    for(int i=0; i < 10; i++)
    {
        samples.push_back(data[i]);
    }
    
    SpectralFeatures spectralFeatures;
    
    // RMS
    std::cout << "RMS in dB: " << spectralFeatures.getRMS(samples, Unit::DB) << std::endl;
    std::cout << "RMS linear: " << spectralFeatures.getRMS(samples, Unit::LINEAR) << std::endl;
    
    // CENTROID
    std::cout << "Centroid in time: " << spectralFeatures.getCentroid(samples, sampleRate, Domain::TIME) << std::endl;
    
    // PEAK
    std::cout << "Peak in time: " << spectralFeatures.getPeak(samples, sampleRate, Domain::TIME) << std::endl;
    
    //SPREAD
    std::cout << "Spread in time: " << spectralFeatures.getSpread(samples, sampleRate, Domain::TIME) << std::endl;
    
    return 0;
}
