# frozen_string_literal: true

# For shop products stored as directory-style files like:
#   _shop/desktop-black-hole/index.md
# derive slug "desktop-black-hole" automatically so permalinks using :slug
# do not end with "-index".

module Jekyll
  class ShopSlugFromFolder < Generator
    safe true
    priority :highest

    def generate(site)
      shop = site.collections["shop"]
      return if shop.nil?

      shop.docs.each do |doc|
        next unless doc.basename_without_ext == "index"

        # If the user explicitly set slug: in front matter, respect it.
        current_slug = doc.data["slug"].to_s
        if !current_slug.empty? && !current_slug.include?("/") && !current_slug.end_with?("index")
          next
        end

        # Use the immediate parent directory as source slug.
        parent = File.basename(File.dirname(doc.path.to_s))
        next if parent.nil? || parent.empty?

        doc.data["slug"] = parent

        # Clear memoized URL so it gets recomputed with the new slug.
        doc.instance_variable_set(:@url, nil)
      end
    end
  end
end
