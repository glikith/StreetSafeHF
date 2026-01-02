import 'dart:io';
import 'package:flutter/material.dart';
import 'package:image_picker/image_picker.dart';

import '../widgets/metric_card.dart';
import '../widgets/action_card.dart';
import '../widgets/bottom_nav.dart';
import '../services/api_service.dart';

class HomeScreen extends StatefulWidget {
  const HomeScreen({super.key});

  @override
  State<HomeScreen> createState() => _HomeScreenState();
}

class _HomeScreenState extends State<HomeScreen> {
  File? image;
  bool analysisComplete = false;
  bool loading = false;

  String damage = "";
  String severity = "";
  String priority = "";
  double confidence = 0.0;

  String repairType = "";
  String material = "";
  String laborTime = "";

  final ImagePicker picker = ImagePicker();

  Future<void> pickImage() async {
    final XFile? picked = await picker.pickImage(
      source: ImageSource.gallery,
      imageQuality: 85,
    );

    if (picked != null) {
      setState(() {
        image = File(picked.path);
        analysisComplete = false;
      });
    }
  }

  Future<void> runDiagnostics() async {
    if (image == null) return;

    setState(() {
      loading = true;
    });

    final result = await ApiService.analyzeImage(image!.path);

    setState(() {
      damage = result["damage"];
      severity = result["severity"];
      priority = result["priority"];
      confidence = result["confidence"];

      repairType = result["repair"];
      material = result["material"];
      laborTime = result["time"];

      analysisComplete = true;
      loading = false;
    });
  }

  Color getSeverityColor() {
    switch (severity) {
      case "High":
        return Colors.redAccent;
      case "Medium":
        return Colors.orangeAccent;
      default:
        return Colors.greenAccent;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: SafeArea(
        child: SingleChildScrollView(
          padding: const EdgeInsets.all(20),
          child: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              // HEADER
              const Text(
                "SafeStreet",
                style: TextStyle(
                  color: Colors.white,
                  fontSize: 28,
                  fontWeight: FontWeight.w800,
                ),
              ),
              const SizedBox(height: 4),
              const Text(
                "Automated road damage assessment system",
                style: TextStyle(color: Colors.white60),
              ),

              const SizedBox(height: 30),

              // IMAGE PICKER
              GestureDetector(
                onTap: pickImage,
                child: Container(
                  height: 140,
                  decoration: BoxDecoration(
                    borderRadius: BorderRadius.circular(20),
                    border: Border.all(
                      color: Colors.white24,
                      width: 2,
                    ),
                  ),
                  child: const Center(
                    child: Text(
                      "📸 Upload Road Image",
                      style: TextStyle(color: Colors.white70),
                    ),
                  ),
                ),
              ),

              // IMAGE PREVIEW
              if (image != null) ...[
                const SizedBox(height: 20),
                ClipRRect(
                  borderRadius: BorderRadius.circular(20),
                  child: Image.file(
                    image!,
                    height: 220,
                    width: double.infinity,
                    fit: BoxFit.cover,
                  ),
                ),

                const SizedBox(height: 20),

                // ANALYZE BUTTON
                ElevatedButton(
                  onPressed: loading ? null : runDiagnostics,
                  style: ElevatedButton.styleFrom(
                    backgroundColor: const Color(0xFF673FD7),
                    padding: const EdgeInsets.symmetric(vertical: 16),
                    shape: RoundedRectangleBorder(
                      borderRadius: BorderRadius.circular(20),
                    ),
                  ),
                  child: loading
                      ? const CircularProgressIndicator(
                          color: Colors.white,
                        )
                      : const Text(
                          "RUN DIAGNOSTICS",
                          style: TextStyle(fontWeight: FontWeight.bold),
                        ),
                ),
              ],

              // ANALYSIS RESULT
              if (analysisComplete) ...[
                const SizedBox(height: 30),

                Container(
                  padding: const EdgeInsets.all(20),
                  decoration: BoxDecoration(
                    color: Colors.white.withOpacity(0.08),
                    borderRadius: BorderRadius.circular(20),
                    border: Border(
                      left: BorderSide(
                        color: getSeverityColor(),
                        width: 5,
                      ),
                    ),
                  ),
                  child: Column(
                    crossAxisAlignment: CrossAxisAlignment.start,
                    children: [
                      // REPORT HEADER
                      Row(
                        mainAxisAlignment: MainAxisAlignment.spaceBetween,
                        children: [
                          const Text(
                            "Diagnostic Report",
                            style: TextStyle(
                              color: Colors.white,
                              fontWeight: FontWeight.w600,
                            ),
                          ),
                          Container(
                            padding: const EdgeInsets.symmetric(
                              vertical: 4,
                              horizontal: 12,
                            ),
                            decoration: BoxDecoration(
                              color: getSeverityColor(),
                              borderRadius: BorderRadius.circular(20),
                            ),
                            child: Text(
                              "${(confidence * 100).toInt()}% MATCH",
                              style: const TextStyle(
                                color: Colors.white,
                                fontWeight: FontWeight.bold,
                              ),
                            ),
                          ),
                        ],
                      ),

                      const SizedBox(height: 12),

                      Text(
                        "Detected $damage with $severity severity.",
                        style: const TextStyle(color: Colors.white70),
                      ),

                      const SizedBox(height: 20),

                      // METRICS
                      Row(
                        children: [
                          Expanded(
                            child: MetricCard(
                              label: "Priority",
                              value: priority,
                              highlight: severity == "High",
                            ),
                          ),
                          const SizedBox(width: 12),
                          Expanded(
                            child: MetricCard(
                              label: "Repair Type",
                              value: repairType,
                            ),
                          ),
                        ],
                      ),

                      const SizedBox(height: 25),

                      // ACTIONS
                      const Text(
                        "🛠️ Recommended Action",
                        style: TextStyle(
                          color: Colors.white,
                          fontWeight: FontWeight.w600,
                        ),
                      ),

                      const SizedBox(height: 14),

                      ActionCard(
                        icon: Icons.construction,
                        label: "Material Required",
                        value: material,
                      ),

                      const SizedBox(height: 12),

                      ActionCard(
                        icon: Icons.timer,
                        label: "Estimated Labor",
                        value: laborTime,
                      ),
                    ],
                  ),
                ),
              ],
            ],
          ),
        ),
      ),
      bottomNavigationBar: const BottomNav(),
    );
  }
}
