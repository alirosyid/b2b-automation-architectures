import subprocess
import json

def extract_video_metadata(file_path):
    print(f"[*] Extracting metadata for media pipeline: {file_path}")
    
    try:
        # Requires FFprobe installed on the server
        cmd = [
            "ffprobe", "-v", "quiet", "-print_format", "json", "-show_format", "-show_streams", file_path
        ]
        result = subprocess.run(cmd, capture_output=True, text=True)
        metadata = json.loads(result.stdout)
        
        duration = metadata['format']['duration']
        print(f"[Core Utils] Metadata extracted successfully. Duration: {duration}s")
        return {"status": "success", "duration": duration}
    except Exception as e:
        print(f"[Core Utils] Failed to extract metadata: {e}")
        return {"status": "failed", "error": str(e)}

if __name__ == "__main__":
    # Mocking execution (will fail if no actual file exists)
    extract_video_metadata("./assets/sample_clip.mp4")
