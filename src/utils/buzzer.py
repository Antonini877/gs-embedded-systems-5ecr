import pygame
import numpy

class Buzzer:
    """
    Classe responsável por gerar e controlar o som de beep do alarme.
    Utiliza pygame para síntese e reprodução do som.
    """

    def __init__(self) -> None:
        """
        Inicializa o mixer do pygame, o canal de áudio e gera o som de beep.
        """
        self.alarme_ligado: bool = False
        pygame.mixer.init()
        self.channel: pygame.mixer.Channel = pygame.mixer.Channel(1)
        self.beep_sound: pygame.mixer.Sound = self.generate_beep()

    def generate_beep(self, freq: int = 1000, duration_ms: int = 200) -> pygame.mixer.Sound:
        """
        Gera um som de beep sintético.
        :param freq: Frequência do beep em Hz.
        :param duration_ms: Duração do beep em milissegundos.
        :return: Objeto Sound do pygame.
        """
        sample_rate = 44100
        n_samples = int(sample_rate * duration_ms / 1000)
        t = numpy.linspace(0, duration_ms / 1000, n_samples, False)
        wave = 0.5 * numpy.sin(2 * numpy.pi * freq * t)
        audio = numpy.array(wave * 32767, dtype=numpy.int16)
        stereo_audio = numpy.column_stack((audio, audio))
        sound = pygame.sndarray.make_sound(stereo_audio)
        return sound

    def play_beep_loop(self) -> None:
        """
        Inicia a reprodução contínua do beep enquanto o canal estiver livre.
        """
        if not self.channel.get_busy():
            self.channel.play(self.beep_sound, loops=-1)

    def stop_beep(self) -> None:
        """
        Para a reprodução do beep.
        """
        self.channel.stop()