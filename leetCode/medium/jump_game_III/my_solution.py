def canReach(self, arr: List[int], start: int, passed=None) -> bool:
    if passed is None:
        passed = {}
    elif start is None or start in passed:
        return False
    else:
        passed[start] = 1
    if arr[start] == 0:
        return True
    left = start - arr[start] if start - arr[start] >= 0 else None
    right = start + arr[start] if start + arr[start] < len(arr) else None
    return self.canReach(arr, left, passed) or self.canReach(arr, right, passed)