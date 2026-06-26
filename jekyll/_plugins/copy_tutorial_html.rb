module Jekyll
  class TutorialHtmlFile < StaticFile
    def initialize(site, base, dir, name, dest_dir)
      super(site, base, dir, name)
      @dest_dir = dest_dir
    end

    def destination(dest)
      File.join(dest, @dest_dir, @name)
    end
  end

  class CopyTutorialHtml < Generator
    safe true
    priority :lowest

    def generate(site)
      tutorials = site.collections["tutorials"]
      return unless tutorials&.write?

      remove_auto_discovered_tutorial_files(site)
      add_rendered_tutorial_html(site, tutorials)
    end

    private

    def remove_auto_discovered_tutorial_files(site)
      tutorial_root = File.expand_path("_tutorials", site.source)

      site.static_files.delete_if do |static_file|
        File.expand_path(static_file.path).start_with?(tutorial_root + File::SEPARATOR)
      end
    end

    def add_rendered_tutorial_html(site, tutorials)
      tutorials.docs.each do |doc|
        doc_source_dir = File.dirname(doc.path)
        tutorial_html = File.join(doc_source_dir, "tutorial.html")
        next unless File.file?(tutorial_html)

        # Tutorial collection pages live at /tutorials/.../index/, but the
        # iframe expects tutorial.html one directory above that rendered page.
        doc_url_dir = doc.url.sub(%r{^/}, "").sub(%r{/$}, "")
        dest_dir = File.dirname(doc_url_dir)

        site.static_files << TutorialHtmlFile.new(
          site,
          doc_source_dir,
          "",
          "tutorial.html",
          dest_dir
        )
      end
    end
  end
end
