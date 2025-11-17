# Python exercises for AI Programming Course: Ejercicios de POO
# Exercises solved by Carmen Montalvo Luque, 11/2025

# =====================================================
# Ejercicio 1
#
# En Python existen clases para manipular duraciones de tiempo
# (horas:minutos:segundos), pero no nos gustan, vamos a hacer una nueva
# que se llamará Duration y será inmutable. Debe permitir:
#
#     Crear duraciones de tiempos.
#         Ejemplo: t = Duration(10,20,56)
#         Ojo!!! (10, 62, 15) se debe guardar como (11, 2, 15)
#         Si no indico la hora, minuto o segundo estos valores son cero:
#             Duration() --> (0, 0, 0)
#             Duration(34) --> (34, 0, 0)
#             Duration(34, 15) --> (34, 15, 0)
#             Duration(34, 61) --> (35, 1, 0)
#     Las duraciones de tiempo se pueden comparar.
#     A las duraciones de tiempo les puedo sumar y restar segundos.
#     Las duraciones de tiempo se pueden sumar y restar.
# =====================================================

class Duration:
    # Immutable time duration
    def __init__(self, hours=0, minutes=0, seconds=0):
        total_seconds = hours * 3600 + minutes * 60 + seconds
        if total_seconds < 0:
            raise ValueError("Duration cannot be negative.")
        # Normalize internally
        self._hours = total_seconds // 3600
        rem = total_seconds % 3600
        self._minutes = rem // 60
        self._seconds = rem % 60

    # Properties to keep immutability
    @property
    def hours(self): return self._hours

    @property
    def minutes(self): return self._minutes

    @property
    def seconds(self): return self._seconds

    def __repr__(self):
        return f"Duration({self.hours}, {self.minutes}, {this.seconds})"

    def __str__(self):
        return f"({self.hours}, {self.minutes}, {self.seconds})"

    # Comparison based on total seconds
    def _total_seconds(self):
        return self.hours * 3600 + self.minutes * 60 + self.seconds

    def __eq__(self, other):
        return self._total_seconds() == Duration._total_seconds(other)

    def __lt__(self, other):
        return self._total_seconds() < Duration._total_seconds(other)

    def __le__(self, other):
        return self._total_seconds() <= Duration._total_seconds(other)

    def __gt__(self, other):
        return self._total_seconds() > Duration._total_seconds(other)

    def __ge__(self, other):
        return self._total_seconds() >= Duration._total_seconds(other)

    # Add/subtract seconds
    def add_seconds(self, s):
        return Duration(0, 0, self._total_seconds() + s)

    # Add/subtract durations
    def __add__(self, other):
        return Duration(0, 0, self._total_seconds() + other._total_seconds())

    def __sub__(self, other):
        return Duration(0, 0, self._total_seconds() - other._total_seconds())


# =====================================================
# Ejercicio 2
#
# Crea una clase, y pruébala, que modele fracciones. Debe permitir:
#
#     Crear fracciones indicando numerador y denominador.
#          Ejemplo: f = Fraction(2, 3)
#         Ojo!!! No se puede tener un denominador cero.
#     Las fracciones pueden operar entre sí.
#         Sumar, multiplicar, dividir, restar.
#         Ojo!!! esto se puede hacer: f + 1, 5 * f
#     Las fracciones se pueden comparar.
#         ==, <, <=, >, >=, !=
#         Ojo!!! estas dos fracciones son iguales: 1/2 y 2/4
#         Ojo!!! esto se puede hacer 1 < 1/2
# =====================================================

from math import gcd

class Fraction:
    # Simple fraction with automatic reduction
    def __init__(self, num, den):
        if den == 0:
            raise ZeroDivisionError("Denominator cannot be zero.")

        # Normalize sign
        if den < 0:
            num, den = -num, -den

        g = gcd(num, den)
        self.num = num // g
        self.den = den // g

    def __repr__(self):
        return f"Fraction({self.num}, {self.den})"

    def __str__(self):
        return f"{self.num}/{self.den}"

    # Convert integer to Fraction
    @staticmethod
    def _to_fraction(val):
        if isinstance(val, Fraction):
            return val
        return Fraction(val, 1)

    # Arithmetic
    def __add__(self, other):
        other = Fraction._to_fraction(other)
        return Fraction(self.num * other.den + other.num * self.den, self.den * other.den)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        other = Fraction._to_fraction(other)
        return Fraction(self.num * other.den - other.num * self.den, self.den * other.den)

    def __rsub__(self, other):
        return Fraction._to_fraction(other) - self

    def __mul__(self, other):
        other = Fraction._to_fraction(other)
        return Fraction(self.num * other.num, self.den * other.den)

    def __rmul__(self, other):
        return self * other

    def __truediv__(self, other):
        other = Fraction._to_fraction(other)
        return Fraction(self.num * other.den, self.den * other.num)

    def __rtruediv__(self, other):
        return Fraction._to_fraction(other) / self

    # Comparison using cross multiplication
    def __eq__(self, other):
        other = Fraction._to_fraction(other)
        return self.num * other.den == other.num * self.den

    def __lt__(self, other):
        other = Fraction._to_fraction(other)
        return self.num * other.den < other.num * self.den

    def __le__(self, other):
        other = Fraction._to_fraction(other)
        return self.num * other.den <= other.num * self.den

    def __gt__(self, other):
        other = Fraction._to_fraction(other)
        return self.num * other.den > other.num * self.den

    def __ge__(self, other):
        other = Fraction._to_fraction(other)
        return self.num * other.den >= other.num * self.den

    def __ne__(self, other):
        return not self == other


# =====================================================
# Ejercicio 3
#
# En Python podemos manejar fechas pero no nos gusta, vamos a crear una
# clase Date. Debe permitir:
#
#     Crear fechas.
#         Ejemplo: f = Date(17, 11, 2022)
#         Ojo!!! Estas fechas son erróneas:
#             Date(78, -45, 0)
#             Date(31, 6, 2022)
#             Date(29, 2, 2022)
#     Las fechas se pueden comparar.
#     A las fechas se le pueden sumar y restar días.
#     Las fechas se pueden restar.
#     Se debe poder averiguar el día de la semana de una fecha.
# =====================================================

import datetime

class Date:
    # Simple wrapper around datetime.date with validation
    def __init__(self, day, month, year):
        try:
            self._date = datetime.date(year, month, day)
        except ValueError:
            raise ValueError("Invalid date.")

    def __repr__(self):
        return f"Date({self.day}, {self.month}, {self.year})"

    @property
    def day(self): return self._date.day

    @property
    def month(self): return self._date.month

    @property
    def year(self): return self._date.year

    # Comparisons delegate to datetime.date
    def __eq__(self, other): return self._date == other._date
    def __lt__(self, other): return self._date < other._date
    def __le__(self, other): return self._date <= other._date
    def __gt__(self, other): return self._date > other._date
    def __ge__(self, other): return self._date >= other._date

    # Add/subtract days
    def add_days(self, d):
        return Date(self.day + d, self.month, self.year)

    # Subtract dates → number of days
    def __sub__(self, other):
        if isinstance(other, Date):
            return (self._date - other._date).days
        raise TypeError("Subtraction allowed only between Date objects.")

    # Day of week (0=Monday)
    def weekday(self):
        return self._date.weekday()



