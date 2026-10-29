# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_99`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_99/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 35 |
| Player Tracks | 35 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 117 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 102: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - Row 102: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [4–26], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=27.
> - Action 'Action_RunDeepCrossRoute' range [26-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-190] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-214] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-82] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-239] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-168] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-185] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-193] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-155] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-173] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-160] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-145] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-152] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-169] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [173-179] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-139] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-155] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-160] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-168] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-84] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-155] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-169] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [172-185] for track '10' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [190-191] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-223] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-73] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-205] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [27-31] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-169] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [171-226] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [231-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-237] for track '13' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [4-235] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [4-47] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-155] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [157-193] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [214-223] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [230-233] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-187] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-21] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [23-35] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-44] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [4-56] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [58-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-218] for track '20' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [220-221] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-235] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-53] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [58-103] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [105-107] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [110-239] for track '21' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [52-57] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [52-143] for track '23' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [88-89] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-155] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [157-185] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-239] for track '25' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [91-152] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-222] for track '26' has 6 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-178] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [182-183] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [185-239] for track '28' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-179] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-185] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-234] for track '30' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [181-193] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-205] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-214] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-225] for track '31' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [230-239] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-205] for track '32' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [218-235] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-217] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-231] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-234] for track '34' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '7' has undefined position. Will map to Position_Unknown.
> - Player track '7' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.