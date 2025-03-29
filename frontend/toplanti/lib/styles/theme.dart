import 'package:flutter/material.dart';

final ThemeData appTheme = ThemeData(
  brightness: Brightness.dark,
  scaffoldBackgroundColor: const Color(0xFF0F172A), // lacivert-ton arka plan
  fontFamily: 'Roboto',

  colorScheme: ColorScheme.dark(
    primary: Color(0xFF1E40AF), // lacivert buton
    secondary: Color(0xFF64748B), // gri ikincil renk
    background: Color(0xFF0F172A),
    surface: Color(0xFF1E293B),
    onPrimary: Colors.white,
    onSurface: Colors.white70,
  ),

  textTheme: const TextTheme(
    headlineLarge: TextStyle(fontSize: 26, fontWeight: FontWeight.bold, color: Colors.white),
    headlineMedium: TextStyle(fontSize: 22, fontWeight: FontWeight.bold, color: Colors.white),
    titleMedium: TextStyle(fontSize: 16, fontWeight: FontWeight.w600, color: Colors.white70),
    bodyMedium: TextStyle(fontSize: 14, color: Colors.white60),
    labelSmall: TextStyle(fontSize: 12, color: Colors.grey),
  ),

  elevatedButtonTheme: ElevatedButtonThemeData(
    style: ElevatedButton.styleFrom(
      backgroundColor: Color(0xFF1E40AF),
      foregroundColor: Colors.white,
      padding: const EdgeInsets.symmetric(vertical: 14, horizontal: 24),
      shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(12)),
      textStyle: const TextStyle(fontSize: 16),
    ),
  ),

  cardTheme: CardTheme(
    color: Color(0xFF1E293B),
    elevation: 4,
    margin: const EdgeInsets.all(12),
    shape: RoundedRectangleBorder(borderRadius: BorderRadius.circular(16)),
    shadowColor: Colors.black54,
  ),

  inputDecorationTheme: InputDecorationTheme(
    filled: true,
    fillColor: Color(0xFF1E293B),
    border: OutlineInputBorder(
      borderRadius: BorderRadius.circular(12),
      borderSide: BorderSide.none,
    ),
    hintStyle: TextStyle(color: Colors.white38),
    labelStyle: TextStyle(color: Colors.white70),
  ),

  
);
