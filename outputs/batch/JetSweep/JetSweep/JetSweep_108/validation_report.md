# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_108`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_108/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 20 |
| Action Segments inferred | 87 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 269 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 218: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
> - Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [124–137], lower_priority='Action_ZoneBlock' annotated_start=125, effective_Action_ZoneBlock_start=138.
> - Segment 'Action_ZoneBlock' for track '16' has invalid range: start=125, end=122. Clamping end to start.
> - Action 'Action_None' range [124-247] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-269] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-200] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-262] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-170] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-269] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-230] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [124-256] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-120] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_BallSnap' range [124-134] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [138-139] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [146-161] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-211] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [124-269] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_LeadBlock' for track '14' starts at frame 125, but the player has no visible bounding box on this frame.
> - Action 'Action_LeadBlock' range [125-125] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [142-183] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-211] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [4-30] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [35-120] for track '15' has 3 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-30] for track '16' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-75] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [77-78] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [84-122] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-16] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [19-22] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-122] for track '17' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [12-15] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [21-22] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [42-58] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [60-61] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [64-66] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [89-95] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [100-119] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [141-151] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [153-269] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [43-61] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [63-67] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-86] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [101-102] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [105-118] for track '19' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [143-155] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [163-193] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-224] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [126-127] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [143-213] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [147-269] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-262] for track '22' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [264-266] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-215] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-157] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-161] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [164-170] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-187] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-213] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [215-219] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-228] for track '27' has 1 frames without a visible bounding box.
> - Player track '18' has undefined position. Will map to Position_Unknown.
> - Player track '18' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.