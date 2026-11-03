# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Post10to15_35`
- **Input XML**: `outputs/batch/Post10to15/Post10to15/Post10to15_35/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Post10to15.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 143 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 38: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [20–35], lower_priority='Action_PassBlock' annotated_start=23, effective_Action_PassBlock_start=36.
> - Action 'Action_None' range [20-83] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-121] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-159] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-165] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-171] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-180] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [184-186] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-210] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [35-58] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [60-62] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [65-68] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [70-72] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunPostRoute' range [80-116] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-80] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-109] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-120] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-151] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-178] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [182-210] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-171] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-184] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-196] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-210] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-42] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [45-48] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-171] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [183-189] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-169] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-175] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-48] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-64] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-147] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-210] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-175] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [36-48] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-70] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [72-80] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-102] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-116] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-49] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [51-80] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [82-86] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [91-105] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-115] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [122-210] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-42] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [45-46] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-84] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-108] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-210] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-46] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [20-42] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [45-49] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-80] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-42] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [20-88] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-37] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-102] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-105] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [107-130] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-136] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-47] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-80] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [89-101] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [135-136] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [146-150] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [153-210] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [56-76] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-138] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-175] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-188] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-210] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-91] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-101] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-82] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [87-101] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-120] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-125] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-124] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-210] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [108-126] for track '26' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [133-137] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [139-159] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-178] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-198] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-210] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-210] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [143-157] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-175] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-210] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-153] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-210] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-204] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-210] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-196] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-200] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-210] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-210] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-194] for track '37' has 1 frames without a visible bounding box.
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
> - Player track '29' has undefined position. Will map to Position_Unknown.
> - Player track '29' has undefined team_side. Will map to Team_Unknown.
> - Player track '30' has undefined position. Will map to Position_Unknown.
> - Player track '30' has undefined team_side. Will map to Team_Unknown.
> - Player track '31' has undefined position. Will map to Position_Unknown.
> - Player track '31' has undefined team_side. Will map to Team_Unknown.
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.
> - Player track '36' has undefined position. Will map to Position_Unknown.
> - Player track '36' has undefined team_side. Will map to Team_Unknown.
> - Player track '37' has undefined position. Will map to Position_Unknown.
> - Player track '37' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.