n=int(input("Enter number of songs: "))
playlist=[]
for i in range(n):
    duration=int(input("Enter duration: "))
    playlist.append(duration)
if not all(s>0 for s in playlist):
        print("Invalid Playlist:Contains non-Positive duration")
else:
        total=sum(playlist)
        count=len(playlist)

        repetitive=False
        for song in playlist:
            if playlist.count(song)>1:
                repetitive=True
                break

        if total<300:
            category="Too Short Playlist"
            recommendation="Add more songs"
        elif total>3600:
            category="Too Long Playlist"
            recommendation="reduce playlist length"
        elif repetitive:
            category="Repetitve Playlist"
            recommendation="Add Variety"
        elif max(playlist)-min(playlist)<=1000:
            category="Balanced Playlist"
            recommendation="Good listening session"
        else:
            category="Irregular Playlist"
            recommendation="Adjust song durations"

        print("Total Duration:",total,"seconds")
        print("Songs:",count)
        print("Category:",category)
        print("Recommendation:",recommendation)