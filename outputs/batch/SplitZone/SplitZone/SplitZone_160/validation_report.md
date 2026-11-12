# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_160`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_160/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 23 |
| Player Tracks | 23 |
| Ball Tracks | 0 |
| CSV events parsed | 18 |
| Action Segments inferred | 85 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 322: Duplicate assignment for track ID '4' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '6' (LG) duration 105 frames exceeds threshold 90 frames [start=84, end=188].
> - Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [81–100], lower_priority='Action_ZoneBlock' annotated_start=84, effective_Action_ZoneBlock_start=101.
> - Action 'Action_None' range [81-142] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-147] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-156] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [168-187] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [193-208] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [211-243] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-101] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [103-104] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_SplitBlock' range [87-122] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-197] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-123] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [129-157] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-176] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [128-269] for track '5' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-140] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [157-169] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [171-188] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-117] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [140-155] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-113] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [118-128] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [84-121] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [189-263] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [101-143] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [149-165] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [169-172] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-95] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-140] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [142-148] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [174-181] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-90] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [133-176] for track '12' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-57] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-90] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [96-102] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [14-18] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [41-52] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-93] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [105-157] for track '14' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [174-175] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [119-134] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-174] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [176-178] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [181-186] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [189-206] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [213-218] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [225-234] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [236-248] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [145-269] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-173] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-207] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [166-181] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-203] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [259-269] for track '21' has 1 frames without a visible bounding box.
> - Player track '13' has undefined position. Will map to Position_Unknown.
> - Player track '13' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.