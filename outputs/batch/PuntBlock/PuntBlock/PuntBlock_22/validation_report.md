# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `PuntBlock_22`
- **Input XML**: `outputs/batch/PuntBlock/PuntBlock/PuntBlock_22/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/PuntBlock.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 32 |
| Player Tracks | 32 |
| Ball Tracks | 0 |
| CSV events parsed | 15 |
| Action Segments inferred | 67 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 46: Duplicate assignment for track ID '1' in grid. Overwriting previous assignment.
> - Row 46: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
> - Action 'Action_None' range [25-82] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-278] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-119] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-256] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [25-187] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [191-298] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-251] for track '7' has 2 frames without a visible bounding box.
> - Action 'Action_SecureRecovery' range [252-254] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-253] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-235] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-57] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [75-76] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [78-275] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-53] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [56-296] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [25-98] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [51-52] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [79-82] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [79-99] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [92-98] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [93-94] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [103-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [205-206] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [237-238] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-260] for track '31' has 1 frames without a visible bounding box.
> - Player track '14' has undefined position. Will map to Position_Unknown.
> - Player track '14' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.