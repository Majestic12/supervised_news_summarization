module Reuters
  def Reuters.resolve_page(site)
    reuters_text = []
    puts 'obtaining reuters page...'
    begin
      page = Nokogiri::HTML(RestClient.get(site))
      Reuters.get_headline(page, reuters_text)
      Reuters.get_texts(page, reuters_text)
    rescue Exception => e_reuters_page
      puts e_reuters_page
      puts '...failed obtaining reuters page!'.colorize(:red)
    end
    puts '...done'
    return reuters_text
  end

  private
  def Reuters.get_headline(page, reuters_text)
    puts 'obtaining reuters headlines...'
    reuters_text.push(obtain_general_headline(page, "h1.article-headline"))
    puts '...done'
  end

  private
  def Reuters.get_texts(page, reuters_text)
    puts 'obtaining reuters texts...'
    begin
      page.css("span#articleText p").each do |para|
        if para.css("span")[0] && para.css("span")[0]["class"] == "articleLocation"
          para.css("span.articleLocation").remove
          text = para.text.strip
          reuters_text.push(text.sub("(Reuters) - ", "")) unless text.empty?
        else
          text = para.text.strip
          if text.end_with?(".", "!", "?", "\"", "\'")
            reuters_text.push(text) unless text.empty?
          end
        end
      end
    rescue Exception => e_reuters_texts
      puts e_reuters_texts
      puts '...failed obtaining reuters texts'.colorize(:red)
    end
    puts '...done'
  end
end
