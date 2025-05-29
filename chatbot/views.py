from rest_framework.views import APIView
from rest_framework.response import Response
from .llm_chain import get_rag_response


class ChatbotAPIView(APIView):
    def post(self, request):
        user_input = request.data.get("message")

        if not user_input:
            return Response({"error": "Message is required"}, status=400)
        try:
            response = get_rag_response(user_input)
            return Response({"response": response})
        except Exception as e:
            return Response({"error": str(e)}, status=500)
