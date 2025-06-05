# Simulador de Sistema Embarcado - Detecção de Gases

Este projeto é um simulador visual interativo, desenvolvido em Python com Pygame, que representa o funcionamento de um sistema embarcado para detecção de gases e alerta de incêndio.

## Funcionalidades

- **Sensores simulados:** Ajuste valores de sensores de gás usando sliders.
- **Indicadores visuais:** LEDs coloridos indicam o nível de risco detectado:
  - Verde: Ar puro
  - Amarelo: Nível moderado
  - Vermelho: Nível arriscado
  - Vermelho piscando: Situação de incêndio
- **Alarme sonoro:** Um buzzer simulado dispara em caso de incêndio.
- **Interface gráfica intuitiva:** Visualização do circuito, sensores e indicadores em tempo real.

## Como executar

1. Instale as dependências:
   ```
   pip install pygame
   ```
2. Execute o simulador:
   ```
   python src/simulation.py
   ```

## Estrutura do Projeto

- `src/simulation.py`: Loop principal da simulação.
- `components/`: Componentes gráficos do circuito (circuito, sliders, etc).
- `utils/`: Utilitários como cores, textos e buzzer.

## Objetivo

Este simulador foi desenvolvido para fins educacionais, auxiliando no entendimento de sistemas embarcados de monitoramento de gases e alarmes.

---