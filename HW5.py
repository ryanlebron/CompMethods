import numpy as np
import matplotlib.pyplot as plt
from numpy import fft
import dcst
import argparse

filepath1 = '/Users/ryanlebron/Astronomy/CUNY_Astro/ComputationalMethods/CompMethods/dow.txt'
filepath2 = '/Users/ryanlebron/Astronomy/CUNY_Astro/ComputationalMethods/CompMethods/dow2.txt'



#define function for dft
#there will be two functions, one for 10% one for 2%
def dft10(filepath):
    #load in data from file
    data = np.loadtxt(str(filepath))

    #Calculate the coefficients of the discrete Fourier transform of the data 
    coefficients = fft.rfft(data)

    #set last 90% of coefficients to zero
    length = len(coefficients)
    ninety = int(len(coefficients)*.9)
    coefficients[-ninety:] = 0

    #Calculate the inverse Fourier transform
    inverse_fourier = fft.irfft(coefficients,n=len(data),axis=0)

    #plot data and inverse fourier
    plt.plot(data,'k.',label='Dow Closing Values')
    plt.plot(inverse_fourier,'.',label='Inverse Fourier Transform')
    plt.legend()
    plt.show()

def dft2(filepath):
    #load in data from file
    data = np.loadtxt(str(filepath))

    #Calculate the coefficients of the discrete Fourier transform of the data 
    coefficients = fft.rfft(data)

    #set last 98% of coefficients to zero
    length = len(coefficients)
    ninetyeight = int(len(coefficients)*.98)
    coefficients[-ninetyeight:] = 0

    #Calculate the inverse Fourier transform
    inverse_fourier = fft.irfft(coefficients,n=len(data),axis=0)

    #plot data and inverse fourier
    plt.plot(data,'k.',label='Dow Closing Values')
    plt.plot(inverse_fourier,'.',label='Inverse Fourier Transform')
    plt.legend()
    plt.show()


#define function for DCT
def dct10(filepath):
    #load in data from file
    data = np.loadtxt(str(filepath))

    #calulate the coefficients using DCT
    coefficients = dcst.dct(data)

    #set last 90% of coefficients to zero
    length = len(coefficients)
    ninety = int(len(coefficients)*.9)
    coefficients[-ninety:] = 0

    #Calculate the inverse Fourier transform
    inverse_fourier = dcst.idct(coefficients)

    #plot data and inverse fourier
    plt.plot(data,'k.',label='Dow Closing Values')
    plt.plot(inverse_fourier,'.',label='Inverse Fourier Transform')
    plt.legend()
    plt.show()

def dct2(filepath):
    #load in data from file
    data = np.loadtxt(str(filepath))

    #calulate the coefficients using DCT
    coefficients = dcst.dct(data)

    #set last 98% of coefficients to zero
    length = len(coefficients)
    ninetyeight = int(len(coefficients)*.98)
    coefficients[-ninetyeight:] = 0

    #Calculate the inverse Fourier transform
    inverse_fourier = dcst.idct(coefficients)

    #plot data and inverse fourier
    plt.plot(data,'k.',label='Dow Closing Values')
    plt.plot(inverse_fourier,'.',label='Inverse Fourier Transform')
    plt.legend()
    plt.show()




parser = argparse.ArgumentParser(description='')
parser.add_argument('filepath', type=str, help='input the filepath for the file, dow.txt or dow2.txt')
FUNCTION_MAP = {'dft10' : dft10,
                'dft2' : dft2,
                'dct10': dct10,
                'dct2': dct2 }
parser.add_argument('command', choices=FUNCTION_MAP.keys(), help = 'input which type of transform you would like to use, along with what percent of coefficients to keep. Ex: dct2 will use discrete cosine transform, and keep 2 percent of the coefficients.')

args = parser.parse_args()

func = FUNCTION_MAP[args.command]
file = args.filepath
func(file)