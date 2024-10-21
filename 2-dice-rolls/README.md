# apptainer-examples
Example app that outputs dice rolls in a json file.

1. `cp ./.env.example ./.env`
2. Change .env file to your liking (seed empty if fully random)
3. `apptainer build ./image.sif ./instructions.def`
4. `apptainer run --bind ./results:/mnt -C --no-home ./image.sif 10 /mnt/results.json`