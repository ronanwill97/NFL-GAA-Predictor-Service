from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from NFL.utils.responses import *
from datetime import datetime
import logging

logger = logging.getLogger("django")


@api_view(['POST'])
def receive_response(request):
    if request.method == 'POST':
        try:
            data = request.data  # DRF handles JSON parsing
            if isinstance(data, list):
                for response in data:
                    save_response(response)
            else:
                logger.info(data)
                save_response(data)
        except KeyError:
            return Response('Invalid request data', status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            logger.error(str(e))  # Log the error
            return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)

        return Response("SUCCESS")
    # The decorator automatically restricts this to POST, so the else part is not needed


@api_view(['GET'])
def tally_responses(request):
    try:
        league_round = request.query_params.get('round', '1')
        year = int(request.query_params.get('year', datetime.now().year))
        scores = calculate_scores(league_round, year)

        sorted_scores = sort_scores(scores)
        return Response(sorted_scores)
    except Exception as e:
        logger.error(str(e))  # Log the error
        return Response(str(e), status=status.HTTP_500_INTERNAL_SERVER_ERROR)
