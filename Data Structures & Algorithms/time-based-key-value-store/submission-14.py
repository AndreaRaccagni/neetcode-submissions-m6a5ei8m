class TimeMap:

    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store or not self.store[key]:
            return ""

        values = self.store[key]
        l = 0
        r = len(values) - 1
        res = float('-inf')

        while l <= r:
            mid = l + (r - l) // 2

            if values[mid][1] == timestamp:
                return values[mid][0]
            elif values[mid][1] < timestamp:
                res = mid
                l = mid + 1
            else:
                r = mid - 1

        return values[res][0] if res != float('-inf') else ""
