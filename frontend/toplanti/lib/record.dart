import 'dart:io';
import 'package:flutter/material.dart';
<<<<<<< HEAD
import 'package:toplanti/fileUpload.dart';
=======
import 'package:toplanti/services/transcript_service.dart';

import 'package:toplanti/styles/boxDecoration.dart';
import 'package:toplanti/styles/sizes.dart';

class Record extends StatefulWidget {
  


const Record({super.key});

  @override
  State<Record> createState() => _RecordState();
}

class _RecordState extends State<Record> {
  
  Process? _ffmpegProcess;
  bool isRecording = false;
  String? recordingPath;

  Future <String> getRecordingPath() async{
    final now = DateTime.now();
    final formatted = '${now.year}-${now.month}-${now.day}_${now.hour}-${now.minute}-${now.second}';
    final dir = Directory(".");
    return '${dir.path}/kayit_$formatted.wav';
  }

  Future <void> startRecording() async{
    final path = await getRecordingPath();

    _ffmpegProcess = await Process.start(
      'ffmpeg',
      ['-y', '-f', 'alsa', '-i', 'hw:1,0', path],
      mode: ProcessStartMode.detachedWithStdio
    );

    setState(() {
      isRecording = true;
      recordingPath = path;
    });
  }

    Future stopRecording() async {
      if (_ffmpegProcess != null) {
        _ffmpegProcess!.kill(ProcessSignal.sigterm);
      }

<<<<<<< HEAD
      await uploadFile(recordingPath!);
=======
      
      await TranscriptService.transcribeAudio(File(recordingPath!));

>>>>>>> c9436c2 (Backend ve Flutter tarafı güncellendi, .gitignore ile kayıtlar dışlandı)

   
      if (mounted) {
        setState(() {
          isRecording = false;
        });
      }
    }



  @override
  Widget build(BuildContext context) {
    
    return Container(
      width: context.screenWidth*0.3,
      height: context.screenHeight*0.30,
      padding: EdgeInsets.all(10),
      decoration: standardContainerDecoration,
      child: Padding(
        padding: const EdgeInsets.all(10),
        child: Column(
          mainAxisSize:MainAxisSize.min,
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            Text(
              "Toplantıya Sesli Kayıt",
              textAlign: TextAlign.center,
              style: Theme.of(context).textTheme.headlineMedium,
            ),
            const SizedBox(height: 12),
            Divider(thickness: 1.5, color: Colors.white24),
            const SizedBox(height: 16),

            Row(
              mainAxisAlignment: MainAxisAlignment.spaceEvenly,
              children: [
                ElevatedButton.icon(
                  onPressed: isRecording ? null : startRecording,
                  icon: Icon(Icons.mic),
                  label: Text("Toplantıya Başla")
                ),
                
                ElevatedButton.icon(
                  onPressed: isRecording ? stopRecording : null,
                  icon: Icon(Icons.stop),
                  label: Text("Kaydı Bitir"),
                  style: ElevatedButton.styleFrom(backgroundColor: Colors.red),
                ),
                
               
              ],
            ),

            const SizedBox(height: 16),


             if(recordingPath != null)
                  Text(
                    "Dosya yolu: \n$recordingPath",
                    style: Theme.of(context).textTheme.labelSmall,
                    textAlign: TextAlign.center,
                  )
          ],
        )
    )
   );
  }
}
