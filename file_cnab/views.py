from django.shortcuts import render
from rest_framework.parsers import MultiPartParser
from rest_framework.views import APIView

from .forms import UploadFileForm
from .models import FileCnab
from .serializers import FileCnabSerializer


class UploadFileCnabView(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        file_cnab = request.FILES["file_cnab"]
        
        for item in file_cnab: 
            line = item.decode()
            data = {
                "type_number": line[0],
                "date": f"{line[1:5]}-{line[5:7]}-{line[7:9]}",
                "value": line[9:19],
                "cpf": line[19:30],
                "card": line[30:42],
                "time": f"{line[42:44]}:{line[44:46]}:{line[46:48]}",
                "owner": line[48:62],
                "store":  line[62:]
            }
            serializer = FileCnabSerializer(data=data)
            serializer.is_valid(raise_exception=True)
            serializer.save()
            
            data_serializer = dataSerializer(FileCnab.objects.all())

        return render(request, "list_transactions.html", {"ul": data_serializer})

    def get(self, request):
        return render(request, "home.html", {"form": UploadFileForm})
    
def dataSerializer(serializer):
    new_list = []
    trasactions = [
        "", 
        "Débito", 
        "Boleto", 
        "Financiamento", 
        "Crédito", 
        "Recebimento Empréstimo", 
        "Vendas", 
        "Recebimento TED", 
        "Recebimento DOC", 
        "Aluguel",
    ]
    for object in serializer:
        for index, value in enumerate(trasactions):
            if object.type_number == index:
                object.type = value
                new_list.append(object)

    return new_list

     
