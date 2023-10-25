import os
from organizer_modules import select_folder
from organizer_modules import categories


def count_files(src_path):
    count = {}

    for c in categories:
        if not os.path.exists(src_path + "/" + c):
            continue
        count.update({c: {"count": 0, "size": 0}})
        count[c]["size"] = os.path.getsize(src_path + "/" + c)
        for item in os.listdir(src_path + "/" + c):
            item_path = src_path + "/" + c + "/" + item
            if os.path.isfile(item_path):
                count[c]["count"] += 1
            elif os.path.isdir(item_path):
                count["FOLDER"]["count"] += 1
    # order by count

    count = dict(sorted(count.items(), key=lambda items: items[1]["count"], reverse=True))
    # Add total count
    # count = {"**TOTAL**": {"count": sum([v["count"] for k, v in count.items()])}, **count}
    return count


if __name__ == "__main__":
    counted = count_files(select_folder())
    for k, v in counted.items():
        print(f"{k:<10}: {v['count']:<7} files, {v['size'] / 1000000 } MB")
    input("Press Enter to continue...")
