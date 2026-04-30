module Jekyll
  # Custom StaticFile that can copy to a custom destination path
  class PostAssetFile < StaticFile
    def initialize(site, base, dir, name, dest_dir)
      super(site, base, dir, name)
      @dest_dir = dest_dir
    end

    def destination(dest)
      File.join(dest, @dest_dir, @name)
    end
  end

  class RewritePostImagePaths < Generator
    safe true
    priority :high

    def generate(site)
      site.posts.docs.each do |post|
        image = post.data['image']
        next unless image
        next if image.start_with?('/', 'http')

        # Rewrite relative image path to be absolute based on the post's URL
        # e.g., "assets/image.jpg" -> "/blog/2025/08/who-killed-pip/assets/image.jpg"
        post.data['image'] = File.join(post.url, image)
      end
    end
  end

  class CopyPostAssets < Generator
    safe true
    priority :lowest

    def generate(site)
      # Process each post and copy its colocated assets to match the post's URL
      site.posts.docs.each do |post|
        post_source_dir = File.dirname(post.path)
        assets_dir = File.join(post_source_dir, 'assets')

        # Skip if this post doesn't have an assets folder
        next unless Dir.exist?(assets_dir)

        # Get the post's destination directory (based on permalink)
        # post.url gives us something like "/blog/2025/08/who-killed-pip/"
        # We want to copy assets to that same directory
        post_dest_dir = post.url.sub(%r{^/}, '').sub(%r{/$}, '')

        # Find all files in the post's assets directory
        Dir.glob(File.join(assets_dir, '**', '*')) do |asset_path|
          next unless File.file?(asset_path)

          # Get the relative path within the assets folder
          # e.g., "assets/blog_image.jpg" or "assets/subfolder/image.png"
          asset_path.sub(post_source_dir + '/', '')

          # Extract just the filename and subdirectory within assets
          # e.g., "blog_image.jpg" or "subfolder/image.png"
          asset_relative = asset_path.sub(assets_dir + '/', '')
          subdir_path = File.dirname(asset_relative)
          filename = File.basename(asset_relative)

          # Determine destination: post-slug/assets/[subdir/]filename
          dest_dir = if subdir_path == '.'
                       File.join(post_dest_dir, 'assets')
                     else
                       File.join(post_dest_dir, 'assets', subdir_path)
                     end

          # Create our custom static file
          static_file = PostAssetFile.new(
            site,
            File.dirname(asset_path),
            '',
            filename,
            dest_dir
          )

          site.static_files << static_file
        end
      end
    end
  end
end
