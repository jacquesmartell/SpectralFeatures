//
//  SpectralFeatures.h
//  Main
//
//  Created by Jesús Valdez on 29/01/22.
//

#include "SpectralFeatures.h"

SpectralFeatures::SpectralFeatures(){}
SpectralFeatures::~SpectralFeatures(){}

std::vector<float> SpectralFeatures::getVectorTime(std::vector<float> inSamples, float inSampleRate)
{
    std::vector<float> timeVector;
    
    for(int i = 0; i < inSamples.size(); i++)
        timeVector.push_back(i/inSampleRate);
    
    return timeVector;
}

float SpectralFeatures::getRMS(std::vector<float> inSamples, int inScale)
{
    float sumCuadrados = 0.0f;
    float rmsValue = 0.0f;
    
    for(int i=0; i < inSamples.size(); i++)
    {
        sumCuadrados += powf(inSamples[i], 2);
    }
    
    switch(inScale)
    {
        case DB:
        {
            if(sqrt(sumCuadrados / inSamples.size()) != 0.0f)
                rmsValue = 20.0f * log10(abs(sqrt(sumCuadrados / inSamples.size()))) / 1.0f;
            else
                rmsValue = -60.0f;
            
            break;
        }

        case LINEAR:
        {
            rmsValue = sqrt(sumCuadrados / inSamples.size());
            break;
        }
            
        default:
        {
            rmsValue = 0.0f;
            break;
        }

    }
    
    return rmsValue;
}

float SpectralFeatures::getCentroid(std::vector<float> inSamples, float inSampleRate, int inDomain)
{
    float centroidValue = 0.0f;
    
    switch(inDomain)
    {
        case TIME:
        {
            std::vector<float> timeVector = getVectorTime(inSamples, inSampleRate);
            
            float numerador = 0.0f;
            float denominador = 0.0f;
            
            for(int i = 0; i < timeVector.size(); i++)
            {
                numerador += (inSamples[i] * timeVector[i]);
                denominador += inSamples[i];
            }
            
            centroidValue = numerador / denominador;
            break;
        }
            
        case FREQUENCY:
        {
            std::cout << "FREQUENCY" << std::endl;
            break;
        }

        default:
        {
            centroidValue = 0.0f;
            break;
        }

    }
    
    return centroidValue;
}

float SpectralFeatures::getPeak(std::vector<float> inSamples, float inSampleRate, int inDomain)
{
    float peakValue = 0.0f;
        
    switch(inDomain)
    {
        case TIME:
        {
            std::vector<float> timeVector = getVectorTime(inSamples, inSampleRate);
            
            int maxIndex = 0;
            float maxValue = 0.0f;
            for(int i = 0; i < inSamples.size(); i++)
            {
                if (inSamples[i] >= maxValue)
                    maxIndex = i;
            }
            
            peakValue = timeVector[maxIndex];
            
            break;
        }

        
        case FREQUENCY:
        {
            
            break;
        }
            
        default:
        {
            peakValue = 0.0f;
            break;
        }
    }
    
    return peakValue;
}

float SpectralFeatures::getSpread(std::vector<float> inSamples, float inSampleRate, int inDomain)
{
    float spreadValue = 0.0f;
    
    float centroid = getCentroid(inSamples, inSampleRate, inDomain);
    
    switch(inDomain)
    {
        case TIME:
        {
            std::vector<float> timeVector = getVectorTime(inSamples, inSampleRate);
            
            float sumaSpread = 0.0f;
            float sumaSamples = 0.0f;
            
            for(int i = 0; i < inSamples.size(); i++)
            {
                sumaSpread += powf(timeVector[i] - centroid, 2.0f) * inSamples[i];
                sumaSamples += inSamples[i];
            }
            
            spreadValue = sqrtf(fabs(sumaSpread / sumaSamples));
            
            break;
        }

        
        case FREQUENCY:
        {
            
            break;
        }
            
        default:
        {
            spreadValue = 0.0f;
            break;
        }
    }
    
    return spreadValue;
}
