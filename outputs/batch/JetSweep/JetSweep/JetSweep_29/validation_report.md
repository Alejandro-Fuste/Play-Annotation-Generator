# Play-Annotation-Generator Annotation Enrichment Validation Report

## **Summary**
- **Status**: SUCCESS
- **Video Name**: `JetSweep_29`
- **Input XML**: `outputs/batch/JetSweep/JetSweep/JetSweep_29/generated_base_cvat.xml`
- **Input CSV**: `data/key_actions/JetSweep.csv`

## **Key Metrics**
| Metric | Value |
| :--- | :--- |
| Total XML Tracks | 27 |
| Player Tracks | 27 |
| Ball Tracks | 0 |
| CSV events parsed | 29 |
| Action Segments inferred | 91 |
| Invalid XML Bounding Boxes | 0 |
| Video Start Frame | 0 |
| Video Stop Frame | 239 |

## **Pipeline Errors**
*No critical pipeline errors encountered.*

## **Pipeline Warnings**
> [!WARNING]
> The following non-critical warnings were logged:
> - No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
> - Resolved action overlap for track '5' (C): higher_priority='Action_BallSnap' [74–89], lower_priority='Action_ZoneBlock' annotated_start=78, effective_Action_ZoneBlock_start=90.
> - Action 'Action_None' range [74-206] for track '0' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [208-235] for track '0' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-158] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [163-192] for track '1' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-196] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [201-211] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [234-235] for track '1' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-175] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-192] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [194-195] for track '2' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [198-229] for track '2' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-183] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [185-192] for track '3' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [194-231] for track '3' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-234] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [236-237] for track '5' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [103-180] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [182-192] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [194-206] for track '8' has 1 frames without a visible bounding box.
> - Action 'Action_BallCarry' range [210-230] for track '8' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [74-227] for track '10' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-206] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [208-216] for track '11' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-171] for track '12' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-174] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [178-206] for track '13' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-239] for track '13' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [149-221] for track '14' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-129] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [135-210] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [223-224] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [226-227] for track '18' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [74-172] for track '19' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [78-108] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_ZoneBlock' range [114-117] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-229] for track '20' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [149-239] for track '21' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [0-5] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [9-11] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_PreSnap' range [40-41] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [97-102] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [105-106] for track '22' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [85-88] for track '23' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [186-227] for track '24' has 4 frames without a visible bounding box.
> - Action 'Action_None' range [190-239] for track '25' has 2 frames without a visible bounding box.
> - Action 'Action_None' range [203-205] for track '26' has 1 frames without a visible bounding box.
> - Action 'Action_None' range [210-212] for track '26' has 1 frames without a visible bounding box.
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