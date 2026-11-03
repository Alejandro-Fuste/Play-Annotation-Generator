# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_60`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_60/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 55 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 122: Duplicate assignment for track ID '8' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_PuntBall' range [60-150] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [60-125] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-119] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-142] for track '9' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [77-150] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-150] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [2-138] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-132] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [2-60] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [62-64] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [73-140] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-111] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-127] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-150] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [128-130] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [134-142] for track '26' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [144-145] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-150] for track '26' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.