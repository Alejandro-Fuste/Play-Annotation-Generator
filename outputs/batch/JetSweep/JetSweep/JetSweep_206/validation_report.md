# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_206`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_206/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 24 |
| Player Tracks | 24 |
| Ball Tracks | 0 |
| CSV events parsed | 21 |
| Action Segments inferred | 58 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 414: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Validation warning: Action 'Action_ZoneBlock' for track '4' (RT) duration 122 frames exceeds threshold 90 frames [start=63, end=184].
> - Overlapping action conflict at frame 63 for track '7': 'Action_ZoneBlock' vs 'Action_LeadBlock'. Overriding with 'Action_LeadBlock'.
> - Resolved action overlap for track '7' (C): higher_priority='Action_BallSnap' [59–73], lower_priority='Action_LeadBlock' annotated_start=63, effective_Action_LeadBlock_start=74.
> - Action 'Action_None' range [59-239] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-199] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-150] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-116] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-151] for track '4' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [185-219] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-119] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [74-97] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-93] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-101] for track '9' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-124] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-21] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [63-141] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-148] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-230] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [232-235] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-7] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [95-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [104-142] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [59-112] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [89-228] for track '18' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [231-232] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [82-83] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [94-148] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [113-220] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [197-198] for track '22' has 1 frames without a visible bounding box.
> - Player track '12' has undefined position. Will map to Position_Unknown.
> - Player track '12' has undefined team_side. Will map to Team_Unknown.
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

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.