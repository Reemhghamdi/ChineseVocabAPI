# Chinese Vocabulary API

A REST API for managing Chinese vocabulary with Arabic translations.

## Features
- Create, read, update, and delete vocabulary words.
- Search by Chinese characters, pinyin, or Arabic meaning.
- Filter vocabulary by HSK level.
- Sort words alphabetically or by HSK level.
- Store example sentences for each word.

## Technologies
- Python
- Django
- Django REST Framework
- SQLite

## API Endpoints

- `GET /api/words/` — List vocabulary
- `POST /api/words/` — Add a word
- `GET /api/words/?search=学习` — Search vocabulary
- `GET /api/words/?hsk_level=3` — Filter by HSK level
- `GET /api/words/?ordering=hsk_level` — Sort by HSK level

## Purpose
This project combines my interest in learning Chinese with my practice in backend development and REST API design.