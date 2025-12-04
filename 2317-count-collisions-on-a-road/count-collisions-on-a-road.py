class Solution:
    def countCollisions(self, directions: str) -> int:
        dirs = directions.lstrip('L').rstrip('R')
        print(dirs)
        return len(dirs) - dirs.count('S')