module Jekyll
  class RewriteCollectionImagePaths < Generator
    safe true
    priority :high

    def generate(site)
      # Process all collections (projects, tutorials, store, etc.)
      site.collections.each do |name, collection|
        collection.docs.each do |doc|
          image = doc.data['image']
          next unless image
          next if image.start_with?('/', 'http')

          # Rewrite relative image path to be absolute based on the document's URL
          # e.g., "assets/image.jpg" -> "/projects/colors_of_music/assets/image.jpg"
          doc.data['image'] = File.join(doc.url, image)
        end
      end
    end
  end

  class CopyCollectionAssets < Generator
    safe true
    priority :lowest

    def generate(site)
      # Process each collection that has output enabled
      site.collections.each do |name, collection|
        next unless collection.write?

        collection.docs.each do |doc|
          doc_source_dir = File.dirname(doc.path)
          assets_dir = File.join(doc_source_dir, 'assets')

          # Skip if this document doesn't have an assets folder
          next unless Dir.exist?(assets_dir)

          # Get the document's destination directory (based on URL)
          # doc.url gives us something like "/projects/colors_of_music/"
          doc_dest_dir = doc.url.sub(%r{^/}, '').sub(%r{/$}, '')

          # Find all files in the document's assets directory
          Dir.glob(File.join(assets_dir, '**', '*')) do |asset_path|
            next unless File.file?(asset_path)

            # Extract just the filename and subdirectory within assets
            asset_relative = asset_path.sub(assets_dir + '/', '')
            subdir_path = File.dirname(asset_relative)
            filename = File.basename(asset_relative)

            # Determine destination: doc-url/assets/[subdir/]filename
            dest_dir = if subdir_path == '.'
                         File.join(doc_dest_dir, 'assets')
                       else
                         File.join(doc_dest_dir, 'assets', subdir_path)
                       end

            # Create our custom static file (reusing PostAssetFile from copy_post_assets.rb)
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
end
