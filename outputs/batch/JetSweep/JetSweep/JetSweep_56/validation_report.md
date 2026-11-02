# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_56`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_56/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 36 |
| Player Tracks | 36 |
| Ball Tracks | 0 |
| CSV events parsed | 25 |
| Action Segments inferred | 98 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 329 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - Row 114: Duplicate assignment for track ID '11' in grid. Overwriting previous assignment.
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
> - Validation warning: Action 'Action_BlockSecondLevel' for track '20' (RG) duration 148 frames exceeds threshold 90 frames [start=159, end=306].
> - Resolved action overlap for track '21' (C): higher_priority='Action_BallSnap' [123–138], lower_priority='Action_ZoneBlock' annotated_start=130, effective_Action_ZoneBlock_start=139.
> - Action 'Action_None' range [123-265] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [267-286] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [289-296] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [302-304] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-270] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-294] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [298-304] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [148-262] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [264-284] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [286-292] for track '4' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-202] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [207-233] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [235-239] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-261] for track '6' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [267-289] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [301-308] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [314-315] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [318-329] for track '6' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-302] for track '7' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-301] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [304-306] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-171] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [173-329] for track '9' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-298] for track '10' has 5 frames without a visible bounding box.
> - Action 'Action_None' range [154-167] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [169-283] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-239] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [241-287] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [148-248] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-240] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-169] for track '15' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [123-285] for track '16' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [154-157] for track '17' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [159-275] for track '17' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-300] for track '18' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [123-266] for track '19' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [268-313] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [159-258] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_BlockSecondLevel' range [260-306] for track '20' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-81] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [85-122] for track '21' has 2 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [139-152] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-319] for track '21' has 3 frames without a visible bounding box.
> - Action 'Action_None' range [141-154] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [151-152] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [156-158] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [195-197] for track '24' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [167-171] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [174-176] for track '25' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [183-279] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [192-195] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [199-200] for track '27' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [203-204] for track '28' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [209-212] for track '29' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [214-215] for track '30' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [219-220] for track '31' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [246-248] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [252-256] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [276-278] for track '32' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [270-271] for track '33' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [323-324] for track '35' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [326-329] for track '35' has 1 frames without a visible bounding box.
> - Player track '0' has undefined position. Will map to Position_Unknown.
> - Player track '0' has undefined team_side. Will map to Team_Unknown.
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
> - Player track '32' has undefined position. Will map to Position_Unknown.
> - Player track '32' has undefined team_side. Will map to Team_Unknown.
> - Player track '33' has undefined position. Will map to Position_Unknown.
> - Player track '33' has undefined team_side. Will map to Team_Unknown.
> - Player track '34' has undefined position. Will map to Position_Unknown.
> - Player track '34' has undefined team_side. Will map to Team_Unknown.
> - Player track '35' has undefined position. Will map to Position_Unknown.
> - Player track '35' has undefined team_side. Will map to Team_Unknown.

## **Recommended Fixes / Action Items**
- Review players with undefined positions or team_sides. Ensure they have the correct metadata attributes in CVAT if you need precise group expansion.