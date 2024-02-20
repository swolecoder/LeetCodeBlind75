class Solution:
    def reformatDate(self, date: str) -> str:
        months = {
            'Jan' : '01',
            'Feb' : '02',
            'Mar' : '03',
            'Apr' : '04',
            'May' : '05',
            'Jun' : '06',
            'Jul' : '07',
            'Aug' : '08',
            'Sep' : '09',
            'Oct' : '10',
            'Nov' : '11',
            'Dec' : '12',
        }

        day, month, year = date.split()
         # Adjust slicing based on whether the day is one or two digits
        if day[1].isdigit():
            day = day[:2]  # Two digit day
        else:
            day = '0' + day[0]  # Single digit day, pad with zero
        return year+"-"+months[month]+"-"+day

        