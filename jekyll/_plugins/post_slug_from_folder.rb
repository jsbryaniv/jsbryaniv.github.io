# frozen_string_literal: true

# For posts stored as directory-style files like:
#   _posts/YYYY-MM-DD-my-post/index.md
# derive slug "my-post" automatically so permalinks using :title/:slug
# do not end with "-index".
Jekyll::Hooks.register :posts, :post_init do |post|
  next unless post.basename_without_ext == "index"
  next if post.data["slug"].to_s.strip != ""

  # Use the immediate parent directory as source slug.
  parent = File.basename(File.dirname(post.path.to_s))
  next if parent.nil? || parent.empty?

  # Strip date prefix used by post directories.
  # Example: "2025-08-11-who-killed-pip" -> "who-killed-pip"
  slug = parent.sub(/^\d{4}-\d{2}-\d{2}-/, "")
  next if slug.empty?

  post.data["slug"] = slug
end
