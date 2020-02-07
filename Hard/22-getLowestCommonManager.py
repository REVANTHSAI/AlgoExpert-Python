Time - O(N)| Space O(D)
def getLowestCommonManager(topManager, reportOne, reportTwo):
    return getLowestCommonManager_helper(topManager,reportOne,reportTwo).LCM

def getLowestCommonManager_helper(topManager,reportOne,reportTwo):
    current_reporter_count = 0
    for reports in topManager.directReports:
        curent_result = getLowestCommonManager_helper(reports,reportOne,reportTwo)
        if curent_result.LCM is not None:
            return curent_result
        current_reporter_count += curent_result.reporter_count
    if topManager == reportOne or topManager == reportTwo:
        current_reporter_count += 1
    current_LCM = topManager if current_reporter_count == 2 else None
    return Result(current_LCM,current_reporter_count)

class Result:
    def __init__(self,LCM,reporter_count):
        self.LCM = LCM
        self.reporter_count = reporter_count
