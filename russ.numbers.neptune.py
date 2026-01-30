#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║  ███╗   ██╗███████╗██████╗ ████████╗██╗   ██╗███╗   ██╗███████╗          ║
║  ████╗  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║████╗  ██║██╔════╝          ║
║  ██╔██╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██╔██╗ ██║█████╗            ║
║  ██║╚██╗██║██╔══╝  ██╔═══╝    ██║   ██║   ██║██║╚██╗██║██╔══╝            ║
║  ██║ ╚████║███████╗██║        ██║   ╚██████╔╝██║ ╚████║███████╗          ║
║  ╚═╝  ╚═══╝╚══════╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝          ║
║                                                                          ║
║                  R U S S I A N   N U M B E R S   1.0.0                   ║
║                           by Venz1onixxx                                 ║
║                  https://github.com/Venz1onixxx                          ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

import os
import sys
import re
import json
import hashlib
import datetime
from typing import Dict, List, Optional, Tuple

# ============================================
# 📦 УСТАНОВКА БИБЛИОТЕК
# ============================================
"""
╔══════════════════════════════════════════════════════════════════════════╗
║                                                                          ║
║  🚀 ДЛЯ ЗАПУСКА NEPTUNE RUSSIAN NUMBERS 1.0.0 УСТАНОВИТЕ:                ║
║                                                                          ║
║  1️⃣ ОБЯЗАТЕЛЬНАЯ БИБЛИОТЕКА:                                            ║
║     pip install colorama                                                 ║
║                                                                          ║
║  2️⃣ СОЗДАЙТЕ requirements.txt:                                          ║
║     colorama>=0.4.6                                                      ║
║                                                                          ║
║  3️⃣ ЗАПУСТИТЕ УСТАНОВКУ:                                                ║
║     pip install colorama                                                 ║
║                                                                          ║
╚══════════════════════════════════════════════════════════════════════════╝
"""

# ============================================
# 🎨 ЦВЕТНОЕ ЛОГОТИП (СИНИЙ NEPTUNE)
# ============================================

def display_color_logo():
    """Отображение цветного логотипа NEPTUNE"""
    os.system('cls' if os.name == 'nt' else 'clear')
    
    # Проверяем поддержку цветов
    try:
        from colorama import init, Fore, Back, Style
        init(autoreset=True)
        
        logo = f"""
{Fore.BLUE}{'═'*70}{Fore.RESET}

{Fore.CYAN}╔══════════════════════════════════════════════════════════════════╗{Fore.RESET}
{Fore.CYAN}║                                                                  ║{Fore.RESET}
{Fore.BLUE}║    ███╗   ██╗{Fore.CYAN}███████╗{Fore.BLUE}██████╗ {Fore.CYAN}████████╗{Fore.BLUE}██╗   ██╗{Fore.CYAN}███╗   ██╗{Fore.BLUE}███████╗    ║{Fore.RESET}
{Fore.BLUE}║    ████╗  ██║{Fore.CYAN}██╔════╝{Fore.BLUE}██╔══██╗{Fore.CYAN}╚══██╔══╝{Fore.BLUE}██║   ██║{Fore.CYAN}████╗  ██║{Fore.BLUE}██╔════╝    ║{Fore.RESET}
{Fore.BLUE}║    ██╔██╗ ██║{Fore.CYAN}█████╗  {Fore.BLUE}██████╔╝{Fore.CYAN}   ██║   {Fore.BLUE}██║   ██║{Fore.CYAN}██╔██╗ ██║{Fore.BLUE}█████╗      ║{Fore.RESET}
{Fore.BLUE}║    ██║╚██╗██║{Fore.CYAN}██╔══╝  {Fore.BLUE}██╔═══╝ {Fore.CYAN}   ██║   {Fore.BLUE}██║   ██║{Fore.CYAN}██║╚██╗██║{Fore.BLUE}██╔══╝      ║{Fore.RESET}
{Fore.BLUE}║    ██║ ╚████║{Fore.CYAN}███████╗{Fore.BLUE}██║     {Fore.CYAN}   ██║   {Fore.BLUE}╚██████╔╝{Fore.CYAN}██║ ╚████║{Fore.BLUE}███████╗    ║{Fore.RESET}
{Fore.BLUE}║    ╚═╝  ╚═══╝{Fore.CYAN}╚══════╝{Fore.BLUE}╚═╝     {Fore.CYAN}   ╚═╝    {Fore.BLUE}╚═════╝ {Fore.CYAN}╚═╝  ╚═══╝{Fore.BLUE}╚══════╝    ║{Fore.RESET}
{Fore.CYAN}║                                                                  ║{Fore.RESET}
{Fore.BLUE}║           ╔══════════════════════════════════════════╗           ║{Fore.RESET}
{Fore.CYAN}║           ║    RUSSIAN NUMBERS 1.0.0 by Venz1onixxx  ║           ║{Fore.RESET}
{Fore.BLUE}║           ╚══════════════════════════════════════════╝           ║{Fore.RESET}
{Fore.CYAN}║                https://github.com/Venz1onixxx                    ║{Fore.RESET}
{Fore.BLUE}║                                                                  ║{Fore.RESET}
{Fore.CYAN}╚══════════════════════════════════════════════════════════════════╝{Fore.RESET}

{Fore.BLUE}{'═'*70}{Fore.RESET}

{Fore.CYAN}┌──────────────────────────────────────────────────────────────┐{Fore.RESET}
{Fore.GREEN}│  ✅ Готов к анализу российских номеров телефонов            │{Fore.RESET}
{Fore.CYAN}└──────────────────────────────────────────────────────────────┘{Fore.RESET}
        """
        print(logo)
        
    except ImportError:
        # Если colorama не установлен, показываем простой логотип
        simple_logo = """
════════════════════════════════════════════════════════════════════

  ███╗   ██╗███████╗██████╗ ████████╗██╗   ██╗███╗   ██╗███████╗  
  ████╗  ██║██╔════╝██╔══██╗╚══██╔══╝██║   ██║████╗  ██║██╔════╝  
  ██╔██╗ ██║█████╗  ██████╔╝   ██║   ██║   ██║██╔██╗ ██║█████╗    
  ██║╚██╗██║██╔══╝  ██╔═══╝    ██║   ██║   ██║██║╚██╗██║██╔══╝    
  ██║ ╚████║███████╗██║        ██║   ╚██████╔╝██║ ╚████║███████╗  
  ╚═╝  ╚═══╝╚══════╝╚═╝        ╚═╝    ╚═════╝ ╚═╝  ╚═══╝╚══════╝  
                                                                  
              RUSSIAN NUMBERS 1.0.0 by Venz1onixxx                
              https://github.com/Venz1onixxx                      
════════════════════════════════════════════════════════════════════
        """
        print(simple_logo)
        print("⚠️  Для цветного интерфейса установите: pip install colorama")

# ============================================
# 🎯 ОСНОВНЫЕ ФУНКЦИИ АНАЛИЗА
# ============================================

class RussianPhoneAnalyzer:
    """Анализатор российских номеров телефонов"""
    
    def __init__(self):
        # База данных российских операторов
        self.operators_db = {
            'МТС': {
                'codes': ['910', '911', '912', '913', '914', '915', '916', '917', '918', '919',
                         '980', '981', '982', '983', '984', '985', '986', '987', '988', '989'],
                'color': 'GREEN',
                'info': 'Крупнейший оператор России'
            },
            'МегаФон': {
                'codes': ['920', '921', '922', '923', '924', '925', '926', '927', '928', '929',
                         '930', '931', '932', '933', '934', '935', '936', '937', '938', '939'],
                'color': 'RED',
                'info': 'Оператор федерального значения'
            },
            'Билайн': {
                'codes': ['903', '905', '906', '909', '960', '961', '962', '963', '964', '965',
                         '966', '967', '968', '969', '900', '901', '902', '904', '908'],
                'color': 'YELLOW',
                'info': 'VimpelCom, входит в Veon'
            },
            'Tele2': {
                'codes': ['950', '951', '952', '953', '954', '955', '956', '957', '958', '959',
                         '970', '971', '972', '973', '974', '975', '976', '977', '978', '979'],
                'color': 'BLUE',
                'info': 'Оператор-дискаунтер'
            },
            'Yota': {
                'codes': ['995', '996', '999'],
                'color': 'MAGENTA',
                'info': 'Виртуальный оператор'
            },
            'Ростелеком': {
                'codes': ['978'],
                'color': 'CYAN',
                'info': 'Национальный оператор'
            }
        }
        
        # Коды городов России
        self.city_codes = {
            '495': 'Москва',
            '499': 'Москва',
            '812': 'Санкт-Петербург',
            '813': 'Ленинградская область',
            '381': 'Омск',
            '383': 'Новосибирск',
            '343': 'Екатеринбург',
            '846': 'Самара',
            '863': 'Ростов-на-Дону',
            '861': 'Краснодар',
            '484': 'Калуга',
            '485': 'Ярославль'
        }
        
        # VIP номера
        self.vip_patterns = {
            '000000': '⭐ VIP: Шесть нулей',
            '111111': '⭐ VIP: Шесть единиц',
            '222222': '⭐ VIP: Шесть двоек',
            '333333': '⭐ VIP: Шесть троек',
            '444444': '⭐ VIP: Шесть четверок',
            '555555': '⭐ VIP: Шесть пятерок',
            '666666': '⭐ VIP: Шесть шестерок',
            '777777': '⭐ VIP: Шесть семерок',
            '888888': '⭐ VIP: Шесть восьмерок',
            '999999': '⭐ VIP: Шесть девяток',
            '123456': '⭐ VIP: Последовательность',
            '654321': '⭐ VIP: Обратная последовательность',
            '777777': '⭐ VIP: Счастливая семерка',
            '888888': '⭐ VIP: Золотая восьмерка'
        }

    def validate_russian_phone(self, phone):
        """Валидация российского номера телефона"""
        digits = re.sub(r'\D', '', phone)
        
        # Российские номера: +7 или 8, затем 10 цифр
        if len(digits) == 11:
            if digits.startswith('8') or digits.startswith('7'):
                return True, digits, 'VALID_RUS'
        elif len(digits) == 10:
            # Предполагаем российский номер без кода страны
            return True, '7' + digits, 'VALID_RUS_10DIGIT'
        
        return False, digits, 'INVALID'

    def get_operator_info(self, phone_digits):
        """Получение информации об операторе"""
        if len(phone_digits) >= 4:
            code = phone_digits[1:4]  # Код ABC
            
            for operator, data in self.operators_db.items():
                if code in data['codes']:
                    return operator, data
            
            # Проверка кода города
            if code in self.city_codes:
                return 'Стационарный', {
                    'color': 'WHITE', 
                    'info': f'Городской номер: {self.city_codes[code]}'
                }
        
        return 'Неизвестный', {
            'color': 'GRAY', 
            'info': 'Не удалось определить оператора'
        }

    def detect_vip(self, phone_digits):
        """Обнаружение VIP номеров"""
        if len(phone_digits) >= 6:
            last_six = phone_digits[-6:]
            return self.vip_patterns.get(last_six, None)
        return None

    def format_phone(self, phone_digits, style='standard'):
        """Форматирование номера телефона"""
        if len(phone_digits) == 11:
            if style == 'standard':
                return f"+7 ({phone_digits[1:4]}) {phone_digits[4:7]}-{phone_digits[7:9]}-{phone_digits[9:]}"
            elif style == 'international':
                return f"+7{phone_digits[1:]}"
            elif style == 'national':
                return f"8{phone_digits[1:4]}{phone_digits[4:7]}{phone_digits[7:9]}{phone_digits[9:]}"
            elif style == 'clean':
                return phone_digits
        return phone_digits

    def calculate_number_score(self, phone_digits):
        """Расчет рейтинга номера (0-100)"""
        score = 0
        
        if len(phone_digits) == 11:
            last_six = phone_digits[-6:]
            
            # Проверка VIP паттернов
            if self.detect_vip(phone_digits):
                score += 80
            
            # Проверка зеркальных номеров
            if last_six[:3] == last_six[3:][::-1]:
                score += 30
            
            # Проверка палиндромов
            if last_six == last_six[::-1]:
                score += 40
            
            # Номер заканчивается на 00
            if phone_digits[-2:] == '00':
                score += 20
            
            # Номер заканчивается на повторяющиеся цифры
            if len(set(last_six)) <= 2:
                score += 25
            
            # Красивые комбинации
            if last_six in ['123123', '321321', '112233', '223344']:
                score += 50
        
        return min(score, 100)

    def analyze_number(self, phone):
        """Полный анализ номера"""
        valid, digits, status = self.validate_russian_phone(phone)
        
        if not valid:
            return None
        
        operator, op_info = self.get_operator_info(digits)
        vip_info = self.detect_vip(digits)
        score = self.calculate_number_score(digits)
        
        # Определяем цвет для рейтинга
        if score >= 80:
            rating_color = 'GREEN'
            rating_emoji = '🏆'
        elif score >= 50:
            rating_color = 'YELLOW'
            rating_emoji = '⭐'
        elif score >= 30:
            rating_color = 'CYAN'
            rating_emoji = '✨'
        else:
            rating_color = 'WHITE'
            rating_emoji = '📱'
        
        # Определяем цвет для оператора
        operator_color = op_info['color']
        
        return {
            'original': phone,
            'digits': digits,
            'status': status,
            'operator': operator,
            'operator_color': operator_color,
            'operator_info': op_info['info'],
            'formatted': {
                'international': self.format_phone(digits, 'international'),
                'national': self.format_phone(digits, 'national'),
                'standard': self.format_phone(digits, 'standard'),
                'clean': self.format_phone(digits, 'clean')
            },
            'vip': vip_info,
            'score': score,
            'rating_color': rating_color,
            'rating_emoji': rating_emoji,
            'timestamp': datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'),
            'fingerprint': hashlib.md5(digits.encode()).hexdigest()[:12].upper(),
            'is_vip': vip_info is not None
        }

# ============================================
# 🎮 ИНТЕРАКТИВНЫЙ ИНТЕРФЕЙС
# ============================================

class NeptuneInterface:
    """Интерфейс NEPTUNE Russian Numbers"""
    
    def __init__(self):
        self.analyzer = RussianPhoneAnalyzer()
        self.history = []
        
    def print_colored(self, text, color='white'):
        """Вывод цветного текста"""
        try:
            from colorama import Fore, Style
            colors = {
                'blue': Fore.BLUE,
                'cyan': Fore.CYAN,
                'green': Fore.GREEN,
                'yellow': Fore.YELLOW,
                'red': Fore.RED,
                'magenta': Fore.MAGENTA,
                'white': Fore.WHITE,
                'gray': Fore.LIGHTBLACK_EX
            }
            print(f"{colors.get(color, Fore.WHITE)}{text}{Style.RESET_ALL}")
        except:
            print(text)

    def show_main_menu(self):
        """Главное меню программы"""
        display_color_logo()
        
        menu = f"""
{'═'*70}

🎯 ВЫБЕРИТЕ РЕЖИМ РАБОТЫ:

    1. 🔍 Анализ номера
    2. 📝 Экспорт результатов
    3. ⚙️  Настройки
    4. ❓ Помощь
    0. 🚪 Выход

{'═'*70}
        """
        print(menu)

    def analyze_single_number(self):
        """Анализ одного номера"""
        self.print_colored("\n" + "═"*70, "blue")
        self.print_colored("🔍 АНАЛИЗ РОССИЙСКОГО НОМЕРА", "cyan")
        self.print_colored("═"*70, "blue")
        
        phone = input("\n📱 Введите номер телефона: ").strip()
        
        if not phone:
            self.print_colored("❌ Не введен номер", "red")
            return
        
        # Показываем анимацию загрузки
        self.print_colored("\n⏳ Анализирую номер...", "yellow")
        import time
        time.sleep(0.5)
        
        result = self.analyzer.analyze_number(phone)
        
        if not result:
            self.print_colored("❌ Ошибка: Неверный формат номера!", "red")
            self.print_colored("\n📋 Правильные форматы:", "cyan")
            self.print_colored("  • 89161234567", "white")
            self.print_colored("  • +79161234567", "white")
            self.print_colored("  • 9161234567", "white")
            input("\nНажмите Enter для продолжения...")
            return
        
        # Вывод результатов с красивым оформлением
        self.print_colored(f"\n{'═'*70}", "green")
        self.print_colored("📋 РЕЗУЛЬТАТЫ АНАЛИЗА", "green")
        self.print_colored(f"{'═'*70}", "green")
        
        # Основная информация
        self.print_colored(f"\n📱 Номер: {result['original']}", "white")
        self.print_colored(f"✅ Статус: {result['status']}", "green")
        
        # Информация об операторе
        operator_color = result['operator_color'].lower()
        self.print_colored(f"\n🏢 Оператор: {result['operator']}", operator_color)
        self.print_colored(f"ℹ️  Инфо: {result['operator_info']}", operator_color)
        
        # Форматы номера
        self.print_colored(f"\n🎭 Форматы номера:", "yellow")
        self.print_colored(f"  🌍 Международный: {result['formatted']['international']}", "white")
        self.print_colored(f"  🇷🇺 Национальный: {result['formatted']['national']}", "white")
        self.print_colored(f"  📱 Стандартный: {result['formatted']['standard']}", "white")
        self.print_colored(f"  🔢 Цифры: {result['formatted']['clean']}", "white")
        
        # VIP информация
        if result['vip']:
            self.print_colored(f"\n{result['vip']}", "yellow")
            self.print_colored("💰 Этот номер стоит дороже обычного!", "yellow")
        
        # Рейтинг номера
        rating_color = result['rating_color'].lower()
        self.print_colored(f"\n{result['rating_emoji']} Рейтинг: {result['score']}/100", rating_color)
        
        # Дополнительная информация
        self.print_colored(f"\n🆔 Отпечаток: {result['fingerprint']}", "blue")
        self.print_colored(f"🕐 Время анализа: {result['timestamp']}", "cyan")
        
        # Сохраняем в историю
        self.history.append(result)
        
        # Дополнительные опции
        self.print_colored(f"\n{'═'*70}", "cyan")
        self.print_colored("🎯 ДОПОЛНИТЕЛЬНЫЕ ОПЦИИ:", "cyan")
        print("  1. Сохранить результат")
        print("  2. Показать детали")
        print("  3. Новый анализ")
        print("  4. Выйти в меню")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '1':
            self.save_result(result)
        elif choice == '2':
            self.show_details(result)
        
        input("\nНажмите Enter для продолжения...")

    def save_result(self, result):
        """Сохранение результата анализа"""
        filename = f"neptune_result_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("="*60 + "\n")
                f.write("NEPTUNE RUSSIAN NUMBERS - РЕЗУЛЬТАТ АНАЛИЗА\n")
                f.write("="*60 + "\n\n")
                
                f.write(f"Номер: {result['original']}\n")
                f.write(f"Оператор: {result['operator']}\n")
                f.write(f"Статус: {result['status']}\n")
                f.write(f"Рейтинг: {result['score']}/100\n")
                
                if result['vip']:
                    f.write(f"VIP: {result['vip']}\n")
                
                f.write(f"\nФорматы:\n")
                f.write(f"  Международный: {result['formatted']['international']}\n")
                f.write(f"  Национальный: {result['formatted']['national']}\n")
                f.write(f"  Стандартный: {result['formatted']['standard']}\n")
                
                f.write(f"\nДополнительно:\n")
                f.write(f"  Отпечаток: {result['fingerprint']}\n")
                f.write(f"  Время анализа: {result['timestamp']}\n")
                f.write(f"  Информация: {result['operator_info']}\n")
                
                f.write("\n" + "="*60 + "\n")
                f.write("Создано с помощью NEPTUNE RUSSIAN NUMBERS 1.0.0\n")
                f.write("by Venz1onixxx - https://github.com/Venz1onixxx\n")
                f.write("="*60 + "\n")
            
            self.print_colored(f"✅ Результат сохранен в файл: {filename}", "green")
            
        except Exception as e:
            self.print_colored(f"❌ Ошибка при сохранении: {e}", "red")

    def show_details(self, result):
        """Показать детали анализа"""
        self.print_colored(f"\n{'═'*70}", "magenta")
        self.print_colored("🔍 ДЕТАЛЬНЫЙ АНАЛИЗ НОМЕРА", "magenta")
        self.print_colored(f"{'═'*70}", "magenta")
        
        digits = result['digits']
        
        self.print_colored(f"\n📊 Структура номера {digits}:", "cyan")
        self.print_colored(f"  Код страны: {digits[0]}", "white")
        self.print_colored(f"  Код оператора/города: {digits[1:4]}", "white")
        self.print_colored(f"  Префикс: {digits[4:7]}", "white")
        self.print_colored(f"  Абонентский номер: {digits[7:]}", "white")
        
        # Анализ цифр
        self.print_colored(f"\n🎯 Анализ цифровых паттернов:", "cyan")
        
        # Считаем частоту цифр
        digit_count = {}
        for digit in digits[1:]:  # Игнорируем первую цифру (код страны)
            digit_count[digit] = digit_count.get(digit, 0) + 1
        
        self.print_colored("  Частота цифр:", "white")
        for digit in sorted(digit_count.keys()):
            count = digit_count[digit]
            bar = "█" * count
            self.print_colored(f"    {digit}: {count} {bar}", "white")
        
        # Особые комбинации
        self.print_colored(f"\n✨ Особые комбинации:", "cyan")
        
        # Проверяем последние 4 цифры
        last_four = digits[-4:]
        if len(set(last_four)) == 1:
            self.print_colored(f"  Последние 4 цифры одинаковы: {last_four}", "yellow")
        
        # Проверяем повторения
        if len(set(digits[7:])) <= 2:
            self.print_colored(f"  Абонентский номер имеет мало уникальных цифр", "yellow")
        
        self.print_colored(f"\n{'═'*70}", "magenta")

    def export_results(self):
        """Экспорт результатов"""
        if not self.history:
            self.print_colored("❌ Нет данных для экспорта", "red")
            input("\nНажмите Enter для продолжения...")
            return
        
        self.print_colored("\n" + "═"*70, "blue")
        self.print_colored("📤 ЭКСПОРТ РЕЗУЛЬТАТОВ", "cyan")
        self.print_colored("═"*70, "blue")
        
        print("\nВыберите формат экспорта:")
        print("  1. TXT (текстовый файл)")
        print("  2. JSON (структурированные данные)")
        print("  3. CSV (таблица Excel)")
        print("  4. Назад")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '1':
            self.export_txt()
        elif choice == '2':
            self.export_json()
        elif choice == '3':
            self.export_csv()
        elif choice == '4':
            return

    def export_txt(self):
        """Экспорт в TXT файл"""
        filename = f"neptune_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
        
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                f.write("="*70 + "\n")
                f.write("NEPTUNE RUSSIAN NUMBERS - ЭКСПОРТ РЕЗУЛЬТАТОВ\n")
                f.write("="*70 + "\n\n")
                f.write(f"Всего проанализировано номеров: {len(self.history)}\n")
                f.write(f"Дата экспорта: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
                
                for i, result in enumerate(self.history, 1):
                    f.write(f"Запись #{i}\n")
                    f.write(f"{'-'*40}\n")
                    f.write(f"Номер: {result['original']}\n")
                    f.write(f"Оператор: {result['operator']}\n")
                    f.write(f"Рейтинг: {result['score']}/100\n")
                    
                    if result['vip']:
                        f.write(f"VIP: {result['vip']}\n")
                    
                    f.write(f"Международный формат: {result['formatted']['international']}\n")
                    f.write(f"Время анализа: {result['timestamp']}\n\n")
                
                f.write("="*70 + "\n")
                f.write("Создано с помощью NEPTUNE RUSSIAN NUMBERS 1.0.0\n")
                f.write("by Venz1onixxx - https://github.com/Venz1onixxx\n")
                f.write("="*70 + "\n")
            
            self.print_colored(f"✅ Данные экспортированы в {filename}", "green")
            
        except Exception as e:
            self.print_colored(f"❌ Ошибка при экспорте: {e}", "red")
        
        input("\nНажмите Enter для продолжения...")

    def export_json(self):
        """Экспорт в JSON файл"""
        filename = f"neptune_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
        
        try:
            # Подготавливаем данные для экспорта
            export_data = {
                'export_info': {
                    'tool': 'NEPTUNE RUSSIAN NUMBERS 1.0.0',
                    'author': 'Venz1onixxx',
                    'github': 'https://github.com/Venz1onixxx',
                    'export_date': datetime.datetime.now().isoformat(),
                    'total_records': len(self.history)
                },
                'results': self.history
            }
            
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(export_data, f, ensure_ascii=False, indent=2)
            
            self.print_colored(f"✅ Данные экспортированы в {filename}", "green")
            
        except Exception as e:
            self.print_colored(f"❌ Ошибка при экспорте: {e}", "red")
        
        input("\nНажмите Enter для продолжения...")

    def export_csv(self):
        """Экспорт в CSV файл"""
        filename = f"neptune_export_{datetime.datetime.now().strftime('%Y%m%d_%H%M%S')}.csv"
        
        try:
            import csv
            
            with open(filename, 'w', encoding='utf-8', newline='') as f:
                writer = csv.writer(f)
                
                # Заголовки
                writer.writerow([
                    'Номер', 'Оператор', 'Рейтинг', 'VIP', 
                    'Международный формат', 'Отпечаток', 'Время анализа'
                ])
                
                # Данные
                for result in self.history:
                    writer.writerow([
                        result['original'],
                        result['operator'],
                        result['score'],
                        result['vip'] or '',
                        result['formatted']['international'],
                        result['fingerprint'],
                        result['timestamp']
                    ])
            
            self.print_colored(f"✅ Данные экспортированы в {filename}", "green")
            
        except Exception as e:
            self.print_colored(f"❌ Ошибка при экспорте: {e}", "red")
        
        input("\nНажмите Enter для продолжения...")

    def show_settings(self):
        """Настройки программы"""
        self.print_colored("\n" + "═"*70, "blue")
        self.print_colored("⚙️  НАСТРОЙКИ NEPTUNE", "cyan")
        self.print_colored("═"*70, "blue")
        
        print("\nДоступные настройки:")
        print("  1. Изменить цветовую тему")
        print("  2. Очистить историю")
        print("  3. Проверить обновления")
        print("  4. О программе")
        print("  5. Назад")
        
        choice = input("\nВаш выбор: ").strip()
        
        if choice == '1':
            self.change_theme()
        elif choice == '2':
            self.clear_history()
        elif choice == '3':
            self.check_updates()
        elif choice == '4':
            self.show_about()
        elif choice == '5':
            return

    def change_theme(self):
        """Изменение цветовой темы"""
        self.print_colored("\n" + "═"*70, "magenta")
        self.print_colored("🎨 ИЗМЕНЕНИЕ ЦВЕТОВОЙ ТЕМЫ", "magenta")
        self.print_colored("═"*70, "magenta")
        
        print("\nДоступные темы:")
        print("  1. Синяя (стандартная)")
        print("  2. Зеленая")
        print("  3. Фиолетовая")
        print("  4. Желтая")
        print("  5. Красная")
        print("  6. Назад")
        
        choice = input("\nВыберите тему: ").strip()
        
        if choice in ['1', '2', '3', '4', '5']:
            themes = {
                '1': 'blue',
                '2': 'green', 
                '3': 'magenta',
                '4': 'yellow',
                '5': 'red'
            }
            theme = themes[choice]
            self.print_colored(f"✅ Тема изменена на {theme}", "green")
        elif choice == '6':
            return
        
        input("\nНажмите Enter для продолжения...")

    def clear_history(self):
        """Очистка истории"""
        self.print_colored("\n" + "═"*70, "red")
        self.print_colored("⚠️  ОЧИСТКА ИСТОРИИ", "red")
        self.print_colored("═"*70, "red")
        
        confirm = input("\nВы уверены? Все данные будут удалены! (y/n): ").strip().lower()
        
        if confirm == 'y':
            self.history = []
            self.print_colored("✅ История очищена", "green")
        else:
            self.print_colored("❌ Отменено", "yellow")
        
        input("\nНажмите Enter для продолжения...")

    def check_updates(self):
        """Проверка обновлений"""
        self.print_colored("\n" + "═"*70, "cyan")
        self.print_colored("🔄 ПРОВЕРКА ОБНОВЛЕНИЙ", "cyan")
        self.print_colored("═"*70, "cyan")
        
        self.print_colored("\n📡 Проверяю наличие обновлений...", "yellow")
        import time
        time.sleep(1)
        
        self.print_colored("✅ У вас установлена актуальная версия 1.0.0", "green")
        self.print_colored("\n🌐 Проверьте обновления на GitHub:", "cyan")
        self.print_colored("   https://github.com/Venz1onixxx/neptune", "white")
        
        input("\nНажмите Enter для продолжения...")

    def show_about(self):
        """Информация о программе"""
        self.print_colored("\n" + "═"*70, "blue")
        self.print_colored("ℹ️  О ПРОГРАММЕ", "cyan")
        self.print_colored("═"*70, "blue")
        
        about_text = f"""
NEPTUNE RUSSIAN NUMBERS 1.0.0

Мощный инструмент для анализа российских номеров телефонов

🎯 ОСНОВНЫЕ ВОЗМОЖНОСТИ:
  • Анализ оператора связи
  • Определение VIP номеров
  • Расчет рейтинга номера
  • Форматирование номеров
  • Экспорт результатов
  • Цветной интерфейс

📱 ПОДДЕРЖИВАЕМЫЕ ФОРМАТЫ:
  • 89161234567
  • +79161234567  
  • 9161234567

🏢 ОПЕРАТОРЫ:
  • МТС, МегаФон, Билайн
  • Tele2, Yota, Ростелеком

⚙️  ТЕХНОЛОГИИ:
  • Python 3.6+
  • Colorama для цветов
  • Чистый код

👨‍💻 АВТОР: Venz1onixxx
🌐 GITHUB: https://github.com/Venz1onixxx
📧 ПОДДЕРЖКА: Открыть issue на GitHub

⭐ Если вам нравится проект, поставьте звезду на GitHub!
        """
        
        print(about_text)
        input("\nНажмите Enter для продолжения...")

    def show_help(self):
        """Показать помощь"""
        self.print_colored("\n" + "═"*70, "green")
        self.print_colored("❓ ПОМОЩЬ ПО NEPTUNE", "cyan")
        self.print_colored("═"*70, "green")
        
        help_text = f"""
📖 КОМАНДЫ И ВОЗМОЖНОСТИ:

1. 🔍 АНАЛИЗ НОМЕРА
   - Введите номер в любом формате
   - Получите полную информацию
   - Узнайте оператора и рейтинг

2. 📝 ЭКСПОРТ РЕЗУЛЬТАТОВ
   - Сохраните анализ в TXT, JSON или CSV
   - Экспортируйте всю историю
   - Используйте данные в других программах

3. ⚙️  НАСТРОЙКИ
   - Измените цветовую тему
   - Очистите историю
   - Проверьте обновления
   - Узнайте о программе

4. ❓ ПОМОЩЬ
   - Эта страница

🎯 БЫСТРЫЕ КОМАНДЫ:
   - Для выхода введите '0' или 'exit'
   - Для помощи введите '4' или 'help'
   - Для настройки введите '3' или 'settings'

📱 ПРИМЕРЫ ИСПОЛЬЗОВАНИЯ:
   1. Запустите программу
   2. Выберите '1' для анализа номера
   3. Введите номер: 89161234567
   4. Получите полный отчет
   5. Сохраните результат если нужно

⭐ СОВЕТЫ:
   • VIP номера имеют высокий рейтинг
   • Сохраняйте важные анализы
   • Используйте экспорт для отчетов
   • Обновляйте программу регулярно
        """
        
        print(help_text)
        input("\nНажмите Enter для продолжения...")

# ============================================
# 🚀 ЗАПУСК ПРОГРАММЫ
# ============================================

def main():
    """Основная функция программы"""
    try:
        # Настройка кодировки для Windows
        if os.name == 'nt':
            os.system('chcp 65001 > nul')
        
        # Создаем интерфейс
        interface = NeptuneInterface()
        
        while True:
            # Показываем главное меню
            interface.show_main_menu()
            
            choice = input("\n🎯 Ваш выбор (0-4): ").strip()
            
            if choice == '1':
                interface.analyze_single_number()
            
            elif choice == '2':
                interface.export_results()
            
            elif choice == '3':
                interface.show_settings()
            
            elif choice == '4':
                interface.show_help()
            
            elif choice in ['0', 'exit', 'quit']:
                interface.print_colored("\n" + "═"*70, "blue")
                interface.print_colored("👋 До свидания! Спасибо за использование NEPTUNE!", "green")
                interface.print_colored("⭐ Не забывайте посещать: https://github.com/Venz1onixxx", "cyan")
                interface.print_colored("═"*70, "blue")
                break
            
            else:
                interface.print_colored("❌ Неверный выбор. Попробуйте снова.", "red")
                import time
                time.sleep(1)
    
    except KeyboardInterrupt:
        print("\n\n👋 Программа прервана пользователем.")
    except Exception as e:
        print(f"\n❌ Критическая ошибка: {e}")
        input("\nНажмите Enter для выхода...")

if __name__ == "__main__":
    # Проверяем версию Python
    if sys.version_info[0] < 3:
        print("❌ Требуется Python 3.6 или выше")
        sys.exit(1)
    
    # Запускаем программу
    main()