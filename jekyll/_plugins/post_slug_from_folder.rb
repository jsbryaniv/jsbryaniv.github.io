# frozen_string_literal: true

# For posts stored as directory-style files like:
#   _posts/YYYY-MM-DD-my-post/index.md
# derive slug "my-post" automatically so permalinks using :slug
# do not end with "-index".
#
# WHY THIS IS A GENERATOR AND NOT A HOOK:
#
# Jekyll 3.x's Document#read calls populate_title which matches the relative
# path against DATE_FILENAME_MATCHER. For directory-style posts, the regex
# captures "who-killed-pip/index" as the slug (the folder + filename joined),
# which gets slugified to "who-killed-pip-index".
#
# A :post_init hook fires before read(), so it can pre-set data["slug"] and
# populate_title's `||=` respects it. But this is fragile and environment-
# dependent (it fails on some CI setups).
#
# A Generator runs after all documents are fully read, so we can reliably
# overwrite the bad slug that populate_title created.

module Jekyll
  class PostSlugFromFolder < Generator
    safe true
    priority :highest

    def generate(site)
      site.posts.docs.each do |post|
        next unless post.basename_without_ext == "index"

        # If the user explicitly set slug: in front matter, respect it.
        # We detect "explicit" by checking if the current slug does NOT contain
        # path separators or "index" — those indicate it was set by the user.
        current_slug = post.data["slug"].to_s
        if !current_slug.empty? && !current_slug.include?("/") && !current_slug.end_with?("index")
          next
        end

        # Use the immediate parent directory as source slug.
        parent = File.basename(File.dirname(post.path.to_s))
        next if parent.nil? || parent.empty?

        # Strip date prefix used by post directories.
        # Example: "2025-08-11-who-killed-pip" -> "who-killed-pip"
        slug = parent.sub(/^\d{4}-\d{2}-\d{2}-/, "")
        next if slug.empty?

        post.data["slug"] = slug

        # Clear memoized URL so it gets recomputed with the new slug
        post.instance_variable_set(:@url, nil)
      end
    end
  end
end
