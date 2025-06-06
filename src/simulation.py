import pygame
import sys
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

        # Define os sensores conforme a tabela desejada
        sensor1, sensor2 = get_sensor_states(max_value)

        # Atualiza sensores visuais
        process_sensor_colors(circuito, sensor1, sensor2)

        # Atualiza LEDs e alarme com base nos sensores
        alarme_ligado = process_leds_and_alarm(circuito, sensor1, sensor2, now)

        # Controle do beep contínuo
        if alarme_ligado:
            buzzer.play_beep_loop()
        else:
            buzzer.stop_beep()

        circuito.draw()
        sliders.draw(screen, draw_text, Colors.BLACK, Colors.RED)
        pygame.display.flip()
        clock.tick(60)

def get_sensor_states(max_value: float):
    """
    Retorna o estado dos sensores conforme a faixa:
    - Ar puro: sensor1=0, sensor2=0
    - Moderado: sensor1=1, sensor2=0
    - Arriscado: sensor1=0, sensor2=1
    - Em chamas: sensor1=1, sensor2=1
    """
    if max_value < 0.2:
        return 0, 0
    elif max_value < 0.5:
        return 1, 0
    elif max_value < 0.8:
        return 0, 1
    else:
        return 1, 1

def process_sensor_colors(circuito: Circuit, sensor1: int, sensor2: int) -> None:
    """
    Atualiza as cores dos sensores conforme os estados.
    """
    circuito.set_sensor_a_color(Colors.YELLOW if sensor1 else Colors.BLACK)
    circuito.set_sensor_b_color(Colors.YELLOW if sensor2 else Colors.BLACK)

def process_leds_and_alarm(circuito: Circuit, sensor1: int, sensor2: int, now: int) -> bool:
    """
    Atualiza os LEDs e retorna se o alarme deve estar ligado.
    """
    if sensor1 == 0 and sensor2 == 0:
        # Ar puro
        circuito.set_led_color(0, Colors.GREEN)
        circuito.set_led_color(1, Colors.BLACK)
        circuito.set_led_color(2, Colors.BLACK)
        circuito.set_led_color(3, Colors.BLACK)
        return False
    elif sensor1 == 1 and sensor2 == 0:
        # Moderado
        circuito.set_led_color(0, Colors.BLACK)
        circuito.set_led_color(1, Colors.YELLOW)
        circuito.set_led_color(2, Colors.BLACK)
        circuito.set_led_color(3, Colors.BLACK)
        return False
    elif sensor1 == 0 and sensor2 == 1:
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