# Итератор для удаления дубликатов
class Unique(object):

    def __init__(self, items, ignore_case=False):

        self.myset = set()

        self.index = -1

        # Нужно реализовать конструктор
        # В качестве ключевого аргумента, конструктор должен принимать bool-параметр ignore_case,
        # в зависимости от значения которого будут считаться одинаковые строки в разном регистре
        # Например: ignore_case = True, Aбв и АБВ разные строки
        #           ignore_case = False, Aбв и АБВ одинаковые строки, одна из них удалится
        # По-умолчанию ignore_case = False

        self.ignore_case = ignore_case
        if self.ignore_case:
            for item in items:
                item = str(item)

                low_str = item.lower()
                set_has_str = False
                for str_in_set in self.myset:
                    if low_str == str_in_set.lower():
                        set_has_str = True
                        break
                if not set_has_str:
                    self.myset.add(item)

        else:
            self.myset = set(items)

        self.limit = len(self.myset)

    def __next__(self):
        self.index += 1
        if self.index < self.limit:
            return self.myset.pop()
        else:
            raise StopIteration

    def __iter__(self):
        return self
