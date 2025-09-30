#!/bin/bash

options="Apagar\nReiniciar\nCerrar sesion\nSuspender"
choince=$(echo -e "$options" | rofi -dmenu -p "Menu del sistema")

case "$choice" in
  "Apagar") systemctl poweroff ;;
  "Reiniciar") systemctl reboot ;;
  "Cerrar sesion") i3-msg exit ;;
  "Suspender") systemctl suspend ;;
esac
