import pygame as pg
import moderngl as mgl
import sys
from model import *
from camera import Camera
from light import Light
from mesh import Mesh
from scene import Scene
from scene_renderer import SceneRenderer


class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # init pygame 
        pg.init()
        # tamanho da janela
        self.WIN_SIZE = win_size
        #opengl attributos
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        #opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        #configurações do mouse
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # detecta e usa opengl context 
        self.ctx = mgl.create_context()
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # iluminação
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)
        #cenas
        self.scene = Scene(self)
        #renderizar
        self.scene_renderer = SceneRenderer(self)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self):
        # clear framebuffer
        self.ctx.clear(color=(0.08, 0.16, 0.18))
        # renderiza a cena
        self.scene_renderer.render()
        # troca buffers
        pg.display.flip()

    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001
        

    def run(self):
        while True:
            self.get_time()
            self.check_events()
            self.camera.update()
            self.render()
            self.delta_time = self.clock.tick(60)



if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()





























