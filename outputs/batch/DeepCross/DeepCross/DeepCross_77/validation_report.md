# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `DeepCross_77`
- **Input XML**: `outputs/batch/DeepCross/DeepCross/DeepCross_77/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/DeepCross.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 42 |
| Player Tracks | 42 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 120 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 80: Duplicate assignment for track ID '0' in grid. Overwriting previous assignment.
> - Row 80: Duplicate assignment for track ID '9' in grid. Overwriting previous assignment.
> - Row 80: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '15' (C): higher_priority='Action_BallSnap' [11–23], lower_priority='Action_PassBlock' annotated_start=14, effective_Action_PassBlock_start=24.
> - Action 'Action_RunDeepCrossRoute' range [23-226] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-246] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-249] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [251-261] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-157] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-164] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-227] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-181] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-231] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-227] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-118] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-143] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-159] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-198] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [205-216] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-254] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [260-267] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-97] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [100-227] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [166-198] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [204-234] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-117] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-159] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [161-162] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-183] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-206] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-209] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-231] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-227] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [11-156] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-62] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [68-99] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [102-269] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-227] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [24-39] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [41-90] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [95-113] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [152-155] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-208] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-97] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-171] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [175-214] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [217-227] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-246] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-260] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-151] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [11-227] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-42] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [60-62] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [64-72] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [75-232] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [14-227] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [72-74] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-128] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-157] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [161-165] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [172-175] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [177-227] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [238-257] for track '25' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [260-265] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [188-227] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-227] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-269] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-251] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [253-257] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [260-266] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-248] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [254-255] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-232] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-242] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-267] for track '34' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-251] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-269] for track '36' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-269] for track '37' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [241-242] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [255-260] for track '38' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [245-250] for track '39' has 1 frames without a visible bounding box.
> - Player track '10' has undefined position. Will map to Position_Unknown.
> - Player track '10' has undefined team_side. Will map to Team_Unknown.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
> - Player track '16' has undefined position. Will map to Position_Unknown.
> - Player track '16' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.