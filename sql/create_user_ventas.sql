-- ========================================
-- Script para crear tabla user_ventas
-- Ejecutar en SQL Server Management Studio
-- Base de datos: FepasaPr
-- ========================================

USE FepasaPr;
GO

-- Crear tabla user_ventas
CREATE TABLE user_ventas (
    id INT IDENTITY(1,1) PRIMARY KEY,
    email NVARCHAR(255) UNIQUE NOT NULL,
    nombre NVARCHAR(255) NOT NULL,
    password_hash NVARCHAR(255) NOT NULL,
    is_active BIT DEFAULT 1,
    reset_token NVARCHAR(255) NULL,
    reset_token_expires DATETIME NULL,
    created_at DATETIME DEFAULT GETDATE(),
    updated_at DATETIME DEFAULT GETDATE(),
    last_login DATETIME NULL
);
GO

-- Crear índices para mejor performance
CREATE INDEX idx_email ON user_ventas(email);
CREATE INDEX idx_reset_token ON user_ventas(reset_token);
GO

-- Verificar que la tabla se creó correctamente
SELECT TABLE_NAME, COLUMN_NAME, DATA_TYPE, IS_NULLABLE
FROM INFORMATION_SCHEMA.COLUMNS
WHERE TABLE_NAME = 'user_ventas'
ORDER BY ORDINAL_POSITION;
GO