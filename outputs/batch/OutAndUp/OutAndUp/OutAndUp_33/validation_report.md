# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_33`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 37 |
| Player Tracks | 37 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 123 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 36: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [23–26], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=27.
> - Action 'Action_None' range [23-86] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-92] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-242] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-215] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-220] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-269] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-90] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-105] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [107-117] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [130-132] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-104] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-216] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-91] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-225] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [232-250] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-149] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [154-161] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-196] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-230] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [258-259] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-221] for track '7' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-244] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [258-269] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-180] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-180] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [207-210] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-61] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [65-134] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-228] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-239] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-114] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-184] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [117-127] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [129-215] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-42] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [48-130] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-156] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-163] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [165-231] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-209] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-44] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-71] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-86] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [90-97] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-136] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-121] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [124-232] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-34] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-147] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-211] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [214-215] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [222-223] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-58] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-61] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-174] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-182] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-228] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-245] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-175] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-191] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-202] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-226] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [229-243] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [246-254] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-224] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '29' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-236] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-228] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-245] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [266-267] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-197] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-218] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-210] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-243] for track '34' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [252-254] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '36' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.