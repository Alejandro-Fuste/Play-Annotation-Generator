# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Draw_2`
- **Input XML**: `outputs/batch/Draw/Draw/Draw_2/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Draw.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 40 |
| Player Tracks | 39 |
| Ball Tracks | 1 |
| CSV events parsed | 18 |
| Action Segments inferred | 86 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [57–67], lower_priority='Action_PassBlock' annotated_start=60, effective_Action_PassBlock_start=68.
> - Action 'Action_None' range [57-205] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '1' starts at frame 148, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [148-148] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-75] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-32] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-147] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-220] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-238] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-50] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' for track '4' starts at frame 148, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [148-148] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-162] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-56] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [102-164] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [166-214] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-132] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-114] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-68] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [70-75] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-186] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-44] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-64] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-34] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [39-40] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [52-56] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [68-74] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-122] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-259] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [2-5] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-59] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [63-90] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [83-162] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [164-168] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-191] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-138] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-193] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-215] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-214] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [223-262] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [175-255] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-224] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-204] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-244] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-207] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-226] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [230-234] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [243-269] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-214] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-233] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-223] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-226] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-269] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-223] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-258] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [263-269] for track '35' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '39' has undefined position. Will map to Position_Unknown.
> - Player track '39' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.