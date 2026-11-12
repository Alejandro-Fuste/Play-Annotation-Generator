# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_73`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_73/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 72 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '2' (C) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
> - Resolved action overlap for track '2' (C): higher_priority='Action_BallSnap' [124–141], lower_priority='Action_ZoneBlock' annotated_start=129, effective_Action_ZoneBlock_start=142.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (RT) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (LG) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LT) duration 98 frames exceeds threshold 90 frames [start=129, end=226].
> - Action 'Action_None' range [227-258] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [142-192] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [194-196] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [198-200] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-207] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-299] for track '4' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-215] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [220-299] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-299] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-290] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-248] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-226] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [227-290] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-285] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-219] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-175] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-179] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-156] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-226] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-219] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-234] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-161] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-199] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-236] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [249-250] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [256-257] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [275-276] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [280-282] for track '26' has 1 frames without a visible bounding box.
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