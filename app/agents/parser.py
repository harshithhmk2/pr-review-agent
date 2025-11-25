from unidiff import PatchSet

def parse_unified_diff(diff_text: str):
    patch = PatchSet(diff_text.splitlines(True))
    files = []

    for file in patch:
        file_data = {
            "path": file.path,
            "hunks": []
        }

        for hunk in file:
            changes = []
            for line in hunk:
                changes.append({
                    "type": "+" if line.is_added else "-" if line.is_removed else " ",
                    "content": line.value.strip(),
                })

            file_data["hunks"].append({
                "new_start": hunk.target_start,
                "changes": changes
            })

        files.append(file_data)

    return files
