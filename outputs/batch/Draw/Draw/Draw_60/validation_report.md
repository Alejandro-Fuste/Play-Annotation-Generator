# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_60`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 39 |
| Player Tracks | 39 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 100 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 389 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 389 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [50–62], lower_priority='Action_PassBlock' annotated_start=53, effective_Action_PassBlock_start=63.
> - Action 'Action_None' range [50-129] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [132-136] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-186] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-99] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-103] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-173] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-256] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-116] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-174] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-112] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [117-121] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-297] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [300-306] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-180] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-105] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-167] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-167] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [94-146] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [63-71] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [50-188] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [84-88] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [95-99] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [106-110] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-160] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-121] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-174] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [176-192] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-212] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [132-133] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-134] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-201] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [206-367] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [370-375] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [382-384] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-260] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [152-239] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-323] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-332] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [335-389] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-222] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-251] for track '22' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [253-259] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [261-262] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [273-276] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-362] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [364-379] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-242] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-254] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-357] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-333] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [337-341] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-265] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-256] for track '27' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [276-277] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [279-288] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [290-304] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-329] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [345-348] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [353-355] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [383-384] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [291-298] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [303-314] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [299-300] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [317-319] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [343-389] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [351-354] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [378-379] for track '38' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
> - Player track '15' has undefined position. Will map to Position_Unknown.
> - Player track '15' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.