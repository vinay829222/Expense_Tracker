from tracker.models import RequestLogs

class RequestLogging:
    def __init__(self,get_response):
        self.get_response=get_response

    def __call__(self, request):
        request_info=request
        #print(request_info)

        #print(request_info.path,request_info.method) 

       # print(self.get_response(request))

        RequestLogs.objects.create(
            request_info=vars(request_info),
            request_type=request_info.path,
            request_method=request_info.method
        )

        


        return self.get_response(request)

   