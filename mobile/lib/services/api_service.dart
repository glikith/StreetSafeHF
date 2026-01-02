class ApiService {
  static Future<Map<String, dynamic>> analyzeImage(String imagePath) async {
    // TODO: Replace with HTTP multipart request to backend
    await Future.delayed(const Duration(seconds: 1));

    return {
      "damage": "Pothole",
      "severity": "High",
      "priority": "Immediate",
      "confidence": 0.89,
      "repair": "Patch",
      "material": "Cold Mix Asphalt",
      "time": "45 mins / 2 workers"
    };
  }
}
