# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_64`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_64/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 107 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [60–66], lower_priority='Action_PassBlock' annotated_start=63, effective_Action_PassBlock_start=67.
> - Action 'Action_BallCarry' range [189-230] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [233-249] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [252-259] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-257] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-291] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [60-185] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-125] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-223] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-229] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-249] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-283] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [287-297] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-194] for track '5' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-149] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [313-314] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-302] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [308-322] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-220] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-75] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-314] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-166] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [169-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-229] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-179] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [189-197] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [201-329] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-161] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-220] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-329] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-91] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [99-102] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-134] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [60-80] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-94] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-247] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [249-329] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-182] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-259] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-80] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [90-95] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [97-98] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [143-145] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-78] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [81-84] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [86-110] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [113-118] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-77] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-19] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-183] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-272] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [190-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-281] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-203] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-230] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-299] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [233-255] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [242-243] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-255] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-261] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [265-267] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [271-291] for track '32' has 1 frames without a visible bounding box.
> - Player track '6' has undefined position. Will map to Position_Unknown.
> - Player track '6' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.