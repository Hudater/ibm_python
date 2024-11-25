# import pytermgui as ptg
# from allFn import *

# CONFIG = """
# config:
#     InputField:
#         styles:
#             prompt: dim italic
#             cursor: '@72'
#     Label:
#         styles:
#             value: dim bold

#     Window:
#         styles:
#             border: '60'
#             corner: '60'

#     Container:
#         styles:
#             border: '96'
#             corner: '96'
# """

# with ptg.YamlLoader() as loader:
#     loader.load(CONFIG)

# with ptg.WindowManager() as manager:
#     window = (
#         ptg.Window(
#             "TUI for assignment 3",
#             ptg.InputField("1", prompt="Enter the serial no of function you want to run: "),
#             "",
#             ["Submit", lambda *_: submit(manager, window)],
#             width=75,

#             box="DOUBLE",
#         )
#         .set_title("[210 bold]Assignment 3")
#         .center()
#     )

#     manager.add(window)

# # calculate_sum()
# # calculate_sum_custom()
# # find_max()
# # find_max_custom()
# # find_min()
# # find_min_custom()