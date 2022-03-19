import time, doctest

from modules import fileReader, paymentCalculator

def main():

    """
    >>> fileReader.readtxt('testFile')
    ['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00']
    
    >>> paymentCalculator.calculate(['RENE=MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00', 'ASTRID=MO10:00-12:00,TH12:00-14:00,SU20:00-21:00'])
    ['The amount to pay RENE is: 215 USD', 'The amount to pay ASTRID is: 85 USD']
    
    >>> paymentCalculator.processHours('MO10:00-12:00,TU10:00-12:00,TH01:00-03:00,SA14:00-18:00,SU20:00-21:00')
    215
    """
    file_name=input('Please insert the name of the file:')
    results_list=paymentCalculator.calculate(fileReader.readtxt(f'{file_name}'))
    
    for result in results_list:
        print(result)
        
    pass
main()
doctest.testmod()
