# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `SplitZone_4`
- **Input XML**: `outputs/batch/SplitZone/SplitZone/SplitZone_4/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/SplitZone.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 68 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 299 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
> - Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [121–133], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=134.
> - Action 'Action_None' range [196-210] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-172] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-208] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-158] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [163-273] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-183] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [193-194] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-210] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [162-211] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [124-195] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [121-135] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [140-156] for track '10' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [13-46] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [121-136] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-250] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [134-191] for track '14' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [59-76] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [79-120] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_None' for track '15' starts at frame 121, but the player has no visible bounding box on this frame.
> - Action 'Action_None' range [121-121] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [153-156] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [158-162] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [165-167] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-172] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-268] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [158-168] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-256] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [233-256] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [248-299] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [267-268] for track '24' has 1 frames without a visible bounding box.
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
> - Player track '25' has undefined position. Will map to Position_Unknown.
> - Player track '25' has undefined team_side. Will map to Team_Unknown.
> - Player track '26' has undefined position. Will map to Position_Unknown.
> - Player track '26' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.