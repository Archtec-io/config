# Reads the config file and removes key, tokens, URLs, etc.
# Use: python cleanconfig.py /home/user/minetest.conf /home/user/cleanconfig.conf
# (C) 2023 Niklp, MIT License

import sys

inpath = sys.argv[1]
outpath = sys.argv[2]

print("Inputpath: " + inpath)
print("Outputpath: " + outpath)

infile = open(inpath, "r")
inlines = infile.readlines()

outfile = open(outpath, "w")
outtext = ""

for line in inlines:
	split = line.split("=", 1)

	if line == "\n" * len(line):
		outtext += line
		continue

	outtext += split[0]

	if len(split) > 1:
		idx_1 = line.find("token")
		idx_2 = line.find("key")
		idx_3 = line.find("url")
		idx_4 = line.find("seed")

		if idx_1 > 0 or idx_2 > 0 or idx_3 > 0 or idx_4 > 0:
			outtext += "=" + "" + "\n"
		else:
			outtext += "=" + split[1]

# change some values by hand
outtext += "\n" + "# CHANGED FOR GITHUB ACTIONS!" + "\n"
outtext += "port =" + "\n"
outtext += "secure.http_mods =" + "\n"
outtext += "server_announce = false" + "\n"

outfile.write(outtext)

infile.close()
outfile.close()

print("DONE")
