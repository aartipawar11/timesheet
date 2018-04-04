
from rest_framework.response import Response

class ApiResponse:

	def success(self, response,code,token=None):
		
		msg = response if isinstance(response, str)  else "Successfully"
		result  = [] if isinstance(response, str)  else response
		res = {
			"data":{
				"message":  msg,
				"responseCode": code,
				"result":result,

			}
		}
		if not token is None:
			res['data']['token'] = token
		return Response(res)

	def paginationSuccess(self, response,code,count):
		
		res = {
			"data":{
				"message":  "Successfully",
				"responseCode": code,
				"result":response,
				"total_records":count
				

			}
		}
		
		return Response(res)
	
	def error(self, response,code):
		return Response({
			"data":{
				"message":  "error",
				"responseCode": code,
				"error":response
			}
		})	