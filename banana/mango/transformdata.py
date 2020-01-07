from django.http import JsonResponse

class transformData:
    
    def __init__(self,blockId):
        self.blockId = blockId
        
    def getJsonData(self):
        data = {
            "version": "2.0",
            "template": {
                "outputs": [
                {
                    "simpleText": {
                    "text": "평소에는 아무렇지도 않던 일들이 괴롭고 귀찮게 느껴졌다."
                    }
                }
                ],
                "quickReplies": [
                {
                    "messageText": "극히 드물다",
                    "action": "block",
                    "blockId": self.blockId,
                    "label": "극히 드물다"
                },
                {
                    "messageText": "가끔 있었다",
                    "action": "block",
                    "blockId": self.blockId,
                    "label": "가끔 있었다"
                },
                {
                    "messageText": "종종 있었다",
                    "action": "block",
                    "blockId": self.blockId,
                    "label": "종종 있었다"
                },
                {
                    "messageText": "대부분 그랬다",
                    "action": "block",
                    "blockId": self.blockId,
                    "label": "대부분 그랬다"
                }
                ]
            }
        }
        return JsonResponse(data)
    
    def getJsonDump(self):
        data = {
            "version": "2.0",
            "template": {
            "outputs": [
                {
                "simpleText": {
                    "text": "설문을 종료합니다."
                }
                }
            ]
            }
        }
        return JsonResponse(data)