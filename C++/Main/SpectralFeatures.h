//
//  SpectralFeatures.h
//  Main
//
//  Created by Jesús Valdez on 29/01/22.
//

#include <iostream>
#include <vector>
#include "math.h"

enum Domain
{
    TIME = 1,
    FREQUENCY = 2
};

enum Unit
{
    DB = 1,
    LINEAR = 2
};

class SpectralFeatures
{
public:
    
    SpectralFeatures();
    ~SpectralFeatures();
    
    std::vector<float> getVectorTime(std::vector<float> inSamples, float inSampleRate);
    
    float getRMS(std::vector<float> inSamples, int inUnit);
    
    float getCentroid(std::vector<float> inSamples, float inSampleRate, int inDomain);
    
    float getPeak(std::vector<float> inSamples, float inSampleRate, int inDomain);
    
private:
    
    
    
};
