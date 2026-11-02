# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_204`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_204/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 29 |
| Player Tracks | 29 |
| Ball Tracks | 0 |
| CSV events parsed | 22 |
| Action Segments inferred | 82 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 410: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '3' (C): higher_priority='Action_BallSnap' [81–95], lower_priority='Action_ZoneBlock' annotated_start=93, effective_Action_ZoneBlock_start=96.
> - Action 'Action_ZoneBlock' range [93-145] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-161] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [96-152] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [162-163] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-175] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_LeadBlock' range [93-122] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-130] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-148] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [150-239] for track '6' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [171-172] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [93-150] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [110-161] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-147] for track '10' has 4 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-70] for track '11' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [81-85] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [89-101] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [108-111] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [114-115] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-94] for track '12' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [102-131] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [136-137] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-51] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [53-60] for track '14' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [89-91] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [99-100] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [109-112] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-1] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [7-12] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [17-25] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [36-37] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [73-75] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [81-92] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [94-96] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [98-102] for track '15' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [104-110] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [112-166] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [170-183] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [110-217] for track '16' has 4 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [219-236] for track '16' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [91-101] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-191] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [120-176] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [138-141] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [146-148] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [144-174] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [157-171] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [160-222] for track '24' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [168-210] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [212-213] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [220-226] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [229-237] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [227-228] for track '28' has 1 frames without a visible bounding box.
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
> - Player track '27' has undefined position. Will map to Position_Unknown.
> - Player track '27' has undefined team_side. Will map to Team_Unknown.
> - Player track '28' has undefined position. Will map to Position_Unknown.
> - Player track '28' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.