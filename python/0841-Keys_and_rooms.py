'''
Description:
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1, and each room may have some keys to access the next room.
Formally, each room i has a list of keys rooms[i], and each key rooms[i][j] is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v opens the room with number v.
Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.
'''


class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # Start in room 0
        room_indices = [0]
        visited = [False] * len(rooms)

        while room_indices:

            room_index = room_indices.pop(0)

            # Mark as visited
            visited[room_index] = True

            # Access keys in room
            keys = rooms[room_index]

            for key in keys:

                if not visited[key]:
                    room_indices.append(key)

        return not False in visited
