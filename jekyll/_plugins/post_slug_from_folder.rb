# frozen_string_literal: true

# For posts stored as directory-style files like:
#   _posts/YYYY-MM-DD-my-post/index.md
# derive slug "my-post" automatically so permalinks using :title/:slug
# do not end with "-index".
Jekyll::Hooks.register :posts, :post_init do |post|
  Jekyll.logger.debug "SlugPlugin:", "Processing #{post.path}"
  Jekyll.logger.debug "SlugPlugin:", "  basename_without_ext = #{post.basename_without_ext}"
  
  next unless post.basename_without_ext == "index"
  
  Jekyll.logger.debug "SlugPlugin:", "  Is index file"
  Jekyll.logger.debug "SlugPlugin:", "  Existing slug = '#{post.data["slug"]}'"
  
  next if post.data["slug"].to_s.strip != ""

  # Use the immediate parent directory as source slug.
  parent = File.basename(File.dirname(post.path.to_s))
  Jekyll.logger.debug "SlugPlugin:", "  Parent directory = #{parent}"
  
  next if parent.nil? || parent.empty?

  # Strip date prefix used by post directories.
  # Example: "2025-08-11-who-killed-pip" -> "who-killed-pip"
  slug = parent.sub(/^\d{4}-\d{2}-\d{2}-/, "")
  Jekyll.logger.debug "SlugPlugin:", "  Computed slug = #{slug}"
  
  next if slug.empty?

  post.data["slug"] = slug
  Jekyll.logger.info "SlugPlugin:", "Set slug for #{post.path} to '#{slug}'"
end
