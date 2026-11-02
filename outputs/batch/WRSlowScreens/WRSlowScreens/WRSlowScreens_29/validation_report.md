# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `WRSlowScreens_29`
- **Input XML**: `outputs/batch/WRSlowScreens/WRSlowScreens/WRSlowScreens_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/WRSlowScreens.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 77 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Action 'Action_None' range [17-154] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-299] for track '1' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [17-65] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [67-68] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-178] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-88] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-298] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-105] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-215] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_RunAfterCatch' range [131-291] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [17-173] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-293] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-292] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-120] for track '18' has 3 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [20-64] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [67-70] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PassBlock' range [73-299] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [48-191] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_ReleaseToScreen' range [193-208] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [43-46] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [122-123] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [130-143] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [148-150] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-176] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [180-181] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-203] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-211] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [222-225] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [240-241] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [152-299] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [216-217] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [290-291] for track '28' has 1 frames without a visible bounding box.
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
> - Play definition: no definition found for 'Play_Pass_WRSlowScreens'.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.