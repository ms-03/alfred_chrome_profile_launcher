import os
import json
import pdb

def main():
    chrome_state_file = os.environ['HOME'] + "/Library/Application Support/Google/Chrome/Local State"
    json_data = json.load(open(chrome_state_file, 'r'))

    res = {"items": [{
		"uid": "SECRET",
		"title": "SECRET",
		"subtitle": "Google Chrome Profile",
		"arg": "SECRET",
		"autocomplete": "SECRET",
    }]}
    for v in json_data["profile"]["info_cache"].values():
        profile = v["gaia_given_name"] if v["is_using_default_name"] else v["name"]
        res["items"].append({
    		"uid": profile,
    		"title": profile,
    		"subtitle": "Google Chrome Profile",
    		"arg": profile,
    		"autocomplete": profile,
        })
    print("{}".format(json.dumps(res,indent=4)))

if __name__=='__main__':
    main()
