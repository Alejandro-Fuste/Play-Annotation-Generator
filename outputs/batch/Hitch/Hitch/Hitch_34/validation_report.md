# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_34`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_34/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 44 |
| Player Tracks | 44 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 145 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [22–37], lower_priority='Action_PassBlock' annotated_start=30, effective_Action_PassBlock_start=38.
> - Action 'Action_None' range [22-54] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [61-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-73] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-109] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [22-57] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-124] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-133] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-48] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-162] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-176] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-202] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-48] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-55] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-88] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-96] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [101-114] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [118-133] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-139] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-42] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [45-196] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [204-210] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [215-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-176] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-204] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-20] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-36] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-47] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [83-86] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-98] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-101] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [147-177] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [22-33] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [38-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [127-129] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-40] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [54-57] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-48] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [22-48] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-90] for track '17' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [92-226] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-238] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [38-51] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [65-67] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-92] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-182] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [114-226] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-29] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [30-63] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [65-68] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [71-75] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [77-89] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [30-39] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [41-42] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-53] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-68] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [71-73] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [55-220] for track '23' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [232-238] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-96] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-104] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [83-92] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [96-110] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-175] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [177-191] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-209] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [119-121] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-134] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [136-140] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-183] for track '27' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [190-193] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-201] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-239] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-138] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [131-133] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-159] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-151] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-157] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [159-179] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [188-198] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-211] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-234] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-172] for track '33' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-220] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-159] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-165] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-193] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-225] for track '37' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-224] for track '38' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-223] for track '39' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-227] for track '40' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '41' has 1 frames without a visible bounding box.
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
> - Player track '38' has undefined position. Will map to Position_Unknown.
> - Player track '38' has undefined team_side. Will map to Team_Unknown.
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.
> - Player track '40' has undefined position. Will map to Position_Unknown.
> - Player track '40' has undefined team_side. Will map to Team_Unknown.
> - Player track '41' has undefined position. Will map to Position_Unknown.
> - Player track '41' has undefined team_side. Will map to Team_Unknown.
> - Player track '42' has undefined position. Will map to Position_Unknown.
> - Player track '42' has undefined team_side. Will map to Team_Unknown.
> - Player track '43' has undefined position. Will map to Position_Unknown.
> - Player track '43' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.