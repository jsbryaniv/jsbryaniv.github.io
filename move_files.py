
from __future__ import annotations

from pathlib import Path


def convert_posts_to_bundles(posts_dir: str = "_posts", dry_run: bool = True) -> None:
    """
    Convert flat Jekyll post files into post bundle folders.

    Arguments:
    - posts_dir
        Path to the Jekyll _posts directory
    - dry_run
        If True, only print planned changes without modifying files

    Returns:
    - None
    """

    # Get posts directory
    posts_path = Path(posts_dir)

    # Check that posts directory exists
    if not posts_path.exists():
        raise FileNotFoundError(f"Posts directory not found: {posts_path}")

    # Get candidate post files
    post_files = sorted(
        [
            path
            for path in posts_path.iterdir()
            if path.is_file() and path.suffix.lower() in {".md", ".markdown"}
        ]
    )

    # Process each post file
    for post_file in post_files:
        # Get bundle directory and target index path
        bundle_dir = posts_path / post_file.stem
        index_file = bundle_dir / "index.md"

        # Skip if bundle directory already exists
        if bundle_dir.exists():
            print(f"Skipping {post_file} -> bundle already exists: {bundle_dir}")
            continue

        # Report action
        print(f"Convert: {post_file} -> {index_file}")

        # Skip filesystem changes in dry run mode
        if dry_run:
            continue

        # Create bundle directory
        bundle_dir.mkdir(parents=False, exist_ok=False)

        # Read original content
        content = post_file.read_text(encoding="utf-8")

        # Write new index.md
        index_file.write_text(content, encoding="utf-8")

        # Remove original file
        post_file.unlink()


if __name__ == "__main__":
    # Run once in dry-run mode first
    convert_posts_to_bundles(posts_dir="_posts", dry_run=True)

    # Then switch to False when ready
    # convert_posts_to_bundles(posts_dir="_posts", dry_run=False)

    