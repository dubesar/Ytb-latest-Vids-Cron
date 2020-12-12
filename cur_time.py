from datetime import datetime, timezone   
local_time = datetime.now(timezone.utc).astimezone()
publishTime = local_time.isoformat()
print(publishTime)