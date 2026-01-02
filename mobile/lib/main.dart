import 'package:flutter/material.dart';
import 'screens/home_screen.dart';

void main() {
  runApp(const SafeStreetApp());
}

class SafeStreetApp extends StatelessWidget {
  const SafeStreetApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      title: 'SafeStreet',
      debugShowCheckedModeBanner: false,
      theme: ThemeData(
        fontFamily: 'Inter',
        scaffoldBackgroundColor: const Color(0xFF0F0C29),
      ),
      home: const HomeScreen(),
    );
  }
}
