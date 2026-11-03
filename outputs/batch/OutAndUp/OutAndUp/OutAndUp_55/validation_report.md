# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `OutAndUp_55`
- **Input XML**: `outputs/batch/OutAndUp/OutAndUp/OutAndUp_55/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/OutAndUp.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 95 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Segment 'Action_ThrowPass' for track '2' has invalid range: start=117, end=83. Clamping end to start.
> - Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [19–33], lower_priority='Action_PassBlock' annotated_start=22, effective_Action_PassBlock_start=34.
> - Action 'Action_None' range [19-227] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [34-83] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-260] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [92-222] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [225-227] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_RunGoRoute' range [229-261] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-212] for track '6' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [19-98] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-240] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-69] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-184] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-92] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [94-108] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [117-144] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [148-149] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [151-162] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [165-168] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [175-177] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [179-210] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-269] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-156] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-221] for track '12' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [19-68] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-87] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-152] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-206] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [218-222] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [224-225] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-230] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-87] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-98] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-269] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [19-203] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-207] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [34-74] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [19-169] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-266] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-59] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [92-130] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [133-136] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [141-180] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [182-260] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-156] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [158-218] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [220-225] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [231-232] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [22-62] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-91] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [86-87] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-227] for track '23' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [230-235] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [111-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-199] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [206-212] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-216] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [231-240] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [115-119] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-125] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [127-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-203] for track '26' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.