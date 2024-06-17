import pygame
class SoundManager:

    def __init__(self, sound_files=None):
        pygame.mixer.init()
        
        # Dictionary to store sound effects
        self.sound_effects = {}
        
        # Variable to store background music path
        self.background_music = None

        # Load sound effects if provided
        if sound_files:
            for name, filepath in sound_files.items():
                self.load_sound_effect(name, filepath)

    def load_sound_effect(self, name, filepath):
        """
        Load a sound effect.
        
        Parameters:
        name (str): The name to refer to the sound effect.
        filepath (str): The path to the sound effect file.
        """
        self.sound_effects[name] = pygame.mixer.Sound(filepath)

    def play_sound_effect(self, name):
        """
        Play a loaded sound effect.
        
        Parameters:
        name (str): The name of the sound effect to play.
        """
        if name in self.sound_effects:
            self.sound_effects[name].play()
        else:
            print(f"Sound effect '{name}' not found.")