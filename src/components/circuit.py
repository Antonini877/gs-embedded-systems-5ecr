import pygame
from utils.text import draw_text
from utils.colors import Colors
from typing import List, Any

class Circuit:
    """
    Classe que representa o circuito do setor, incluindo sensores e LEDs.
    Permite alterar e consultar as cores dos sensores e LEDs, além de desenhar o circuito na tela.
    """

    def __init__(self, screen: Any) -> None:
        """
        Inicializa o circuito com a tela pygame e cores padrão.
        :param screen: Superfície pygame onde o circuito será desenhado.
        """
        self.screen = screen
        self.sensor_a_color: tuple = Colors.BLACK
        self.sensor_b_color: tuple = Colors.BLACK
        self.led_colors: List[tuple] = [Colors.BLACK, Colors.BLACK, Colors.BLACK, Colors.BLACK]

    def set_led_color(self, idx: int, color: tuple) -> None:
        """
        Altera a cor de um LED específico (0 a 3).
        :param idx: Índice do LED (0 a 3)
        :param color: Cor no formato RGB
        """
        if 0 <= idx < 4:
            self.led_colors[idx] = color

    def get_led_color(self, idx: int) -> tuple:
        """
        Retorna a cor de um LED específico (0 a 3).
        :param idx: Índice do LED (0 a 3)
        :return: Cor no formato RGB
        """
        if 0 <= idx < 4:
            return self.led_colors[idx]
        return Colors.BLACK

    def set_sensor_a_color(self, color: tuple) -> None:
        """
        Altera a cor do sensor A.
        :param color: Cor no formato RGB
        """
        self.sensor_a_color = color

    def set_sensor_b_color(self, color: tuple) -> None:
        """
        Altera a cor do sensor B.
        :param color: Cor no formato RGB
        """
        self.sensor_b_color = color

    def draw(self) -> None:
        """
        Desenha o circuito completo na tela pygame, incluindo sensores, Raspberry Pi, LEDs e conexões.
        """
        # SENSOR A
        sensor_a_rect = pygame.Rect(40, 60, 90, 50)
        pygame.draw.rect(self.screen, self.sensor_a_color, sensor_a_rect, 2)
        draw_text(self.screen, "SENSOR A", (50, 80))

        # SENSOR B
        sensor_b_rect = pygame.Rect(40, 140, 90, 50)
        pygame.draw.rect(self.screen, self.sensor_b_color, sensor_b_rect, 2)
        draw_text(self.screen, "SENSOR B", (50, 160))

        # RASPBERRY PI (central)
        pi_rect = pygame.Rect(180, 40, 260, 180)
        pygame.draw.rect(self.screen, Colors.RED, pi_rect, 2)
        draw_text(self.screen, "RASPBERRY PI", (230, 80), Colors.RED)

        # 4 LEDs (direita)
        led_rects = []
        for i in range(4):
            led_rect = pygame.Rect(480, 40 + i*35, 90, 30)
            led_rects.append(led_rect)
            pygame.draw.rect(self.screen, self.led_colors[i], led_rect, 2)
            draw_text(self.screen, f"LED {i+1}", (510, 47 + i*35))

        # ALARME (direita, embaixo)
        alarme_rect = pygame.Rect(480, 190, 90, 40)
        pygame.draw.rect(self.screen, Colors.BLACK, alarme_rect, 2)
        draw_text(self.screen, "ALARME", (495, 205))

        # Linhas dos sensores para PI
        pygame.draw.line(self.screen, Colors.BLACK, sensor_a_rect.midright, (pi_rect.left, pi_rect.top + 30), 2)
        pygame.draw.line(self.screen, Colors.BLACK, sensor_b_rect.midright, (pi_rect.left, pi_rect.bottom - 30), 2)
        draw_text(self.screen, "ENTRADAS", (130, 60))

        # Linhas do PI para cada LED
        for i, led_rect in enumerate(led_rects):
            pygame.draw.line(
                self.screen, Colors.BLACK,
                (pi_rect.right, pi_rect.top + 30 + i*35),
                led_rect.midleft, 2
            )
        # Linha do PI para o alarme
        pygame.draw.line(self.screen, Colors.BLACK, (pi_rect.right, pi_rect.bottom - 30), alarme_rect.midleft, 2)
        draw_text(self.screen, "SAÍDAS", (440, 60))