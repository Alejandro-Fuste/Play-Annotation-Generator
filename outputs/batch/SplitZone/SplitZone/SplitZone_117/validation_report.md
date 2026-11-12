# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_117`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_117/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 23 |
| Action Segments inferred | 73 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '11' (C) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [126–143], lower_priority='Action_ZoneBlock' annotated_start=129, effective_Action_ZoneBlock_start=144.
> - Validation warning: Action 'Action_ZoneBlock' for track '19' (RG) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
> - Validation warning: Action 'Action_ZoneBlock' for track '20' (RT) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
> - Validation warning: Action 'Action_ZoneBlock' for track '21' (LG) duration 111 frames exceeds threshold 90 frames [start=129, end=239].
> - Action 'Action_None' range [126-290] for track '1' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [126-184] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-150] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-158] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-308] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-184] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [144-158] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [160-161] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [164-306] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [308-323] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [126-284] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-221] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-292] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-202] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-324] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-239] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [129-206] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [209-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [25-29] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [187-188] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [202-238] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-253] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-317] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [319-323] for track '26' has 2 frames without a visible bounding box.
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