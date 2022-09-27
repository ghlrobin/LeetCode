class Solution(object):
    def reorderLogFiles(self, logs):
        """
        :type logs: List[str]
        :rtype: List[str]
        """
        # split between letter list and digit list by checking last char of each element
        l = []
        d = []
        for s in logs:
            if s[-1].isdigit():
                d.append(s)
            else:
                l.append(s)
                
        # sort by 1. words(except the identifier), 2. indentifier
        l.sort(key = lambda x : (x[x.index(' '):], x[:x.index(' ')]))
        return l + d
                