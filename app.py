from flask import Flask, request, jsonify
import yt_dlp

app = Flask(__name__)

@app.route('/search', methods=['GET'])
def search():
    query = request.args.get('term')
    ydl_opts = {'format': 'bestaudio', 'noplaylist': True, 'quiet': True}
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        # YouTube'da ara ve ilk sonucu al
        info = ydl.extract_info(f"ytsearch1:{query}", download=False)['entries'][0]
        return jsonify([{
            'trackId': info['id'],
            'trackName': info['title'],
            'artistName': info['uploader'],
            'previewUrl': info['url'], # Burası artık 30 sn değil, tam şarkı URL'si olacak
            'artworkUrl100': info['thumbnail']
        }])

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)