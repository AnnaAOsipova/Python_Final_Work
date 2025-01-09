from checkers import checkout
import logging
import yaml

with open("testdata.yaml") as f:
    data = yaml.safe_load(f)

def test_step5():
    logging.info("Test5 Started")
    assert checkout(f"cd ~; nikto -h {data['address']} -ssl -Tuning 4", "0 error(s)"), "Test 1 FAIL"
    logging.info("Site checking complete")