import sublist3r 
from typing import Optional

from fastapi import APIRouter

router = APIRouter()

@router.post("/find/")
async def find_subdomains(domain="google.com", threads: int = 40, ports=None, silent=True, verbose=False, enable_bruteforce=False, engines=None):
	subdomains = sublist3r.main(domain=domain, threads=threads, savefile=None, ports=ports, silent=silent, verbose=verbose, enable_bruteforce=enable_bruteforce, engines=engines)
	return {"data": subdomains}
