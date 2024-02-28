from datetime import datetime
import sys
input_list_date = [datetime.strptime(str(line.strip()), '%Y-%m-%d') for line in sys.stdin]
print((max(input_list_date) - min(input_list_date)).days)