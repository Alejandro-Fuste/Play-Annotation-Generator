# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PinAndPull_10`
- **Input XML**: `outputs/batch/PinAndPull/PinAndPull/PinAndPull_10/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PinAndPull.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 21 |
| Player Tracks | 20 |
| Ball Tracks | 1 |
| CSV events parsed | 17 |
| Action Segments inferred | 48 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '13' (C): higher_priority='Action_BallSnap' [128–141], lower_priority='Action_PullLeadBlock' annotated_start=131, effective_Action_PullLeadBlock_start=142.
> - Action 'Action_None' range [128-161] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-195] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-239] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [131-197] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [202-211] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-219] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [222-238] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-203] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [216-217] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-239] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PullLeadBlock' range [142-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-222] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-239] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-83] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [38-127] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-159] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-239] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-220] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [228-239] for track '20' has 2 frames without a visible bounding box.
> - Player track '17' has undefined position. Will map to Position_Unknown.
> - Player track '17' has undefined team_side. Will map to Team_Unknown.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
> - Player track '19' has undefined position. Will map to Position_Unknown.
> - Player track '19' has undefined team_side. Will map to Team_Unknown.
> - Player track '20' has undefined position. Will map to Position_Unknown.
> - Player track '20' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.