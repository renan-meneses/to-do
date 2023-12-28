from rest_framework.permissions import IsAuthenticated

import pandas as pd
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework import status
from apps.tasks.models import TaskModel

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def process_excel(request):
    if 'excel_file' not in request.FILES:
        return Response({'error': 'Nenhum arquivo fornecido.'}, status=status.HTTP_400_BAD_REQUEST)

    excel_file = request.FILES['excel_file']

    try:
        df = pd.read_excel(excel_file, skiprows=1)

        for item in df.iterrows():
            print(item.Nome)
            

        return Response({'message': 'Arquivo Excel processado com sucesso.'}, status=status.HTTP_200_OK)

    except Exception as e:
        print(f"Erro durante o processamento do Excel: {str(e)}")
        return Response({'error': f'Erro durante o processamento do Excel: {str(e)}'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)