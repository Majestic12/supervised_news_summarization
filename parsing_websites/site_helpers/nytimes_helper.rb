module Nytimes
  def Nytimes.resolve_page(site)
    nytimes_text = []
    puts 'obtaining nytimes page...'
    begin
      page = WebPageParser::NewYorkTimesPageParserV2.new(:url => site)
      puts 'obtaining nytimes headlines...'
      headline = page.title.strip
      headline.concat(".") unless headline.end_with?(".", "?", "!", "\"", "\'")
      nytimes_text.push(headline)
      puts if headline.empty? ? '...failed obtaining nytimes headline!'.colorize(:red) : '...done'
      puts 'obtaining nytimes texts...'
      first_content, *rest_content = *page.content
      nytimes_text.push(first_content.sub(/[A-Z]*\W*\s*[a-z]*\s\W\s+/, ""))
      nytimes_text.push(rest_content)
      puts '...done'
    rescue Exception => e_nytimes_page
      puts e_nytimes_page
      puts '...failed obtaining or parsing nytimes page!'.colorize(:red)
    end
    puts '...done'
    return nytimes_text
  end
end
