from django.shortcuts import render
from django.http import HttpRequest


def calculo(request):
    if request.method == 'POST' :
        monto = float(request.POST.get('monto'))
        tasa = round((float(request.POST.get('tasa'))/100/12),4)
        plazo = (float(request.POST.get('plazo'))*12)
        cuota = round(((float(monto)*tasa) / (1-(1+tasa) ** -plazo)),2)
        total_a_pagar = round((cuota*plazo),2)
        

        diccionario = [{ 
            'monto': monto,
            'tasa' : tasa,
            'plazo' : plazo,
            'cuota': cuota,    
            'total_a_pagar' : total_a_pagar,
        },
        ]

        ctx = {
            'diccionario':diccionario
        }

        return render(request, 'prestamo/calculo.html', ctx)
    else :
        
        return render(request, 'prestamo/calculo.html')
