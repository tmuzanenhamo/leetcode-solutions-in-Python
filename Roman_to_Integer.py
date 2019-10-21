class Solution:
    def romanToInt(self, s: str) -> int:
        roman_values = {'I': 1, 'V': 5, 'X': 10,'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        tot = 0
        first = 0
        sec = 0
        
        for i in s:
            first = roman_values[i]
            tot += first
            
            if first > sec :
                tot = tot-2*sec
                
            sec = first
        return tot