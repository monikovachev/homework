skumriq_kg = float(input())
caca_kg = float(input())
palamud_total_kg = float(input())
safrid_total_kg = float(input())
midi_total_kg = float(input())

MIDI_KG_PRICE = 7.50
PALAMUD_KG_PRICE = skumriq_kg + skumriq_kg * 0.60
SAFRID_KG_PRICE = caca_kg + caca_kg * 0.80

total_price = palamud_total_kg * PALAMUD_KG_PRICE\
              + safrid_total_kg * SAFRID_KG_PRICE\
              + midi_total_kg * MIDI_KG_PRICE

print(f'{total_price:.2f}')

