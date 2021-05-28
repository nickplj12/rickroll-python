import pyglet
vid_path='main'
window=pyglet.window.Window(resizable=True, caption='Video')
player = pyglet.media.Player()
source = pyglet.media.StreamingSource()
MediaLoad = pyglet.media.load(vid_path)

player.queue(MediaLoad)
player.play()

@window.event
def on_draw():
    if player.source and player.source.video_format:
        player.get_texture().blit(50,50)


pyglet.app.run()