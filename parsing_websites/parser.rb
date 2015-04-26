require 'nokogiri'
require 'restclient'
require 'web-page-parser'

# for console output only
require 'colorize'

require_relative 'utility_helper'
require_relative 'site_helpers/reuters_helper'
require_relative 'site_helpers/cnn_helper'
require_relative 'site_helpers/nytimes_helper'
require_relative 'site_helpers/washpost_helper'

time_start = Time.now

# PROVIDE MAIN CIRCA URL HERE
#BASE_URL = 'http://circanews.com/news/statue-of-liberty-security-incident'

# CONSTANTS
REUTERS_MATCH = "www.reuters.com"
CNN_MATCH = "cnn.com"
NYTIMES_MATCH = "www.nytimes.com" # does not parse www.nytimes.com/interactive
WASHPOST_MATCH = "www.washingtonpost.com"
#DIR_NAME = BASE_URL.split("/").last.strip.gsub!("-", "_")
#FILE_NAME = DIR_NAME + "/" + "story.txt"
TEXTS = []
SOURCE_URLS = []

# MAIN
begin
	puts ''
	puts '**************************'
	puts 'starting...'.colorize(:green)
	print 'enter url:'
	BASE_URL = gets.chomp
	DIR_NAME = "../sources/" + BASE_URL.split("/").last.strip.gsub!("-", "_")
	FILE_NAME = DIR_NAME + "/" + "story.txt"
	create_directory(DIR_NAME)
	puts ''
	puts 'obtaining circa page...'
	begin
		circa_page = Nokogiri::HTML(RestClient.get(BASE_URL))
	rescue Exception => e_page
		puts e_page
		puts '...failed to obtain circa page!'.colorize(:red)
	end
	puts '...done'
	puts ''
	# GETTING HEADLINES
	puts 'obtaining circa news headline...'
	TEXTS.push(obtain_general_headline(circa_page, "h1#hero-unit-title"))
	puts '...done'
	puts ''
	# GETTING ARTICLE TEXTS
	puts 'obtaining texts...'
	begin
		paras = circa_page.css("div#permalink-points p")
		paras.each do |para|
			if para["class"] == "quote point-comment"
				para.at_css("small").remove
				TEXTS.push('"' + para.text.strip + '"')
			else
				TEXTS.push(para.text.strip)
			end
		end
	rescue Exception => e_texts
		puts e_texts
		puts '...failed to obtain texts!'.colorize(:red)
	end
	puts '...done'
	puts ''
	# GETTING SOURCE URLS
	puts 'obtaining source urls...'
	sources = circa_page.css("div.citation-list ul li")
	begin
		sources.map do |link|
			this_link = link.css("a").text
			SOURCE_URLS.push(this_link) unless this_link.empty?
		end
	rescue Exception => e_sources
		puts e_sources
		puts '...failed while obtaining source urls from circa!'.colorize(:red)
	end
	puts SOURCE_URLS.length.to_s + ' sources found'.colorize(:green)
	puts '...done'
	puts ''
	puts 'writing circa text to file...'
	write_to_file(FILE_NAME, TEXTS)
	puts "...done"
	puts ''
	puts 'checking and writing sources...'
	source_number = 0
	begin
		SOURCE_URLS.each do |source|
			source_number += 1
			if source.match(REUTERS_MATCH)
				puts '...found reuters as a source...'.colorize(:blue)
				reuters_text = Reuters.resolve_page(source)
				puts ''
				puts 'writing reuters text to file...'
				write_to_file(get_source_filename(DIR_NAME, source_number), reuters_text)
				puts '...done'
				puts ''
			elsif source.match(CNN_MATCH)
				puts '...found cnn as a source...'.colorize(:blue)
				cnn_text = Cnn.resolve_page(source)
				puts ''
				puts 'writing cnn text to file...'
				write_to_file(get_source_filename(DIR_NAME, source_number), cnn_text)
				puts '...done'
				puts ''
			elsif source.match(NYTIMES_MATCH)
				puts '...found nytimes as a source...'.colorize(:blue)
				nytimes_text = Nytimes.resolve_page(source)
				puts ''
				puts 'writing nytimes text to file...'
				write_to_file(get_source_filename(DIR_NAME, source_number), nytimes_text)
				puts '...done'
				puts ''
			end
		end
	rescue Exception => e_source_check
		puts e_source_check
		puts '...failed while checking sources!'.colorize(:red)
	end
	puts '...done'
	puts ''
	puts '...ending'.colorize(:green)
	time_end = Time.now
	puts 'that took ' + time_elapsed(time_start, time_end).to_s + ' seconds'
	puts ''
	puts '**************************'
	puts ''
rescue Exception => e_main
	puts ''
	puts e_main
	puts 'catastrophic failure!'.colorize(:red)
	puts ''
end
