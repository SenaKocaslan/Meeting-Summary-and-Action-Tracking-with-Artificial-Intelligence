-- Veritabanı Oluştur
CREATE DATABASE toplantilar_db;

\c toplantilar_db

-- Kullanıcılar Tablosu
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100) UNIQUE
);

-- Toplantılar Tablosu
CREATE TABLE meetings (
    id SERIAL PRIMARY KEY,
    title VARCHAR(255),
    description TEXT,
    datetime TIMESTAMP
);

-- Özetler Tablosu
CREATE TABLE summaries (
    id SERIAL PRIMARY KEY,
    meeting_id INT REFERENCES meetings(id),
    summary TEXT,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- Görevler Tablosu
CREATE TABLE tasks (
    id SERIAL PRIMARY KEY,
    meeting_id INT REFERENCES meetings(id),
    assigned_to INT REFERENCES users(id),
    task_description TEXT,
    status VARCHAR(50) DEFAULT 'pending'
);

-- Yeni Kullanıcı Oluştur
CREATE USER meeting_user WITH PASSWORD 'meeting_pass';

-- Kullanıcıya Veritabanı Bağlantı Yetkisi Ver
GRANT CONNECT ON DATABASE toplantilar_db TO meeting_user;

-- Kullanıcıya Tablolarda Okuma, Ekleme ve Güncelleme Yetkisi Ver
GRANT SELECT, INSERT, UPDATE ON ALL TABLES IN SCHEMA public TO meeting_user;
