source "https://rubygems.org"

# Keep local/CI builds aligned with the dependency set supported by GitHub Pages.
gem "github-pages", "~> 232", group: :jekyll_plugins

group :jekyll_plugins do
  gem "jekyll-feed"
  gem "jemoji"
  gem "jekyll-gist"
  gem "jekyll-algolia"
  gem "jekyll-sitemap"
  gem "jekyll-seo-tag"
  gem "jekyll-seo"
end

# Windows and JRuby do not include zoneinfo files.
platforms :mingw, :x64_mingw, :mswin, :jruby do
  gem "tzinfo"
  gem "tzinfo-data"
end

# Performance booster for watching directories on Windows.
gem "wdm", "~> 0.1.1", platforms: [:mingw, :x64_mingw, :mswin]

# Use the released gem rather than executing dependency code from a Git tag.
gem "eventmachine", "~> 1.2.7"

gem "webrick"
gem "jekyll-admin", group: :jekyll_plugins
gem "DevSculptor", "~> 1.0"
gem "jekyll-remote-theme", "~> 0.4.3"
