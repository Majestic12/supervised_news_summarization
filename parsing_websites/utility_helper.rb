# in seconds
def time_elapsed(start, finish)
  (finish - start)
end

def write_to_file(file_name, file_text)
  puts 'writing text to file...'
	begin
		text_file = File.open(file_name, "w")
		file_text.each{ |text| text_file.puts text }
		text_file.close
	rescue Exception => e_file_write
		puts e_file_write
		puts "...failed to write text to file!".colorize(:red)
	end
  puts '...done'
end

def create_directory(dir_name)
  puts 'creating directory if it does not already exist...'
  begin
		Dir.mkdir(dir_name) unless File.exists?(dir_name)
	rescue Exception => e_dir
		puts e_dir
		puts "...failed to create directory!".colorize(:red)
	end
  puts '...done'
end

def obtain_general_headline(page, css_tag)
  puts 'obtaining general news headline...'
	begin
		headline = page.css(css_tag).text.strip
		headline.concat(".") unless headline.end_with?(".", "?", "!", "\"", "\'")
    puts '...no headline found!' if headline.empty?
	rescue Exception => e_headline
		puts e_headline
		puts '...failed to obtain general headline!'.colorize(:red)
	end
	puts '...done'
  return headline
end

def get_source_filename(dir_name, source_number)
  return DIR_NAME + "/doc_" + source_number.to_s + ".txt"
end
