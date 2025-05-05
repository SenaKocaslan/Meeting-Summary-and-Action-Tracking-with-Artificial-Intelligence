class Transcript {
  
  final int id;
  final String dosyaAdi;
  final String icerik;

  Transcript({
    required this.id,
    required this.dosyaAdi,
    required this.icerik
  });

  factory Transcript.fromJson(Map<String, dynamic> json){
    return Transcript(
      id: json['id'], 
      dosyaAdi: json['dosya_adi'], 
      icerik: json['transkript']
    );
  }

}