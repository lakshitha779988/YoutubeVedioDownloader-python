from pytube import YouTube





isexit=True
while isexit:
    youtube_url=input("enter your you tube url")
    yt=YouTube(youtube_url)

    title=yt.title
    caption=yt.captions
    viwes_count=yt.views
    time=round(yt.length/60)
    description=yt.description

    stream=yt.streams.get_by_itag(22)
    stream.download()


    print(f"Title:{title} \nCaption:{caption}\nviwes:{viwes_count} \nlength:{time} \ndescription:{description}")

    exit=input("are you want to exit").lower()
    if exit=="yes":
        isexit=False