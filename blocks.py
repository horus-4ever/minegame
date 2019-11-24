import pygame
import constants as const
import os

ALL_BLOCKS = []

#base class for all textures / block / item
class Block():
    #should have a texture
    #should know if block is an obstacle
    obstacle = False

    def __init__(self, position):
        self.position = position

    @classmethod
    def new(cls, name, image_path, **kwargs):
        """All derived class from MetaBlock should not override this new method, since
        it creates the __class__.image"""
        global ALL_BLOCKS
        typ = type(name, (Block,), kwargs)
        try:
            path = os.path.join(const.TEXTURE_PATH, image_path)
            image = pygame.image.load(path)
            image = pygame.transform.scale(image, const.BLOCK_SIZE)
            typ.image = image
            typ.image_path = image_path
        except:
            return None
        #if all went good, return the object
        ALL_BLOCKS.append(typ)
        return typ

    def draw(self, surface):
        """Blit the block's image to screen.
        If it fails, return False, else True."""
        try:
            surface.blit(self.getTexture(), self.position)
        except:
            print("Error")
            return False
        return True

    def getTexture(self):
        """Assume that all derived class from MetaBlock have got 'image'"""
        return self.__class__.image

    def getTexturePath(self):
        """Return the path where the texture's image is stored"""
        return self.__class__.image_path

    def getTypeName(self):
        """Return the class name, cause it's OOP and polymorphism"""
        return self.__class__.__name__

    def isObstacle(self):
        """Return wether the block is considered as an obstacle or not."""
        return self.__class__.obstacle

    def __repr__(self):
        """Return a string describing the object"""
        return f"name : <{self.getTypeName()}>, texture : <{self.getTexturePath()}>, position : <{self.position}>"

#define all blocks
Grass1 = Block.new("Grass1", "grass1.jpg")
Grass2 = Block.new("Grass2", "grass2.jpeg")
Brique1 = Block.new("Brique1", "briques1.jpg", obstacle = True)
Plank = Block.new("Plank", "plank1.png")
Sand = Block.new("Sand", "sand1.jpg")
Water = Block.new("Water", "water1.jpg", obstacle = True)
Dirt = Block.new("Dirt", "soil1.jpg")