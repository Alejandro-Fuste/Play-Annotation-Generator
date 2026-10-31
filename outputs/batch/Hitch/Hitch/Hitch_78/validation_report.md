# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Hitch_78`
- **Input XML**: `outputs/batch/Hitch/Hitch/Hitch_78/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Hitch.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 28 |
| Player Tracks | 28 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 64 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Segment 'Action_BallCarry' for track '2' has invalid range: start=153, end=35. Clamping end to start.
> - Resolved action overlap for track '20' (C): higher_priority='Action_BallSnap' [2–16], lower_priority='Action_PassBlock' annotated_start=5, effective_Action_PassBlock_start=17.
> - Action 'Action_None' range [116-178] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_RunHitchRoute' range [22-35] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-59] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [64-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-112] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-205] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-183] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-208] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-93] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [108-206] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-76] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-85] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-210] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-198] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [200-223] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-40] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [53-74] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [93-94] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [98-187] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-194] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [17-35] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [40-198] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [5-197] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [39-210] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-108] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-95] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [100-204] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-144] for track '25' has 1 frames without a visible bounding box.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.