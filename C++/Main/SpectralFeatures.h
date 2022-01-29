//
//  SpectralFeatures.h
//  Main
//
//  Created by Jesús Valdez on 29/01/22.
//

#include <iostream>
#include <vector>
#include "math.h"

class SpectralFeatures
{
public:
    
    SpectralFeatures();
    ~SpectralFeatures();
    
    float getRMS(std::vector<float> inSamples, std::string inUnit);
    
private:
    
    
    
};
