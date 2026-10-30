# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `FieldGoalBlock_50`
- **Input XML**: `outputs/batch/FieldGoalBlock/FieldGoalBlock/FieldGoalBlock_50/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/FieldGoalBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 97 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_None' range [18-45] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-61] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [69-150] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-60] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-68] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-107] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-48] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-51] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-61] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-95] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [113-115] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-122] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [125-128] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [64-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-98] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-119] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-148] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-61] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [68-78] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-82] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-93] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [47-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-150] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-133] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [18-48] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-57] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_BlockKick' range [63-72] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-150] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-69] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [125-127] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-28] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-41] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-61] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [66-78] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [80-81] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-59] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [107-110] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' for track '17' starts at frame 18, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [18-18] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-17] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [18-20] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [18-19] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [26-37] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-44] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-83] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-109] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [29-40] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-56] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-135] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-84] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-129] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-137] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-150] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-105] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-148] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [102-147] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-123] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-147] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-150] for track '28' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.
> - Player track '21' has undefined position. Will map to Position_Unknown.
> - Player track '21' has undefined team_side. Will map to Team_Unknown.
> - Player track '22' has undefined position. Will map to Position_Unknown.
> - Player track '22' has undefined team_side. Will map to Team_Unknown.
> - Player track '23' has undefined position. Will map to Position_Unknown.
> - Player track '23' has undefined team_side. Will map to Team_Unknown.
> - Player track '24' has undefined position. Will map to Position_Unknown.
> - Player track '24' has undefined team_side. Will map to Team_Unknown.
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.