import heapq
class Solution:
    def minMeetingRooms(self, intervals):
        intervals.sort(key = lambda x : x[0])
        rooms = []
        for interval in intervals:
            #print(interval)
            s_time = interval[0]
            f_time = interval[1]
            if len(rooms) == 0 or rooms[0][0] > s_time:
                heapq.heappush(rooms, (f_time, [interval]))
            else:
                room = heapq.heappop(rooms)[1]
                room.append(interval)
                heapq.heappush(rooms, (f_time, room))
            #print(rooms)
        return len(rooms)