require 'watir-webdriver'
require 'colorize'

browser = nil

Given(/^A web calculator$/) do
    browser = Watir::Browser.new
    browser.goto 'http://127.0.0.1:5000'
    browser.send_keys :f11
end

When(/^enter (\d+) \+ (\d+)$/) do |arg1, arg2|
    browser.div(:id, 'btn-' + arg1).click
    sleep(1)
    browser.div(:id, 'btn-add').click
    sleep(1)
    browser.div(:id, 'btn-' + arg2).click
    sleep(1)
    browser.div(:id, 'btn-equal').click
    sleep(1)
end

Then(/^get the result is (\d+)$/) do |arg1|
    result_int = browser.span(:id => 'result-int').text
    expect(result_int).to eq arg1
    browser.close
end



Given(/^A web calculator again$/) do
    browser = Watir::Browser.new    
    browser.goto 'http://127.0.0.1:5000'
    browser.send_keys :f11
end

When(/^enter <augend> \+ <addend>$/) do |table|
    table.hashes.each do |record|
        record[:augend].split('') do |char|
            browser.div(:id, 'btn-' + char).click
            sleep(1)
        end
        
        browser.div(:id, 'btn-add').click
        sleep(1)

        record[:addend].split('') do |char|
            browser.div(:id, 'btn-' + char).click
            sleep(1)
        end

        browser.div(:id, 'btn-equal').click
        sleep(1)
    end
end

Then(/^get the sum is <sum>$/) do |table|
    expect(browser.span(:id => 'result-int').text).to eq table.hashes()[0][:sum]
    browser.close
end