# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_33`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_33/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 115 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 35: Duplicate assignment for track ID '2' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '16' (C): higher_priority='Action_BallSnap' [23–39], lower_priority='Action_PassBlock' annotated_start=26, effective_Action_PassBlock_start=40.
> - Action 'Action_None' range [23-151] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-162] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-209] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-213] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-129] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-150] for track '3' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [155-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-169] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [184-195] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-201] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-206] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-236] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [185-194] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-195] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-77] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-239] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-174] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [177-183] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-150] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [154-187] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-132] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [23-202] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-235] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [127-170] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-239] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-58] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [61-66] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [23-239] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-81] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [85-150] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [155-162] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [167-169] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [185-186] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [189-195] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [204-206] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [210-211] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [219-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-61] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [66-97] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [104-106] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-206] for track '19' has 4 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [215-239] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [26-73] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [37-39] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [40-97] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-239] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [43-83] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-95] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-79] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [87-88] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [91-92] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-115] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [117-151] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-165] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [167-209] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [78-79] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-106] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-147] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-151] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-192] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [137-165] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '27' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [198-205] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-202] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [204-219] for track '28' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [205-208] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-239] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-232] for track '31' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.