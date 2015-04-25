module Cnn
  def Cnn.resolve_page(site)
    cnn_text = []
    puts 'obtaining cnn page...'
    begin
      page = Nokogiri::HTML(RestClient.get(site))
      Cnn.get_headline(page, cnn_text)
      Cnn.get_texts(page, cnn_text)
    rescue Exception => e_cnn_page
      puts e_cnn_page
      puts '...failed obtaining cnn page!'.colorize(:red)
    end
    puts '...done'
    return cnn_text
  end

  private
  def Cnn.get_headline(page, cnn_text)
    puts 'obtaining cnn headlines...'
    cnn_text.push(obtain_general_headline(page, "h1.pg-headline"))
    puts '...done'
  end

  private
  def Cnn.get_texts(page, cnn_text)
    puts 'obtaining cnn texts...'
    begin
      page.css("p.zn-body__paragraph").each do |para|
        if para.css("cite")[0] && para.css("cite")[0]["class"] == "el-editorial-source"
          para.css("cite.el-editorial-source").remove
          cnn_text.push(para.text.strip)
        elsif para["class"] == "zn-body__paragraph zn-body__footer"
          #skip
        else
          text = para.text.strip
          if text.end_with?(".", "!", "?", "\"", "\'")
            cnn_text.push(text) unless text.empty?
          end
        end
      end
    rescue Exception => e_cnn_texts
      puts e_cnn_texts
      puts '...failed obtaining cnn texts'.colorize(:red)
    end
    puts '...done'
  end
end
