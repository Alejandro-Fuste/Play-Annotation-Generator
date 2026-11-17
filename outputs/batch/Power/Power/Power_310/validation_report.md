# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `Power_310`
- **Input XML**: `outputs/batch/Power/Power/Power_310/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/Power.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 25 |
| Player Tracks | 25 |
| Ball Tracks | 0 |
| CSV events parsed | 9 |
| Action Segments inferred | 47 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 619: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - Row 620: Duplicate assignment for track ID '12' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Action 'Action_PreSnap' range [22-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-135] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-234] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-103] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-101] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [104-132] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-83] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-89] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [91-94] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [84-91] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PullBlock' range [97-104] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-220] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [22-104] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [106-171] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [182-183] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-86] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [88-239] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_DownBlock' range [84-85] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [141-142] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [148-166] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [157-160] for track '19' has 1 frames without a visible bounding box.
> - Player track '1' has undefined position. Will map to Position_Unknown.
> - Player track '1' has undefined team_side. Will map to Team_Unknown.
> - Player track '2' has undefined position. Will map to Position_Unknown.
> - Player track '2' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.