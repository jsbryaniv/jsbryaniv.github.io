"""
Convert tutorial HTML files into a carousel of PNG images.

Usage:
    python make_carousel.py path/to/tutorial.html

Output:
    PNG files saved next to the HTML: panel-1.png, panel-2.png, ...

Setup (first time only):
    pip install playwright
    playwright install chromium
"""

# Import libraries
import sys
import time
from pathlib import Path
from PIL import Image
from playwright.sync_api import sync_playwright


# Define make carousel function
def make_tutorial_carousel(html_path: str) -> None:
    """
    Screenshots each panel of a tutorial HTML file and
    saves the PNG files next to the HTML file.

    Args:
        html_path: Path to the tutorial HTML file.
    """

    # Check path
    path = Path(html_path).resolve()
    if not path.exists():
        print(f"File not found: {path}")
        sys.exit(1)
    if path.name != "tutorial.html":
        print(f"File is not named tutorial.html: {path}")
        sys.exit(1)
    output_dir = path.parent / "carousel"
    output_dir.mkdir(exist_ok=True)

    # Enter playwright block
    with sync_playwright() as p:

        # Open page in headless browser
        browser = p.chromium.launch()
        page = browser.new_page(device_scale_factor=2)
        page.goto(path.as_uri())

        # Wait for the panel stage to exist
        page.wait_for_selector(".tutorial-panel-stage")

        # Loop over panels
        panel_count = page.locator(".tutorial-panel").count()
        print(f"Found {panel_count} panels")
        for i in range(panel_count):

            # Wait for all code animations in the active panel to finish
            active = page.locator(".tutorial-panel.is-active")
            animations = active.locator(".code-animation")
            anim_count = animations.count()

            if anim_count > 0:
                # Wait for each animation to reach the done state
                for j in range(anim_count):
                    page.wait_for_selector(
                        ".tutorial-panel.is-active .code-animation.done",
                        timeout=30000,
                    )

            # Screenshot just the stage element
            stage = page.locator(".tutorial-panel-stage")
            out_path = output_dir / f"panel-{i + 1}.png"
            stage.screenshot(path=str(out_path))
            print(f"Saved {out_path.name}")

            # Advance to next panel (skip on last)
            if i < panel_count - 1:
                page.locator(".tutorial-panel-next").click()
                # Brief pause for transition to complete
                time.sleep(0.6)

        browser.close()

    # Combine PNGs into a PDF
    png_files = sorted(output_dir.glob("panel-*.png"))
    images = [Image.open(f).convert("RGB") for f in png_files]
    pdf_path = output_dir / "carousel.pdf"
    images[0].save(pdf_path, save_all=True, append_images=images[1:])
    print(f"Saved {pdf_path.name}")
    print("Done.")


# --- Main Script ---
if __name__ == "__main__":

    # Validate args
    if len(sys.argv) < 2:
        print("Usage: python make_carousel.py <path/to/tutorial.html|folder>")
        sys.exit(1)
    target = Path(sys.argv[1])

    # If a folder, find all tutorial.html files recursively
    if target.is_dir():
        html_files = sorted(target.rglob("tutorial.html"))
        if not html_files:
            print(f"No tutorial.html files found under {target}")
            sys.exit(1)
        print(f"Found {len(html_files)} tutorial(s)")
        for html_file in html_files:
            print(f"\n--- {html_file} ---")
            make_tutorial_carousel(str(html_file))

    # Otherwise treat it as a single file
    else:
        make_tutorial_carousel(str(target))
