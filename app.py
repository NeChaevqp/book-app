import flet as ft

def replenish_clicked(e):
    e.control.update()

def your_books_clicked(e):
    e.control.update()

def support_clicked(e):
    e.control.update()

def subscription_clicked(e):
    e.control.update()

def feedback_clicked(e):
    e.control.update()

def main(page: ft.Page):
    page.title = "BookBot"
    page.theme_mode = color="#000000"  # Темная тема

    # Создаём и добавляем элементы на страницу
    page.add(
        ft.Column([
            ft.Text('BookBot', style=ft.TextStyle(color="#FFFFFF", size=20, weight="bold")),
            ft.Text('0 ₽', style=ft.TextStyle(color="#696969", size=35, weight="bold")),  # Желтый цвет в HEX
            ft.ElevatedButton('💰 Пополнить', on_click=replenish_clicked, bgcolor="#000000", color="#FFFFFF"),
            ft.ElevatedButton('🎖️ Твои книги', on_click=your_books_clicked, bgcolor="#000000", color="#FFFFFF"),
            ft.ElevatedButton('⚡ Тех.Поддержка', on_click=support_clicked, bgcolor="#000000", color="#FFFFFF"),
            ft.ElevatedButton('🔜 Подписка \n(Не доступна)', on_click=subscription_clicked, bgcolor="#000000", color="#FFFFFF"),
            ft.ElevatedButton('😍 Отзывы', on_click=feedback_clicked, bgcolor="#000000", color="#FFFFFF"),
        ], alignment='center')
    )

ft.app(target=main)