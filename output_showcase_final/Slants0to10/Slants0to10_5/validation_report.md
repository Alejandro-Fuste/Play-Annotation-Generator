# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Slants0to10_5`
- **Input XML**: `output_showcase_final/Slants0to10/Slants0to10_5/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Slants0to10.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 5: Duplicate assignment for track ID '15' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [1–9], lower_priority='Action_PassBlock' annotated_start=4, effective_Action_PassBlock_start=10.
> - Segment 'Action_PassBlock' for track '15' has invalid range: start=4, end=0. Clamping end to start.
> - Action 'Action_None' range [1-239] for track '0' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [1-41] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [44-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [85-154] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [159-209] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-154] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-98] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-85] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [1-62] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-216] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-51] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-68] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [10-37] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [103-105] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-159] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [57-97] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [1-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [4-48] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [54-100] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [102-103] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [46-103] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [155-156] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-163] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '26' has 1 frames without a visible bounding box.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
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
> - Play definition: no definition found for 'Play_Pass_Slants0to10'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.