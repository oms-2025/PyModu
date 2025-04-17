def drawSprite(filepath, absolute=True, x=0, y=0, angle=0, fx=False, fy=False, scale=1, visible=True, sheet=False, sheetpath="", sheetrows=1, sheetcolumns=1, clock=None):
    # drawSprite v1.8
    try:
        (w, h) = pygame.display.get_surface().get_size()
        if scale<=0:
            print("Cannot scale to less than zero. Aborting draw cycle")
            return("scale<=ZeroError")
        if fx!=True and fx!=False:
            print("fx must be a boolean. Aborting draw cycle")
            return("fxBooleanError")
        if fy!=True and fy!=False:
            print("fy must be a boolean. Aborting draw cycle")
            return("fyBooleanError")
        if visible!=True and visible!=False:
            print("visible must be a boolean. Aborting draw cycle")
            return("visibleBooleanError")
        if sheet:
            if type(sheetpath)!=str:
                print("sheetpath must be a string. Aborting draw cycle")
                return("sheetpathStringError")
            if sheetrows > 0 and sheetcolumns > 0:
                pass
            else:
                print("sheetrows and sheetcolumns must be greater than zero. Aborting draw cycle")
                return("sheetrows/columns<=ZeroError")
        angle=angle%360
        sprite=tsk.Sprite(filepath, x, y)
        if absolute:
            sprite.x=x-sprite.width/2
            sprite.y=y-sprite.height/2
        else:
            sprite.x=(x-sprite.width/2)+(w/2)
            sprite.y=(y-sprite.height/2)+(h/2)
        sprite.scale=scale
        sprite.visible=visible
        sprite.flip_x=fx
        sprite.flip_y=fy
        sprite.angle=angle
        sprite.draw()
        return([sprite.angle, sprite.center, sprite.x, sprite.y, sprite.center_x, sprite.center_y, sprite.width, sprite.height, sprite.flip_x, sprite.flip_y, sprite.image, sprite.scale, sprite.visible])
    except Exception as e:
        print("Uncaught error:", e)