#include <iostream>
#include <vector>
#include "math.h"

float getRMS(std::vector<float> inSamples, std::string inUnit)
{
    float sumCuadrados = 0.0f;
    float rmsValue = 0.0f;
    
    for(int i=0; i < inSamples.size(); i++)
    {
        sumCuadrados += powf(inSamples[i], 2);
    }
    
    // DECIBELS OR LINEAR
    if (inUnit == "linear")
        rmsValue = sqrt(sumCuadrados / inSamples.size());
    else if (inUnit == "dB")
    {
        if(sqrt(sumCuadrados / inSamples.size()) != 0.0f)
            rmsValue = 20.0f * log10(abs(sqrt(sumCuadrados / inSamples.size()))) / 1.0f;
        else
            rmsValue = -60.0f;
    }
    else
        rmsValue = 0.0f;
    
    return rmsValue;
}

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
    
    // RMS
    std::cout << "RMS en dB: " << getRMS(samples, "dB") << std::endl;
    std::cout << "RMS lineal: " << getRMS(samples, "linear") << std::endl;
    
    return 0;
}
