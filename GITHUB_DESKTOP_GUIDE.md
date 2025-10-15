# GitHub Desktop - Пошаговая Инструкция

**Автор:** Aleksei Novgorodtsev (AIDoctrine)  
**Репозиторий:** AIDoctrine/fpc-ae1r  
**Дата:** Октябрь 2025

---

## 🎯 Преимущества GitHub Desktop

✅ Не нужно загружать файлы по одному  
✅ Один Commit → Push вместо 14 коммитов  
✅ Удобная работа с обновлениями  
✅ Визуальный просмотр изменений

---

## 📁 ЭТАП 1: Создание репозитория

### Если репозиторий ещё не создан

1. https://github.com/AIDoctrine → **"New"**
2. Имя: `fpc-ae1r`
3. Description: `FPC v2.2r + AE-1r: Predicting and Preventing LLM Failures via Measurable Internal States`
4. Public ✅
5. **☐ README / ☐ .gitignore / ☐ License** (все ВЫКЛЮЧЕНЫ!)
6. **"Create repository"**

### Если репозиторий создан с галочками

**Вариант 1 (рекомендую):** Удалите и создайте заново БЕЗ галочек.

**Как удалить:**
- Репозиторий → Settings → внизу "Delete this repository"
- Подтвердите удаление
- Создайте новый (см. выше)

**Вариант 2:** Работайте с существующим (см. раздел "Проблемы" ниже)

---

## 📦 ЭТАП 2: Клонирование

### В GitHub Desktop:

1. **File → Clone repository**
2. Вкладка **GitHub.com**
3. Выберите `AIDoctrine/fpc-ae1r`
4. Local path: `C:\Projects\fpc-ae1r` (или ваш путь)
5. **"Clone"**

---

## 📂 ЭТАП 3: Копирование файлов

### Шаг 3.1: Откройте папку репозитория

В GitHub Desktop:
- **Repository → Show in Explorer** (Windows)
- Или **Repository → Show in Finder** (Mac)

### Шаг 3.2: Скачайте файлы

Все файлы готовы в этом чате:
```
computer:///mnt/user-data/outputs/fpc-ae1r-github/
```

Кликните на ссылку выше и скачайте папку.

### Шаг 3.3: Скопируйте ВСЕ файлы

Из скачанной папки `fpc-ae1r-github/` → в `C:\Projects\fpc-ae1r\`

**Проверьте наличие:**
- ✓ README.md
- ✓ LICENSE
- ✓ .gitignore
- ✓ requirements.txt
- ✓ **fpc_ae1r.py** (960 KB - ВАЖНО!)
- ✓ paper/ (папка с main.tex)
- ✓ docs/ (папка)
- ✓ examples/ (папка)
- ✓ tests/ (папка)

---

## 💾 ЭТАП 4: Commit & Push

### В GitHub Desktop:

**Левая панель** покажет все новые файлы (около 14 файлов).

### Шаг 4.1: Создайте коммит

Внизу слева:
- **Summary:** `Initial commit: FPC-AE1r v1.0.0-arxiv`
- **Description:** (опционально)
  ```
  - Production implementation
  - Updated paper (SimpleQA validation)
  - Solo author: Aleksei Novgorodtsev (AIDoctrine)
  - Ready for arXiv submission
  ```

### Шаг 4.2: Commit

Нажмите **"Commit to main"** (синяя кнопка внизу слева)

### Шаг 4.3: Push

Нажмите **"Push origin"** (кнопка вверху справа)

🎉 **Готово!** Все файлы на GitHub.

---

## 🏷️ ЭТАП 5: Создание Release

### На GitHub (web):

1. https://github.com/AIDoctrine/fpc-ae1r
2. Справа **"Releases"** → **"Create a new release"**
3. **Tag version:** `v1.0.0-arxiv`
4. **Release title:** `v1.0.0-arxiv: Initial arXiv Submission`
5. **Description:**
   ```markdown
   Initial release by Aleksei Novgorodtsev (AIDoctrine).
   
   ## Key Features
   - Full FPC-AE1r production implementation
   - SimpleQA-Verified validation (75.7% F1-score)
   - 72% error interception rate
   - Cross-model testing (GPT-4o + Claude-3.7)
   - <50ms overhead, cryptographic audit trail
   
   ## Results
   - 5,400+ correlation tests (ρ=0.71, p<0.001)
   - 100 SimpleQA questions validated
   - Consistent across OpenAI and Anthropic
   
   See paper/ directory for LaTeX manuscript.
   ```
6. **"Publish release"**

---

## 🎨 ЭТАП 6: Настройка (опционально)

### Topics

На главной странице репозитория:
- ⚙️ About → Edit
- Topics: `llm`, `ai-safety`, `arxiv`, `hallucination-detection`, `mechanistic-interpretability`, `eu-ai-act`
- **Save**

### Description

- Description: `FPC v2.2r + AE-1r: Predicting and Preventing LLM Failures via Measurable Internal States`
- Website: `https://colab.research.google.com/drive/18LcJYXptiQ6V-82rtc2mvK43KTXyrM_v`

---

## 📊 ЭТАП 7: Добавление фигур (позже)

Когда сгенерируете фигуры:

1. Поместите PDF файлы в локальную папку `paper/figures/`
2. GitHub Desktop покажет новые файлы
3. Commit: `Add paper figures`
4. Push

**Нужные файлы:**
- `figure_s1_pipeline.pdf`
- `figure_s2_states.pdf`
- `figure_formula_a_correlation.pdf`
- `figure_formula_b_temperature.pdf`
- `figure_cross_formula_comparison.pdf`
- `figures/figure_mechanistic_unified.pdf`

---

## ✅ Финальная проверка

На https://github.com/AIDoctrine/fpc-ae1r проверьте:

- [ ] README.md отображается с результатами
- [ ] Структура папок видна
- [ ] LICENSE распознан (MIT)
- [ ] fpc_ae1r.py присутствует (~960 KB)
- [ ] Release v1.0.0-arxiv создан
- [ ] Topics добавлены
- [ ] Ссылка на Colab работает

---

## 🐛 Решение проблем

### Проблема: Репозиторий создан с галочками

**Решение:**
1. Клонируйте существующий
2. Удалите автоматически созданные файлы (README.md, LICENSE, .gitignore)
3. Скопируйте НАШИ файлы
4. Commit с описанием: `Replace auto-generated files`
5. Push

### Проблема: Файлов слишком много в Changes

**Ответ:** Это нормально! Около 14 файлов + подпапки - это правильно.

### Проблема: Git не видит .gitignore

**Решение:** Убедитесь, что файл называется `.gitignore` (с точкой), а не `gitignore`

---

## 🎯 Структура репозитория

```
fpc-ae1r/
├── README.md
├── LICENSE  
├── .gitignore
├── requirements.txt
├── fpc_ae1r.py          ← 960 KB, основной код
├── CONTRIBUTING.md
│
├── paper/
│   ├── main.tex         ← Обновленная статья
│   ├── bibliography.bib
│   └── figures/
│       └── README.md
│
├── docs/
│   ├── TESTING.md
│   └── FORMULAS.md
│
├── examples/
│   └── basic_usage.py
│
└── tests/
    └── .gitkeep
```

---

## ⏱ Итого времени: ~10 минут

1. Создание репо: 2 мин
2. Клонирование: 1 мин
3. Копирование: 3 мин
4. Commit & Push: 2 мин
5. Release: 2 мин

---

## 📧 Помощь

**Автор:** Aleksei Novgorodtsev (AIDoctrine)  
**Email:** alexey.novgorodtsev@gmail.com  
**ORCID:** [0009-0009-2407-7049](https://orcid.org/0009-0009-2407-7049)

---

**Успехов с публикацией на arXiv! 🚀**
