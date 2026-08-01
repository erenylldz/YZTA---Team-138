import os
from pathlib import Path

import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from apps.analyses.rag.ingestion.youtube_ingestion import (
    ingest_youtube_video,
)


def main() -> None:
    metadata_dir = Path("data/youtube/metadata")
    transcript_dir = Path("data/youtube/transcripts")

    info_files = sorted(metadata_dir.glob("*.info.json"))

    success_count = 0
    skipped_count = 0
    failed_count = 0

    print(f"{len(info_files)} video bulundu.\n")

    for index, info_path in enumerate(info_files, start=1):
        video_id = info_path.name.removesuffix(".info.json")

        transcript_path = transcript_dir / f"{video_id}.tr.json3"

        if not transcript_path.exists():
            transcript_path = (
                transcript_dir / f"{video_id}.tr-orig.json3"
            )

        print(f"[{index}/{len(info_files)}] {video_id}")

        if not transcript_path.exists():
            failed_count += 1
            print("  HATA: Türkçe transcript bulunamadı.")
            continue

        try:
            result = ingest_youtube_video(
                transcript_path=transcript_path,
                info_path=info_path,
                skip_existing=True,
            )

            if result.skipped:
                skipped_count += 1
                print(f"  Atlandı: {result.title}")
                print(f"  Mevcut chunk: {result.chunk_count}")
            else:
                success_count += 1
                print(f"  Başarılı: {result.title}")
                print(f"  Chunk: {result.chunk_count}")
                print(f"  Yeni kayıt: {result.created}")

        except Exception as exc:
            failed_count += 1
            print(f"  HATA: {exc}")

    print("\n" + "=" * 50)
    print(f"Yeni işlenen: {success_count}")
    print(f"Atlanan: {skipped_count}")
    print(f"Başarısız: {failed_count}")
    print(f"Toplam: {len(info_files)}")


if __name__ == "__main__":
    main()