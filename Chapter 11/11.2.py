from string import Template

t = Template('${village} folk send $$10 to $cause')
tstr = t.substitute(village = 'Nottingham', cause = 'the ditch fund')
print(tstr)

# safe_substitute() will leave placeholders unchanged if data is missing
t2 = Template('Return the $item to $owner')
t2str = t2.safe_substitute({'item': 'unladen swallow'})
print(t2str)