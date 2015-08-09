from django.shortcuts import render_to_response
from django.template import RequestContext
from forms import RomanForm

integer_to_roman = {
        '1': 'I', '2': 'II', '3': 'III', '4': 'IV', '5': 'V',
        '6': 'VI', '7': 'VII', '8': 'VIII', '9': 'IX', '10': 'X',
        '20': 'XX', '30': 'XXX', '40': 'XL', '50': 'L',
        '60': 'LX', '70': 'LXX', '80': 'LXXX', '90': 'XC', '100': 'C',
        '200': 'CC', '300': 'CCC', '400': 'CD', '500': 'D',
        '600': 'DC', '700': 'DCC', '800': 'DCCC', '900': 'CM', '1000': 'M',
        '2000' : 'MM', '3000' : 'MMM'
        }

# Recursive function that accepts a list of integers
# and converts it itno Roman Numerals
def recursive(integer_list, prefix, coef, num_to_add, roman_number):
    if len(integer_list) == 0:
        return 1
    number = integer_list.pop()
    print "number: ", number
    if number == '0':
        num_to_add = num_to_add + number
    # In case if 'number' is anything else than '0'
    else:
        num_to_calc = integer_to_roman[number + prefix * coef + num_to_add]
        prefix = '0'
        coef = coef + 1
        roman_number.append(num_to_calc)
    return (recursive(integer_list, prefix, coef, num_to_add, roman_number), roman_number)

# This function accepts an instance of HttpRequest,
# which consists of dictionaries that represent
# information from the current Web request (request.META,
# request.POST etc) and returns an instance of
# HttpResponse object
def roman_form(request):
    if request.method == 'POST':
         form = RomanForm(request.POST)
         if form.is_valid():
             # Get a dictionary of 'cleaned data' from the from
             cd = form.cleaned_data
             integer = cd['integer']
             # Convert retrieved from 'cleaned data' dictionary
             # integer into a list
             integer_list = list(str(integer))
             # Call recursive function 'recursive' to calculate
             # the conversion of integer into Roman numeral
             f, roman_number_list = recursive(integer_list, '', 0, '', [])
             # Reverse the resulting list and convert it
             # into a string for display on the page
             roman_number_str = ''.join((list(reversed(roman_number_list))))
             return  render_to_response('roman_form.html', {'roman_number': roman_number_str, 'flag': 2 }, RequestContext(request))
    else:
         form = RomanForm()
    return render_to_response('roman_form.html', {'form': form, 'flag': 1 }, RequestContext(request))