# apptainer-examples
Example app that outputs dice rolls in a json file.

1. `cp ./.env.example ./.env`
2. Change .env file to your liking (seed empty if fully random)
3. `apptainer build --sandbox ./sandbox ./instructions.def`
4. `apptainer run --bind ./results:/mnt -C --no-home --writable ./sandbox 10 /mnt/results.json`