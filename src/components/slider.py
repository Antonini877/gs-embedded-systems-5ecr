import pygame
from typing import List, Callable, Optional, Any

class SliderGroup:
    """
    Classe que representa um grupo de sliders para ajuste de valores de sensores.
    Permite desenhar sliders, manipular eventos do mouse e obter os valores atuais.
    """

    def __init__(self, x: int = 100, y_start: int = 250, width: int = 200, gap: int = 30, nomes: Optional[List[str]] = None) -> None:
        """
        Inicializa o grupo de sliders.
        :param x: Posição X inicial dos sliders.
        :param y_start: Posição Y inicial do primeiro slider.
        :param width: Largura dos sliders.
        :param gap: Espaço vertical entre sliders.
        :param nomes: Lista de nomes dos sliders.
        """
        self.slider_width: int = width
        self.slider_height: int = 6
        self.slider_x: int = x
        self.slider_y_start: int = y_start
        self.slider_gap: int = gap
        self.slider_values: List[float] = [0.0, 0.0, 0.0]
        self.slider_dragging: List[bool] = [False, False, False]
        self.nomes: List[str] = nomes if nomes else ["CO", "CO2", "CH4"]

    def draw(self, screen: Any, draw_text: Callable, color_line: tuple, color_handle: tuple) -> None:
        """
        Desenha os sliders na tela.
        :param screen: Superfície pygame onde os sliders serão desenhados.
        :param draw_text: Função para desenhar texto.
        :param color_line: Cor da linha do slider.
        :param color_handle: Cor do ponteiro do slider.
        """
        for idx, value in enumerate(self.slider_values):
            y = self.slider_y_start + idx * self.slider_gap
            pygame.draw.rect(
                screen,
                color_line,
                pygame.Rect(self.slider_x, y, self.slider_width, self.slider_height),
                2
            )
            # Ponteiro do slider
            handle_x = self.slider_x + int(value * self.slider_width)
            pygame.draw.circle(screen, color_handle, (handle_x, y + self.slider_height // 2), 10)
            # Texto
            draw_text(screen, f"{self.nomes[idx]}: {int(value*100)}%", (self.slider_x + self.slider_width + 30, y - 8))

    def handle_event(self, event: Any) -> None:
        """
        Manipula eventos do mouse para interação com os sliders.
        :param event: Evento pygame.
        """
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            for i in range(3):
                y = self.slider_y_start + i * self.slider_gap
                handle_x = self.slider_x + int(self.slider_values[i] * self.slider_width)
                if abs(mx - handle_x) < 12 and abs(my - (y + self.slider_height // 2)) < 12:
                    self.slider_dragging[i] = True
        elif event.type == pygame.MOUSEBUTTONUP:
            self.slider_dragging = [False, False, False]
        elif event.type == pygame.MOUSEMOTION:
            mx, my = pygame.mouse.get_pos()
            for i in range(3):
                if self.slider_dragging[i]:
                    rel_x = min(max(mx - self.slider_x, 0), self.slider_width)
                    self.slider_values[i] = rel_x / self.slider_width

    def get_values(self) -> List[float]:
        """
        Retorna os valores atuais dos sliders.
        :return: Lista de valores (float) entre 0.0 e 1.0.
        """
        return self.slider_values