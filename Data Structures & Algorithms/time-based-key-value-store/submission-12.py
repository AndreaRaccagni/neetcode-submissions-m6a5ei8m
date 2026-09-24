class TimeMap:

    def __init__(self):
        self.store = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.store:
            self.store[key] = []
        self.store[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.store:
            return ''

        entries = self.store[key]
        l = 0
        r = len(entries) - 1
        index = -1

        while l <= r:
            mid = l + (r - l) // 2

            if timestamp == entries[mid][1]:
                return entries[mid][0]
            elif timestamp > entries[mid][1]:
                index = mid
                l = mid + 1
            else:
                r = mid - 1

        return entries[index][0] if index != -1 else ''