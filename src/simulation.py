import pygame
import sys
from typing import List
from components.circuit import Circuit
from components.slider import SliderGroup
from utils.colors import Colors
from utils.text import draw_text
from utils.buzzer import Buzzer

def main() -> None:
    """
    Função principal que inicializa o pygame, cria os componentes do circuito,
    sliders e buzzer, e executa o loop principal da simulação.
    """
    pygame.init()
    screen = pygame.display.set_mode((700, 340))
    pygame.display.set_caption("Diagrama Circuito")

    circuito = Circuit(screen)
    sliders = SliderGroup()
    buzzer = Buzzer()
    alarme_ligado = False

    clock = pygame.time.Clock()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            sliders.handle_event(event)

        screen.fill(Colors.WHITE)

        slider_values = sliders.get_values()
        max_value = max(slider_values)
        now = pygame.time.get_ticks()

        # Atualiza sensores
        process_sensor_colors(circuito, slider_values)

        # Atualiza LEDs e alarme
        alarme_ligado = process_leds_and_alarm(circuito, max_value, now)

        # Controle do beep contínuo
        if alarme_ligado:
            buzzer.play_beep_loop()
        else:
            buzzer.stop_beep()

        circuito.draw()
        sliders.draw(screen, draw_text, Colors.BLACK, Colors.RED)
        pygame.display.flip()
        clock.tick(60)

def process_sensor_colors(circuito: Circuit, slider_values: List[float]) -> None:
    """
    Atualiza as cores dos sensores conforme os valores dos sliders.
    SENSOR A fica amarelo se algum slider >= 0.2.
    SENSOR B fica amarelo se algum slider >= 0.5.
    """
    if any(v >= 0.2 for v in slider_values):
        circuito.set_sensor_a_color(Colors.YELLOW)
    else:
        circuito.set_sensor_a_color(Colors.BLACK)
    if any(v >= 0.5 for v in slider_values):
        circuito.set_sensor_b_color(Colors.YELLOW)
    else:
        circuito.set_sensor_b_color(Colors.BLACK)

def process_leds_and_alarm(circuito: Circuit, max_value: float, now: int) -> bool:
    """
    Atualiza os LEDs e retorna se o alarme deve estar ligado.
    - Ar puro: LED 1 verde, demais apagados, alarme desligado.
    - Moderado: LED 2 amarelo, demais apagados, alarme desligado.
    - Arriscado: LED 3 vermelho, demais apagados, alarme desligado.
    - Em chamas: LED 4 pisca em vermelho, demais apagados, alarme ligado.
    """
    if max_value < 0.2:
        # Ar puro
        circuito.set_led_color(0, Colors.GREEN)
        circuito.set_led_color(1, Colors.BLACK)
        circuito.set_led_color(2, Colors.BLACK)
        circuito.set_led_color(3, Colors.BLACK)
        return False
    elif max_value < 0.5:
        # Moderado
        circuito.set_led_color(0, Colors.BLACK)
        circuito.set_led_color(1, Colors.YELLOW)
        circuito.set_led_color(2, Colors.BLACK)
        circuito.set_led_color(3, Colors.BLACK)
        return False
    elif max_value < 0.8:
        # Arriscado
        circuito.set_led_color(0, Colors.BLACK)
        circuito.set_led_color(1, Colors.BLACK)
        circuito.set_led_color(2, Colors.RED)
        circuito.set_led_color(3, Colors.BLACK)
        return False
    else:
        # Em chamas: LED 4 pisca em vermelho, alarme ligado
        circuito.set_led_color(0, Colors.BLACK)
        circuito.set_led_color(1, Colors.BLACK)
        circuito.set_led_color(2, Colors.BLACK)
        if (now // 100) % 2 == 0:  # 5 Hz = 100 ms ON, 100 ms OFF
            circuito.set_led_color(3, Colors.RED)
        else:
            circuito.set_led_color(3, Colors.BLACK)
        return True

if __name__ == "__main__":
    main()