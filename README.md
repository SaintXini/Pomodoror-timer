# ⏱️ Pomodoro Timer

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Tkinter](https://img.shields.io/badge/GUI-Tkinter-orange)
![License](https://img.shields.io/badge/License-MIT-green)

> **ES:** Aplicación de escritorio que implementa la técnica Pomodoro para mejorar la productividad, alternando ciclos de trabajo enfocado con descansos cortos y largos.
>
> **EN:** Desktop application implementing the Pomodoro Technique to improve productivity, alternating focused work cycles with short and long breaks.

---

## 📋 Descripción / Description

**ES:** Pomodoro Timer es una aplicación de escritorio construida con Python y Tkinter que ayuda a gestionar el tiempo mediante ciclos de 25 minutos de trabajo seguidos de descansos de 5 minutos, con un descanso largo de 15 minutos cada 4 ciclos completados. El proyecto está organizado siguiendo una separación de responsabilidades (configuración, lógica de negocio e interfaz gráfica), lo que facilita su mantenimiento y escalabilidad.

**EN:** Pomodoro Timer is a desktop application built with Python and Tkinter that helps manage time through 25-minute work cycles followed by 5-minute breaks, with a 15-minute long break every 4 completed cycles. The project follows a separation-of-concerns structure (configuration, business logic, and GUI), making it easier to maintain and extend.

---

## ✨ Funcionalidades / Features

- Temporizador de trabajo y descanso configurable / Configurable work and break timer
- Descansos cortos y largos automáticos cada 4 pomodoros / Automatic short and long breaks every 4 pomodoros
- Notificaciones emergentes al finalizar cada ciclo / Pop-up notifications at the end of each cycle
- Interfaz gráfica simple e intuitiva con `ttkbootstrap` / Simple, intuitive GUI styled with `ttkbootstrap`
- Lógica del temporizador desacoplada de la interfaz, lista para pruebas unitarias / Timer logic decoupled from the UI, ready for unit testing

---

## 🛠️ Stack tecnológico / Tech Stack

| Capa / Layer | Tecnología / Technology |
|---|---|
| Lenguaje / Language | Python 3 |
| Interfaz gráfica / GUI | Tkinter + ttkbootstrap |
| Arquitectura / Architecture | Separación por capas (config / core / gui) |
| Control de versiones / Version control | Git & GitHub |

---

## 📁 Estructura del proyecto / Project Structure

```
pomodoro_timer/
├── main.py                  # Punto de entrada / Entry point
├── requirements.txt
├── config/
│   └── settings.py          # Constantes de tiempo y ventana / Time & window constants
├── core/
│   └── pomodoro_logic.py    # Lógica del temporizador (sin GUI) / Timer logic (no GUI)
└── gui/
    └── app.py               # Interfaz gráfica con Tkinter / Tkinter GUI
```

---

## 🚀 Instalación local / Local Setup

```bash
# Clonar el repositorio / Clone the repository
git clone https://github.com/SaintXini/Pomodoror-timer
cd Pomodoror-timer

# Instalar dependencias / Install dependencies
pip install -r requirements.txt

# Ejecutar la aplicación / Run the application
python main.py
```

---

## 🧠 Cómo funciona / How it works

**ES:** El temporizador alterna entre estado de trabajo (`work_time`) y descanso (`break_time`). Cada vez que se completa un ciclo de trabajo, se incrementa el contador de pomodoros; al llegar al cuarto ciclo, se otorga un descanso largo en lugar de uno corto. Toda esta lógica vive en `PomodoroLogic`, independiente de Tkinter, por lo que puede probarse de forma aislada.

**EN:** The timer alternates between a work state (`work_time`) and a break state (`break_time`). Each time a work cycle finishes, the pomodoro counter increases; on the fourth cycle, a long break is granted instead of a short one. All of this logic lives in `PomodoroLogic`, independent of Tkinter, so it can be tested in isolation.

---

## 👨‍💻 Autor / Author

**Martín Santiago Con Xinico**
[LinkedIn](https://www.linkedin.com/in/martín-con-xinico) · [GitHub](https://github.com/SaintXini)

---

## 📄 Licencia / License

Este proyecto está bajo la licencia MIT. / This project is licensed under the MIT License.
