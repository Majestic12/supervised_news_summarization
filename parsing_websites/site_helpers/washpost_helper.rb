module Washpost
  def Washpost.resolve_page(site)
    washpost_text = []
    puts 'obtaining washington post page...'
    begin
      page = WebPageParser::WashingtonPostPageParserV1.new(:url => site)
      puts 'obtaining washington post headlines...'
      headline = page.title.strip
      headline.concat(".") unless headline.end_with?(".", "?", "!", "\"", "\'")
      washpost_text.push(headline)
      puts headline
      puts if headline.empty? ? '...failed obtaining washington post headline!'.colorize(:red) : '...done'
      puts 'obtaining washington post texts...'
      washpost_text.push(page.content)
      puts page.content
      puts '...done'
    rescue Exception => e_washpost_page
      puts e_washpost_page
      puts '...failed obtaining or parsing washington post page!'.colorize(:red)
    end
    puts '...done'
    return washpost_text
  end
end
