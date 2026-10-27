# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Counter_333`
- **Input XML**: `outputs/batch/Counter/Counter/Counter_333/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Counter.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 38 |
| Player Tracks | 38 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 113 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 668: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_DownBlock' for track '17' (RT) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
> - Validation warning: Action 'Action_PullBlock' for track '20' (C) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [144–160], lower_priority='Action_PullBlock' annotated_start=147, effective_Action_PullBlock_start=161.
> - Validation warning: Action 'Action_DownBlock' for track '21' (RG) duration 97 frames exceeds threshold 90 frames [start=147, end=243].
> - Action 'Action_PullLeadBlock' range [147-221] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [224-243] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [244-249] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-259] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [261-321] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-329] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [194-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-242] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-321] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-177] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-216] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-225] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-187] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-175] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [177-181] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-190] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-208] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [210-311] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-291] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-244] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-254] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-261] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-302] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-179] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-329] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-171] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [175-196] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [198-199] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [201-243] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-265] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-286] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '19' starts at frame 144, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [144-144] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-268] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-309] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [144-160] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [165-166] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [232-236] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-259] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [265-266] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [268-271] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [147-195] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [197-233] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [236-237] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [244-250] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-256] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [81-90] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-164] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-174] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [179-185] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-184] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-221] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-224] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-232] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-237] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-329] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-264] for track '28' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [262-263] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-295] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [309-317] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-324] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [273-288] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [307-329] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [320-325] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-327] for track '37' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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