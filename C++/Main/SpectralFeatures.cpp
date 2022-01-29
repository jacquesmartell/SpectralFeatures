//
//  SpectralFeatures.h
//  Main
//
//  Created by Jesús Valdez on 29/01/22.
//
#include "SpectralFeatures.h"

SpectralFeatures::SpectralFeatures(){}
SpectralFeatures::~SpectralFeatures(){}

float SpectralFeatures::getRMS(std::vector<float> inSamples, std::string inScale)
{
    float sumCuadrados = 0.0f;
    float rmsValue = 0.0f;
    
    for(int i=0; i < inSamples.size(); i++)
    {
        sumCuadrados += powf(inSamples[i], 2);
    }
    
    // DECIBELS OR LINEAR
    if (inScale == "linear")
        rmsValue = sqrt(sumCuadrados / inSamples.size());
    else if (inScale == "dB")
    {
        if(sqrt(sumCuadrados / inSamples.size()) != 0.0f)
            rmsValue = 20.0f * log10(abs(sqrt(sumCuadrados / inSamples.size()))) / 1.0f;
        else
            rmsValue = -60.0f;
    }
    else
        rmsValue = 0.0f;
    
    std::cout << "RMS en " << inScale << ": " << rmsValue << std::endl;
    
    return rmsValue;
}
